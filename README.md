<h3>BLOGGER</h3>

<h1>Author</h1>

    Dan Kariuki

Description

    A python based appliaction which gives users the ability to post a Blog. Users can comment on other blogs or posts, and such posts can be moderated in view off their implicit and/or explicit inference towards other clients sentiments and perceptions.

<a href='https://forties.herokuapp.com/' live link>

<h2>User stories</h2>

    
    
    As a user, I would like to view the blog posts on the site
    As a user, I would like to comment on blog posts
    As a user, I would like to view the most recent posts
    As a user, I would like to an email alert when a new post is made by joining a subscription.
    As a user, I would like to see random quotes on the site
    As a writer, I would like to sign in to the blog.
    As a writer, I would also like to create a blog from the application.
    As a writer, I would like to delete comments that I find insulting or degrading.
    As a writer, I would like to update or delete blogs I have created.

    


|       Behaviour               |                   Input          |                 Output          |

|:On page load                  |: On page load                    |:  View the welcome page, Posts :|  

|: Select SignUp                |: Username, password,email        |:  Register.ConfirmationLink    :|

|:Confirmed User, Client, Writer|: Profile, Post, Comment          |:  Update&Comment Profile       :|

|:Submit                        |: Profile, Post,Comment           |:  Submitted                    :|


<h3>Development Installation</h3>
    To get the code..

    Cloning the repository:

https://github.com/Buttonupd/Scatter
  ```
2. Move to the folder and install requirements
```bash
cd pitchblog
pip3 install -r requirements.txt

    Exporting Configurations

export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

    Running the application

python3.7 manage.py server

    Testing the application

python3.7 manage.py test

    Open the application on your browser 127.0.0.1:5000.

Known Bugs
     
    There are no known bugs


Contact Info
    Dankariuki0101@gmail.com

Licence: MIT Licence





