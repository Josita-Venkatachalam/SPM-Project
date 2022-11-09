==================
INSTALLATION GUIDE
==================

(1) set up and run a WAMP or MAMP server

(2) execute the contents of 'database.sql' in phpMyAdmin, i.e. at:

       http://localhost/phpmyadmin  OR
	   http://localhost/phpMyAdmin

(3) find your web server's root directory (e.g. C:\wamp\www) and create a
    folder called 'SPM-Project'. Clone our repository into the folder.

(4) if you don't already have Flask installed, do:

	   python -m pip install flask
	   python -m pip install flask_cors
	   python -m pip install Flask-SQLAlchemy
	   python -m pip install mysql-connector-python

(5) in the 'flask' directory, run "python app.py" in a terminal.

(6) go to http://localhost/SPM-Project/ where the application should be working!


===============
TROUBLESHOOTING
===============

If running the Flask application gives you an error message along the lines
of "ProgrammingError: (mysql.connector.errors.ProgrammingError) Character set
'255' unsupported", then the following temporary 'fix' will resolve it:

	   python -m pip install mysql-connector-python==0.29



Overview of our app 

Database Setup
-If you are not performing testing, you may load the database.sql file to run the 5 core functionalities of our application. 
-However if you are performing testing, you can find the respective scripts needed for testing under the "Test Scripts" folder

1) CRUD Roles_
- login using login.html file by entering relavant credentials and click 'HR Login'
- Click on 'View All Roles' icon and it will bring you to 'View All Roles' page where you can see a table of all roles
- To perform updation or deletion of the roles click on the respective buttons
- To create a role you may click on the create role button at the bottom of the View All Roles table

2) CRUD skills
- login using login.html file by entering relavant credentials and click 'HR Login"
- Click on 'View All Skills' icon and it will bring you to 'View All Skills' page where you can see a table of all skills
- To perform updation or deletion of the skills click on the respective buttons
- To create a role you may click on the create role button at the bottom of the View All Skills table

3) Assigning skills to roles
- login using login.html file by entering relavant credentials and click 'HR Login'
- Click on 'View All Roles' icon and it will bring you to 'View All Roles' page where you can see a table of all roles
- Then for the role you want to assign skills to click on the "Assign Skills" button  which brings you to view all skills page
- Now you may click on the "Assign" or "Deassign" buttons for the respective skill you want to assign or deassign to the role you have already chosen

3) Assigning skills to courses
- login using login.html file by entering relavant credentials and click 'HR Login'
- Click on 'View All Courses' icon and it will bring you to 'View All Courses' page where you can see a table of all courses
- Then for the course you want to assign skills to click on the "Assign Skills" button  which brings you to view all skills page
- Now you may click on the "Assign" or "Deassign" buttons for the respective skill you want to assign or deassign to the course you have already chosen

4) Viewing and Deleting Learning Journeys
- login using login.html file by entering relavant credentials and click 'Staff Login'
- Click on 'View Learning Journey ' icon and it will bring you to 'View All Your Learning Journeys' page where you can see a table of all learning journeys of that user.
- To delete a learning journey simply click on the delete button on the same row of the learning journey

5)Creation of Learning Journey
- login using login.html file by entering relavant credentials and click 'Staff Login'
- Click on 'View Learning Journey ' icon and it will bring you to 'View All Your Learning Journeys' page where you can see a table of all learning journeys of that user.
- To create a new learning journey you may click on the "Create New Learning Journey"  button at the bottom of the View All Your Learning Journeys table
- You will be brough to View All Roles page to select your target role for the learning Journey
- After selecting role you will see a table of skills required to be fulfilled for your chosen role and to view the courses to be taken to fulfill each of these skills you may click on the "Look for Courses" button on the respective skill
- Once you have selected a skill you will be brought to Courses selection page where if you have already taken the course , it will indictae " Completed" otherwise, you will be able to see a checkbox for you to select the courses you want to take
- Once you have selected atleast 1 course, you will be able to officially create the learning journey by clicking on the "Create Learning Journey " button

6) Updating existing Learning Journey
- login using login.html file by entering relavant credentials and click 'Staff Login'
- Click on 'View Learning Journey ' icon and it will bring you to 'View All Your Learning Journeys' page where you can see a table of all learning journeys of that user.
- Click on the "Update" button for the learning journey which you want to Update
- Afterwhich you can select the skill for which you want to update the courses for
- Lastly you will can see the courses for the skill you have chosen with courses you are currently taking appearing with a button named "Remove" but courses you have not added to your learning journey will appear with button named "Add"
- Once you have made all the updates you wanted to, you may click on the "Back to View All Learning Journeys" button.
- Your changes to course selection will also be updated on the View Your Courses summary table which you can access from the homepage that you will see post login with an icon named " View Your Courses"





