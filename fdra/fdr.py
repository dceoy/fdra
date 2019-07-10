#!/usr/bin/env python
"""
FDR-based p-value adjuster.
https://github.com/dceoy/fdra
"""

import numpy as np
import pandas as pd


def qvalue(pvalues, method='BH'):
    """Calculate q-values by the Benjamini-Hochberg method.
    Args:
        pvalues (list): p-value list or array
        method (str): `BH` (Benjamini-Hochberg) or `BY` (Benjamini-Yekutieli)
    Returns:
        numpy.ndarray: q-value array
    """
    pvals = pvalues if isinstance(pvalues, np.ndarray) else np.array(pvalues)
    if np.sum((pvals < 0) | (pvals > 1)):
        raise ValueError('Invalid p-values')
    else:
        n = len(pvals)
        df_p = pd.DataFrame({'pval': pvals}).sort_values(
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
        raise ValueError('Unimplemented method')
    return df_q.set_index(
        'index', drop=True
    ).sort_index()['qval'].clip(
        lower=0, upper=1
    ).values
