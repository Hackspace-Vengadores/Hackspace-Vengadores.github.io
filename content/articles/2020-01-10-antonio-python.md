Title: Primer día (Antonio)
date: 2020-01-13 10:00
Modified: 2020-01-13 18:00
comments: true
slug: review-antonio
tags: python
series: Python
series_index: 5
author: AntonioAllende

<!-- PELICAN_BEGIN_SUMMARY -->
[TOC]

## Numpy

$$
f_{1}\left(x\right)=\operatorname{sen}\left(x\right)\\
f_{2}\left(x\right)=\operatorname{cos}\left(x\right)\\
f_{3}\left(x\right)=\operatorname{tan}\left(x\right)
$$

```python
def example():
    print("Hello World")
```


```python
>>> import numpy as np
>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.ndim
2
>>> a.dtype.name
'int64'
>>> a.itemsize
8
>>> a.size
15
>>> type(a)
<type 'numpy.ndarray'>
>>> b = np.array([6, 7, 8])
>>> b
array([6, 7, 8])
>>> type(b)
<type 'numpy.ndarray'>
```

<!-- PELICAN_END_SUMMARY -->
