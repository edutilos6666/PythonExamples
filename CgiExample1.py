#! /usr/bin/python3

'''
firstly in /opt/lampp/etc/httpd.conf , do followings :
<Directory "/opt/lampp/cgi-bin">
    AllowOverride None
#    Options None
   Options +ExecCGI
   Require all granted
   AddHandler cgi-script .rb .py
</Directory>


then: 

cp /home/edutilos/PycharmProjects/PythonExamples/CgiExample1.py /opt/lampp/cgi-bin/python
sudo chmod 777 CgiExample1.py  # in /opt/lampp/cgi-bin/python

and start lampp 
sudo /opt/lampp/lampp start
#restart 
sudo /opt/lampp/lampp restart

and in browser : 
http://localhost/cgi-bin/python/CgiExample1.py


# stop lampp 
sudo /opt/lampp/lampp stop

'''

str = """Content-type:text/html

<html>
  <head>
     <title>example1</title>
  </head>
  <body>
     <h1>Example1</h1>
     <h2>Example1</h2>
     <h3>Example1</h3>
     <h4>Example1</h4>
     <h5>Example1</h5>
     <h6>Example1</h6>
  </body>
</html>
"""
print(str)


