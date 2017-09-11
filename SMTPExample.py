import smtplib
import copy
import base64

user = None
password = None




def example4():
    'sending attachment and html message'
    filename = "ListExample.py"
    f = open(filename, "rb")
    c = f.read()
    f.close()
    content = base64.b64encode(c)

    FROM = copy.copy(user)
    receivers = [
        "edutilosaghayev@yahoo.com",
        "foobar666@inbox.ru",
        "Nijat.Aghayev@ruhr-uni-bochum.de"
    ]

    marker = "ACDEFGHIJKLMNOPQRSTUVWXYZ"
    part1 = """From: {0}
To: {1}
MIME-Version:1.0
Subject:Sending attachment
Content-Type:multipart/mixed; boundary={2}
--{2}
""".format(FROM, " , ".join(receivers),marker)

    part2_content = """<h1>heading1</h1>
<h2>heading2</h2>
<h3>heading3</h3>
<h4>heading4</h4>
<h5>heading5</h5>
<h6>heading6</h6>"""
    part2 = """Content-Type:text/html
Content-Transfer-Encoding:8bit 

{0}
--{1}
""".format(part2_content, marker)

    part3 = """Content-Type:multipart/mixed; name="{0}"
Content-Transfer-Encoding:base64
Content-Disposition:attachment; filename={0}

{1}
--{2}--
""".format(filename, content, marker)

    message = part1 + part2 + part3


    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, password)
    server.sendmail(FROM , receivers, message)
    server.close()
    print("Message was sent successfully.")
    print()




def example3():
    'multiple receivers with html message'
    FROM = copy.copy(user)
    receivers = [
        "edutilosaghayev@yahoo.com",
        "foobar666@inbox.ru",
        "Nijat.Aghayev@ruhr-uni-bochum.de"
    ]

    content = """<h1>Heading1</h1>
<h2>Heading2</h2>
<h3>Heading3</h3>
<h4>Heading4</h4>
<h5>Heading5</h5>
<h6>Heading6</h6>
"""

    message = """From: {0}
To: {1}
MIME-Version: 1.0
Content-Type: text/html
Subject:Test content-type and multiple receivers

{2}
""".format(FROM, ", ".join(receivers), content)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(user, password)
    server.sendmail(FROM, receivers, message)
    server.close()
    print("Message was sent successfully.")


    print()

def example2():
    'with port 465'
    FROM = copy.copy(user)
    TO = "Nijat.Aghayev@ruhr-uni-bochum.de"
    message = """From: {0}
Subject: Test 465

Hello World from gmail""".format(FROM)

    try:
        server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server_ssl.ehlo()
        server_ssl.login(user, password)
        server_ssl.sendmail(FROM , TO , message)
        server_ssl.close()
        print("Message was sent successfully.")
    except:
        print("Message could not be sent.")

    print()


def example1():
    'with port 587'
    FROM = copy.copy(user)
    TO = "Nijat.Aghayev@ruhr-uni-bochum.de"
    message = """From: edutilosaghayev@gmail.com 
Subject: Test 

hello world from gmail"""
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, password)
        server.sendmail(FROM , TO , message)
        server.close()
        print("Message was sent successfully.")
    except:
        print("Error while sending message")

    print()