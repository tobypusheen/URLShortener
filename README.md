URLShortener
===
This is a simple PoC of shorten URL WEB service

Overview
---
The URLShortener is implemented by GET method with Python and flask.

Requirement
---
Python3 and flask

```
pip3 install requirements.txt
```

Installation
---
clone this repo


Usage
---
First, modify the segments in `main.py`
```
us = URLShortener(ServiceHost='http://localhost:5000/', debug=True)
...
app.run(debug=True, host='0.0.0.0', port='5000')
```
must give a accessiable host and port, and set the `debug=False`, if you don't want to see the debug message.

then, you can run service
```
python3 main.py
```

APIs
---
You can use `/create` to shorten URL in browser by
```
http://localhost:5000/create?url=http://www.example.com
```

and also can use `/create` shorten URL by curl in terminal
```
curl http://localhost:5000/create?url=http://www.example.com
```

you will get a shortenURL
```
http://localhost:5000/F8Ul4LeX
```

And the URLShortener provides `/list` will show how many shorten URLs
```
{
  "3nfoqWzL": "http://www.yahoo.com.tw/",
  "BUUh8536": "http://testdata",
  "F8Ul4LeX": "http://http://www.example.com",
  "L36msscq": "http://http://www.reddit.com",
  "YUAPDZv5": "http://http://localhost:5000/create?url=https://www.google.com.tw/search?q=%E7%B8%AE%E7%B6%B2%E5%9D%80%E6%9C%8D%E5%8B%99&oq=%E7%B8%AE%E7%B6%B2%E5%9D%80%E6%9C%8D%E5%8B%99&aqs=chrome..69i57.200j0j4&sourceid=chrome&ie=UTF-8",
  "b1C4Vhse": "http://www.facebook.com",
  "njwhgE6i": "https://www.google.com",
  "vh1CUczP": "https://twitter.com",
  "vnv5n4go": "https://www.linkedin.com/in/toby-lin-b72025119/",
  "yr7QWibm": "https://github.com/tobypusheen"
}
```

Known Iusses
---

The known issue is that it can not shorten the URL with the parameter `&`. For example,
```
https://www.google.com.tw/search?num=30&ei=lk84W-mtJYHu-QanxouYBA&q=台北市天氣&oq=台北市天氣&gs_l=psy-ab.3...0.0.0.4276.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.TmB0CgGeK4k
```
I keep track of this issue and try to slove it.


Author
---
A man who enjoys challenge, Toby Lin, chaoti.lin@gmail.com,

