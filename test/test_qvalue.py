#!/usr/bin/env python

import os
import unittest
import pandas as pd
from fdra.fdr import qvalue


class QvaluesByR(unittest.TestCase):
    """Random p-values and their q-values calculated by stats::p.adjust in R
    """
    def test_qvalue(self, precision=5):
        df = pd.read_csv(
            os.path.join(os.path.dirname(__file__), 'qvalues_by_r.csv'),
            index_col=None
        ).assign(
            BH_new=lambda d: qvalue(d['pval'], method='BH'),
            BY_new=lambda d: qvalue(d['pval'], method='BY')
        ).round(precision)
        for id, row in df.iterrows():
            self.assertEqual(row['BH'], row['BH_new'])
            self.assertEqual(row['BY'], row['BY_new'])


if __name__ == '__main__':
    unittest.main()
