fdra
====

FDR-based p-value adjuster by the Benjamini-Hochberg method

[![wercker status](https://app.wercker.com/status/72d47378ed8e3fbef1adacfa30801f15/s/master "wercker status")](https://app.wercker.com/project/byKey/72d47378ed8e3fbef1adacfa30801f15)

Installation
------------

```sh
$ pip install -U https://github.com/dceoy/fdra/archive/master.tar.gz
```

Example
-------

```python
import numpy as np
import pandas as pd
from fdra.fdr import qvalue

pvals = np.random.uniform(size=10)
qvals = qvalue(pvalues=pvals)

print(pd.DataFrame({'pval': pvals, 'qval': qvals}))
```

Unit tests
----------

```sh
$ python ./test/test_qvalue.py
```
