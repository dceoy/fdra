#!/usr/bin/env python
#
# FDR-based p-value adjuster
# https://github.com/dceoy/fdra

import pandas as pd


def qvalue(pvalues, method='BH'):
    """Calculate q-values by the Benjamini-Hochberg method
    Args:
        pvalues (numpy.ndarray): p-value array
    Returns:
        numpy.ndarray: q-value array
    """
    n = len(pvalues)
    if method == 'BH':      # Benjamini-Hochberg method
        return pd.DataFrame({'pval': pvalues}).sort_values(
            by='pval', ascending=False
        ).reset_index().assign(
            qval=lambda d: (d['pval'] * n / (n - d.index.values)).cummin()
        ).set_index(
            'index', drop=True
        ).sort_index()['qval'].values
    else:
        raise RuntimeError('Unimplemented method')
