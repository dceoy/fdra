#!/usr/bin/env python

import os
import unittest
import pandas as pd
from fdra.fdr import qvalue


class QvaluesByR(unittest.TestCase):
    """Random p-values and their q-values calculated by stats::p.adjust in R
    """
    df_p = pd.read_csv(
        os.path.join(os.path.dirname(__file__), 'qvalues_by_r.csv'),
        index_col=None
    )

    def test_BH_qvalue(self, precision=5):
        """Test of the Benjamini-Hochberg method
        """
        df_q = self.df_p.assign(
            BH_new=lambda d: qvalue(d['pval'], method='BH')
        )
        for id, row in df_q.round(precision).iterrows():
            self.assertEqual(row['BH'], row['BH_new'])

    def test_BY_qvalue(self, precision=5):
        """Test of the Benjamini-Yekutieli method
        """
        df_q = self.df_p.assign(
            BY_new=lambda d: qvalue(d['pval'], method='BY')
        )
        for id, row in df_q.round(precision).iterrows():
            self.assertEqual(row['BY'], row['BY_new'])


if __name__ == '__main__':
    unittest.main()
