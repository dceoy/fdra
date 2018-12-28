#!/usr/bin/env python
#
# FDR-based p-value adjuster
# https://github.com/dceoy/fdra

import pandas as pd
import numpy as np


def qvalue(pvalues, method='BH'):
    """Calculate q-values by the Benjamini-Hochberg method
    Args:
        pvalues (list): p-value list or array
        method (str): `BH` (Benjamini-Hochberg) or `BY` (Benjamini-Yekutieli)
    Returns:
        numpy.ndarray: q-value array
    """
    n = len(pvalues)
    df_p = pd.DataFrame({'pval': pvalues}).sort_values(
        by='pval', ascending=False
    ).reset_index()
    if method == 'BH':
        df_q = df_p.assign(
            qval=lambda d: (d['pval'] * n / (n - d.index.values)).cummin()
        )
    elif method == 'BY':
        w = np.sum(np.reciprocal(np.arange(1, n + 1, dtype='float32')))
        df_q = df_p.assign(
            qval=lambda d: (d['pval'] * n / (n - d.index.values) * w).cummin()
        )
    else:
        raise RuntimeError('Unimplemented method')
    return df_q.set_index(
        'index', drop=True
    ).sort_index()['qval'].clip(
        lower=0, upper=1
    ).values
