

- Commands:
	- If virtualenv is being used then always start with "workon 'env_name'".
	- source /opt/homebrew/bin/virtualenvwrapper.sh
	1. django-admin startproject myproject: used to create a new project named 'myproject'.
	2. from django.urls import path: is used to import path django.urls, This is just a default Django function that allows us to configure URLs.
	    from . import views: is used 
	    urlpatterns= [path('', views.index, name= 'index')]: is used to specify a new URL.
	    This combined with path is what allows us to configure each URL.
	    when the (''(quotes)) is empty, that means this is the root URL.
	    If e.g.: we add '/download', that means the user has goes to our website/download.
	    When a user reaches the specified URL in the (''), what will happen.
	    To use views we need to import it from '.'. views.index is used to call the index function.
	    now we go to the views.py file and pass a function named index. Now whatever we do in the function(index) is going to be assigned to that particular URL(root URL in our case since ' ' are blank.
	    It goes to that URL and then what is done in that index function is going to be what is going to rendered to the user.
	    Anything can be used instead of name but that is used to avoid confusions, and give views.index kind of like an ID
	    
	3. python3 manage.py startapp: is used run project on our localhost, so we can see what we are building.
	4.  to show what we have done in views.py we need to import include along with path from django.urls in the urls.py file of myproject folder.
	    ![[Screenshot 2023-12-28 at 8.28.55 PM.png]]
	    
	    This is used to include myapp.urls, it goes into myapp directory and looks for similar urls to the one mentioned in myproject's urls.py
            
    5. Template: Django Template Language:
        ![[Screenshot 2023-12-29 at 12.34.03 AM.png]]
        
        We can create our own template files to use in django instead of the default one, all we need to do is create a folder containing our templates, go to settings.py and insert the root directory(BASE_DIR) and the folders' names. So what it will do is go to the root folder and look for the folders according to the name provided in settings.py, whatever is put in the 'DIRS': section of TEMPLATES must correlate with the name of the folder in the directory(templates in the above case).
        
        return render takes a request and name of the html page(template) in question. So we have a function that is taking a request and returns renders/rendering index.html.
        'render is used to render an html page.
        ![[Screenshot 2023-12-29 at 12.49.53 AM.png]]

In HTML there are 2 methods to submit a form: GET and POST.
	6.  Word counter in django:
		The name of the variable can be changed here it is text, but can be changed to anything we like, like words.
		![[Screenshot 2023-12-29 at 2.11.54 PM.png]]
		The text we type gets stored in that variable.
		To use the data stored in the variable we are gonna use an 'action', action is where we want all this data to send to.
		![[Screenshot 2023-12-29 at 2.45.28 PM.png]]
		There was a new variable and we use request.GET to be able to send a request to whatever is being passed to the particular view, and then we want to get it. And what we want to get is the 'words'.
		![[Screenshot 2023-12-29 at 2.49.55 PM.png]]
		Coming to the HTML page, we can see that we are sending the data(from textarea in the form) to 'counter'. And in the views.py we are getting that data in request.GET[words] (words can be changed to any other word only if it matches with the name of the variable that is used to store the input from the textarea).
		The method in the form is for us to know the type of method/request we are using. Its either a GET or POST method. 
		GET method is mostly used when we are not passing any personal information since it can be shown in the URL.
		In POST method the information that we are sending isn't going to be shown in the URL. 
		If we don't put/specify a method then it automatically uses GET method.
		POST needs to be specified.
		If we try to use it in our project then we'll get the following error:
		![[Screenshot 2023-12-29 at 3.47.16 PM.png]]
		Anytime we are using a POST method django expects us to use CSRF token.
		CSRF: Cross Site Request Forgery
		Its like an attack.
		Now when you're passing data through URLs, an attacker or someone that has bad intention for our site can tap into those and get that information by using this CSRF token. Django provides a default CSRF token which allow us to prevent that attack.
		7. Static Files in Django:
		In Django we need to tell where to locate the static files(unlike in normal HTML where the files only need to be linked using the link tag).
		The static files need to be stored in the static folder.
		We also need to go into the settings.py file(settings.py is the bedrock of the whole project).
		Go to myproject->settings.py.
		First we need to import the os(import os).
		It gets the specific OS we are working on.
		Then we need to get down to STATIC_URL, and under it we need to type STATICFILES_DIRS= (os.path.join(BASE_DIR, 'static')), 
		So what this is doing is that from OS its going to the base directory, which is also the root directory of the project(myproject), the folder that contains the manage.py file, and then it is going to the folder that has static.
		In that folder we create a file (e.g.: style.css).
		After making the necessary changes in the css file we need to link it to our main HTML file: 
		![[Screenshot 2023-12-29 at 8.02.09 PM.png]]
		As we can see we need to add something called static in href, since  the link is not seen by Django unless we add that.
		Now this alone won't make the color red, to do so we need to load it before we can use that tag. In Django whenever we need to load something we need to add it to the top of the file.
		![[Screenshot 2023-12-29 at 8.08.05 PM.png]]

Django models:
	In Django we don't need to write a single line of SQL code to get our database running. Here, there is something called model view template to do that. The model is whats used for our database, The view whats users see and the template are the pages we create.
	

View:
	
	![[Screenshot 2024-01-11 at 3.46.48 AM.png]]

Template:
	
	![[Screenshot 2024-01-11 at 3.45.26 AM.png]]

From the model we pass a lot of data into a template file.

The model is very easy to configure instead of using a database table or SQL code, we are just gonna use the classes in python to build a database.
	![[Screenshot 2024-01-11 at 3.54.00 AM.png]]

In models.py we can create a new model by creating new classes. like in the above example.

To use it in views we need to import that model from models.py so we use: 'from .models import Features'(example).
Now we can just make one of the functions in views.py inherit the Features.

	![[Screenshot 2024-01-11 at 4.00.15 AM.png]]
	
	![[Screenshot 2024-01-11 at 4.14.38 AM.png]]
	Changing Lorem ipsum to feature properties. 

in HTML, we don't see indentations, what we see is just code tags and code blocks. So that is what we also need to use to end our for loop. If we don't put an for loop here, what is going to happen is it is going to loop through all the watch code below these. And then we are going to see all this code multiple times and we're going to get all the images multiple times. And it's not what we want. So let's go back up here. And then this ends the for loop. In Python using the notation to end our if statement and our for loop. in HTML in the template, we used a code block for the tag or whatever you want to call it.
	![[Screenshot 2024-01-11 at 4.56.43 AM.png]]
    Unlike regular python we don't to use ''(quotes) to write: True. So, here True won't have quotes.
    We can also use elif and else along with if conditions here:
	    ![[Screenshot 2024-01-11 at 5.01.06 AM.png]]

This is how we can do some basic dynamic rendering in django.

Obviously, all these are just normal Python classes, which we are inheriting in our views right here. But we can make all these more advanced by turning them into real databases.

If we come to the root directory, we'll see that there's a file named sb.sqlite3.db. So this file is what stores all our database in Django. So when we create a new Django project, it would default automatically, we have your databases saved using SQL Lite.

Django uses SQL Lite by default.

So we want to change this class into a real django model and turn it into to a database, we need to add some things right here. For example, where we have this feature, what we just need to do is to say, open the bracket, and say models.Model. Now this converts this basic class into a model. And then whenever we're using this model, we don't need to add an ID again, because automatically each attribute or each object has an ID when it's created. So now we can
remove this. So now when we have name, we can change it to equals to. So now instead of writing str, we write something we'll say mode simply means character field, it means like a string of food that collects characters, now we're gonna open a bracket, and it takes one attribute, the attribute is Max length, So this max length is five the maximum amount of characters that can be inside this character field. And then details, it should also be a character field. And there are various type of fields a lot of fields in this django model the integer field, Boolean field etc.
	![[Screenshot 2024-01-11 at 5.55.20 AM.png]]
Now, there's something we need to do before this can be saved into our database. For now, this is just code in a file named models spy, we need to send all these fields into our database, so it can be registered right there. But before we do that, this app, in which we are doing all our project which is called myapp, we need to register it in our main project settings file, and then we can scroll all the way up, we will look for where we see installed apps right here. And then we can just add a new attribute myapp, and this is going to add this my app into our main project. So we need to add that before we can start integrating databases of this my app into our main projects. So now we need to migrate this data into our database. 
	![[Screenshot 2024-01-11 at 6.05.42 AM.png]]

Let's go back to our command prompt, and then just open a new command prompt, change directory to the current working one. So what want to do now is to type python manage.py make migrations. What this command line does is that it saves any changes we made in the models file. And then we can see, it says we created a model named Features. So it's gonna save that changes.
	![[Screenshot 2024-01-11 at 6.16.28 AM.png]]
And then first to send all these changes into our database, we need to migrate it by saying python manage.py migrate. So it's a two step method. First of all need to make migrations and then migrate. So to make migrations we need to do it any time we add or change anything in these models.py, if changes are made then we'll need to come in and do these two step again, make migrations and migrate. So it can be reflected in our database.
	![[Screenshot 2024-01-11 at 6.23.18 AM.png]]

We have content types, out admin content types, authentication, all these, and then applying myap.0001 initial. So what this is, is all this model we have in here. So right now our database has been migrated. But where did our database go exactly. So what just happened right now. We have something called the Django admin panel. So all these databases are being pushed, are being moved into these into the SQL lite database(db.sqlite3). How can we view it and edit it and control it as we like that where Django admin.py comes in. Now, obviously, if we are using Postgres or using any other interface, we can just easily use those interfaces because they are more advanced. But because we are starting from the basics of Django, we should learn to use Django admin.py first. 

So if we come to our project now, and then we go to slash admin, so your project slash admin, and we hit enter, we're gonna see that its gonna ask us to log in. So right here, we see it says we should log in, but with what details, we don't have any details we've never added, sign up and sign in, into our project. But this is an admin site, it is not our normal site, it has gone into another part of that site. Only we developers can get credentials to this particular site. And to do that, we're going to come into our command prompt. And then we're gonna say python manage.py createsuperuser. Now this command line creates super user. What it does is it creates an admin user. So right here we see  for user name, we can say admin, and then it asks for email address, we can skip that, and then it asks for password. So now this super user is created successfully, and we can use these to log in.
	![[Screenshot 2024-01-11 at 6.43.00 AM.png]]

So if we type admin, and we come here and just input the password, and enter, its gonna take us to an admin dashboard, as we can see right here, we can maintain and control our size, anyhow we like without even having an external database UI.
	![[Screenshot 2024-01-11 at 6.50.48 AM.png]] 
So if we come to this users we're gonna see all the users we have in our project. So right here, we only have one user which is admin. And that is us, which was the user we created, right here in the command line interface.
	![[Screenshot 2024-01-11 at 6.54.15 AM.png]]

So later, we are also going to integrate sign in and sign up. So once these are registered, it will be saved to this list. But what we want to do now is that we created this database named feature and migrated that into our database. But why aren't we seeing it here? So for this admin panel, there's a file in our project, which is controlling it, if we come right here, we're gonna see we have admin.py. So this file is where we need to register our models. So this Model Database, which we created, we need to import it here and register it in the admin, once that is done, it automatically is going to reflect here. So what we just need to do is to say: 'from .models import Features', and then we can just say: 'admin.site.register(Features)'. 
	![[Screenshot 2024-01-11 at 7.11.14 AM.png]]

After a refresh, we're gonna see now that we have a new database table named Features. And that we have no database there.
We can create a new database from the site itself now. e.g. For the previous example we can add/change the attributes(name and details from the site). After saving the addition/changes, we have one new object in our database.

Well, how can we get all this data that we have right here in our views, or in myproject. So what we need to make sure we're doing first of all, is that we're importing that feature, that feature model. So this model right here, is linked to this database. So once we can access this feature in our code, automatically, we can access all the values we have in this database. Now we're gonna have a new variable, named: feature= features.objects.all. So we have this new variable. And this new variable is getting from this feature that we imported. And it's saying  .objects.all. So this feature that we imported is in this database. 
	![[Screenshot 2024-01-11 at 7.45.59 AM.png]]

Now, each of the value we have in this database or each of the data is an object. So its from that feature database gets all the objects we have here, get every single thing as storage in this variable. And now this variable is a list. And then right you are passing it to the HTML.
	![[Screenshot 2024-01-11 at 7.53.31 AM.png]]

- User Registration:
	First we need to add a new url in urls.py named register.
	For that we add path('register', views.register, name='register') in the url patterns
	![[Screenshot 2024-01-11 at 8.41.45 PM.png]]
	And then in views.py make a new method register where the return is:  return render(request, 'register.html')
	![[Screenshot 2024-01-12 at 12.02.26 AM.png]]
	
	Now we create an HTML page named register
	where the user can register with username, email and password(the user needs to input the password 2 times to confirm it).
	![[Screenshot 2024-01-12 at 12.04.19 AM.png]]
	![[Screenshot 2024-01-12 at 12.04.47 AM.png]]
	Now since we are using POST method, therefore we need to give a csrf token too otherwise the page will throw an error towards the user.
	So we add it using: {% csrf token %}, right below form tag.
	![[Screenshot 2024-01-12 at 12.07.40 AM.png]]
	Now we need to be able to collect this data that the user inputs, to do so we go back to views.py and use a variable 'username' to store the data from username in the register html page, and do the same thing for password fields and email.
	Now all we need to do is save this in our database(the database accessible from the admin panel). This database is for the users active on our platform.
	But before doing all of this we need to check whether the request method is POST. We are supposed to take the inputs only if the method is POST. If POST is used that means something is being sent to views.py, but if this doesn't happen that means we are just looking for the normal register.html template.
	After checking that we need to make sure that the 2 input passwords are equal.
	So we use an if condition to check that to continue what we want to do, but before doing that there are some things we need to import. What we need to import is redirect.
	Redirect allows us to lets say we've created a user successfully, we want to take the user to another page, it allows us to redirect the user to another page.
	Then we need to import: from django.contrib.auth.models import User, auth
	The User here is the user model we've seen here, and then auth is the function or the method that allows us to authenticate.
	After that we import is messages: from django.contrib import messages
	Now that we have all this we can continue with our authentication.
	
	![[Screenshot 2024-01-12 at 2.21.24 AM.png]]
	
	![[Screenshot 2024-01-12 at 12.40.55 AM.png]]
	(do not forget to put ':' after POST in request.method== 'POST' )
	Coming back to checking password and password2 we also need to check as to whether if the email already exists in the database or not.  If it exists we'll want to throw an error using message.
	![[Screenshot 2024-01-12 at 2.39.14 AM.png]]
	So this is gonna check if the email already exists. If it exists, then we would want to throw an error message. So we are saying we want to filter the database and check, if there is an email, which already exists with this email that the user just submitted. So if that already exists, we want to send a message/response back if there's an error or anything. So since there's an error, which is that the email is already in use, so we say messages.info(request, 'Email already used').
	
	So if there is a message email already used, it is going to show up over here in red colour or something. And then we now want to return the user names, we don't want to continue with the signup process since the email is already used. So we redirect the user back to register. So what we just did, after sending/telling the user what happened, we just redirect the user back to register with these details right here. So the user has to go through that form again.
	
	Now we check for the username, as to whether it already exists or not, since we don't multiple accounts to have the same email or username.
	If it exists then we return the user back to the register page.

	 Now after checking both if email and username are unique, we go back to the main condition that is if password== password2, if it is true then a new user is to be created. So what we just did now was that we gave it a command that it should create a new user with these credentials. So these are the credentials in this credential. So when the user name equals to this user name, the email equals to this email and the password, we can just pick one from this one of these two passwords, since they are the same thing. So now that we have all those details, we can just go ahead and save that user. Now that a user has been created successfully, they should be redirected to the login page where they try to to login and see if their credentials can be used to login successfully.
	 Now if the password and password2 are not equal we can use an else condition and messages to tell the user that the passwords don't match.
	 (else:
		 messages.info(request, 'Passwords aren't the same.'))
	Then we just redirect the user back to the register page.
	
	![[Screenshot 2024-01-12 at 4.29.37 AM.png]]
	
	![[Screenshot 2024-01-12 at 4.43.03 AM.png]]
	
	Now after all this is loaded, then we check the first condition which was if the request method is 'POST' or not, if it isn't(if it is just normal request on this page) then we tell it to render register.html page.
	Now to show messages if there is any error, we can just use a for loop to show the appropriate message according to the error(the messages from messages.info). This is all done in register.html
	
	![[Screenshot 2024-01-12 at 4.37.03 AM.png]]
	Now the user can be successfully created and stored in the database but we still need them to be able to log in but right now we don't have any url for login, so the next step is to create a login page.

- User Login And Logout In Django:
	The first step is to go to urls.py and add: path('login',  views.login, name='login') in the urlpatterns.
	
	![[Screenshot 2024-01-12 at 5.47.12 AM.png]]
	
	Now we need to create a function named login in the views.py file.
	Here, the return is: return render(request, 'login.html')
	
	![[Screenshot 2024-01-12 at 5.49.04 AM.png]]
	
	Now we create a new file in templates named login.html.
	
	![[Screenshot 2024-01-12 at 5.50.36 AM.png]]
	
	Now just like in register we will check if the request method is 'POST' first.
	Also, we will store the data from the input in variables if the condition is true.
	Then we will use user attribute to authenticate the username password received from the user.
	(user= auth.authenticate(username=username, password=password(user should be equal to auth.......))).
	Now we can log the user in but before that what if the data/information provided by the user is incorrect? So there should be a check for that.
	
	If user is None, that means the user is fake. That means the user is not on our platform.
	
	If it is not None, that means that the user is really on our platform and is registered.
	Then we can use: auth.login(request, user)
	So that we know that the user is real, and after login design we can now redirect user to the home page.
	
	But what if the user is not registered? for that we send a message using: messages.info(request, 'Credentials are Invalid').
	
	And then we need to redirect the user back to the login page.
	
	Now if the first condition that request method is 'POST' is false, then we put the else condition:
	else:
		return render(request, 'login.html')
	
	![[Screenshot 2024-01-12 at 6.21.07 AM.png]]
	
	After doing all this we go back to our login.html and add a for loop for the messages.
	
	![[Screenshot 2024-01-12 at 6.22.38 AM.png]]
	
	As an extra we will change One Page Bootstrap to Welcome (username).
	Above One Page Bootstrap we will add an if condition: {% if user.is_authenticated %}(This is used to check if the user is logged in)
	< h1 >Welcome {{user.username}}' < /h1 >
	
	This will get the current user that is loading and get its username.
	Now what if the user is just a random guest user visiting, then we just add an else statement and put the previous heading for One Page Bootstrap in there.
	
	![[Screenshot 2024-01-12 at 6.43.31 AM.png]]
	
	Now according to whether the user is logged in or not the the page will be/look different, that is where we're talking about dynamic values, the same page, the same code, the same everything, but different output.
	
	We can also do the same thing for the other options, where we see the services, etc. If the user is not logged in, like if the user is just here, we can change all this to log in and sign up. And then once a user is logged in, we continue to log out.
	
	So we've talked about how the user can register on our platform. We've talked about how they can log in on our platform. But we have not talked about this, how a user can log out. So we need to add a lot of functionality. So we don't always have to restart our platform, or just be trying to clear cookies every time time the user wants to log out.
	
	So we just have to put a button in the page, which says log out, which once clicked will log the user out.
	
	What we want to do is use that if statement again, and see that if the user is logged in, then what want to show there is logout, but when the user is not logged in, what we want to show is login.
	
	![[Screenshot 2024-01-12 at 7.07.11 AM.png]]
	
	So now the same button, but different texts. This is dynamic. Now we need to add the links to login and logout too so we simply write: href= "login" and href= "logout" for login and logout pages.
	
	So if a user is not logged in, they can click here and go to the login page and we can also add a button below if they don't have an account then they can create one by signing up.
	
	So what we want to do now is logout.
	First we go to urls.py to create a path in urlpatterns.
	
	![[Screenshot 2024-01-12 at 7.17.39 AM.png]]
	
	Then we go to views.py and create a function to logout where in the function we write auth.logout(request).
	So this single line of code will log the user out of our platform.
	And then once the user has been logged out of the platform, we want return and redirect the user back to the home page.
	
	![[Screenshot 2024-01-12 at 7.25.46 AM.png]]
	
	![[Screenshot 2024-01-12 at 7.27.35 AM.png]]

- Dynamic Url Routing In Django:
	Dynamic URLs is to for example, we have the same URL but with different ID passed in it. Let's say we have this as our website slash Tomi. So our website slash Tom and then this is the File page one is going to give us an error because we don't have anything like that. But let's assume this is the profile page for this user named Tomi. And then we also have user name Tim. And then we also have for a user named John. So let's say we have for every user on our website, they each have a profile page. So for us to code this, it is just going to be one page, we are going to code. But because it is getting different user name, it is going give different outputs. So that is dynamic URL routing, different URL being passed, or different values being passed in the URL.
	
	![[Screenshot 2024-01-12 at 9.35.23 PM.png]]
	
	Now lets make an example, lets go to urls.py, here in urlpatterns we write: path('post/<str:pk>').  So what this means is that we're having slash posts or website slash posts, then slash strings. And we are naming the string pk. So it's just like a variable. So the variable is named pk and is a string, if we want it to be an integer, we can just say, 'int' then views.post and we can give it a name 'post'.
	So now first, to be able to collect this in our views, we need to come here now. Add another new function in view say, post, and we're gonna take a request. And after this view, taking a request it is also going to take that particular variable which has been passed, which is called 'pk'. And then now what we just want to do is to say, so we have this 'pk', and it then can: return render(request, 'post.html'). So now lets create a new file, named 'post.html'. Now let's send whatever value is in that URL to this 'post.html. So we can see {'pk':pk}.
	
	![[Screenshot 2024-01-12 at 9.47.53 PM.png]]

	 Now let's save this and got to post.html and write 'The value in the url is {{pk}}'.
	 
	 ![[Screenshot 2024-01-12 at 9.48.07 PM.png]]
	 
	 Now if we go back to the browser and write '127.0.1:8000/post/12' then we can see that it says 'The value in the url is 12'
	 
	 ![[Screenshot 2024-01-12 at 9.50.49 PM.png]]
	 
	 So whatever is in this url, if it is like tim, then it changes to Tim.
	 
	 ![[Screenshot 2024-01-12 at 9.58.26 PM.png]]
	 
	 (used h1 headings for making it look more bold and big)
	 So is dynamic, whatever we pass in the URL. This is what is used in most sites, like when you have a profile page, which is like john, and then you see the name of the person john. We can change the username from the top and get the profile page, posts everything we need about a specific user.
	 So it is still one same template file, one same code, but different outputs relating to what has been passed, or query to form in the URL. So that is what we mean by dynamic URLs.
	 Now, we can also add some more features like right here, in the URLs. We can have our integer(int) here. So now this is an integer. If we come here, and then we hit refresh, we're gonna see that page not found. Why did that happen? This is simply because we write in our code, we say we want only an integer right here. If anything, apart from an integer is being passed in the URL, we receive page not found, so it's not part of our code/it is not part of our project. whereby if we change this now to 98. We see, now it says the value here is 98. That is because it sees what we told it to ask for, it sees what we told it to look for. So that's the same thing we can do with any type, any file, any data type. 
	 
	 ![[Screenshot 2024-01-12 at 10.14.02 PM.png]]
	 
	![[Screenshot 2024-01-12 at 10.14.52 PM.png]]
	
	![[Screenshot 2024-01-12 at 10.15.27 PM.png]]
	
	But the good thing with string, is that we can put in an integer in a string, and it's gonna see it as a string, even if we mean it as an integer. So most of the times we would want to use string because it helps us avoid running into arrows.

- Postgresql setup:
	![[Screenshot 2024-01-13 at 3.22.15 AM.png]]
	
	![[Screenshot 2024-01-13 at 3.23.16 AM.png]]
	
	![[Screenshot 2024-01-13 at 3.24.01 AM.png]]
	
	![[Screenshot 2024-01-13 at 3.24.37 AM.png]]
	
	('PASSWORD' will have the master password setup for postgre)
	
	![[Screenshot 2024-01-13 at 3.25.31 AM.png]]
	
	![[Screenshot 2024-01-13 at 3.26.02 AM.png]]
	These 2 libraries are gonna allow us to connect postgres to our django project. Without them we will get errors.
	This pillow takes care of everything. Let's say we have a database that deals with images or files, this pillow takes care of it and helps to connect them together.
	
	![[Screenshot 2024-01-13 at 3.34.41 AM.png]]
	
	![[Screenshot 2024-01-13 at 3.41.24 AM.png]]
	
	It is performing the migrations but this time taking into Postgres.
	
	![[Screenshot 2024-01-13 at 3.43.16 AM.png]]
	
	![[Screenshot 2024-01-13 at 3.43.36 AM.png]]
	
	So now we will come back to Postgres and on Tables, right click on it refresh, we're gonna see that we now have a bunch of tables, even with that model, which we created my app underscore feature.
	
	![[Screenshot 2024-01-13 at 3.46.15 AM.png]]
	
	![[Screenshot 2024-01-13 at 3.46.47 AM.png]]
	It shows all the data base, which we've saved from our admin panel earlier on.
	It should show us right here, because we migrated everything here.
	So we can do the same for MySQL or Roku, they also have similar processes. It should prove more helpful to use some external database than just using the default sqlite.
	So right now, this is it. And the data output we do not have anything right here. But now if we use like if we create a new one now it should show right here.
	So this is how to connect Postgres to your Django project.

Building a blog with Django:
	![[Screenshot 2024-01-13 at 11.09.48 PM.png]]
	
	![[Screenshot 2024-01-13 at 11.11.21 PM.png]]
	
	![[Screenshot 2024-01-13 at 11.11.48 PM.png]]
	
	![[Screenshot 2024-01-13 at 11.12.40 PM.png]]
	
	![[Screenshot 2024-01-13 at 11.13.45 PM.png]]
	Drag/Put index.html in the blog folder.
	So we're going to write URL patterns. Again, there'll be a list, and we're going to save path. And when we leave it blank like this, it means the home URL.
	![[Screenshot 2024-01-13 at 11.24.06 PM.png]]
	 from django.urls import path: is used to import path django.urls, This is just a default Django function that allows us to configure URLs.
	 Now if we put something like notifications, what this mean is slash notification or website slash notification. When we leave it blank, it means the home URL.
	
	![[Screenshot 2024-01-13 at 11.24.25 PM.png]]
	
	![[Screenshot 2024-01-13 at 11.25.06 PM.png]]
	So now we can write views.index, and we can give it a name of index. So this is saying that once a user comes to the home, it should go to the views.index function. So that means in this views.py file, it should look for an index function and then do whatever was being asked to do.
	
	![[Screenshot 2024-01-14 at 12.24.24 AM.png]]
	
	![[Screenshot 2024-01-14 at 12.29.11 AM.png]]
	
	![[Screenshot 2024-01-14 at 12.30.14 AM.png]]
	
	![[Screenshot 2024-01-14 at 12.30.35 AM.png]]
	
	![[Screenshot 2024-01-14 at 12.31.36 AM.png]]
	Now, what this is saying is that whenever a user requires an index, an HTML page, it should go to the base directory, which is the root directory, then it should go into the folder named templates, and look for that exact HTML page. So when we're trying to render this HTML page index.html, is going to request for this index.html in the root directory. And then it's going to look for a template name, a folder named templates, and then gets that index.html.
	
	![[Screenshot 2024-01-14 at 12.35.20 AM.png]]
	And now this can be rendered.
	
	![[Screenshot 2024-01-14 at 12.36.22 AM.png]]
	But if we come here and hit refresh button, nothing still happens. And this is because we configured all this in our app(posts), we need to configure it for our main project(blog). So that our project knows where to look for a URL.
	Now, for us to do this, we're gonna write: from django.urls import path, (we also have to import->) include. And then we can write:  path('', include('posts.url')).
	
	![[Screenshot 2024-01-14 at 12.43.43 AM.png]]
	Now what this is saying is that once a user comes to the home, which is just the main website, it should include the home URL in posts.url, which is this. So it's going to look for something similar to this. 
	
	![[Screenshot 2024-01-14 at 12.29.11 AM 1.png]]
	Now we come here to refresh, we can see now that we have this HTML page.
	
	![[Screenshot 2024-01-14 at 1.06.02 AM.png]]
	We have a written setup, we have a front end setup.
	Now, what we need to do is to create a database that is going to store all our blog posts. So it's going to store the title of the blog post, when the blog post was created, and then the main body and the main text of the blog post. So we're going to come into models.py, where we are gonna create a new django model.
	
	![[Screenshot 2024-01-14 at 1.12.50 AM.png]]
	
	![[Screenshot 2024-01-14 at 1.13.42 AM.png]]
	
	![[Screenshot 2024-01-14 at 1.14.11 AM.png]]
	Now, we migrated this model to our database, but we didn't save it or showcase it in our admin panel. To do this we are going to have to come to admin.py.
	
	![[Screenshot 2024-01-14 at 1.28.13 AM.png]]
	
	![[Screenshot 2024-01-14 at 1.39.31 AM.png]]
	So now we have 3 posts, we have 3 blog posts on our blog. And now we just want to assess everything right here, instead of just having the dummy data.
	
	![[Screenshot 2024-01-14 at 1.42.13 AM.png]]
	So now we want to make this dynamic, right now this is all static.
	We're gonna get all this from our database.
	
	![[Screenshot 2024-01-14 at 1.43.43 AM.png]]
	
	![[Screenshot 2024-01-14 at 1.44.16 AM.png]]
	
	![[Screenshot 2024-01-14 at 1.44.47 AM.png]]
	So in this particular line, we have a variable and we are giving it posts, which is this posts(Post) we imported: Post.objects.all(), that means we're getting all the objects from this database right here, we can see these as object one object to object three in the admin panel. So we're getting all the objects, saving them there, and then we're passing it into our template, which is index.html'.
	
	![[Screenshot 2024-01-14 at 2.11.40 AM.png]]
	To show the blog posts from latest to oldest we can use 'reversed' with for loop.
	Now we don't want the user to be able to read the whole blog post from the home page.
	
	![[Screenshot 2024-01-14 at 2.18.33 AM.png]]
	using truncatewords we can truncate the paragraph to just the specified amount of words we want, like in the above example, the body gets truncated to 20 words.
	
	![[Screenshot 2024-01-14 at 2.21.22 AM.png]]
	Now we need to make the posts clickable so that the user can click the link and read the post on a different post.
	
	![[Screenshot 2024-01-14 at 2.27.27 AM.png]]
	To check whether they have turned into links or not.
	Now we need to make it so such that we click on a link it should take us to a dynamic and unique page.
	
	![[Screenshot 2024-01-14 at 2.31.50 AM.png]]
	
	![[Screenshot 2024-01-14 at 2.32.46 AM.png]]
	So we want to get all the data here, so we once like once a user clicks on this, it is gonna take us to that /posts, but it's gonna be like /posts/1, /post/2, different pages for different urls.
	So these blog posts since it is the first post it is gonna have an ID of 1. So it can be /post/1, this can be /post/2, this can be /post/3.
	And then we're gonna get all this dynamically from the database.
	
	![[Screenshot 2024-01-14 at 2.38.12 AM.png]]
	Right here, we can just say, we can give it an integer or a string, but a string is preferred to avoid any errors. So a string, which is pk, so this is a post/(a string, which is)pk.
	
	![[Screenshot 2024-01-14 at 2.56.37 AM.png]]
	In post we write a variable 'posts' whose value is Post.object.get(id=pk), this is used to get the object from Post whose id=pk.
	So once we have these, we just simply pass it to the HTML, let's copy that here and paste.
	
	![[Screenshot 2024-01-14 at 2.47.36 AM.png]]
	
	![[Screenshot 2024-01-14 at 2.47.49 AM.png]]
	So obviously, this'll have an ID of one because it's the first or maybe an ID of zero, maybe. But once we get the ID, it is gonna be passed in this URL and from the URL it is going to be passed in views. We can see that this function is getting that pk, which is the name we gave it right here. And then from that pk, we are using to to filter our database. So we've added a new variable. And then once it's been assigned to that variable posts, which is our model(Post in this case).object.get, so it's going to get to that particular posts, which has the ID of pk. So then once we have that, we're just passing it to our post.html. Because what we did in our index.html, we can go there now and access that post.
	
	![[Screenshot 2024-01-14 at 3.01.14 AM.png]]

Weather Detector:
	![[Screenshot 2024-01-14 at 3.50.33 AM.png]]
	
	![[Screenshot 2024-01-14 at 3.52.35 AM.png]]
	
	![[Screenshot 2024-01-14 at 4.00.53 AM.png]]
	
	![[Screenshot 2024-01-14 at 4.03.14 AM.png]]
	
	![[Screenshot 2024-01-14 at 4.05.52 AM.png]]
	
	![[Screenshot 2024-01-14 at 4.11.18 AM.png]]
	
	![[Screenshot 2024-01-14 at 4.14.43 AM.png]]
	Now what this is doing is that we're creating another home URL, we're now in the urls.py file of the main project. And then once it comes to this one, it should include weather or not URLs that means weather is this app, which we created right here. And then we go to the urls.py file of it. And then anything we do to the same path is what should be done.
	It's just including the urls. So if we come here, we see we have the same blank path. So anything we do here, what we're doing here is taking views.index, and what are we doing with this view.index is rendering this index.html.
	
	![[Screenshot 2024-01-14 at 4.33.00 AM.png]]
	
	![[Screenshot 2024-01-14 at 4.35.15 AM.png]]
	
	![[Screenshot 2024-01-14 at 4.47.59 AM.png]]
	
	![[Screenshot 2024-01-14 at 4.49.29 AM.png]]
	
	![[Screenshot 2024-01-14 at 4.50.34 AM.png]]
	So it says local variable city referred before assignment. Now this unbound error always happens, anytime you are using an if statement, and there is a variable been assigned without adding an else statement. Now we just need to do else.
	
	![[Screenshot 2024-01-14 at 4.52.45 AM.png]]
	We're gonna be using an API, which is called Open weather map. So it's a website, which has an API for us to use. So we can get those details(country code, temperature etc.) from their website. But before we can use their API, we have to sign up to their site, it's totally free.
	
	![[Screenshot 2024-01-14 at 5.05.58 AM.png]]
	JSON: When we send a request to the API, its going to give us a response in a JSON format. So we need to import JSON to be able to actually get pass or filter this data. And then we need to import urllib.request.
	
	![[Screenshot 2024-01-14 at 5.15.25 AM.png]]
	Now this res is the request we are sending to openweathermap.
	
	![[Screenshot 2024-01-14 at 5.19.36 AM.png]]
	So we want to open a particular url, and that url is going to be ('http://api.openweathermap.org/data/2.5/weather?q=' +city
	q is the parameter here, q is going to be the city.
	q actually means query. The city we actually want to get the details of, and then we use concatenation and then city. After adding the city what we need to add now is our api key, before that we add '&appid=' first: '&appid= (api_key)').read()
	
	![[Screenshot 2024-01-14 at 5.21.07 AM.png]]
	
	![[Screenshot 2024-01-14 at 5.57.35 AM.png]]
	
	![[Screenshot 2024-01-14 at 5.26.29 AM.png]]
	
	![[Screenshot 2024-01-14 at 5.29.56 AM.png]]
	
	![[Screenshot 2024-01-14 at 5.34.20 AM.png]]
	This is the data we after passing a request to this url.
	
	![[Screenshot 2024-01-14 at 5.41.37 AM.png]]
	So now we have the current weather details of this city stored in this json_data.
	But now we need to change this json data into a python dictionary so that it is easier to access.
	
	![[Screenshot 2024-01-14 at 5.47.22 AM.png]]
	
	![[Screenshot 2024-01-14 at 5.48.05 AM.png]]
	Now we can access this from our HTML."
	
	![[Screenshot 2024-01-14 at 5.59.18 AM.png]]
	
	![[Screenshot 2024-01-14 at 6.01.07 AM.png]]
	Now it will start seeing data as a normal variable again, so to access the data as a dictionary we need to do the following.
	
	![[Screenshot 2024-01-14 at 6.03.38 AM.png]]
	
	![[Screenshot 2024-01-14 at 6.04.55 AM.png]]
	This is to hide the details until they've been searched for. This says if data.country_code is like above then it should show everything.

Django Real-time chatapp:
	![[Screenshot 2024-01-14 at 10.01.25 AM.png]]
	
	![[Screenshot 2024-01-14 at 10.02.05 AM.png]]
	
	![[Screenshot 2024-01-14 at 10.03.42 AM.png]]
	
	![[Screenshot 2024-01-14 at 10.06.04 AM.png]]
	
	![[Screenshot 2024-01-14 at 10.06.30 AM.png]]
	
	![[Screenshot 2024-01-14 at 10.06.51 AM.png]]
	
	![[Screenshot 2024-01-14 at 10.10.47 AM.png]]
	
	![[Screenshot 2024-01-14 at 10.08.53 AM.png]]
	
	![[Screenshot 2024-01-14 at 10.09.17 AM.png]]
	
	![[Screenshot 2024-01-14 at 10.09.55 AM.png]]
	
	![[Screenshot 2024-01-14 at 10.11.19 AM.png]]
	So now that we have this, what we want to do is to set up the model that we're going to be using in this project. So we're going to set up 2 models, the 1st is going to be for the chatroom, and the 2nd one is going to be for the messages.
	
	![[Screenshot 2024-01-14 at 10.16.48 AM.png]]
	Message is the model or database that stores all the messages. We can use another Django model, like a relationship model, like the many to many field, the foreign key to link this with this room.
	
	![[Screenshot 2024-01-14 at 8.31.09 PM.png]]
	
	![[Screenshot 2024-01-14 at 8.31.27 PM.png]]
	
	![[Screenshot 2024-01-14 at 8.32.05 PM.png]]
	
	![[Screenshot 2024-01-14 at 8.32.54 PM.png]]
	
	![[Screenshot 2024-01-14 at 8.57.40 PM.png]]
	So now that we've created this home.html, we need to connect it to the room.html page and check: If it's a new room, that means if someone has not created it before, we first of all want to create this room, and then enter, but if there is a room that already exists, we just want to enter the room and see all the messages.
	
	![[Screenshot 2024-01-14 at 9.01.28 PM.png]]
	Now we need to add a new path, and its gonna be the path for room.html.  This one is going to be a dynamic one.  So we write: path('<str:rooms>/'(So this is string/room/(anything we want to add to it)), views.room, name= 'room')
	
	![[Screenshot 2024-01-14 at 9.06.00 PM.png]]
	So this is not just taking a request, we can see in the urls.py file that we're passing a variable into this particular url named room. So we need to come into views and also collect room.
	
	![[Screenshot 2024-01-14 at 9.08.42 PM.png]]
	Now we need to go to home.html, go to form and here, we need to set this form to an action that once the user clicks on 'Submit'. If we first send data to the views that will check, if this particular room is set or not.
	
	![[Screenshot 2024-01-14 at 9.15.49 PM.png]]
	
	![[Screenshot 2024-01-14 at 9.16.20 PM.png]]
	So now we have this(room.html) url, so if we go to anything, it is automatically going to see that as a room. Now we go to home.html, here, we are going to add some things to our form. The method is going to be check method, action is going to be checkview(where it is going), we add a csrf token, so now we are sending the room and username to this checkview.
	
	![[Screenshot 2024-01-14 at 9.22.20 PM.png]]
	Now in our checkview, before we do anything, we need to check if that room name exists in our database.
	First we need to import somethings.
	Then we create some variables room and username, and pass 'room_name' and 'username'.
	Then we check: if room.objects.filter(name=room).exists():(this checks if there is an object in this room model, which has the name of the room, that the user sent), and if it exists then we need to redirect this room(which is specified in the room function). But before we can redirect we need to import it)
	return redirect('/'+room+'/?username='+username)(we're redirecting the user to /room(and then we don't need to say that name, because we already have that name, and we know it exists. And we also want to pass the username of the person that wants to enter that room. So we're sending a message with entering  and doing stuff like that. Now we can just write '/?username='+username, so thats how we took the username).
	But if this is a new room that the user is just creating, what we want to do is have a new variable which should be = Room.objects.create(name=room), so we want to create new room with the name of room.So we're gonna get that room and then create a new room with that particular name.
	After that we just write new_room.save().
	So now once this is saved we can redirect the user to that page, exactly the same thing we did back in the if condition.
	
	![[Screenshot 2024-01-14 at 10.33.16 PM.png]]
	 
	 ![[Screenshot 2024-01-14 at 10.46.17 PM.png]]
	 So lets say e.g.: we created a room named Coders. It takes us to this particular url named Coders.
	 
	 ![[Screenshot 2024-01-14 at 10.48.28 PM.png]]
	 So this is our/Coders then username=. So we have the name of the room and then username, so the user that entered this room.
	 
	 ![[Screenshot 2024-01-14 at 10.51.02 PM.png]]
	 And then when we come here and hit refresh, we can see that our room has been created successfully(Name of the room is coders).
	 
	 ![[Screenshot 2024-01-14 at 10.52.52 PM.png]]
	 Now if we go in the Room again but with a different username, if we hit refresh we see that we don't have a new object created.
	 
	![[Screenshot 2024-01-14 at 10.56.00 PM.png]]
	It just takes us into the existing one.
	Now we need to make it so such that if the user inputs a message hits send, we need the message to be stored in the database with the details of this room and the user.
	Now we go to room.html.
	Here, we're going to create some things which are going to allow us to submit it.
	So in the form we're going to add the csrf token.
	
	![[Screenshot 2024-01-14 at 11.04.21 PM.png]]
	Just to make sure that whenever we use a POST method, everything works. Here we don't write method= 'POST' because we're going to be using AJAX to submit this form. So if we come here, normally and type in a message and hit send, that page is gonna reload.
	
	![[Screenshot 2024-01-14 at 11.08.13 PM.png]]
	Thats what we don't want in our chat. So we want it to be in real time. We want everything to happen without this page even thinking of refreshing. So once we hit something its gonna send and we want it sent, without the page refreshing it is gonna be created in our message database.
	
	![[Screenshot 2024-01-14 at 11.12.52 PM.png]]
	And then later on we're also going to show it automatically in real time, without page refreshing. This is where AJAX comes in. It allows us to do things like get database in real time, asynchronously, and some other features that we can use with django. Ajax is used with JavaScript. So we're gonna be using some basic JavaScript. To use Ajax, we just need to make sure that we have the following line/script loaded in our template file.
	
	![[Screenshot 2024-01-14 at 11.18.15 PM.png]]
	
	![[Screenshot 2024-01-14 at 11.18.49 PM.png]]
	
	![[Screenshot 2024-01-14 at 11.19.20 PM.png]]
	Once we have that imported, we're good to go.
	So first of all, we have this form, so we want to click send. Here, we have 4 inputs, but we only have 2 inputs shown. 
	
	![[Screenshot 2024-01-14 at 11.20.10 PM.png]]
	
	![[Screenshot 2024-01-14 at 11.22.44 PM.png]]
	Because the type of these are hidden. So we don't want the user to write anything new, we're gonna give it a value ourselves. The user is the current user that is logged in, and then the room ID is the ID of this room the user is in. 
	
	![[Screenshot 2024-01-14 at 11.25.12 PM.png]]
	Now we go to our views and get the 2 hidden details, after getting them we pass them back to room.html and then implement it in our form. 
	
	![[Screenshot 2024-01-14 at 11.29.27 PM.png]]
	So what this code does, is that the username is being passed in this room, we have that read. 
	Now since we have the name of that room, we're gonna use this name to access the database.
	
	![[Screenshot 2024-01-14 at 11.32.37 PM.png]]
	So what this is doing is that, we have a new variable, and then from this room model .object.get is getting the particular model which has the name of this room(Coders in this case). Now that we have the details that we need, all we need to do now is to pass it our HTML.
	
	![[Screenshot 2024-01-14 at 11.37.07 PM.png]]
	So now we have all of this sent to our HTML.Now in our HTML we should be able to access this. 
	
	![[Screenshot 2024-01-14 at 11.55.23 PM.png]]
	
	![[Screenshot 2024-01-14 at 11.55.50 PM.png]]
	
	![[Screenshot 2024-01-14 at 11.57.06 PM.png]]
	So as we can see this room_details is that particular room from the model.
	
	![[Screenshot 2024-01-14 at 11.58.40 PM.png]]
	So what we're doing here is getting that particular model and getting this ID(from the html page).
	Remember once we have a new object , it automatically has an ID.  and we get that ID. Now that we have all of this we should be good to go for using our Ajax.
	
	![[Screenshot 2024-01-14 at 11.59.29 PM.png]]
	So to use Ajax we're gonna open up a new script below the end of body tag.
	
	![[Screenshot 2024-01-15 at 12.11.41 AM.png]]
	So what this code does line by line is that:
	1. document- what this is doing is that once we load this document form, we're saying that this .on('submit') of this post form, when a user clicks on the submit button of this post form(the submit button created above). We want to have a function here and we want to give this 'e' value. So we'll write e.preventDeafault(). So what this prevent default does is that normally in a form once we hit submit, the page is going to refresh or go to another page. So this prevent default is gonna prevent from reloading or going to another page. Now we know that the page isn't gonna reload. Now we're gonna use our Ajax to send those details to our database. 
	2. So what we're doing now is that we're writing ajax, and then we're writing the type is POST. Normally when we're aren't using ajax, we know well, we're gonna use something like method. But since we're using ajax we don't need that. So already accessing the type 'POST', and url is sending is sending it to send. And then the data is just basically what the data username with the #username,room id and then the message. Everything is there in the form. Thats just what we're sending.
	
	![[Screenshot 2024-01-15 at 12.29.13 AM.png]]
	3. And then the csrf token:
	
	![[Screenshot 2024-01-15 at 12.30.39 AM.png]]
	This is how we implement the csrf token. 
	4. So one the success function, we can just say something like message sent. 
	
	![[Screenshot 2024-01-15 at 12.32.16 AM.png]]
	So what this is doing is that the success function that means if the message was sent to the database, we're gonna print a particular message. So this is gonna be accessed from views.py function.
	
	![[Screenshot 2024-01-15 at 12.35.34 AM.png]]
	And then this, so what this is doing is that once a user hits on send and it has saved in the database we want to delete this. We want to delete that particular line from the input. 
	
	![[Screenshot 2024-01-15 at 12.38.00 AM.png]]
	
	![[Screenshot 2024-01-15 at 12.38.14 AM.png]]
	(Line cleared when the input is sent.)
	
	![[Screenshot 2024-01-15 at 12.39.11 AM.png]]
	Now here we'll add a new url, and we're gonna name this url sent. We can see, its sending all the data to a url named send.
	
	![[Screenshot 2024-01-15 at 12.41.15 AM.png]]
	Now we create a new function for it in views.py.
	
	![[Screenshot 2024-01-15 at 12.43.37 AM.png]]
	So now that this view has all this data. which can be inputted, all we just want to do is store that data in this message database. 
	
	![[Screenshot 2024-01-15 at 12.45.55 AM.png]]
	
	![[Screenshot 2024-01-15 at 12.46.37 AM.png]]
	Now we're not rendering any HTML page, we just want to return back to the frontend or the JavaScript the message. So we're gonna give it an HTTP response. But before we can do that we have to import it here.
	
	![[Screenshot 2024-01-15 at 12.48.52 AM.png]]
	
	![[Screenshot 2024-01-15 at 12.49.38 AM.png]]
	(friendly reminder: room= room_id) Now we can say return HttpResponse.
	So this HttpResponse,
	
	![[Screenshot 2024-01-15 at 12.58.14 AM.png]]
	this data, on success that everything works perfectly. We're giving the function the value of data, and then want to alert data, so this data is this HttpResponse.
	
	![[Screenshot 2024-01-15 at 1.00.27 AM.png]]
	So when we alert, its just gonna say: 'Message sent successfully'.
	
	![[Screenshot 2024-01-15 at 1.01.42 AM.png]]
	
	![[Screenshot 2024-01-15 at 1.01.53 AM.png]]
	
	![[Screenshot 2024-01-15 at 1.02.17 AM.png]]
	
	![[Screenshot 2024-01-15 at 1.02.28 AM.png]]
	
	![[Screenshot 2024-01-15 at 1.02.52 AM.png]]
	Another example
	
	![[Screenshot 2024-01-15 at 1.03.17 AM.png]]
	
	![[Screenshot 2024-01-15 at 1.03.25 AM.png]]
	
	![[Screenshot 2024-01-15 at 1.03.34 AM.png]]
	
	![[Screenshot 2024-01-15 at 1.03.45 AM.png]]
	
	![[Screenshot 2024-01-15 at 1.04.07 AM.png]]
	2 different rooms for 2 different chats. So we can use this to access the the messages for each room.
	So what we have done to this point is that the user can create a new room, enter that room, its gonna be a dynamic url, and then the user can send a message and that message will be saved in the database.
	So what we just need to do now since we have all the data stored, we don't have too much of work to do, we just need to get all the data and showcase it. But we need to do a little bit of extra work to make sure that this data showcase in real time. So if a user from another mobile phone or from another place in the world, texts have also sent a message, we want to see it right here in real time without even refreshing this page. So we're using AJAX for this. 
	We use Ajax so that when a user submits, the page doesn't refresh, and then it was cleared from here.  And the message gets stored in the database.
	Now we need to use Ajax again to load the messages data in real time.
	So if we're using normal django to just load all the messages, we can just got to views, create a new function or we don't even need a new function, we're just gonna come to the room and then we'll just specify the message and send it to the HTML file. and then just showcase it. But if we do that once the user updates or creates a new message it isn't going to be updated in real time.
	Thats why we go to urls.py and add a new view for getting all the messages, and this url is gonna be dynamic.
	
	![[Screenshot 2024-01-15 at 9.04.36 AM.png]]
	Just like the path for room.
	
	![[Screenshot 2024-01-15 at 9.08.57 AM.png]]
	This is saying that getMessages/a particular room that we want to get the message from. So we're gonna have the room name. So e.g., if the room name is Coders, its gonna be like getMessages/Coders.
	Then we go to our views.py file and create a new function, getMessages which takes request and room as arguements.
	And for now lets pass.
	
	![[Screenshot 2024-01-15 at 9.10.52 AM.png]]
	Now we need to go back to views.py and what we want to do here is that we want to get all the messages of that particular room the user is in. So now that we have the room name, so we can use the room name to get the messages of that room. Now when we get all the messages of this room then we're gonna return a JSON response of all the messages. Then from our frontend, we're gonna use AJAX JavaScript to access that JSON response and showcase it to our user. Now first of all we need to make sure that we're importing JSON response, so that we can use that.
	
	![[Screenshot 2024-01-15 at 9.19.01 AM.png]]
	
	![[Screenshot 2024-01-15 at 9.37.01 AM.png]]
	So now that we have the room that we're looking for, lets get the messages associated with our room.
	So what is this line(room icontains= room_details.id) of code is doing?
	Now in our models.py:
	We created a model named Message. Now this message, is just the model that's going to be storing all the messages on this platform. And then we added four attributes, the value of that message, the date that message was sent, the user, and now what we are specific about is the room. This room, is which room was this message being sent from? Like, which room does this message belong to? So this room is just specifying the room ID of the message that this that this message belongs to. So now that we know that room ID, we can now get all the messages.
	Now if we come back to views:
	We're saying Message.objects.filter(room= room_details.id), so now we want to filter with all the list of the data we have here, with the room =the room details.id.
	Now this is that our filtering without the messages with the one in which the room is this room_details.id.
	Now lets just return a JsonResponse.
	And then lets return messages as a list. 
	So this is returning a JSON response, and is returning it as a variable: messages.
	
	![[Screenshot 2024-01-15 at 9.41.42 AM.png]]
	
	![[Screenshot 2024-01-15 at 9.42.13 AM.png]]
	(returning as a variable)
	So this is what we're gonna be using to access it. And we return it as a list of messages,
	
	![[Screenshot 2024-01-15 at 9.44.46 AM.png]]
	which is this messages of value. So we're getting all the values from here. 
	Now we need to go to room.html.
	So at line 70 we're gonna add another script.
	
	![[Screenshot 2024-01-15 at 9.53.22 AM.png]]
	So what this code is doing line by line:
	1. So this saying this document which is this page, then we want to do everything in this function.
	
	![[Screenshot 2024-01-15 at 9.54.52 AM.png]]
	2. ![[Screenshot 2024-01-15 at 9.55.12 AM.png]]
	So this is setInterval, what it does is that anything inside this bracket or the function:
	
	![[Screenshot 2024-01-15 at 9.56.12 AM.png]]
	is going to be again and again with this particular amount of time, which is one second.
	
	![[Screenshot 2024-01-15 at 9.57.48 AM.png]]
	So this means that all this function and getting all the requests and everything is going to be done every second.  
	
	![[Screenshot 2024-01-15 at 9.59.19 AM.png]]
	Thats why we can access the data in real time. So once an update is made the next second, we have that data updated already.
	3. So now we're now using the Ajax:
	
	![[Screenshot 2024-01-15 at 10.02.37 AM.png]]
	We're saying GET.
	
	![[Screenshot 2024-01-15 at 10.03.02 AM.png]]
	So this time we're getting the particular data from the url:
	
	![[Screenshot 2024-01-15 at 10.04.04 AM.png]]
	getMessages/{{room}}/
	
	![[Screenshot 2024-01-15 at 10.04.50 AM.png]]
	(room is from views.py(the room function))
	And then if we've got everything successful, we're getting the JsonResponse from getMessage function in views.py
	![[Screenshot 2024-01-15 at 10.08.13 AM.png]]
	right here, so this is what we're getting here. 
	And if its successful,
	
	![[Screenshot 2024-01-15 at 10.09.22 AM.png]]
	we can do console.log(response).
	So we're going to the response that we got, which is that particular data.
	
	![[Screenshot 2024-01-15 at 10.12.24 AM.png]]
	And then there is ("#display").empty();
	So what this is, is, so if we come here, we'll see that we have a new div tag with an ID of display. 
	
	![[Screenshot 2024-01-15 at 10.18.46 AM.png]]
	So first of all, I made sure that this is empty, I removed everything there. We're just gonna comment them out. 
	
	![[Screenshot 2024-01-15 at 10.20.17 AM.png]]
	So we removed everything in there. And then we looped through, so we say for varkey, in response.messages, so for each value in this response, and this response, which includes the JsonResponse, it was saying .messages, as we can see its this messages of everything we get here in views.py function. So as seen for(var key in response.messages).
	
	
	![[Screenshot 2024-01-15 at 10.30.44 AM.png]]
	 Now, we have a new variable named temp.
	
	![[Screenshot 2024-01-15 at 10.32.45 AM.png]]
	 and then we can see that we have this particular div tag in here. So this is the div tag we use in here. 
	
	![[Screenshot 2024-01-15 at 10.33.46 AM.png]]
	 So we just specified a new JavaScript variable with the HTML tag. So exactly the same thing.
	
	![[Screenshot 2024-01-15 at 10.35.38 AM.png]]
	 So it's div class, container darker, everything. 
	
	![[Screenshot 2024-01-15 at 10.37.56 AM.png]]
	But now in here we can see that we just added dummy messages. Hello, everyone. How are you guys doing?
	
	![[Screenshot 2024-01-15 at 10.39.17 AM.png]]
	 But right here thats not what is there again.
	
	![[Screenshot 2024-01-15 at 10.40.44 AM.png]]
	Right here, what is there is response messages[key].user. So this first of all, is the user name of the person that sent the message.
	
	![[Screenshot 2024-01-15 at 10.42.11 AM.png]]
	And this is the value of the message, which is like Hey, what's up guys.
	
	![[Screenshot 2024-01-15 at 10.43.10 AM.png]]
	And this is the date.
	
	![[Screenshot 2024-01-15 at 10.43.46 AM.png]]
	So now we have this in an HTML tag, while we were gonna append it to the div tag that has this hashtag display ID.
	
	![[Screenshot 2024-01-15 at 10.44.21 AM.png]]So now this is empty,
	
	![[Screenshot 2024-01-15 at 10.44.56 AM.png]]then we're gonna append whatever we get into this div tag.
	
	![[Screenshot 2024-01-15 at 10.47.04 AM.png]]
	So after having that done, we would just add an error. So if anything happened, if we add an error, we just say an error occurred.

Django REST Framework:
	The django REST framework is a library which allows us to build APIs in our django project.
	
	![[Screenshot 2024-01-16 at 4.11.51 AM (2).png]]
	
	![[Screenshot 2024-01-16 at 4.14.08 AM (2) 1.png]]
	
	![[Screenshot 2024-01-16 at 4.17.21 AM (2).png]]
	So for now we're not gonna create a django app. Later we're gonna create one to use serializers and stuff like that. So for now we're gonna stick with our 'drfproj' directory, so thats where we're gonna put our views.py, or anything we're gonna be using.
	
	![[Screenshot 2024-01-16 at 4.21.42 AM (2).png]]
	So in this views.py file thats where we're gonna code, just like a normal project. 
	
	![[Screenshot 2024-01-16 at 4.23.26 AM (2).png]]
	django.shortcuts is the module, like a class/function in the django library, in which we can input some things. 
	Now we want to use the API view from the REST framework. So the REST framework provides us with an API view class or function, or whatever it is. So with that API view we're gonna be able to be able to access a lot of types of APIs that are available in the djangorestframework. So when we use the API view we can do something like GET request or POST request, and somethings that are being rendered or are being given to us by the REST framework.
	
	![[Screenshot 2024-01-16 at 4.45.05 AM (2).png]]
	This APIView is gonna allow us to create a function like class on it, so that we're able to use everything available in this APIView. But along with this APIView we want to send a response. 
	Now, for example, let's say someone, another developer tries to access our API, once it sends a request to our API, we'll want to give the developer a response, some sort of results. So let's say user send a get request just to get a list of a query set or something, or a list of data, we want to give the user back a response or that data. So first, to give a response, we're gonna have to import, response from the rest framework: from rest_framework. import.response import Response. So what this is doing is just saying: from rest_framework.response import response.
	Now that everything is imported, we can now create a class to inherit from this APIView, so that we can get a lot of methods that we can work with.
	
	![[Screenshot 2024-01-16 at 4.50.54 AM (2).png]]
	This TesView is inheriting from this APIView.
	So now under this class we want to have a GET function, which just gonna be like a GET request to this API. 
	
	![[Screenshot 2024-01-16 at 4.53.26 AM (2).png]]
	So now that we have this function setup what we just want to specify is data. So this is a testview and in this testview we have a GET request.
	
	![[Screenshot 2024-01-16 at 4.55.12 AM (2).png]]
	So we want to have data that we want to send back to the user or just give as a result. For now lets just hard code our data ourself. Later we're gonna use the django model so that this data will be from the database we have or something. For now, lets just have a simple dictionary that we're gonna send back.
	
	![[Screenshot 2024-01-16 at 5.00.05 AM (2).png]]
	So this is the data we want to send back as a response.
	
	![[Screenshot 2024-01-16 at 5.01.23 AM (2).png]]
	So what we just did, was that we used this Response which we imported from rest_framework.response, and then we're returning a response of this particular data. 
	So what we want to do now is to go set a url for this so that we can actually test this when we run it on our localhost. So now lets come into urls.py.
	(empty path shows the home url)
	
	![[Screenshot 2024-01-16 at 5.06.46 AM (2).png]]
	So now that we've that TesView imported, we can easily use it in here.
	
	![[Screenshot 2024-01-16 at 5.08.22 AM (2).png]]
	Now, since TestView is class based view, we have to add .asview(). Now the reason why we're adding .as_view() is because the view which we're using in views.py is a class based view.
	If we're using a function of this view, what we need to do is that we can just say TesView here:
	
	![[Screenshot 2024-01-16 at 5.12.10 AM (2).png]]
	as the view. But since we're using a class based view, we must do this even though its gonna give us an error, and django isn't going to recognise that as a valid view.
	So now we've all this setup, we've it linking to the home URL using the TesView.as_view(), and we give it a name of 'test'. Now we run a server and test it immediately.
	But if we do that we aren't gonna see anything, we might even get an error. And the reason why we might get an error is because right here:
	
	![[Screenshot 2024-01-16 at 5.20.06 AM (2).png]]
	what we did was we installed the djangorestframework and immediately we just came to start importing everything in our project.
	
	![[Screenshot 2024-01-16 at 5.21.26 AM (2).png]]
	But before doing this we need to do some second configurations, to be able to use some particular types of libraries, not all. So for this djangorestframework we need to add some things to our settings. Now lets go to settings,py file.
	
	![[Screenshot 2024-01-16 at 5.24.14 AM (2).png]]
	First of all in our INSTALLED_APPS, we need to add where we are, rest_framework, so django can recognise it. Thats all to do with the settings.
	
	![[Screenshot 2024-01-16 at 5.26.23 AM (2).png]]
	Now under the urls.py, we need to add one url in which the rest_framework can be recognised. So first of all we need to import include. After that we can just do path('api-auth', include('rest_framework.urls')(and then we're just gonna include from rest_framework.urls)),.
	
	![[Screenshot 2024-01-16 at 5.31.53 AM (2).png]]
	So now when we run this server, and when we come to home,
	
	![[Screenshot 2024-01-16 at 5.33.08 AM (2).png]]
	it should give us this TesView:
	
	![[Screenshot 2024-01-16 at 5.33.49 AM (2).png]]
	and TesView should just be give get, to just like either sending a GET request. And then we're just gonna give it response of this particular data.
	
	![[Screenshot 2024-01-16 at 5.37.59 AM (2).png]]
	
	![[Screenshot 2024-01-16 at 5.50.57 AM (2).png]]
	djangorestframwork comes with this template to showcase out API and basically test all our API. Now here, it is giving us in a dictionary right here, and this exact thing we've written in data. So normally the API gives us a response in json format, but here, it is giving us a response in dictionary format, because those words we actually setup right in our class function. Normally it should be a json format. So as we can see choosing the GET request, and then the http 200 says OK, because its allowing a GET request, because we specified the get function in class function. If we specify the POST function, its gonna show that we're allowing a POST request.
	So now if we pick the json option from the dropdown menu:
	
	![[Screenshot 2024-01-16 at 6.02.39 AM (2).png]]
	
	![[Screenshot 2024-01-16 at 6.03.00 AM (2).png]]
	We're gonna see that it gives us this in json format. So right here, it gives us in a blank json format, no template, nothing just a blank json format, as if we go this url.
	
	![[Screenshot 2024-01-16 at 6.05.55 AM (2).png]]
	But normally in the homepage it shows us this:
	
	![[Screenshot 2024-01-16 at 6.06.42 AM (2).png]]
	
	![[Screenshot 2024-01-16 at 6.07.29 AM (2).png]]
	Now if we come back to the REST framework page and scroll down, in installation we see that exactly what it is doing here, is what we've done in our project. 
	We don't need the optional packages below djangorestframework so we didn't install them for now.

Django REST Framework Serializers:
	So serializers is a structure, a representation that represents a data, we want to return in json format or accept in a json format. So we can use serializers to transform our django models into json. Lets first create a new app in our django project.
	
	![[Screenshot 2024-01-16 at 6.15.23 AM (2).png]]
	After this we're gonna go into our models.
	So the serializer is, think about it like a form, like a model form. Once you have model, the way we create a form for model, so we can submit in Django, so we can submit a form, or update or whatever we want to do. Think of that as a serializer. So serializer is just basically the same thing, we have a model, then we have a serializer that we link that model to and then we specify the fields we want to have in that particular serializer and we just have to use it in views. So that was the theoretical part. Now let's dive into practicals.
	
	![[Screenshot 2024-01-16 at 6.24.53 AM (2).png]]
	So this serializers.py is the file in which we're gonna configure our serialization. For now, we're gonna leave it blank. First we gonna create a new model that we're gonna use. So lets go to models.py.
	
	![[Screenshot 2024-01-16 at 6.28.40 AM (2).png]]
	So now, as we know, whenever we create a model file or make changes to an existing one we need to migrate it into our database.
	But before we do that lets register this in our INSTALLED_APPS.
	
	![[Screenshot 2024-01-16 at 6.30.53 AM (2).png]]
	
	![[Screenshot 2024-01-16 at 6.32.02 AM (2).png]]
	Now we go back to serializers.py.
	So now, we need to import the serializers from the rest_framework.
	And we also need to import the post model from the models.py file. And after that we can create a serializer for our POST model by specifying only some fields. 
	
	![[Screenshot 2024-01-16 at 6.36.17 AM (2).png]]
	So after we have these 2 things imported we're just gonna create a serializer class for that student.
	
	![[Screenshot 2024-01-16 at 6.38.55 AM (2).png]]
	(fields is a tuple which gets values from the models.py file)
	So now lets go back to the views.py file.
	
	![[Screenshot 2024-01-16 at 6.44.29 AM (2).png]]
	Now lets create a POST method in our class. So in this TestView class we're gonna create a POST method so that we can receive data just like in a form. So to do this we're just gonna add a function below in our TesView class. 
	
	![[Screenshot 2024-01-16 at 6.48.46 AM (2).png]]
	So when we do something like this, what it means is that we're actually want to use a form or submit a data or something like this.
	
	![[Screenshot 2024-01-16 at 6.50.45 AM (2).png]]
	So this is exactly what we do in a django form, and form is being used as a reference because its very similar to this.
	
	![[Screenshot 2024-01-16 at 6.53.23 AM (2).png]]
	So what we just did first of all we specified the serializer, but our serializer is this student serializer. So normally if one was using a POST, like if we don't wanna submit a form we can just remove this and say serializer= StudentSerializer(remove, data= request.data). But because we want to submit something like a form we have to say data=request.data, it needs to get the data which is being posted into this particular API view.
	So then we get that. The next line implies that if all the values are correct, just like we want to collect an integer field and we have a character field or text field then that serializer isn't valid. So this is just checking if everything we want, if all the values are correct. And if its valid we'll just save it. And then we just return a response of that particular data which the user saved.
	But if this doesn't happen we'll just return a response of an error. 
	
	![[Screenshot 2024-01-16 at 7.08.08 AM (2).png]]
	Now lets save this and our server once again.
	Now to test this API we need Postman.
	It is an application/software which is used for testing our API.
	So since our app is in production or our project is in production is on live or something. First to test it locally on our localhost we can use this application.
	
	![[Screenshot 2024-01-17 at 5.51.36 AM (2).png]]
	First of all, we're gonna come in the browser and then copy. So we'll copy the URL, because that's the URL we're gonna be testing anyway. So right here in the textfield in Postman, we're just gonna paste. This is the URL we're gonna be testing. And we want it to be a POST method. So right here, we're gonna go into body. And then we're going to click on form-data. Now we're going to input KEY. So this key is where we want to submit. So let's see, we'll come back into our VS code, we come into our serializer, we can see that the fields required a name, and age. So we know that in our models name is a character field and age is an integer field. So to avoid any error, we need to make sure that we abide by everything. So name, does give us the value of admin. And then key, that is the age range, just give it a value of 25. Now, if we hit Send, sending the request how postman works, it's gonna test the API for us. Now as we can see, it gives us a response of this particular data name, admin, age 25. But how do we know that this particular data has been submitted into model? So what wants to know is, is this data is really saved in our database, for us to be able to do this, we need to check, we need to open up our admin interface, and set up our admin panel and then check our database.
	
	![[Screenshot 2024-01-17 at 6.03.03 AM (2).png]]
	
	![[Screenshot 2024-01-17 at 7.11.28 AM (2).png]]
	from .models import student, and then we want to register that student in our admin interface. So admin.site.register(Student).
	Let's go to slash admin.
	So now we can see that under DRF app, we have students, if we click on me, we should have one object in there. So as we can see, we have one student, which is admin. And we submitted that from our API. We didn't create this from our admin panel, or from our project or from our website.
	
	![[Screenshot 2024-01-17 at 7.20.11 AM (2).png]]
	Its through our API. Now the reason why it gives us this is because if we come back here in our code, we'll see that we wrote that, if it's valid, it should save that data. And if it wants to save that data, it should give us a response of serializer.data.
	
	![[Screenshot 2024-01-17 at 7.23.45 AM (2).png]]
	So that means if that is successful, the response we want to get is the data which was submitted. So if we come back to postman, anytime we get the data that we submitted here, it means that was successful.
	
	![[Screenshot 2024-01-17 at 7.26.43 AM (2).png]]
	So thats how to submit from our API. Now lets talk about serializing the data that is going out. (here it means using the get method). So first of all, we already our model registered, and have created a superuser. Now to use a GET method, we're gonna come back to our views code. Now in our get method here:
	
	![[Screenshot 2024-01-17 at 7.32.56 AM (2).png]]
	What we did earlier, its just a blank data, just a normal dictionary, but in this post method, in this post function, we are using serialization, we're serializing our data. So lets say we also want to serialize the data in this get function. Now what we're gonna do, since we already have self request, argument and keyword argument, we're gonna specify a query set.
	
	![[Screenshot 2024-01-17 at 7.37.41 AM (2).png]]
	Now the reason we need to specify many= True, is because this queryset(qs) is a list of objects. So from this Student model we're getting all the objects(all the data in the Students database). So as we can see, its more than one.
	
	![[Screenshot 2024-01-17 at 7.41.05 AM (2).png]]
	It is gonna be a list. Thats why we've to specify many=True. So after specifying query set in a variable(qs), we have another variable named serializerwhich is taken from the StudentSerializer, and we pass in the query set, and then we have tell that many=True. 
	
	![[Screenshot 2024-01-17 at 7.45.37 AM (2).png]]
	Now if it was just one one data we can just put query set(qs) in StudentSerializer. But since its more than one we have to put many= True. So now that we have that we can just return a response of serializer.data.
	
	![[Screenshot 2024-01-17 at 7.48.02 AM (2).png]]
	So when a user tries to access this API using the get method. Its just gonna return a response of this serializer.data.
	
	![[Screenshot 2024-01-17 at 7.50.05 AM (2).png]]
	And this serializer is a list of the objects in this Student model, which is basically data in that site.
	
	![[Screenshot 2024-01-17 at 7.57.22 AM (2).png]]
	Now coming back to Postman, if we remove the fields from form-data, and use none instead and use GET this we'll see that its giving us a preset a list of the data we have in our project. So its giving us in a JSON format. 
	Now if you don't see this, this particular square bracket, then that is just a dictionary. But since we see the square bracket, and curly braces, which is not taking each of the data, now we know that it's returning it in a JSON format, which is the normal standard way of returning API response or request. So that is what we can do when we're talking about get serializing our gets request.
	Now lets say we want only one data, so first of all since we have this query set(qs) which is all the objects, and we know that all the objects is more than one, so lets use a variable(student1) which should be = qs.first(). Now what this qs.first() does is that its going to get the first object in this Student model. So next in serializer we remove many=True and now we're not passing the whole query set we're just passing the first student, which is student1.  So now we can just return a response of serializer.data.
	
	![[Screenshot 2024-01-17 at 8.10.41 AM (2).png]]
	
	![[Screenshot 2024-01-17 at 8.12.05 AM (2).png]]

Authentication in djangorestframework:
	This authentication is going to allow us to prtect our API endpoint. So we might have some API that we might just allow anybody to use without authenticating or without authorising that user. But we also might have some APIs for which we want the user to, first of all be authenticated. We want the user to have an API key or token or something before they can access that particular API. 
	Just for example, when we use the YouTube Data API, we need to provide that API key which we get from our Google Cloud account or something like that. So that API key is going to be used to authorize us or to athenticate us to be able to use the API.
	
	![[Screenshot 2024-01-17 at 8.22.37 AM (2).png]]
	
	![[Screenshot 2024-01-17 at 8.23.09 AM (2).png]]
	
	![[Screenshot 2024-01-17 at 8.22.08 AM (2).png]]
	AllowAny allows anybody to access this particular API, IsAdminUser means the person has to be an admin user before they can access the API. isAuthenticated is the one we're gonna talk aboout. Here the user has to be authenticated into this application before we can give the user can be given the chance/way/something to be able to use our API.
	So before any of the functions, let's just add a variable named permission_classes. Now this permission classes is going to give us the permissions we want to collect before a user can access any of these.
	
	![[Screenshot 2024-01-17 at 8.31.49 AM (2).png]]
	Now if we want to allow anybody, we can also leave it just like this in the above picture.
	This means that anybody can access it. Or we can just remove the variable altogether.
	
	![[Screenshot 2024-01-17 at 8.33.59 AM (2).png]]
	So what this here means is that user needs to authenticated before they can use it.
	
	![[Screenshot 2024-01-17 at 8.35.38 AM (2).png]]
	So now as we can see it requires us to be authenticated. or to provide some authentication token or something, before it can give us access to our APIs.
	
	![[Screenshot 2024-01-17 at 8.37.56 AM (2).png]]
	
	![[Screenshot 2024-01-17 at 8.38.38 AM (2).png]]
	
	![[Screenshot 2024-01-17 at 8.39.08 AM (2).png]]
	So this is going to migrate our rest_framework.authtoken into our database.
	Now lets flush all the data we have in our database, So we can create a token for each user.
	
	![[Screenshot 2024-01-17 at 8.41.40 AM (2).png]]
	So this is gonna flush all the data we have in our database, just click yes, and then done.
	So now we don't have any user.
	
	![[Screenshot 2024-01-17 at 8.43.33 AM (2).png]]
	Now we create a super user again and run the server again.
	
	![[Screenshot 2024-01-17 at 8.44.22 AM (2).png]]
	
	![[Screenshot 2024-01-17 at 8.44.56 AM (2).png]]
	So now we see that we have an AUTH_TOKEN app and in that we have a Tokens model.
	
	![[Screenshot 2024-01-17 at 8.46.49 AM (2).png]]
	So this is gonna create a token for whatever user we're passing.
	
	![[Screenshot 2024-01-17 at 8.48.03 AM (2).png]]
	It gives a token, and its also gonna save it in the host(token?).
	
	![[Screenshot 2024-01-17 at 8.49.59 AM (2).png]]
	So now lets see how to use this token in Postman to authenticate.
	
	![[Screenshot 2024-01-17 at 8.51.29 AM (2).png]]
	Authorization should be the default Key.
	
	![[Screenshot 2024-01-17 at 8.54.08 AM (2).png]]
	To automate the whole process. So that we don't have to do it for every user.
	The views from rest_framework.authtoken.views is a default built-in views which allows us to just send the user's credentials and then it obtains the authentication token for us.
	
	![[Screenshot 2024-01-17 at 8.57.57 AM (2).png]]
	So that is how we can do that, we also access this from our code, we can do something like sending a request to this particular page, and then getting the authentication token.
	