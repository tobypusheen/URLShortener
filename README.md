URLShortener
===
This is a simple PoC of shorten URL WEB service

Overview
---
The URLShortener is implemented by GET method with Python and Flask.

Requirement
---
Python3

Installation
---
clone this repo

Usage
---
you can run service by `python3 main.py`

Known Iusses
---
The known issue is that it can not shorten the URL with the parameter `&`. For example,
```
https://www.google.com.tw/search?num=30&ei=lk84W-mtJYHu-QanxouYBA&q=台北市天氣&oq=台北市天氣&gs_l=psy-ab.3...0.0.0.4276.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.TmB0CgGeK4k
```
I keep track of this issue and try to slove it.


Author
---
A man who enjoys challenge, Toby Lin, chaoti.lin@gmail.com


