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
