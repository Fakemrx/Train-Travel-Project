# Train-Travel-Project

My second Django project btw.
It includes such apps as: registration & authorisation, cities, trains, routes (based on cities & trains).

If you already authorised you can:
 - Add/delete city
 - Add/delete train
 - Add/delete favourite routes
 - Get and view extended information about cities/trains
 - Logout

If you are not an authorised user you can:
 - Login
 - Register
 - Find routes you want

The main feature of this project - foreign connections in models (e. g. Routes app model). App includes a lot of forms which are based on one template.
Also each page has a parent 'base' which adds Navbar, main buttons/links, messages of errors/warnings/successes. 
All design solutions were taken from bootstrap. There are no included js/css files (except select2). That project gave me main knowledges about Django and how work with it.
There's not so much ORM usage, but there are about 40% of app is covered by tests. I hope you liked it! (It's much better than Django blog)

To run this project on your PC you need to:
 - Clone project from git/download it as a .ZIP file. (In PyCharm go to Welcome menu -> Get from VCS -> Choose a Repository URL menu item -> Choose Git and paste HTTPS url to this project)
 - Install everything from requirements.txt (pip install -r requirements.txt)
 - Create vitrualenv (In PyCharm go to File -> Settings -> Project -> Python interpreter -> Add interpreter -> Add local -> Choose new/existing, but be sure to choose Python 3.9)
