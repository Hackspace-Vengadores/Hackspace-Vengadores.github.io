Title: Primer día
subtitle: AntonioAllende
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
!!! danger

    Esta es una advertencia de peligro o error

!!! warning

    Esta es una advertencia, advertencia o advertencia.

!!! important

    Esta es importante o de nota

!!! hint

    Esta es una sugerencia o consejo

!!! hint "Use comillas dobles para cambiar el título"

    Este cuadro de advertencia contiene un mosaico personalizado porque lo coloqué entre comillas dobles después de `hint`.

!!! important ""

    Este cuadro no requiere un título, pero sigue siendo una advertencia `important` y se resaltará como tal.


| Season | Episodes | First aired        |
| ------ | -------- | ------------------ |
| 1      | 13       | June 2, 2002       |
| 2      | 12       | June 1, 2003       |
| 3      | 12       | September 19, 2004 |
| 4      | 13       | September 10, 2006 |
| 5      | 10       | January 6, 2008    |

> Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Pellentesque eu tincidunt tortor aliquam nulla facilisi.

[Example Link](https://www.mozilla.org/){: class="ampl"} blah blah

<!-- PELICAN_END_SUMMARY -->
