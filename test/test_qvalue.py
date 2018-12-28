#!/usr/bin/env python

import os
import unittest
import pandas as pd
from fdra.qvalue import calculate_qvalue


class QvaluesFromRFunctions(unittest.TestCase):
    def test_calculate_qvalue(self, precision=10):
        df = pd.read_csv(
            os.path.join(os.path.dirname(__file__), 'qvalues.csv'),
            index_col=None
        ).assign(
            BH_new=lambda d: calculate_qvalue(d['pval'], method='BH')
        ).round(precision)
        for id, row in df.iterrows():
            self.assertEqual(row['BH'], row['BH_new'])


if __name__ == '__main__':
    unittest.main()
