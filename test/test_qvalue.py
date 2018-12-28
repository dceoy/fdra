#!/usr/bin/env python

import os
import unittest
import pandas as pd
from fdra.fdr import qvalue


class QvaluesByR(unittest.TestCase):
    def test_qvalue(self, precision=10):
        df = pd.read_csv(
            os.path.join(os.path.dirname(__file__), 'qvalues_by_r.csv'),
            index_col=None
        ).assign(
            BH_new=lambda d: qvalue(d['pval'], method='BH')
        ).round(precision)
        for id, row in df.iterrows():
            self.assertEqual(row['BH'], row['BH_new'])


if __name__ == '__main__':
    unittest.main()
