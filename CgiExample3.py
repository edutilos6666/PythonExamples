#! /usr/bin/python3

'''
Get and Post Request from form 

<html>
<head>
 <title>GetRequest.html</title>
</head>
<body>
  <h2>GetRequest.html</h2>
  <form method="GET" action="http://localhost/cgi-bin/python/CgiExample3.py">
    fname : <input type="text" name="fname" /> <br/>
    lname : <input type="text" name="lname" /> <br/> 
    <input type="submit" /> <br/>
  </form>
</body>
</html>



'''

import cgi, cgitb

form = cgi.FieldStorage()

fname = form.getvalue("fname")
lname = form.getvalue("lname")

pattern = """Content-type:text/html

fname = {0}
lname = {1}
"""

str = pattern.format(fname, lname)

print(str)