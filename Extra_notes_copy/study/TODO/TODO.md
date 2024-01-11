- Environment variables pdh lena

- Commands:
	- If virtualenv is being used then always start with "workon 'env_name'".
	- source /opt/homebrew/bin/virtualenvwrapper.sh
	1. django-admin startproject myproject: used to create a new project named 'myproject'.
	2. from django.urls import path: is used to import path django.urls
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
            ![[Screenshot 2023-12-28 at 8.28.55 PM.png]]	This is used to include myapp.urls, it goes into myapp directory and looks for similar urls to the one mentioned in myproject's urls.py
            
        5. Template: Django Template Language:
            ![[Screenshot 2023-12-29 at 12.34.03 AM.png]]
            We can create our own template files to use in django instead of the default one, all we need to do is create a folder containing our templates, go to settings.py and insert the root directory(BASE_DIR) and the folders' names. So what it will do is go to the root folder and look for the folders according to the name provided in settings.py, whatever is put in the 'DIRS': section of TEMPLATES must correlate with the name of the folder in the directory(templates in the above case).
            
            return render takes a request and name of the html page(template) in question. So we have a function that is taking a request and returns renders/rendering index.html
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

