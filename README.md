# Arith

## Specification

This application is designed to fulfil the requirements of the third milestone project of the Code Institute Full Stack Developer course 2018.

It is a simple game in which the user practises her/his mental arithmetic by attempting to calculate sums, differences, products and quotients of positive integers.  Multiple users should be catered for, and the app must keep track of how many questions each user has attempted, and how many have been answered correctly.   It should pass this data to HTML templates which are styled with CSS and thus displayed to each user in the browser.

In accordance with project guidelines, there is no persistence of data.   All information is held in volatile memory.   Similarly, there is no security or user validation.

The application uses Flask for routing and templating, and will be deployed to Heroku.   All logic is implemented in Python on the server.   Javascript on the client machine is used only for callbacks on text input etc.

We define one class: User, representing the user, storing name, number of problems attempted, number correct.   The app should calculate and display the user's score and percentage rating as well as the name and percentage score of the leading player.

The app will store an identifying userid and also the user's latest answer as a browser session object on the client machine.

The app will use the native random function to generate operands and operator to form a sum to be computed, e.g. ("28 x 13 = ? ")

We define a range for the operands (2 to n), initially fixed, later user-set.

We use an <input> element on the page for the user to type in their answer.  They will then be congratulated or commiserated with and subsequently will proceed to attempting to answer the next randomly-generated arithmetic problem.   Their score and relative standing will be updated.


## Testing

Once the basic framework is set up, a TDD approach will be adopted.

Tests will be created to check the logic regarding validation of user input, checking arithmetic operations and maintaining and updating user data.

The simple interface will lend itself to responsive design, so the application will be usable on mobile without difficulty.   I note, though, that the more features I introduce, the more danger of the UI becoming cluttered.

Manual tests on different devices will also be necessary.

## Design & Development

- First, I conceived the basic idea of randomly generated arithmetical problems as seeming to fulfil the project requirements.

- Next, I coded the basic functionality and templates incrementally, until sufficient core functionality and views were implemented and appeared to be working OK.   As I am not as experienced or as fluent in Python as in Java or Javascript, I was constantly on [Stack Overflow](www.stackoverflow.com), <https://www.tutorialspoint.com/flask/flask_quick_guide.htm> and other such sites looking for Pythonic and Flaskian ways of doing things!

- Small changes were contained in separate commits with informative explanatory messages as far as I could manage in order to maintain a clear and detailed version control history.

- Then, prior to testing and styling, I deployed the app to Heroku as documented hereunder.

## Deployment to Heroku

I created an app on Heroku and then set Heroku as a remote for my local repo in addition to the existing Github remote, and pushed my code to it, as shown in the log:

```
 21:16 /arith: 2052$ heroku git:remote -a arith
set git remote heroku to https://git.heroku.com/arith.git
21:21 /arith: 2053$ git remote -v
heroku	https://git.heroku.com/arith.git (fetch)
heroku	https://git.heroku.com/arith.git (push)
origin	git@github.com:teraspora/arith.git (fetch)
origin	git@github.com:teraspora/arith.git (push)
21:28 /arith: 2054$ git push -u heroku master 
Counting objects: 88, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (85/85), done.
Writing objects: 100% (88/88), 11.85 KiB | 674.00 KiB/s, done.
Total 88 (delta 40), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote: 
remote: -----> Python app detected
remote: -----> Installing python-3.6.7
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip
remote:        Collecting click==6.7 (from -r /tmp/build_85788446f1f796621fa0efa7f8fb0f13/requirements.txt (line 1))
remote:          Downloading https://files.pythonhosted.org/packages/34/c1/8806f99713ddb993c5366c362b2f908f18269f8d792aff1abfd700775a77/click-6.7-py2.py3-none-any.whl (71kB)
remote:        Collecting Flask==1.0.2 (from -r /tmp/build_85788446f1f796621fa0efa7f8fb0f13/requirements.txt (line 2))
remote:          Downloading https://files.pythonhosted.org/packages/7f/e7/08578774ed4536d3242b14dacb4696386634607af824ea997202cd0edb4b/Flask-1.0.2-py2.py3-none-any.whl (91kB)
remote:        Collecting itsdangerous==0.24 (from -r /tmp/build_85788446f1f796621fa0efa7f8fb0f13/requirements.txt (line 3))
remote:          Downloading https://files.pythonhosted.org/packages/dc/b4/a60bcdba945c00f6d608d8975131ab3f25b22f2bcfe1dab221165194b2d4/itsdangerous-0.24.tar.gz (46kB)
remote:        Collecting Jinja2==2.10 (from -r /tmp/build_85788446f1f796621fa0efa7f8fb0f13/requirements.txt (line 4))
remote:          Downloading https://files.pythonhosted.org/packages/7f/ff/ae64bacdfc95f27a016a7bed8e8686763ba4d277a78ca76f32659220a731/Jinja2-2.10-py2.py3-none-any.whl (126kB)
remote:        Collecting MarkupSafe==1.0 (from -r /tmp/build_85788446f1f796621fa0efa7f8fb0f13/requirements.txt (line 5))
remote:          Downloading https://files.pythonhosted.org/packages/4d/de/32d741db316d8fdb7680822dd37001ef7a448255de9699ab4bfcbdf4172b/MarkupSafe-1.0.tar.gz
remote:        Collecting numpy==1.15.0 (from -r /tmp/build_85788446f1f796621fa0efa7f8fb0f13/requirements.txt (line 6))
remote:          Downloading https://files.pythonhosted.org/packages/88/29/f4c845648ed23264e986cdc5fbab5f8eace1be5e62144ef69ccc7189461d/numpy-1.15.0-cp36-cp36m-manylinux1_x86_64.whl (13.9MB)
remote:        Collecting pandas==0.23.3 (from -r /tmp/build_85788446f1f796621fa0efa7f8fb0f13/requirements.txt (line 7))
remote:          Downloading https://files.pythonhosted.org/packages/f4/cb/a801eaf624e36fffaa6cf1f4597a1e4b0742c200ed928e689c58fb3cb811/pandas-0.23.3-cp36-cp36m-manylinux1_x86_64.whl (8.9MB)
remote:        Collecting python-dateutil==2.7.3 (from -r /tmp/build_85788446f1f796621fa0efa7f8fb0f13/requirements.txt (line 8))
remote:          Downloading https://files.pythonhosted.org/packages/cf/f5/af2b09c957ace60dcfac112b669c45c8c97e32f94aa8b56da4c6d1682825/python_dateutil-2.7.3-py2.py3-none-any.whl (211kB)
remote:        Collecting pytz==2018.5 (from -r /tmp/build_85788446f1f796621fa0efa7f8fb0f13/requirements.txt (line 9))
remote:          Downloading https://files.pythonhosted.org/packages/30/4e/27c34b62430286c6d59177a0842ed90dc789ce5d1ed740887653b898779a/pytz-2018.5-py2.py3-none-any.whl (510kB)
remote:        Collecting Werkzeug==0.14.1 (from -r /tmp/build_85788446f1f796621fa0efa7f8fb0f13/requirements.txt (line 10))
remote:          Downloading https://files.pythonhosted.org/packages/20/c4/12e3e56473e52375aa29c4764e70d1b8f3efa6682bef8d0aae04fe335243/Werkzeug-0.14.1-py2.py3-none-any.whl (322kB)
remote:        Collecting six>=1.5 (from python-dateutil==2.7.3->-r /tmp/build_85788446f1f796621fa0efa7f8fb0f13/requirements.txt (line 8))
remote:          Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
remote:        Installing collected packages: click, itsdangerous, MarkupSafe, Jinja2, Werkzeug, Flask, numpy, pytz, six, python-dateutil, pandas
remote:          Running setup.py install for itsdangerous: started
remote:            Running setup.py install for itsdangerous: finished with status 'done'
remote:          Running setup.py install for MarkupSafe: started
remote:            Running setup.py install for MarkupSafe: finished with status 'done'
remote:        Successfully installed Flask-1.0.2 Jinja2-2.10 MarkupSafe-1.0 Werkzeug-0.14.1 click-6.7 itsdangerous-0.24 numpy-1.15.0 pandas-0.23.3 python-dateutil-2.7.3 pytz-2018.5 six-1.12.0
remote: 
remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote: 
remote: -----> Compressing...
remote:        Done: 72M
remote: -----> Launching...
remote:        Released v3
remote:        https://arith.herokuapp.com/ deployed to Heroku
remote: 
remote: Verifying deploy... done.
To https://git.heroku.com/arith.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'heroku'.

```
So, I tried to open the app in a browser.   Result: "Application Error" message from Heroku - page couldn't be served.   Log:

```
21:58 /arith: 2060$ heroku logs --tail
2019-01-16T20:58:37.029049+00:00 app[api]: Enable Logplex by user johnlynch.32768@gmail.com
2019-01-16T21:25:12.056244+00:00 heroku[router]: at=info code=H81 desc="Blank app" method=GET path="/" host=arith.herokuapp.com request_id=9688a23f-e7a9-4813-b613-5df67c40b916 fwd="80.233.31.148" dyno= connect= service= status=502 bytes= protocol=https
2019-01-16T21:32:22.727543+00:00 app[api]: Release v3 created by user johnlynch.32768@gmail.com
2019-01-16T21:32:22.747918+00:00 app[api]: Scaled to web@1:Free by user johnlynch.32768@gmail.com
2019-01-16T21:32:32.804352+00:00 app[web.1]: * Debugger is active!
2019-01-16T21:32:32.805443+00:00 app[web.1]: * Debugger PIN: 960-713-823
2019-01-16T21:32:36.000000+00:00 app[api]: Build succeeded
2019-01-16T21:33:30.715437+00:00 heroku[web.1]: Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch
2019-01-16T21:33:30.715437+00:00 heroku[web.1]: Stopping process with SIGKILL
2019-01-16T21:33:30.785251+00:00 heroku[web.1]: Process exited with status 137
2019-01-16T21:33:30.881992+00:00 heroku[web.1]: State changed from crashed to starting
2019-01-16T21:33:36.542720+00:00 heroku[web.1]: Starting process with command `python3 run.py`
2019-01-16T21:33:38.407562+00:00 app[web.1]: * Serving Flask app "run" (lazy loading)
2019-01-16T21:33:38.407583+00:00 app[web.1]: * Environment: production
2019-01-16T21:33:38.407629+00:00 app[web.1]: WARNING: Do not use the development server in a production environment.
2019-01-16T21:33:38.407669+00:00 app[web.1]: Use a production WSGI server instead.
2019-01-16T21:33:38.407697+00:00 app[web.1]: * Debug mode: on
2019-01-16T21:33:38.425706+00:00 app[web.1]: * Running on http://127.0.0.1:12162/ (Press CTRL+C to quit)
2019-01-16T21:33:38.426543+00:00 app[web.1]: * Restarting with stat
2019-01-16T21:33:38.749701+00:00 app[web.1]: * Debugger is active!
2019-01-16T21:33:38.751246+00:00 app[web.1]: * Debugger PIN: 310-516-164
2019-01-16T21:34:36.926578+00:00 heroku[web.1]: Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch
2019-01-16T21:34:36.926654+00:00 heroku[web.1]: Stopping process with SIGKILL
2019-01-16T21:34:37.003507+00:00 heroku[web.1]: Process exited with status 137
2019-01-16T21:53:52.987682+00:00 heroku[web.1]: State changed from crashed to starting
2019-01-16T21:53:57.561585+00:00 heroku[web.1]: Starting process with command `python3 run.py`
2019-01-16T21:54:58.096583+00:00 heroku[web.1]: State changed from starting to crashed
2019-01-16T21:54:57.977555+00:00 heroku[web.1]: Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch
2019-01-16T21:54:57.977719+00:00 heroku[web.1]: Stopping process with SIGKILL
2019-01-16T21:54:58.079550+00:00 heroku[web.1]: Process exited with status 137
2019-01-16T21:57:43.000000+00:00 app[api]: Build started by user johnlynch.32768@gmail.com
2019-01-16T21:58:06.116939+00:00 app[api]: Deploy 17aecc4f by user johnlynch.32768@gmail.com
2019-01-16T21:58:06.116939+00:00 app[api]: Release v4 created by user johnlynch.32768@gmail.com
2019-01-16T21:58:07.402778+00:00 heroku[web.1]: State changed from crashed to starting
2019-01-16T21:58:15.446732+00:00 app[web.1]: * Serving Flask app "run" (lazy loading)
2019-01-16T21:58:15.446754+00:00 app[web.1]: * Environment: production
2019-01-16T21:58:15.446800+00:00 app[web.1]: WARNING: Do not use the development server in a production environment.
2019-01-16T21:58:15.446870+00:00 app[web.1]: Use a production WSGI server instead.
2019-01-16T21:58:15.446917+00:00 app[web.1]: * Debug mode: on
2019-01-16T21:58:15.525680+00:00 app[web.1]: * Running on http://127.0.0.1:35684/ (Press CTRL+C to quit)
2019-01-16T21:58:15.530464+00:00 app[web.1]: * Restarting with stat
2019-01-16T21:58:15.795617+00:00 app[web.1]: * Debugger is active!
2019-01-16T21:58:15.796647+00:00 app[web.1]: * Debugger PIN: 254-766-664
2019-01-16T21:58:19.000000+00:00 app[api]: Build succeeded
2019-01-16T21:59:13.659184+00:00 heroku[web.1]: State changed from starting to crashed
2019-01-16T21:59:17.123915+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=arith.herokuapp.com request_id=e2f52003-b11f-4a47-8364-a6afb3c67e7a fwd="80.233.31.148" dyno= connect= service= status=503 bytes= protocol=https
```
Tried again, and "Method Not Allowed" displayed.

I think I need to set the port and IP address, adjust the app.run() statement.

Consulted my notes.

```
22:24 /arith: 2061$ heroku ps:scale web=1
Scaling dynos... done, now running web at 1:Free
00:16 /arith: 2062$ 
```
Updated run.py to get IP & PORT.

Giving "Method not allowed"

Log says:
```
00:41 /arith: 2069$ history |grep tail
 2060  heroku logs --tail
 2069  history |grep tail
00:43 /arith: 2070$ !2060
heroku logs --tail

2019-01-16T21:33:30.715437+00:00 heroku[web.1]: Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch
2019-01-16T21:33:30.715437+00:00 heroku[web.1]: Stopping process with SIGKILL
2019-01-16T21:33:30.785251+00:00 heroku[web.1]: Process exited with status 137
2019-01-16T21:33:30.881992+00:00 heroku[web.1]: State changed from crashed to starting
2019-01-16T21:33:36.542720+00:00 heroku[web.1]: Starting process with command `python3 run.py`
2019-01-16T21:33:38.407562+00:00 app[web.1]: * Serving Flask app "run" (lazy loading)
2019-01-16T21:33:38.407583+00:00 app[web.1]: * Environment: production
2019-01-16T21:33:38.407629+00:00 app[web.1]: WARNING: Do not use the development server in a production environment.
2019-01-16T21:33:38.407669+00:00 app[web.1]: Use a production WSGI server instead.
2019-01-16T21:33:38.407697+00:00 app[web.1]: * Debug mode: on
2019-01-16T21:33:38.425706+00:00 app[web.1]: * Running on http://127.0.0.1:12162/ (Press CTRL+C to quit)
2019-01-16T21:33:38.426543+00:00 app[web.1]: * Restarting with stat
2019-01-16T21:33:38.749701+00:00 app[web.1]: * Debugger is active!
2019-01-16T21:33:38.751246+00:00 app[web.1]: * Debugger PIN: 310-516-164
2019-01-16T21:34:36.926578+00:00 heroku[web.1]: Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch
2019-01-16T21:34:36.926654+00:00 heroku[web.1]: Stopping process with SIGKILL
2019-01-16T21:34:37.003507+00:00 heroku[web.1]: Process exited with status 137
2019-01-16T21:53:52.987682+00:00 heroku[web.1]: State changed from crashed to starting
2019-01-16T21:53:57.561585+00:00 heroku[web.1]: Starting process with command `python3 run.py`
2019-01-16T21:54:58.096583+00:00 heroku[web.1]: State changed from starting to crashed
2019-01-16T21:54:57.977555+00:00 heroku[web.1]: Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch
2019-01-16T21:54:57.977719+00:00 heroku[web.1]: Stopping process with SIGKILL
2019-01-16T21:54:58.079550+00:00 heroku[web.1]: Process exited with status 137
2019-01-16T21:57:43.000000+00:00 app[api]: Build started by user johnlynch.32768@gmail.com
2019-01-16T21:58:06.116939+00:00 app[api]: Deploy 17aecc4f by user johnlynch.32768@gmail.com
2019-01-16T21:58:06.116939+00:00 app[api]: Release v4 created by user johnlynch.32768@gmail.com
2019-01-16T21:58:07.402778+00:00 heroku[web.1]: State changed from crashed to starting
2019-01-16T21:58:15.446732+00:00 app[web.1]: * Serving Flask app "run" (lazy loading)
2019-01-16T21:58:15.446754+00:00 app[web.1]: * Environment: production
2019-01-16T21:58:15.446800+00:00 app[web.1]: WARNING: Do not use the development server in a production environment.
2019-01-16T21:58:15.446870+00:00 app[web.1]: Use a production WSGI server instead.
2019-01-16T21:58:15.446917+00:00 app[web.1]: * Debug mode: on
2019-01-16T21:58:15.525680+00:00 app[web.1]: * Running on http://127.0.0.1:35684/ (Press CTRL+C to quit)
2019-01-16T21:58:15.530464+00:00 app[web.1]: * Restarting with stat
2019-01-16T21:58:15.795617+00:00 app[web.1]: * Debugger is active!
2019-01-16T21:58:15.796647+00:00 app[web.1]: * Debugger PIN: 254-766-664
2019-01-16T21:58:19.000000+00:00 app[api]: Build succeeded
2019-01-16T21:59:13.659184+00:00 heroku[web.1]: State changed from starting to crashed
2019-01-16T21:59:17.123915+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=arith.herokuapp.com request_id=e2f52003-b11f-4a47-8364-a6afb3c67e7a fwd="80.233.31.148" dyno= connect= service= status=503 bytes= protocol=https
2019-01-16T22:05:35.530023+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/favicon.ico" host=arith.herokuapp.com request_id=7224204d-5f30-447d-a3a9-19590c1eb1cb fwd="80.233.31.148" dyno= connect= service= status=503 bytes= protocol=https
2019-01-16T22:05:35.379541+00:00 heroku[router]: at=error code=H10 desc="App crashed" method=GET path="/" host=arith.herokuapp.com request_id=e6a9519f-1bdd-48b9-b5fe-160375b470b4 fwd="80.233.31.148" dyno= connect= service= status=503 bytes= protocol=https
2019-01-16T22:06:27.603828+00:00 heroku[web.1]: Starting process with command `python3 run.py`
2019-01-16T22:07:28.036537+00:00 heroku[web.1]: Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch
2019-01-16T22:07:28.036537+00:00 heroku[web.1]: Stopping process with SIGKILL
2019-01-16T22:07:28.273710+00:00 heroku[web.1]: Process exited with status 137
2019-01-16T22:28:16.041462+00:00 heroku[web.1]: State changed from crashed to starting
2019-01-16T22:28:25.261899+00:00 app[web.1]: * Serving Flask app "run" (lazy loading)
2019-01-16T22:28:25.261920+00:00 app[web.1]: * Environment: production
2019-01-16T22:28:25.261976+00:00 app[web.1]: WARNING: Do not use the development server in a production environment.
2019-01-16T22:28:25.267438+00:00 app[web.1]: Use a production WSGI server instead.
2019-01-16T22:28:25.267486+00:00 app[web.1]: * Debug mode: on
2019-01-16T22:28:25.371225+00:00 app[web.1]: * Running on http://127.0.0.1:41730/ (Press CTRL+C to quit)
2019-01-16T22:28:25.376247+00:00 app[web.1]: * Restarting with stat
2019-01-16T22:28:25.731210+00:00 app[web.1]: * Debugger is active!
2019-01-16T22:28:25.732603+00:00 app[web.1]: * Debugger PIN: 263-024-923
2019-01-16T22:29:05.678185+00:00 heroku[web.1]: State changed from crashed to starting
2019-01-16T23:14:31.512482+00:00 heroku[web.1]: State changed from starting to crashed
2019-01-17T00:26:36.569576+00:00 app[api]: Release v5 created by user johnlynch.32768@gmail.com
2019-01-17T00:26:38.689049+00:00 heroku[web.1]: State changed from crashed to starting
2019-01-17T00:26:46.176938+00:00 app[web.1]: * Serving Flask app "run" (lazy loading)
2019-01-17T00:26:46.176960+00:00 app[web.1]: * Environment: production
2019-01-17T00:26:46.177032+00:00 app[web.1]: WARNING: Do not use the development server in a production environment.
2019-01-17T00:26:46.177094+00:00 app[web.1]: Use a production WSGI server instead.
2019-01-17T00:26:46.177139+00:00 app[web.1]: * Debug mode: on
2019-01-17T00:26:46.249008+00:00 app[web.1]: * Running on http://127.0.0.1:10741/ (Press CTRL+C to quit)
2019-01-17T00:26:46.253278+00:00 app[web.1]: * Restarting with stat
2019-01-17T00:26:46.566478+00:00 app[web.1]: * Debugger is active!
2019-01-17T00:26:46.567968+00:00 app[web.1]: * Debugger PIN: 692-561-128
2019-01-17T00:27:43.884312+00:00 heroku[web.1]: State changed from starting to crashed
2019-01-17T00:27:43.960787+00:00 heroku[web.1]: State changed from crashed to starting
2019-01-17T00:27:43.785849+00:00 heroku[web.1]: Error R10 (Boot timeout) -> Web process failed to bind to $PORT within 60 seconds of launch
2019-01-17T00:27:43.785928+00:00 heroku[web.1]: Stopping process with SIGKILL
2019-01-17T00:27:43.861561+00:00 heroku[web.1]: Process exited with status 137
2019-01-17T00:27:50.901805+00:00 app[web.1]: * Serving Flask app "run" (lazy loading)
2019-01-17T00:27:50.901831+00:00 app[web.1]: * Environment: production
2019-01-17T00:27:50.901833+00:00 app[web.1]: WARNING: Do not use the development server in a production environment.
2019-01-17T00:27:50.901863+00:00 app[web.1]: Use a production WSGI server instead.
2019-01-17T00:27:50.901889+00:00 app[web.1]: * Debug mode: on
2019-01-17T00:27:50.957830+00:00 app[web.1]: * Running on http://127.0.0.1:23865/ (Press CTRL+C to quit)
2019-01-17T00:27:50.960631+00:00 app[web.1]: * Restarting with stat
2019-01-17T00:28:48.959263+00:00 heroku[web.1]: State changed from starting to crashed
2019-01-17T00:37:05.258742+00:00 app[web.1]: * Serving Flask app "run" (lazy loading)
2019-01-17T00:37:05.258773+00:00 app[web.1]: * Environment: production
2019-01-17T00:37:05.258775+00:00 app[web.1]: WARNING: Do not use the development server in a production environment.
2019-01-17T00:37:05.258808+00:00 app[web.1]: Use a production WSGI server instead.
2019-01-17T00:37:05.258834+00:00 app[web.1]: * Debug mode: on
2019-01-17T00:37:05.314720+00:00 app[web.1]: * Running on http://0.0.0.0:56872/ (Press CTRL+C to quit)
2019-01-17T00:37:05.317966+00:00 app[web.1]: * Restarting with stat
2019-01-17T00:37:09.939195+00:00 app[api]: Release v7 created by user johnlynch.32768@gmail.com
2019-01-17T00:37:11.297563+00:00 heroku[web.1]: Restarting
2019-01-17T00:37:18.178926+00:00 heroku[web.1]: Starting process with command `python3 run.py`
2019-01-17T00:37:22.038779+00:00 app[web.1]: * Serving Flask app "run" (lazy loading)
2019-01-17T00:37:22.038803+00:00 app[web.1]: * Environment: production
2019-01-17T00:37:22.038862+00:00 app[web.1]: WARNING: Do not use the development server in a production environment.
2019-01-17T00:37:22.038920+00:00 app[web.1]: Use a production WSGI server instead.
2019-01-17T00:37:22.038966+00:00 app[web.1]: * Debug mode: on
2019-01-17T00:37:22.136427+00:00 app[web.1]: * Running on http://0.0.0.0:43127/ (Press CTRL+C to quit)
2019-01-17T00:37:22.141383+00:00 app[web.1]: * Restarting with stat
2019-01-17T00:37:22.544621+00:00 app[web.1]: * Debugger is active!
2019-01-17T00:37:22.568490+00:00 app[web.1]: * Debugger PIN: 444-425-988
```
