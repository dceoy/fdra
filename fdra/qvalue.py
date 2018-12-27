#!/usr/bin/env python

import numpy as np
import pandas as pd
from scipy.interpolate import splev, splrep


def calculate_qvalue(pvalues, method='BH', tau_interval=0.05):
    df_p = pd.DataFrame({'pval': pvalues}).sort_values(
        by='pval', ascending=False
    ).reset_index()
    n = df_p.shape[0]
    if method == 'BH':      # Benjamini-Hochberg method
        return df_p.assign(
            qval=lambda d: (d['pval'] * n / (n - d.index.values)).cummin()
        ).set_index('index', drop=True).sort_index()['qval']
    elif method == 'BY':    # Benjamini-Yekutieli method
        return df_p.assign(
            em=np.cumsum(
                np.reciprocal(np.arange(1, n + 1, dtype='float32'))
            )[::-1]
        ).assign(
            qval=lambda d:
            (d['pval'] * n / (n - d.index.values) / d['em']).cummin()
        ).set_index('index', drop=True).sort_index()['qval']
    elif method == 'ST':   # Storey-Tibshirani method
        pi0 = pd.DataFrame({
            'tau': np.arange(start=tau_interval, stop=1, step=tau_interval)
        }).assign(
            pi=lambda d: d['tau'].apply(
                lambda t: np.sum(df_p['pval'] > t) / n / (1 - t)
            )
        ).pipe(
            lambda d: np.float32(splev(1, splrep(d['tau'], d['pi'], k=3)))
        )
        return df_p.assign(
            qval=lambda d: (
                d['pval'] * pi0 * n / (n - d.index.values)
            ).cummin()
        ).set_index('index', drop=True).sort_index()['qval']
    else:
        raise RuntimeError('Unimplemented method')
