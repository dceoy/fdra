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

    def test_invalid_input(self):
        """qvalue should fail with invalid input
        """
        self.assertRaises(ValueError, qvalue, self.df_p['pval'] + 1)
        self.assertRaises(ValueError, qvalue, self.df_p['pval'] - 1)

    def test_bh_qvalue(self, precision=5):
        """qvalue with BH (Benjamini-Hochberg) should give correct q-values
        """
        df_q = self.df_p.assign(
            BH_new=lambda d: qvalue(d['pval'], method='BH')
        )
        for _, row in df_q.round(precision).iterrows():
            self.assertEqual(row['BH'], row['BH_new'])

    def test_by_qvalue(self, precision=5):
        """qvalue with BY (Benjamini-Yekutieli) should give correct q-values
        """
        df_q = self.df_p.assign(
            BY_new=lambda d: qvalue(d['pval'], method='BY')
        )
        for _, row in df_q.round(precision).iterrows():
            self.assertEqual(row['BY'], row['BY_new'])


if __name__ == '__main__':
    unittest.main()
