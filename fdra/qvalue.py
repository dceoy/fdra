#!/usr/bin/env python

import pandas as pd


def qvalue(pvalues, method='BH'):
    n = len(pvalues)
    if method == 'BH':
        return pd.DataFrame({'pval': pvalues}).sort_values(
            by='pval', ascending=False
        ).reset_index().assign(
            qval=lambda d: (d['pval'] * n / (n - d.index.values)).cummin()
        ).set_index('index', drop=True).sort_index()['qval']
    else:
        raise RuntimeError('Unimplemented method')
