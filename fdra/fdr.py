#!/usr/bin/env python
#
# FDR-based p-value adjuster
# https://github.com/dceoy/fdra

import pandas as pd


def qvalue(pvalues, method='BH'):
    df_p = pd.DataFrame({'pval': pvalues}).sort_values(
        by='pval', ascending=False
    ).reset_index()
    n = df_p.shape[0]
    if method == 'BH':      # Benjamini-Hochberg method
        return df_p.assign(
            qval=lambda d: (d['pval'] * n / (n - d.index.values)).cummin()
        ).set_index(
            'index', drop=True
        ).sort_index()['qval'].values
    else:
        raise RuntimeError('Unimplemented method')
