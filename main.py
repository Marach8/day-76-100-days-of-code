from flask import Flask

app1 = Flask(__name__, static_url_path='/static')

@app1.route('/')
def home():
  ab = '''Welcom to my Homepage!
  <p><a href='/portfolio'>Go to my Portfolio</a></p>
    <p><a href='/linktree'>Go to linktree</a></p>'''
  return ab


@app1.route('/linktree')  
def funca():
  page1 = f'''<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>My Link Tree</title>
  <link href="static/linktree.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <img src='static/images/FB_IMG_16424079268446465.png'/>
  <h2>My name is Ajah Emmanuel.</h2>
  <h5>I am a Software Engineer</h5>
  <ul>
  <l1><a href='https://www.linkedin.com/in/ajah-emmanuel-bb6175218'><h3> My LinkedIn Profile</h3></a></l1>
  <l1><a href='https://twitter.com/FmrsMarach?t=vVzg_FDdjEuamnrEVfYi6g&s=09'><h3>My Twitter Handle</h3></a></l1>
  <l><a href='https://www.facebook.com/profile.php?id=100089050818615&mibextid=ZbWKwL'><h3>My Facebook Handle</h3></a></l>
  </ul>
    <p><a href='/portfolio'>Go to my Portfolio</a></p>
    <p><a href='/'>Go to homepage</a></p>
</body>

</html>'''
  return page1

@app1.route('/portfolio')
def funcb():
  page = '''<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width">
  <title>Emmanuel's Portfolio</title>
  <link href="static/portfolio.css" rel="stylesheet" type="text/css" />
</head>

<body>
  <h1>Emmanuel's Portfolio</h1>
  <h3>Day 65 Solution</h3>
  <p1>This is my Solution for day 65. It took me some time before I came up with the solution</p1>
  <a href='https://replit.com/@Emmanuel2018/Day-65100-days-of-code?s=app'><img src='static/images/Screenshot (7).png' width=70% ></a>
  
  <h3>Day 66 Solution</h3>
  <p1>This is my Solution for day 66. It took me some time before I came up with the solution</p1>
  <a href='https://replit.com/@Emmanuel2018/Day-66100-days-of-code?s=app'><img src='static/images/Screenshot (8).png' width=70% ></a>
  
  <h3>Day 67 Solution</h3>
  <p1>This is my Solution for day 67. It took me some time before I came up with the solution</p1>
  <a href='https://replit.com/@Emmanuel2018/Day-67100-days-of-code?s=app'><img src='static/images/Screenshot (9).png' width=70% ></a>
  
  <h3>Day 68 Solution</h3>
  <p1>This is my Solution for day 68. It took me some time before I came up with the solution</p1>
  <a href='https://replit.com/@Emmanuel2018/Day-68100-days-of-code?s=app'><img src='static/images/Screenshot (10).png' width=70% ></a>
  
  <h3>Day 69 Solution</h3>
  <p1>This is my Solution for day 69. It took me some time before I came up with the solution</p1>
  <a href= 'https://replit.com/@Emmanuel2018/Day-69100-days-of-code?s=app'> <img src='static/images/Screenshot (11).png' width=70% ></a>
  
  <p><a href='/linktree'>Go to my LinkTree</a></p>
  <p><a href='/'>Go to homepage</a></p>
</body>

</html>
'''
  return page

app1.run(host='0.0.0.0', port=81)
