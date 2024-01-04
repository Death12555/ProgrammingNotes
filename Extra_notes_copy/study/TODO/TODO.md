- Environment variables pdh lena

- Commands:
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
				