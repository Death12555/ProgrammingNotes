![[Screenshot 2024-01-18 at 1.02.16 AM.png]]

![[Screenshot 2024-01-18 at 1.03.22 AM.png]]
All of these will work together produce our working REST API.

![[Screenshot 2024-01-18 at 1.04.55 AM.png]]

![[Screenshot 2024-01-18 at 1.06.23 AM.png]]

Since we're running our code on a different OS than we'll be using on our production server, thats why professionals always run their code on a local development server, to isolate their code from their local desktop(its best practice).

So we'll be doing that using the following tools:
1. Vagrant: The first tool is Vagrant, it allows us to describe what kind of server we need for our app, we can save that config as a vagrant file which allows us to easily reproduce and share the same server with other developers.
2. VirtualBox: Once we've told vagrant what kind of server we need, it will create a virtual server exactly described, this means our application code and requirements are installed and running on a virtual server completely isolated from our local machine. 

![[Screenshot 2024-01-18 at 1.37.53 AM.png]]

This has many benefits such as:
- It makes it easier to share code with others regardless of what operating system we're running our code on.
- We'll have exactly the same version of all the requirements for our app.
- We can test our code using exactly the same operating system and requirements that will be used on a real production server.
- And finally, we can easily create and destroy the server as we need making it easier to clean up.

![[Screenshot 2024-01-18 at 1.38.16 AM.png]]

![[Screenshot 2024-01-18 at 1.40.27 AM.png]]

We're going to use a few development tools to help us write and manage our code.

![[Screenshot 2024-01-18 at 1.43.26 AM.png]]

Vagrant vs. Docker:
Both vagrant and docker are similar in that they use virtualization technology to isolate the application from the machine that is running on, however they both do this in different ways and each are better suited to different use cases.

![[Screenshot 2024-01-18 at 2.17.30 AM.png]]

Docker is an open-source containerization tool that allows us to run our application in a lightweight image(instance of a small OS). 
It works by creating something called a docker file that contains all of the steps required to build the image to run your application.

![[Screenshot 2024-01-18 at 2.24.47 AM.png]]

![[Screenshot 2024-01-18 at 2.25.03 AM.png]]

![[Screenshot 2024-01-18 at 2.25.19 AM.png]]

 During the build stage docker installs all of the dependencies and code required to run your app.
An image is typically based on a very lightweight stripped-down version of the Linux operating system. Once we have our image we can use it to run our
application on our local development machine or deploy it to a production sever.

![[Screenshot 2024-01-18 at 2.28.41 AM.png]]

![[Screenshot 2024-01-18 at 2.29.02 AM.png]]

![[Screenshot 2024-01-18 at 2.29.55 AM.png]]

Limitations:
1. Because docker is designed to run in production, it has a steeper learning curve than vagrant.

![[Screenshot 2024-01-18 at 2.31.01 AM.png]]

2. Docker also only has limited versions available for home editions of the windows OS.

![[Screenshot 2024-01-18 at 2.32.44 AM.png]]

Vagrant:
1. It is a tool for managing virtual development environments.
2. However it doesn't come with any virtualization technology out of the box.

![[Screenshot 2024-01-18 at 2.34.33 AM.png]]
3. It works by using something called a hypervisor such as VirtualBox, a tool thats used to run virtual machines on the computer.

![[Screenshot 2024-01-18 at 2.36.50 AM.png]]

4. ![[Screenshot 2024-01-18 at 2.37.13 AM.png]]
With a vagrant we create a vagrant file which contains all of the instructions for creating our development server.

![[Screenshot 2024-01-18 at 2.38.20 AM.png]]

It then uses the hypervisor to create and configure the server on your machine.

Benefits of Vagrant:
1. A vagrant usually consists of a slimmed down but complete version of the Linux OS such as ubuntu.
2. Because vagrant isn't designed to run in production, it has an easier learning curve compared to docker.
3. Also, as vagrant supports a number of different hypervisors, it has a wider range of support for operating systems it runs on.
4. Vagrant should run on any machine in which you can install and use VirtualBox.

![[Screenshot 2024-01-18 at 2.44.28 AM.png]]

Docker:
1. We would use docker if we're looking to streamline our workflow from development to production.
2. And, all of our developers on our project use a supported operating system.

Vagrant:
1. Vagrant is preferred if we're just getting started or if we're looking for a development environment that's supported on a wider range of operating systems.

![[Screenshot 2024-01-18 at 2.51.33 AM.png]]

Creating a development server:
1. Creating a vagrantfile:
	- First go into the CLI, then change to the directory you want.
	- Then type: 'vagrant init ubuntu/bionic64', (it means vagrant init and then the type of server that we want to create) what this does is it initializes our project with a new vagrant file and it bases it on the ubuntu bionic 64 base image. These images are publicly available in the vagrant catalog box, box catalog.
	- If we hit enter then what this will do is that it will go ahead and create a new file in our project
	
	![[Screenshot 2024-01-18 at 8.04.08 AM.png]]
	- If we go to see the newly created file in our project using a text editor we'll see that:
	
	![[Screenshot 2024-01-18 at 8.06.28 AM.png]]
	Most of it has been commented out and its just a template for a server that we can use to run our project.
	So All this will do if we ran this now would be create a basic vanilla  ubuntu image or server based on the standard ubuntu image.
	- so it doesn't make any modifications to it or forward any ports or anything like that.
	- so, now we're going to be modifying this.

2. Configuring our vagrant box:
	Now that we have a template vagrant file for our project, we can go and customize this for the particular requirements that we need for our development server.
	- For now we copy the contents of the file in the tutorial and paste it in the previously created vagrant file, replacing its original contents.
	![[Screenshot 2024-01-18 at 8.21.57 AM.png]]
	- We've kept the vagrant configuration block here(line 8)  which is the standard configuration block that's required in all vagrant files and we've also left the config.vm.box setting to Ubuntu slash Bionic64.
	- So what we've done below this is pinned it to a specific version and this is just to avoid any changes being made or any updates being made to this image(line 15) breaking the steps in this course.
	- We may modify this slightly in the future to incorporate future updates after we've tested them so don't worry if this isn't exactly the same(its 2019014.0.0 according to the video), but just note that this is pinned to a specific version so that it doesn't break if there's modifications made to the base image(line 15).
	- Now we have the config.vm.network line(line 18) and what this does is it maps a port from our local machine to the machine on our server, so when we run our application we'll be running it on a network port 8000 and we want to make this port accessible from our host machine, so the host machine is our laptop or whichever machine we're running the development server on and the guest machine is the development server itself. By default ports are not automatically accessible on any guest machine so we need to add this line to make them accessible so we can access them by going localhost port 8000 and it will automatically map the connection to our guest machine or development server.
	- Now we have this provision block here(line 20), now this is how we can run scripts when we first create our server.
	- We've added some commands to the script and the first one is to disable the auto update(line 21) which conflicts with this auto update(line 24) when we first run it on Ubuntu.
	- We've then added this update line here(line 24) which will update the local repository with all of the available packages so that we can install Python3 virtual env zip(line 25), so we're going to be using these two packages later on. Python3 virtual env is a virtual environment, and zip is the standard zip tool which we can use to create compressed zip files.
	- Then what we do here(from line 26 onwards) is we create a bash aliases file and we basically set Python3 to the default Python version for our vagrant user, now this just means that every time we run Python it will automatically use Python3 instead of the default Python 2.7. This just makes it handy because it means we don't need to type python3 manually every time we run a command.

3. Running and connecting to our dev server:
	- Now that we have a configured vagrant file we can go ahead and start our vagrant box on our machine, we use vagrant by using the terminal or the git bash and we can start the vagrant server for our project by changing to our project location(the root of our project), and typing vagrant up.
	
	![[Screenshot 2024-01-18 at 8.58.27 AM.png]]
	- What this will do is it will download the base image that we've specified in our vagrant file and then it will use VirtualBox to create a new virtual machine and then run our provisioning script when it starts the machine, we can then use our development server and connect to it using the vagrant tool. 
	- Once the vagrant box has been started we can then connect to the vagrant server by using the 'vagrant ssh' command since our box is a completely different isolated box on our machine so it's a guest operating system we need to connect to it using ssh. After typing the command, vagrant will handle the connection to the machine for us.
	- We can see that we're on the machine because the input changes for our git bash or our terminal window. We can see that we're on 'vagrant@ubuntu-bionic'.
	- To disconnect from the machine, simply type 'exit', and this'll take us outside of it and back on to our local machine.
	- So if we type vagrant ssh and we connect to the machine any command that we run in the terminal while we're connected to the machine will be ran on your guest operating system or the development server instead of your local machine, so that's how you connect to the server with vagrant.

Running a Hello World script:
	-  Now that we have our development server up and running, we should understand about how we can use our development server when we're working on our project so because the development server is a virtual machine on our computer by default the file system is not synchronized, that means that all of the files on our development server are different from the files on our local machine.
	- vagrant works by creating a synchronized directory on our vagrant server that updates itself with all of the files in our local project every time we make changes.
	- Once we're connected to the vagrant server type 'cd /vagrant', this will switch us to the vagrant directory on our server.
	- Now everything in this vagrant directory is synchronized with everything in our project folder so if we create a new file in our vagrant project called test.txt, so if we do touch test.txt touch is the Linux command for creating empty files hit enter we can see that this test.txt is automatically listed in our project folder on our local machine so all of the files are synchronized if you type ls on our server this will list all of the files that are accessible and we can see that this list here matches the list here by default when we type ls hidden files are excluded so we can't see .git or .vagrant but we can see license readme.md text.txt, the ubuntu log file and the vagrant file.
	- If we go and remove this text file from our project in atom editor and then go back to our terminal and type ls we can see that the file has been deleted so the synchronization works both ways from the server to our host and from our host to the server.
	- Okay so how do we run code from our project in our vagrant server lets see with a simple hello world script so if we head over to our profiles REST API project in Atom create a new file called hello _world.py hit enter and then we'll just create a simple Python hello world script by typing print Open bracket quote hello world exclamation mark save that file, now let's head over to our terminal make sure we're connected to our vagrant server type ls and we should see the hello world script output here now if we want to run this code on our server all we need to do is type Python hello_world.py hit enter and that's how we run the hello world script on our server.

Python Virtual Environment:
	- We create a Python virtual environment using Python3 with the python venv command so if we do python - m venv and then we set the path where we want to create the virtual environment so the virtual environment is a set of files which we work on and this is the directory where it installs all of the dependencies when you install them with the Python package manager. So we're going to create it in tilde (~)/env what this does is it creates a new file in our vagrant server home directory called env and creates our Python environment there.
	- Now the reason we do it here is because we don't want this environment to synchronize with our local machine so if you ever need to destroy and recreate the vagrant server from scratch you can do that with a fresh Python virtual environment. This is why we specify this tilde because it will create the environment in the home directory of our vagrant server as opposed to the vagrant folder which is synchronized to our local machine.
	- So once we've typed that hit enter and this will go ahead and create a new virtual environment for our project.
	- The way that virtual environments work is we need to activate them and deactivate them so when we're activated on a virtual environment all of the dependencies that we run in the Python application will be pulled from the virtual environment instead of the base operating system the way we activate a virtual environment is we type source and then the path to the activate script within our environment so in our case this path would be in the home directory or tilde(~) /env/bin/ activate then hit enter. We know that we're working on a virtual environment because the name of the virtual environment we're working on appears in brackets at the prefix of the command line input.
	- The way that we switch off a virtual environment is we just type deactivate and then you can see that the name of the virtual environment disappears from the prefix and we are now deactivated from that virtual environment.

Installing Required python packages:
	- Requirements:
		- django== 2.2
		- djangorestframework== 3.9.2
		(Keep these in the same directory as the project and name the file reuirements.txt)
	- Use pip install requirements.txt to install the packages using the reuirements.txt file.

Create a new django project & app:
	Now we can use the Django admin command by typing django-admin.py startproject profiles_project . , what this does is it calls the django-admin.py script it passes in and the arguments start project to say that we want to start a new project and it specifies the name of the project so our project is going to be called the profiles_project and then the location that we want to create the project so this last '.' here this is optional. Now if we don't specify this then it will create a new subfolder called profiles_project, but we don't want to do that we actually want to create it in the root of our project so that's why we put '.' to say do it right here in the root.
	Now that we have the Django project, we need to create an app within our project for our profiles api so a Django project can consist of one or more sub applications within the project that we can use to separate different functionality within our project so we're just going to create one API the profiles REST API so we'll just create one app and we'll call the app profiles_api so python manage.py now that we've created our project we need to use the manage.py scripts instead of django-admin and then we'll type start app profiles_api, hit enter so this will create a new subfolder called profiles_api. This creates a new django app in our project.

Enable our app in the Django settings.py file:
	In the settings.py of our Django project there's a block here called installed apps, this is where we need to list all of the apps that we need to use for our project so in our project we can install apps either via an external dependency which is the ones we installed in our requirements.txt or we can install apps by creating new apps and then adding it to the installed apps list.

Testing:
	We can easily test changes that we make to a Django project by using the Django development server so Django comes with a handy development server that we can use to test our changes in the browser as we make them to the project the way we start the Django development web server is we connect to our vagrant box make sure we're working on our environment and that we're in the /vagrant directory and then type python manage.py run server 0.0.0.0:8000, what this says is it asks django to start running the development web server and this 0.0.0.0 means make it available on all network adapters on our development server and this colon 8000 says start it in port 8000 so we can access it via port 8000, since in our vagrant file we mapped port 8000 on our host machine to port 8000 on the development machine and that's why we specify port 8000 when we start the server.

Setup the Database:
	Data Models:
		In Django we use models to describe the data we need for our application Django then uses these models to set up and configure our database to store our data effectively. Each model in Django maps to a specific table within our database. Django handles the relationship between our models and the database for us so we never need to write any sql statements or interact with the database directly.
	Create our database model:
		Out of the box Django comes with a default user model that's used for the standard authentication system and also theDjango admin. We're going to override this model with our own custom model that allows us to use an email address instead of the standard username that comes with the Django default model. Best practice is to keep all of the models, files, all of the database models in a file called models.py within our app, so within our profiles_api app load up the models.py and we can see that this is a template that is created by default by Django. When we add the app to our project, we're going to modify this file to include our user profile model, the first thing we need to do is import some additional imports at the top here so underneath the from django.db import models, let's import the abstract base user so type 'from django.contrib.auth.models import AbstractBaseUser', then underneath this we're going to import the permissions mixin: 'from django.contrib.auth.models import PermissionsMixin'. These are the standard base classes that we need to use when overriding or customizing the default Django user model.
		Underneath the imports let's create a new class called user profile and inherit from the base the AbstractBaseUser and the PermissionsMixin base classes.
		
		![[Screenshot 2024-01-20 at 8.09.11 AM.png]]
		We need to add a couple of fields for the permission system so the first one is is_active= models.BooleanField(default= True), so this is a field that we can use to determine if a user's profile is activated or not by default we're going to set all of them to activated as true but this allows us to deactivate users if we need to at some point in the future and the boolean field is simply a field that holds a true or false value.
		Below is_active we want is_staff equals models.BooleanField and this one we'll set (default= False), so this determines if the user is a staff user which is used to determine if they should have access to the Django admin and things like that so by default all users in our system are not going to be staff, but if we need to create a staff user we can create this and set is_staff to True.
		Next we need to specify the model manager that we're going to use for the objects and this is required because we need to use our custom user model with the Django CLI so Django needs to have a custom model manager for the user model so it knows how to create users and control users using the Django command line tools. So lets type objects must be objects= and we'll create a user profile manager called UserProfileManager() because we're going to pass in the class that we're going to create the manager class and we haven't created this yet but we are going to create in the future so just leave it there for now and we'll create the user profile manager class in a bit. Below this we need to add a couple more fields to our class and this is for it again to work with the Django admin and also the Django authentication system so we need to specify a USERNAME_FIELD and this is because we're overriding the default username field which is normally called username and we're replacing it with our email field so this means that when we authenticate users instead of them providing a username and password they're just going to provide their email address and password. Ok below this we're going to add a REQUIRED_FIELDS= ['name']. So this says that the username field is required by default so just by setting it setting email and the user name that means that this is required and then we have additional required fields and we want to say that at a minimum the user must specify the username and their email address and their name.
		Ok below this we're going to add a couple of functions which again are used for Django to interact with our custom user model, the first one is get full name so we need to give Django the ability to retrieve the full name of the user so if we type def get_full_name and in the arguments because we are defining a function in a class we must specify (self) as the first argument this is the default Python convention.
		And again we're going to add a doc string to our function here: retrieve full name of user and then for this function we're just going to return the name so 'return self.name' and this defines a function that when you call get_full_name on our model object it will return the full name of the user we're getting the name from 'name'.
		Below this we need to specify get short name so def get_short_name(self) and then in the doc string: retrieve short name of user, and then we'll also return.name. So we're literally just specifying these functions so that we can use/integrate our custom user model with other components in Django and because we don't have a way to specify a shorter name we're just going to return the same name as the full name and the last name because we've kind of merged them both into one single name field here.
		Finally we need to specify the string representation of our model now this is the item that we want to return when we convert a user profile object to a string in Python we do that by typing: def  __str__(self) and we'll do a doc string here as well: Return string representation of our user, and the string representation will use the email address so we'll just do: return self.email, now this is required for all or it's not required but this is recommended for all Django models because otherwise when we convert it to a string it won't necessarily be a meaningful output so in order to customize how we convert this to a string you want to specify this function here and return the field that we want to use to identify this model if we're just reading it in the Django admin or in some Python code where we print it so we'll see this in action later when we look at the Django admin and we'll see all the users listed by their email address.
		BaseUserManager is the default manager model that comes with django.
		
		![[Screenshot 2024-01-20 at 8.53.53 AM.png]]
		So in our UserProfileManager class let's add BaseUserManager as a parent class, and then let's specify a docstring here: manager for user profiles. The way managers work is we specify some functions within the manager that can be used to manipulate objects within the model that the manager is for so the first function that we need to create is the create_user function this is what the Django CLI will use when creating users with the command line tool.
		So we type def to define a function create_user(self,) as the first argument and then the second argument will be (email,) the third argument will be (name,) and the fourth argument will be (password= None) so this means that if we don't specify a password then it will default to none and because of the way the Django password checking system works a non password won't work because it needs to be a hash so basically until we set a password we won't be able to authenticate with the user.
		Ok below this functions create a doc string: create a new user profile, so that's what this function does and then we'll do a check to see if an email address has been provided so we'll do if not email so if the email has been passed in as either an empty string or a null value then we will raise a value error exception so this is the standard behavior that Python expects and what it can do is it can catch our value error exception and display the message on the screen so if we were to not provide an email address then we define the message that we show to users if they try and create a new user profile without an email so let's type raise value error: users must have an email address.
		Okay so this is just to make sure that the user...well when we call this function that a an email address value has been passed in.
		Next we're going to do something called normalize the email address now what normalizing an email address does is it makes the second half of the email address all lowercase so technically with an email address the first half of the email is case-sensitive that means we could have two separate email addresses with the capital letters or with lower case letters and then the second half is always case insensitive so it's best practice to standardize that by making it lowercase, now a lot of email providers such as Gmail and Hotmail and things like that will make the first half case insensitive as well just for convenience but technically it could be case sensitive depending on the email provider so that's why normalized email only takes care of the second half. Okay so let's set email= self.normalize_email(email), so we have our normalized email address. Next we will create our user model by typing user equals self.model(email= email, name= name).
		Now what this does is it creates a new model that the user manager is representing so by default self.model is set to the model that the manager is for and then it will create a new model object and set the email and the name.
		Next we're going to set the password and we can't just pass the password in here as a clear text value, we need to use the set password function that comes with our user model so it's part of the AbstractBaseUser and we set this by doing user.set_password(password) and pass it in like that, the reason we do that is so the password is encrypted we want to make sure the password is converted to a hash and never stored as plain text in the database because this way if somebody should manage to hack the database and retrieve all the users they would only be able to see the hashed passwords which means they wouldn't be able to convert that password to a clear text password and then potentially use that to log into the users other services if they used the same password for Facebook or another website for example.
		They could technically reverse-engineer it eventually if they'd given it enough time so it doesn't mean we don't have to protect our database but it's the best practice for storing any sensitive data in the database is to encrypt it and by default Django does this with the set_password function.
		Okay now we can save the user model so type user.save() and then the standard is to specify the database that you want to use. So django can support multiple databases and we're only going to be using one database but it's best practice to add this line anyway just to make sure that we support multiple databases in the future if we should add it so type (using= self._db). Again this is the standard Django basically the standard procedure for saving objects in django.
		
		![[Screenshot 2024-01-20 at 9.10.06 AM.png]]
		The next function we need to create is the create_superuser function and this will use our create user function to create a new user but also assign a super user status so it's an admin user in the system. So create a new function: def create_superuser(self, email, name, password). We're not going to allow the password to be none in this one because we want all super users to have a password and then we will add a docstring: create and save a new super user with given details.
		Ok now we will use the create_user function to create a user so we'll just do user= self.create_user(email, name, password). So it might seem a bit confusing here because we have self here, we didn't pass self in self is automatically passed in for any class functions so when you call it from a different function or a different part of the code you don't need to specify self because it gets automatically passed in when you call the function, this is part of Python.
		Okay now that we have the user in our superuser function we're going to assign is_superuser= True, so user.is_super= True and then we'll set staff= True so user.is_staff= True and then we will save our user model user.save and again we'll pass in using= self._db and return user.
		We didn't specify is super user in our user model because it automatically is created by the PermissionsMixin.
		Okay now we can save the models.py and that's all we need to do to create our user model manager._
	Set our custom model manager:
		![[Screenshot 2024-01-20 at 9.27.58 AM.png]]
		Now that we've created our custom user model and our custom user model manager, we can configure our Django project to use this as the default user model instead of the one that's provided by Django. We can set the user model in the settings.py file of the project so the way that we set it is we scroll to the bottom of the file and we create a new settings line called AUTH_USER_MODEL, and we set this to a string which represents the model that we want to use as the Django user model so type it by specifying the app that we want to retrieve the model from so that's the profiles_api app and then the name of the model that we want to use, so that's  .UserProfile, so this tells Django to look at our profiles API app and then find the model called UserProfile and use this for all of our authentication and user registration in our project. Okay so make sure we save the file and that's how we configure the custom user model in Django.
	Create migrations and sync DB:
		We're going to create a django migration file for our models that we've added to the project. The way that django manages the database is it creates what's called a migration file that stores all of the steps required to make our database match our django models so every time we change a model or add additional models to our project we need to create a new migration file. The migration file will contain the steps required to modify the database to match our updated models so for example if we add a new model to our project then we need to be able to create a new table in the database and the way that django does this is it uses what's called migrations. We can create django migrations using the django command-line tool so open up the terminal or the git bash window and type cd then change to our workspace and our project location and then do vagrant ssh to connect to a vagrant server. Once we're on the server type cd/vagrant to switch to the vagrant directory and then type source tilde(~)/env/bin/activate to activate our virtual environment. Once we're on the virtual environment we can use the Python or the django manage.py file to create our migrations for our projects so type python manage.py make migrations and then the name of the app we want to make the migrations for so we're going to make it for the profiles_api app hit enter and this should create a new migration file in our project for our user profile model.
		 
		![[Screenshot 2024-01-20 at 9.55.33 AM.png]]So we can see here that it has created a new file 0001_initial.py and this work contains all the steps required to create our models so migrations.CreateModel, we shouldn't usually need to modify or view this file but it's good to know how it works just in case we ever do.
		Okay now that we've created our migration we can go ahead and run our migration which will make all the changes required to set up our database for our Django project so type python manage.py migrate, this will run all the migrations in our project so when we hit enter we can see that it does a bunch of steps here and it says okay next to each one so it will go through our entire Django project and create all the required models or all the required tables in the database for any of our models and any of the dependencies that we have so for example the Django auth system that's out of the box the Django admin it creates tables in the database for all of these projects.

Setup Django Admin:
	Creating a superuser:
		The Django admin is a really useful tool that allows you to create an administrative website for your project that lets us manage our database models this makes it really easy to inspect the database see models and modify them. Before we can use the Django admin we need to create a super user, a super user is a user with the maximum privileges over our database. We're going to be creating a super user in this video using the Django command line tool start by opening up the terminal window and navigating to our project the profiles REST API then type vagrant SSH or if vagrant isn't already started run vagrant up and then vagrant SSH to connect to the development server once we're on the server type cd forward slash vagrant to switch to the vagrant directory and then type source tilde forward slash env slash bin slash activate to activate our Python virtual environment. Once we're on the virtual environment we can then use the Django manage command to create a super user simply type Python manage.py create super user all one word and hit enter it will prompt us to enter an email address, name and password, then we can see that the super user account has been created successfully and that's how we create a super user using the Django CLI.
	Enable Django Admin:
		Next we can enable the Django admin for our user profile model, by default the Django admin is already enabled on all new projects however we need to register any newly created models with the Django admin so it knows that we want to display that model in the admin interface let's go ahead and enable the Django admin for our user profile model. Open up the Atom editor and make sure we have the profiles REST API project open the way that we register models is we add them to this admin.py file which is automatically created when we create a new app in our project, we're going enable our model by first importing our models from the profiles_api project so let's type from profiles_api import models, then we register models by typing admin.site.register(models.UserProfile). This tells the Django admin to register our UserProfile model with the admin site so it makes it accessible through the admin interface.
	Test Django Admin:
		Next we're going to test the Django admin now that we've enabled it for our project we can test the Django admin by starting the development server and heading over to our local host forward slash admin let's open up the terminal or the git bash window and make sure that we are connected to our server and we are on the correct virtual environment then we're going to start our management server or our development server by typing python manage.py run server 0.0.0.0 : 8000, hit enter and this will start the development server and then we can open up Chrome or whatever our favorite browser is and type in 127.0.0.1 : 8000 hit enter this will take us to the Django home page and by default the Django admin is enabled on the forward slash admin URL. So we created a super user for our account, so we're going to enter those super user credentials, then hit login so this is the Django admin and as we can see we have three sections here each one of these sections represents a different app in our project the auth token app is an app that is automatically added or is an app that we added as part of the Django rest framework when we enabled our tokens and authorization is part of Django and these come out the box with Django and allow us to use the authentication system the app that we created is the profiles_api and the model that we registered is called user profile Django figures out the name of the model by basically looking at how we defined it in the class so we can see that we've defined it as user profile so what it does is it separates the camel casing which is the capital letters that breaks up the words in the class name and then it just makes this one lowercase and that's how it automatically generates the name and because the best practice is that we make the class representation of the model a singular so we notice how this is use a profile and not user profiles plural the Django admin will automatically add the s because it knows that in our user profile model we're going to have more than one item if we were to define it as plural and put user profiles here then we would get an extra s here and there is documentation where we can find out how to override this behavior if we like, okay so if we click on our user profiles model we can see that we have the user profile that we created as our super user so every profile that we add in our site will be accessible here in the Django admin if we click on our user profile we can see that the first item is the password hash which is the hashed version of our password. Notice that it didn't store it in clear text because it stores it as an encrypted hash and then we also have the last login the super user status and basically all of the fields that we have available in our model.

Introduction to API Views:
	What is an APIView:
		The Django rest framework offers a couple of helper classes we can use to create our API endpoints the API view and the view set both classes are slightly different and offer their own benefits. The API view is the most basic type of view we can use to build our API it enables us to describe the logic which makes our API endpoint. So what is the API view? An API view allows us to define functions that match the standard HTTP methods HTTP GET to get one or more items HTTP POST to create an item HTTP put to update an item HTTP patch to partially update an item and finally HTTP delete to delete an item. By allowing us to customize the function for each HTTP method on our API URL API views give us the most control over our application logic, this is perfect in cases where you need to do something a little bit different from simply updating objects in the database such as calling other apis or working with local files. So when should we use API views? A lot of the time it will depend on personal preference as we learn more about the Django rest framework, here are some examples of when it might be better to use API views, whenever we need full control over our application logic such as when we're running a very complicated algorithm or updating multiple data sources in one api call or when we're processing files and rendering asynchronous response maybe we're validating a file and returning the result in the same call, another time we might use it is when we are calling other external apis or services in the same request and finally we might want to use api views when we need access to local files or data.
	Creating an APIView:
		![[Screenshot 2024-01-21 at 11.12.50 AM (2).png]]
	Configure view URL:
		![[Screenshot 2024-01-21 at 11.18.36 AM (2).png]]
		
		![[Screenshot 2024-01-21 at 11.40.03 AM (2).png]]
	Testing our API:
		![[Screenshot 2024-01-21 at 11.41.02 AM.png]]
	Create a Serializer:
		![[Screenshot 2024-01-21 at 11.51.16 AM (2).png]]
	Add POST method to APIView:
	These serializers is the serializer module that we created in our profiles API project we're going to use this to tell our API view what data to expect when making post put and patch requests to our API so we set the sterilizer by typing serializer underscore class equals serializers.HelloSerializer. This configures our API view to have the serializer class that we created in the previously so this says whenever we're making a or whenever we're sending a post put or patch request expect an input with name and we're going to validate that input to a maximum length of **10**
	The status object from the rest framework is a list of handy HTTP status codes that we can use when returning responses from our API, so we're going to be using these status codes in our post in our post function handler.
	The self.serializer_class function is a function that comes with the APIView that retrieves the configured serializer class for our view so it's the standard way that we should retrieve the serializer class when working with serializers in a view.
	If the input is not valid well we're going to return a HTTP 400 bad request response so in the if statement type else : and then return and return a response and then in the response we're going to pass in the errors that were generated by the serializer so if we type serializer.errors this will give us a dictionary of all the errors based on the validation rules that were applied to the serializer so it's a good idea to return this so the person that's using the API knows what went wrong when they tried to submit an invalid response.
	By default the response returns HTTP 200 request, now since this was an error we need to change this to a 400 bad request so we return the standard error response code for this type of error in an API so let's actually break this down on to separate lines here and let's add a second parameter called status equals status. (and then in all capitals) HTTP 400 bad request. Now we could pass in just an integer 400 here however it's good to use this status object here to get it because then we can easily see what the request means when we're looking at the code so we know this 400 bad request means there was a bad request made to our API.
	![[Screenshot 2024-01-21 at 12.35.51 PM (2).png]]
	
	![[Screenshot 2024-01-21 at 12.36.48 PM (2).png]]
	Add PUT, PATCH and DELETE methods:
		HTTP PUT is often used to update an object, what we do is we make a request with HTTP PUT and it will update the entire object with what we've provided in the request so this is different from a HTTP patch.
		When we're doing HTTP put we typically do it to a specific URL primary key that's why we have this PK but we default it to none in case we don't want to support the PK in this particular API view but usually what we would do is we would do a PUT to the URL with the ID of the object that we're updating and that's what we use this PK for this is to take the ID of the object to be updated with the PUT request we're not actually going to be updating an object we're just going to return a standard response just to demonstrate how you can add the put method to our API view and test it.
		So what we would typically use HTTP PATCH for is to do an update but only update the fields that were provided in the request so if we had a first name and a last name field and we made a patch request with just providing the last name it would only update the last name whereas if we did a put request and we only provided the last name then in that case it would remove the first name completely because HTTP put is essentially replacing an object with the object that was provided whereas patch is only updating the fields that were provided in the request.
		The delete request is used for deleting objects in the database.
		
		![[Screenshot 2024-01-21 at 1.28.58 PM (2).png]]
	Test the PUT, PATCH, and DELETE methods:
		
		![[Screenshot 2024-01-22 at 1.31.18 AM.png]]

Introduction to Viewsets:
	What is a Viewset?
		Just like API views, view sets allow us to write the logic for our endpoints however instead of defining functions which map to HTTP methods, view sets accept functions that map to common API object actions such as list for getting a list of objects, create for creating new objects, retrieve for getting a specific object, update for updating an object, partial update for updating part of an object and finally destroy for deleting an object.
		Additionally view sets can take care a lot of the common logic for us they're perfect for writing apis that perform standard database operations and they're the fastest way to make an api which interfaces with a database back-end.
		So when should we use view sets? Well a lot of the time this comes down to personal preference however here are some examples of cases when we might want to prefer a view set over an API view, for example if we need to write an API that performs a simple create read update and delete(CRUD) operation on an existing database model or we need a quick and simple API to manage predefined objects or maybe we need a very basic custom logic additional to the view set features already provided by the Django rest framework.
		 Finally we might want to use a view set if our API is working with standard database structure.
	Create a simple Viewset:
		![[Screenshot 2024-01-22 at 2.59.27 AM.png]]
		Below our hello API view let's create a new class called class hello view set and we're going to base our class on viewsets.Viewset which is the base view set class that Django rest framework provides.
		
		![[Screenshot 2024-01-22 at 3.19.14 AM.png]]
	Add a URL Router:
		Just like with our API view we need to register our new view set with a URL to make it accessible through our API the way that we register the viewset with a URL is slightly different from how we register the API view with the URL, if we open up the urls.py file we can see that we passed in a new URL pattern using the path function to register our API view with the hello-view URL. The way that viewsets work is we use what's called a router which is a class that's provided by the Django rest framework in order to generate the different routes that are available for our view set so with our view set we may be accessing the list request which is just the route of our API and in this case we would use a different URL than if we are accessing a specific object to do an update a delete or a get.
		
		![[Screenshot 2024-01-22 at 3.34.24 AM.png]]
		For now let's create a default router and register our view set with the default router and pass the URLs into URL pattern so before we can do this we need a couple more imports here at the top of the file so we need to add include after the path import this imports the function called include which comes with the django.urls module this is used for including lists of URLs in the URL pattern and assigning the lists to a specific URL. Next we're going to import the default router so if we do from rest_framework.routers import DefaultRouter. Okay and the way that we use default route is we assign the router to a variable by doing router= DefaultRouter and then we use router.register to register specific view sets with our router so let's type router.register(the first argument is the name of the URL that we wish to create so we're going to create one called 'hello-viewset')  just like we have hello - view here we're  going to access our API using hello - view set because the router will create all of the four URLs for us we don't need to specify a forward slash here when we define our view set URL name the second argument is the view set that we wish to register to this URL so if we type views.HelloViewSet which is the view set we created previously in our views.py file finally we need to specify a base_name for our view set so we do that by typing base_name= 'hello-viewset' this is going to be used for retrieving the URLs in our router if we ever need to do that using the URL retrieving function provided by Django. Okay so now that we've registered our router and we've created our router and registered our new view set with it let's add this to our URLs patterns create a new line below the existing path that we created and type path and we're going to create a new path with just a blank string and then the second argument we're going to use the include function that we imported here we're going to type include router.urls so as you register new routes with our router it generates a list of URLs that are associated for our view set it figures out the URLs that are required for all of the functions that we add to our view set and then it generates this URLs list which we can pass in to using the path function and the include function to our URL patterns, the reason we specify a blank string here is because we don't want to put a prefix to this URL we just want to include all of the URLs in the base of this URLs file.
	Testing our ViewSet:
		 
		 ![[Screenshot 2024-01-22 at 8.38.27 AM.png]]
		 We may notice that this page looks slightly different from previously when we previously tested our API view and that's because the router has a cool function where it will add this browsable API for all the other items registered to our router unfortunately it doesn't include any APIViews or any URLs that we've registered directly to the URLs pattern it only includes things we register via our router and this is just a limitation of this feature in the Django rest framework.
		 We can see here that we have our hello view set that we registered and if we click it then it will return the response that we defined in our view set in the views.py which is a hello message and a list of all of the features or some features of view sets in the Django rest framework so when we access this URL we do a HTTP GET to the base of the registered view which will take us to this list function that will execute this code and return this response so we can see that our hello view set is working correctly in our project.
	Add create, retrieve, update, partial_update and destroy functions:
		So these functions are going to represent the different HTTP methods that we've added to our APIView but for our viewset.
		Destroy maps to delete so if we wish to remove an object then we would call HTTP delete on our view set which would then call this destroy function and run the code that we write in here. Same goes for all the other methods.
		
		![[Screenshot 2024-01-22 at 10.27.43 AM.png]]
		
		![[Screenshot 2024-01-22 at 10.48.40 AM.png]]
	Test Viewset:
		
		![[Screenshot 2024-01-22 at 10.36.53 AM.png]]
		Unlike the API view we don't actually see the put patch and delete methods here on the hello view set API that's because view sets expect that we will use this endpoint to retrieve a list of objects in the database and we will specify a primary key ID in the URL when making changes to a specific object.
		So if we want to see these additional functions that we added we need to add something to the end of the URL.
		Now in in this case because we aren't actually retrieving any real objects it doesn't matter what you type but if we just put a number here that would represent a primary key of an object that we wanted to change and hit enter then it will change the page to the get request which is the retrieve of that object so when we specify a primary key to a view set URL it calls the retrieve function. 

Create Profiles API:
	Create user profile serializer:
		We're going to add a new serializer to the serializers.py file of our profiles API project. The serializer that we're going to add here is going to be a model serializer, it's very similar to a regular serializer except it has a bunch of extra functionality which makes it really easy to work with existing django database models. So we're going to create a new serializer called user profile serializer we're going to base it off of these serializers.ModelSerializer (model serializer class), and we're going to connect it up to our user profile model.
		
		![[Screenshot 2024-01-22 at 10.58.40 PM.png]]
		Then what we're going to do is define a meta class. The way that we work with model serializers is we use a meta class to configure the serializer to point to a specific model in our project. 
		
		![[Screenshot 2024-01-22 at 11.02.45 PM.png]]
		This sets our serializer up to point to our user profile model, the next thing that you do with a model sterilizer is we need to specify a list of fields in our model that we want to manage through our serializer so this is a list of all the fields that we want to either make accessible in our API or we want to use to create new models with our serializer.
		
		![[Screenshot 2024-01-22 at 11.11.19 PM.png]]
		So this is the list of fields that we want to work with, we want to make an exception to the password field because we only want to use this when creating new users in the system, we don't want to allow the users to retrieve the password hash because there's certain security risks associated with that so we want to make this password field write only the way we do that is we use the extra keywordargs variable here so type extra underscore kwargs equals and this is going to be a dictionary and the keys of the dictionary are the fields that we want to add the custom configuration to so we're only going to provide one for the password field and then create a new dictionary associated with this password and we are going to add two more key value pairs the first one is going to be write_only and the value is going to be true so this says when we create our password field from our model set it to write_only= true that means we can only use it to create new objects or update objects, we can't use it to retrieve objects so when we do a get we won't see the password field included in that response the second thing we're going to do is add a custom style to this and this is just for the browsable api and what it does is it will set the field type to a password field which means we won't be able to see the input as we're typing it so we'll just see the dots or the stars that we would expect in a regular password input field so let's type style : and then this accepts another dictionary and we're going to put input_type and we're going to give it the input type of password.
		The next thing we're going to do is we're going to overwrite the create function by default the model serializer allows us to create simple objects in the database so it uses the default create function of the object manager to create the object, we want to override this functionality for this particular serializer so that it uses the create user function instead of the create function the reason we do this is so that the password gets created as a hash and not the clear text password that it would do by default if we didn't override the function.
		
		![[Screenshot 2024-01-22 at 11.41.13 PM.png]]
		So what happens here is whenever we create a new object with our user profile serializer it will validate the object or validate the fields provided to the serializer and then it will call this create function passing in the validated data so what we want to do here is we want to create and return a new user from our user profiles model manager so we'll type user= models.UserProfile.objects.create_user and then we're going to pass in the appropriate fields from the validated data so we'll pass in email= validated_data and we want to retrieve the email field from the validated data and then we will pass in name= validated_data and we will get the name key then password= validated_data(password) and then finally we will return the new user.
		
		![[Screenshot 2024-01-22 at 11.52.01 PM.png]]
		What this does is it will override the create function and call our create user function that we previously defined here in our user profile manager so we use this function to create new users in the database and as you can see this function calls the set password to set the password instead of just passing all the keys in as plain text.
	Bug in Profile Serializer:
		**Issue:**
		If a user updates their profile, the password field is stored in cleartext, and they are unable to login.
		**Cause:** This is because we need to override the default behaviour of Django REST Frameworks `ModelSerializer` to hash the users password when updating.
		**Fix:**
		To fix the issue, add the below method to the `UserProfileSerializer`
		1.     def update(self, instance, validated_data):
		2.         """Handle updating user account"""
		3.         if 'password' in validated_data:
		4.             password = validated_data.pop('password')
		5.             instance.set_password(password)
		6.         return super().update(instance, validated_data)
		The final `serializers.py` file will look like this: [https://github.com/LondonAppDev/profiles-rest-api/blob/master/profiles_api/serializers.py#L34](https://github.com/LondonAppDev/profiles-rest-api/blob/master/profiles_api/serializers.py#L34)
		**Explanation:**
		The default update logic for the Django REST Framework (DRF) `ModelSerializer` code will take whatever fields are provided (in our case: `email`, `name`, `password`) and pass them directly to the model.
		This is fine for the `email` and `name` fields, however the `password` field requires some additional logic to hash the password before saving the update.
		Therefore, we override the Django REST Framework's `update()` method to add this logic to check for the presence password in the `validated_data` which is passed from DRF when updating an object.
		If the field exists, we will "pop" (which means assign the value and remove from the dictionary) the `password` from the validated data and set it using `set_password()` (which saves the password as a hash).
		Once that's done, we use `super().update()` to pass the values to the existing DRF `update()` method, to handle updating the remaining fields.
	Create a Profiles ViewSet:
		Now we have our user profile serializer we can go ahead and create a view set to access the serializer through an endpoint.
		
		![[Screenshot 2024-01-23 at 5.30.48 AM.png]]
		
		![[Screenshot 2024-01-23 at 5.31.04 AM.png]]
		What we're going to use for our user profile API is something called a model view set, the model view set is very similar to a standard view set except it's specifically designed for managing models through our API so it has a lot of the functionality that we need for managing models built into it all we need to do is create our new Model View set.
		The way we use a model view set is we connect it up to a serializer class just like we would a regular view set and we provide a query set to the model view set so it knows which objects in the database are going to be managed through this view set.
		
		![[Screenshot 2024-01-23 at 6.03.10 AM.png]]
		The Django rest framework knows the standard functions that we would want to perform on a model view set and that is the create function to create new items the, list function to list the models that are in the database, the update partial update and destroy to manage specific model objects in the database Django rest framework takes care of all of this for us just by assigning the serializer class to a model serializer and the query set this is the great thing about the Model View set.
	Register profile Viewset with the URL router:
		
		![[Screenshot 2024-01-23 at 5.53.54 AM.png]]
		Unlike the hello view set that we've registered previously we don't need to specify a base name argument and this is because we have in our view set a query set object, if we provide the query set then Django rest framework can figure out the name from the model that's assigned to it so we only need to specify the base name if we are creating a view set that doesn't have a query set or if we want to override the name of the query set that is associated to it.
	Test creating a profile:
		
		![[Screenshot 2024-01-23 at 6.05.13 AM.png]]
		
		![[Screenshot 2024-01-23 at 6.07.20 AM.png]]
		A new object is created and we get a HTTP 201 created response and it returns the response containing the object that was created.
		
		![[Screenshot 2024-01-23 at 6.09.20 AM.png]]
		
		![[Screenshot 2024-01-23 at 6.13.08 AM.png]]
		We can actually also retrieve the details of a specific view set by putting in the ID of the item that we want to retrieve so if we put in profile slash one this will retrieve this user here the user with the ID of one and it'll give us the specifics of that user and it will allow us to perform put or patch functions or even delete the user from the database.
		
		![[Screenshot 2024-01-23 at 6.18.29 AM.png]]
	Create permission class:
		
		![[Screenshot 2024-01-23 at 6.42.08 AM.png]]
		We're going to import the permissions module from the rest_framework this is going to provide us with the base class that we can use to create a custom permissions class.
		BasePermission, as the name suggests, this is the base permission class that Django rest framework provides for making your own custom permissions classes.
		The way we define permission classes is we add a has_object_permission function to the class which gets called every time a request is made to the API that we assign our permission to, this function will return a true or a false to determine whether the authenticated user has the permission to do the change they're trying to do.
		So what happens here is every time a request is made the djangorestframework will call this function has_object_permission and it will pass in the request object, the view, and the actual object that we're checking the permissions against so when we try and update a user profile this gets called and all of these functions get passed in for the particular request and the attempted object that we're trying to make the change on so we need to check whether we should allow or deny this change and add the rules in here in the has_object_permission logic, what we're going to do is we're going to check the method that is being made for the request and we're going to see whether that is in the safe methods list so the method is the HTTP method that is being used on the current request so that could be a HTTP GET, PUT, PATCH or DELETE request. The safe methods are methods that don't require or don't make any changes to the object so a safe method would be for example HTTP GET because all we're doing is reading an object we're not actually trying to make any changes to the object itself. So we want to allow users to view other users profiles but only be able to make changes to their own profile.
		
		![[Screenshot 2024-01-23 at 7.06.55 AM.png]]
		So if the method being used is a HTTP GET then it will be in the safe methods, therefore it will just return true and allow the request. Now we need to handle what happens if the request is not in the safe methods for example if they're trying to do a HTTP put to update an object. What we're going to do is we're going to check whether the object they're updating matches their authenticated user profile that is added to the authentication of the request so when we authenticate a request in Django rest framework it will assign the authenticated user profile to the request and we can use this to compare it to the object that is being updated and make sure they have the same ID.
		
		![[Screenshot 2024-01-23 at 7.13.33 AM.png]]
		When we return object.id== request.user.id, if this evaluates to true then it will return true and if it doesn't evaluate to true then it will return false, so when the user makes a request we're going to check if the request is in the safe methods, if it is in the safe methods we're just going to allow the request to go through otherwise if it's not in the safe methods so they're using an update or a delete or something like that then we will return the result of if the object.id== request.user.id.
		This way it will return true if the user is trying to update their own profile or otherwise it will return false.
	Add authentication and permissions to Viewset:
		
		![[Screenshot 2024-01-23 at 7.42.42 AM.png]]
		The token authentication is going to be the type of authentication we use for users to authenticate themselves with our API ,it works by generating a random token string when the user logs in and then every request we make to their API that we need to authenticate we add this token string to the request and that's effectively a password to check that every request made is authenticated correctly we're going to configure this on our view set.
		
		![[Screenshot 2024-01-23 at 7.43.14 AM.png]]
		The TokenAuthentication is the type of authentication we're going to be using. We can configure one or more types of authentication with a particular view set in the djangorestframework, the way it works is we just add all the authentication classes to this authentication_classes class variable.
		So the authentication class is set how the user will authenticate that is the mechanism they will use and the permission classes is set how the user gets permission to do certain things so you may have an authenticated user who has permission to do certain things or use certain api's but not other api's and you would control those fine-grained permissions by using permission classes.
		So every request that gets made, it gets passed through our permissions.py file and it checks this has_object_permissions function to see whether the user has permissions to perform the action they're trying to perform.
	Test new permissions:
		
		![[Screenshot 2024-01-23 at 7.45.20 AM.png]]
		As we can see the profiles that we have in the system are still listed as they were before. We also have the option to create new profiles in the system here this is because these actions fall within the safe methods list in the djangorestframework, what that means is the action to list objects and create new objects don't perform any destructive changes to existing objects in the system, therefore we're going to always allow users to be able to list and create new profiles but what we will restrict is users from modifying other users profiles when they're not authenticated.
		
		![[Screenshot 2024-01-23 at 7.49.22 AM.png]]
		So if we head over to a specific profile like the one with ID 1 by adding one to the end of the URL then we may notice that the option to modify this profile is no longer available that's because we're not authenticated with this profile and because we're not authenticated we don't get the option to change it now if we authenticated with this specific user we would be able to update this profile we can also check profile with ID two and we see the same thing so we can see that the permissions are restricting us from being able to modify profiles when we're not authenticated.
	Add search profile features:
		
		![[Screenshot 2024-01-23 at 7.55.06 AM.png]]
		Out of the box the rest framework comes with some modules that we can use to add filtering to a view set really easily.
		
		![[Screenshot 2024-01-23 at 7.58.49 AM.png]]
		search_fields: This tells the filter back-end which fields we're going to make searchable by this filter.
		So what this will do is it will add a filter back end and we can add one or more filter back ends to a particular view set. We're going to add a filter back end for the search filter which is something that comes with djangorestframework and then we'll specify the search fields name and email, this will mean that the djangorestframework will allow us to search for items in this view set by the name or email field.
	Test searching profiles:
		
		![[Screenshot 2024-01-23 at 8.06.26 AM.png]]
		The filters option is added this is because we added the filter_backends to our REST API view set and the Django rest framework gave us this option to help test this feature in the browser so if we click on the filters it will allow us to search for a particular item in our view set and because we specified the email and the name as the search field it will search for anything containing or any name or email containing the string that we provide here.
		
		![[Screenshot 2024-01-23 at 8.06.41 AM.png]]
		
		![[Screenshot 2024-01-23 at 8.08.07 AM.png]]
		Let's search for the name Tester2 and we can see that it filters a result to all of those containing the name Tester2 and we can do the same thing for Tester1 or the name of another user so for example if we search for Tester1 we'll see the results with the word Tester1, if we search for Tester3 you can see all the results containing the name Tester3. Now let's have a little look into how this is working here so the filters option in reality we're not going to be clicking it in the browser when we use our API, we're going to be using it from a different application so the way it works is the filters button adds this search parameter here as a GET parameter to the request so all it does is it puts the question mark(in the search bar) to signify the first GET parameter and it has a parameter called search that's the name of the parameter and it has a value called Tester1 so we can manipulate this manually in the browser URL and we can apply the search like this so if we search for the name Tester3 we can see that it applies the search and returns the name Tester3. We search for the number two we can see that it returns Tester2 because it's the only one that contains the number two. If we put the words or the letter 'T' hit enter then we can see it returns all of them because they all contained the letter T so this is how we would apply the search parameter when we consume the API. We would add it to the URL and then the Django rest framework would filter it accordingly okay so that's how we add search filtering in the API now we can see that that's working.
		
		![[Screenshot 2024-01-23 at 8.25.11 AM.png]]

Create a Login API:
	Create a Login API viewset:
		
		![[Screenshot 2024-01-24 at 3.20.13 AM.png]]
		The type of authentication we're going to use is called token authentication it works by generating a token which is like a random string when we log in and then every request we make to the API that we wish to authenticate we include this token in the headers.
		First we need to add an endpoint to our API that allows us to generate an authentication token this is effectively our login API, fortunately the Django rest framework comes with an auth token view.
		ObtainAuthToken: this is a view that comes with the Django rest framework that we can use to generate an auth token.
		
		![[Screenshot 2024-01-24 at 3.41.59 AM.png]]
		We're going to add a new class called the UserLoginApi view so type class user login API view and we're going to base our class from the obtain auth token class that we added just now then add the doc string handle creating user authentication tokens so this obtain auth token class that is provided by the Django rest framework is really handy and we could just add it directly to a URL in the urls.py file however it doesn't by default enable itself in the browsable Django admin site so we need to override this class and customize it so it's visible in the browsable api so it makes it easier for us to test.
		So what we need to do is add a class variable here called renderer classes underscore classes equals and then we're going to import the default renderer class from the API settings so that's why we needed to import the API settings at the top of the file so set the renderer classes to api_settings.Default_Renderer_Classes, what this does is it adds the renderer classes to our obtain auth token view which will enable it in the Django admin the rest of the view sets and things other things that are provided by the Django admin have this by default but the obtain auth token doesn't have it by default so we need to add it manually.
	Test Login API:
		
		![[Screenshot 2024-01-24 at 4.10.30 AM.png]]
		
		![[Screenshot 2024-01-24 at 4.11.34 AM.png]]
		We can see that it has a username and password input the username is the username field that we're going to be using for authentication which is mapped to the email field.
		
		![[Screenshot 2024-01-24 at 4.13.49 AM.png]]
		Now since we're using the Django admin built-in authentication system it still calls the field username there even though we mapped it to our email field but all we need to know is that the username needs to be the identifier which is the email that we use for the login.
		A token which is the authentication token gets generated after inputting the username(email and password) that we can use to authenticate future requests to our API.
		We can assign this token to the headers of a request so we can authenticate an API request.
	Set token header using ModHeader extension:
		 Now the way that the token authentication works is every single request that's made to the API has an HTTP header. What we do is we add the token to the authorization header for the requests that we wish to authenticate so when we make a request like a HTTP GET HTTP put patch or post with that request we can provide a header and in our header we're going to add a key called authorization and then we're going to pass in this token with the request and then when djangorestframework receives that request it can check whether this token exists in the database and retrieve the appropriate user for this token so we're going to use the mod header chrome extension to set our header and check that we can manage our profile when we're authenticated with it. 
		 
		 ![[Screenshot 2024-01-24 at 4.38.55 AM.png]]
		 So let's copy the string that we were given from our token, and then we're going to open up the mod header chrome extension and we're going to type in the request headers name we're going to type Authorization and we can see that it gives it a drop-down here and then the way we pass in the token is we write 'Token' and then space and then we paste the token so the Django rest framework knows to remove this token part from the prefix here and then just take this as the token so this is the standard convention for providing a token in the authorization header for the Django rest framework okay so that's all we need to do to authenticate the requests.
		 Make sure we have this box checked here.
		 ![[Screenshot 2024-01-24 at 4.39.48 AM.png]]
		 And then head over to api/profile and we can see that we returned the list of profiles now we authenticated as the hbret82@gmail.com profile so take the ID for the profile we authenticated with and put that ID in the URL here so we're going to test with ID 2 so we're going to put profile/one and hit enter, we can see that now we can modify this profile because we've authenticated as that user so we can go ahead and change the name, and then let's change the password.
		 ![[Screenshot 2024-01-24 at 4.40.36 AM.png]]
		  Now hit put and we can see that it returned the updated object with a new name so if we go back to the profiles list by removing the ID we can see that the name has been updated here.
		  ![[Screenshot 2024-01-24 at 4.41.37 AM.png]]
		  So what happens if we go to another profile that we're not authenticated with? Let's go to profile 1, we can see that we're unable to modify this profile because we haven't authenticated with the correct user so let's go back to profile 2 and then if we wanted to disable the authentication while we're browsing the API then we can simply open up the mod header chrome extension and uncheck this box here and then this header will no longer be sent with the HTTP requests so when we uncheck it and then we refresh the page, we can see that the option to modify this profile disappeared because we're no longer authenticated.
		  A couple of things to note about the mod header Chrome extension:
		  - If we're browsing other websites when we have the authorization token enabled then it may conflict with those websites so just make sure to disable the authorization token whenever we're not testing the API as it can often creates some unexpected side effects on websites like Google and Google Drive and things like that.
		  - okay another thing to note is that this isn't how we would use this token in real life when we actually use the API we would pass the token in into whichever client library we're using so if we're using JavaScript then we may use a library like the fetch library, if we're using Python then we may use a library like the request library and these HTTP libraries all allow us to add custom header tokens to our requests, we're just using this mod header chrome extension in order to test our API in the browser.


Create Profile Feed API:
	Add a new model item:
		The first step of creating our user profile feed API is to create a new django model for storing the user profile feed items in the database.
		![[Screenshot 2024-01-24 at 5.39.13 AM.png]]
		from django.conf import settings, this is used to retrieve settings from our settings.py file in the project settings of our Django project, the particular setting that we're going to retrieve is this Auth_User_Model.
		
		![[Screenshot 2024-01-24 at 5.45.36 AM.png]]
		
		![[Screenshot 2024-01-24 at 5.47.01 AM.png]]
		This is going to be the model we use to allow users to store status updates in the system so every time they create a new update it's going to create a new profile feed item object and associate that object with the user that created it.
		 The way we link models to other models in Django is we use what's called a foreign key, when we use the foreign key field it sets up a foreign key relationship in the database to a remote model, the benefit of doing this is that it allows us to ensure that the integrity of the database is maintained so we can never create a profile feed item for a user profile that doesn't exist so let's go ahead and add our user profile field to our profile feed item.
		
		![[Screenshot 2024-01-24 at 6.37.51 AM.png]]
		user _ profile= models.foreign key(), and the first argument of a foreign key field in models is the name of the model that is the remote model for this foreign key, so which model do we want to set a relationship up from this user profile field to a remote model, so we're going to set it up to the user profile model, now we could specify this as a string as the first argument of the foreign key however when we're referencing the Auth_User_Model in Django it's best practice to retrieve this from the settings.py configuration. The reason for this is that we may decide that we want to switch out this user profile model as our default authentication model and we want to switch it back to the Django default model if we hard-coded the name of the model here then we would have to go through and manually update all of the foreign keys where we hard-coded that if we were to switch out the default user model so what we do instead is we've referenced it by typing settings.AUTH_USER_MODEL and what this will do is it will retrieve the value from the auth user model setting in our settings.py file so if we ever swap this auth user model to a different model then the relationships will automatically be updated without us having to go through and manually change it everywhere that we've referenced it in our models.py file.
		The second argument we need to provide is the on delete argument so type on_delete= models.CASCADE. Now what the on_delete does is it tells Django or it tells the database what to do if the remote field is deleted so we have user, we have profile feed items in our database and each one of them has a user profile associated with it now because there's a foreign key association the database needs to know what happens if we remove a user profile what should happen to the profile feed items that are associated with it and the way we do that is by specifying this on_delete so there are different things that we can set on_delete one of them is cascade and what that does is it says basically cascade the changes down through all the related fields so if we have user profile feed items associated to a user profile and we remove that profile then it will cascade the change down and remove the associated feed items from that user another option is to set that field as null so what it would do is models.set null would set the value of the user profile to null if the remote user profile is deleted now it might be better to cascade in this case because if a user wants to delete their profile then we can assume that they also want to delete all the feed items that are associated with their profile.
		status_text is going to be used to contain the text of the feed update.
		So we're going to set a char field here which is a standard character field and allows us to put in a text input up to 255 characters long.
		created_on, what this does is it says every time we create a new feed item automatically add the date time stamp that the item was created so we don't need to manually set this when we're creating the item it will automatically be set to the current time because of this auto now add parameter.
		Finally we're going to add a string representation of our model so that is to tell Python what to do when we convert a model instance into a string.
		From the image the '__str__' function does this job. When we convert this to a string we want to see the status text value that is associated to the model.
	Create and run model migration:
		
		![[Screenshot 2024-01-24 at 6.46.22 AM.png]]
	Add profile feed model to admin:
		
		![[Screenshot 2024-01-24 at 6.52.27 AM.png]]
	Create profile feed item serializer:
		
		![[Screenshot 2024-01-24 at 7.07.13 AM.png]]
		We're going to set our model serializer to our profile feed item class.
		This sets our serializer or our model serializer to our profile feed item model that we created in models.py.
		Our profile feed item has three fields that we've added here one is the user profile that is associated to the feed item the next one is the status text and finally we have the created on, so the user profile is the profile that owns or created the profile feed item the status text will be the content of the feed item, so kind of like a status update and the created on is automatically set to a date time field with the current time that the item was created so we need to make these fields available through our serializer.
		Type fields= and include the ID so we can use that to retrieve specific objects and by default Django adds a primary key ID to all models that we create so the first one we're going to set is ID and then we'll put the user_profile and then status_text and then created_on, so because the ID is set up by Django by default it's automatically set to read only so when we create a new object the new ID is created by the database and it is set to the next available integer field or integer value in the table so it just increases for every object we create, the created on is automatically set as well it's automatically set to the time that it's created so that will by default be read-only so the only fields that will be writable in our serializer in its current state are the user profile and the status text however we don't want the users to be able to set the user profile when they create a new feed item we want to set the user profile based on the user that is authenticated so we don't want to be able to create... or we don't want one user to be able to create a new profile feed item and assign that to another user because that would be a security flaw in the system so we want to set this to the authenticated user and therefore we're going to make the user profile field read-only, so that means that when we list the objects we can see which users created which feed items but when we create an object it can only be assigned to the current user that is authenticated, so below the fields we're going to set a new value called extra_kwargs= and then we set this to a dictionary and this is how we add extra keyword arguments to fields and we're going to set extra arguments to the user_profile field and the arguments we're going to set are read_only and we're going to set that to true so this allows us to set the user profile field to read-only in our model serializer.
	Create viewset for our profile feed item:
		
		![[Screenshot 2024-01-24 at 11.31.01 AM.png]]
		Let's add a new class called class UserProfileFeedViewSet, then we're going to base our class from viewsets.ModelViewSet.
		We're going to use the token authentication to authenticate requests to our endpoints.
		(Note: Do not forget to put ',' after writing TokenAuthentication to make it a tuple.)
		Next we're going to set the serializer class to this serializer that we created previously.
		Next we're going to assign the query set that's going to be managed through our view set.
		We're going to manage all of our profile feed item objects from our model in our view set.
		This sets up a basic model view set that allows us to create and manage feed item objects in the database however, we want to set this user_profile(in ProfileFeedItemSerializer) to read only because we're going to set it based on the authenticated user. In order to do that we need to add a perform_create function to our Model View.
		The perform_create function is a handy feature of the djangorestframework that allows us to override the behavior or customize the behavior for creating objects through a ModelViewSet. So when a request gets made to our viewset, it gets passed into our serializer class and validated and then the serializer.save function is called by default, if we need to customize the logic for creating an object then we can do this using the perform_create function so this perform_create function gets called every time you do an HTTP POST to our view set.
		So when a new object is created djangorestframework calls perform_create and it passes in the serializer that we're using to create the object, the serializer is a ModelSerializer so it has a save function assigned to it and that save function is used to save the contents of the serializer to an object in the database. What we're doing here is we are calling serializer.save and we're passing in an additional keyword for the user_profile this gets passed in in addition to all of the items in the serializer that have been validated, so we're going to set the user profile to this self.request.user, the request object is an object that gets passed into all view sets every time a request is made and as the name suggests it contains all of the details about the request being made to the view set. Because we've added the token authentication to our view set if the user has authenticated then the request will have a user associated to the authenticated user so this user field gets added whenever the user is authenticated. If they're not authenticated then it's just set to an anonymous user account.
		
		![[Screenshot 2024-01-24 at 11.49.50 AM.png]]
		Let's head over to the urls.py and link up our new view set to a URL below the profile the registering of the profile view set lets type router.register and we're going to call this URL 'feed' because it's going to be the user's feed and we're going to assign it to views.UserProfileFeedViewSet.
	Test Feed API:
		
		![[Screenshot 2024-01-24 at 11.55.37 AM.png]]
		
		![[Screenshot 2024-01-24 at 11.55.51 AM.png]]
		Now this is where we can create and modify status updates for our user.
		
		![[Screenshot 2024-01-24 at 11.57.14 AM.png]]
		So if we add a new status text and we'll just write test status for this one and hit post we can see that it goes and creates a new status update for us and returns the object in the browser. So we can see that it created a new object with the id: 1 and it assigned it to the user_profile: 2 because that is the user that we are currently authenticated with.
		Okay. So what if we wanted to modify this. Well let's test the HTTP put and patch methods on this API.
		
		![[Screenshot 2024-01-24 at 12.12.42 PM.png]]
		So add the primary key ID which is the ID field of the object that was just created to the end of the URL of our feed endpoint and hit enter. This will take us to the page where we can modify or perform HTTP put or HTTP patch requests on our object.
		 
		![[Screenshot 2024-01-24 at 12.13.56 PM.png]]
		So if we want to perform a PUT we simply just modify the text here. So let's say we change this to text status 2 and hit PUT, we can see that the status text changes for this object, if we want to test the patch you have to do this in the raw data tab.
		 
		![[Screenshot 2024-01-24 at 12.17.26 PM.png]]
		So we'll remove all of these read only fields and then we'll just leave the status text and we'll just change this to test status 3 and we'll hit patch. Make sure that we remove the trailing comma here because otherwise it will be an invalid json object and we'll get a validation error.
		
		![[Screenshot 2024-01-24 at 12.19.23 PM.png]]
		This all appears to be working. Let's try and delete our object. So hit delete and then this will make an HTTP DELETE request to our object and it will remove the object. And then if we go back to the root of the feed we can see that there are no items here.
		
		![[Screenshot 2024-01-24 at 12.20.41 PM.png]]
		This is when we're authenticated. What happens if we try and create an object when we're not authenticated? So let's uncheck the authorization in the mod headers chrome extension and then we're going to go ahead and just refresh the feed page and let's create a new status, click on the HTML form and we'll just put some test status text and then hit post. We can see that because we are not authenticated we got an uncaught exception raised.
		
		![[Screenshot 2024-01-24 at 12.23.32 PM.png]]
		So this is an error and this is because we cannot assign the anonymous user object to the user profile of the feed item. So this indicates that there are a few more changes that we need to make to our API view set in order to handle this case and ensure that we never see an error like this in our API.
	Add permissions for feed API:
		Previously we tested our feed API in the browser, everything seemed to work okay except for we were able to attempt to create new feed objects when we weren't authenticated.
		We're going to fix this issue by creating a custom permission class and using an existing permission class that comes with the djangorestframework.
		
		![[Screenshot 2024-01-25 at 2.32.55 AM.png]]
		The first change we're going to make is in our permissions.py file we're going to add a new permissions class that's very similar to the UpdateOwnProfile class but it's for updating the users own status so this permission class is going to ensure that if a user is updating a status, that it is a status that is assigned to their user account, this way users can only update their own feed items in the database.
		So let's create a new class called class UpdateOwnStatus and we're going to base our class from permissions.BasePermission.
		Just like with the update own profile we need to add a has_object_permission function to our permission class. Then the arguments that we need to add are self, request, view, and obj.
		Now because this permission class is only to ensure that users can update their own status we're going to allow all these methods that are in the safe methods through so that is if they're trying to retrieve or create a new item we're going to return true.
		Now we need to check that if the user is trying to update a status that means they're not in the safe method so they're trying to perform a put or a patch or a delete we want to make sure that the user owns that status or that the user profile associated with the status is assigned to the user making the request.
		So if the object that is being modified has a user_profile.id the same as the request.user.id then this will return true and it will allow the permission through otherwise it will return false and it will block the request being made.
		Now we need to configure our view set to use this permission.
		
		![[Screenshot 2024-01-25 at 2.53.54 AM.png]]
		We're going to configure it to use our permission but we're also going to add a new permission that comes with the Django rest framework. 'from rest_framework.permissions import IsAuthenticatedOrReadOnly'. As the name suggests this makes sure that a view set is read-only if the user is not authenticated.
		
		![[Screenshot 2024-01-25 at 3.04.43 AM.png]]
		Let's add a new class variable to our view set called permission_classes.
		(Note: Break the tuple here since the input is long and will break the 79 character limit.)
		Let's add our first permission which is the permission we created in permissions.py that is the UpdateOwnStatus permission.
		And then below this we're going to also add the is authenticated or read-only permission from the djangorestframework.
		So this will make sure that a user must be authenticated to perform any request that is not a read request. So that will get rid of the issue of users trying to create a new feed item when they're not authenticated. On top of that we'll also ensure that users can only update statuses where the user_profile is assigned to their user which will stop users being able to update the statuses of other users in the system.
	Test Feed API permissions:
		Okay now that we've set up the permissions on our feed API let's go ahead and test it in the browser.
		![[Screenshot 2024-01-25 at 3.09.34 AM.png]]
		We can see that we are currently unauthenticated because we haven't checked the authorization box in the mod header Chrome extension so let's leave it unauthenticated and let's just click on the URL again and hit enter to reload the page we can see that this time because we added the IsAuthenticatedOrReadOnly permission the only thing that we're allowed to do is read the objects in the API, currently there are no objects so it just returns an empty list.
		
		![[Screenshot 2024-01-25 at 3.14.32 AM.png]]
		
		![[Screenshot 2024-01-25 at 3.14.48 AM.png]]
		
		![[Screenshot 2024-01-25 at 3.15.18 AM.png]]
		Let's try adding authentication back to the mod header Chrome extension and then refresh the page again, we can see that now we're authenticated we have the ability to create new status objects.
		Let's add a new object called new object and hit post to create the new status object, now we're going to test what happens if we try and modify this object from a different user this is to test the UpdateOwnStatus permission.
		
		![[Screenshot 2024-01-25 at 3.21.41 AM.png]]
		So we're going to head over to api/login to generate a new login token for a different user now we're currently using the hbret82@gmail.com.com user so we're going to authenticate with tester1@testmail.com and you can see that we have a new token here so we're just going to copy the contents of this token and then we're going to add a new row to the mod headers extension by clicking add request header.
		
		![[Screenshot 2024-01-25 at 3.26.24 AM.png]]
		We're going to uncheck the first authorization token because we only want to use one at a time and we're going to use the second then we're going to head back to the feed API, we can see here that now we are authenticated as tester1@testmail.com.
		
		![[Screenshot 2024-01-25 at 3.27.20 AM.png]]
		So what happens if we head over to the ID object with the ID of 2. We can see that we're unable to modify this object because it isn't assigned to us the user profile doesn't match the ID that we're currently authenticated as.
		
		![[Screenshot 2024-01-25 at 3.29.08 AM.png]]
		Let's go and create a new item here so New Item hit post and then go back to the route of the URL and we can see that the user profile 1 is the user that we're logged in as.
		
		![[Screenshot 2024-01-25 at 3.29.27 AM.png]]
		 
		![[Screenshot 2024-01-25 at 3.29.50 AM.png]]
		If we were to /3 and modify this object we can see that we can change the text "Changed text".
		
		![[Screenshot 2024-01-25 at 3.31.21 AM.png]]
		
		![[Screenshot 2024-01-25 at 3.31.45 AM.png]]
		So for objects that we create we're able to modify but objects that we didn't create we're unable to modify or delete.
	Restrict viewing status updates to logged in users only:
		So now that we can see the permissions are working for reading objects when we're not authenticated, what happens if we want to restrict this API so only authenticated users can view it, this is very common with many apps we often will only want to limit certain api's for users who are authenticated with the system and if we're not authenticated we don't want to allow them to even read or view other objects so let's go ahead and modify our feed API to ensure that users are authenticated to view it.
		
		![[Screenshot 2024-01-25 at 4.20.31 AM.png]]
		What we're going to do is we're going to go to the top of the file and we can see here what we imported IsAuthenticatedOrReadOnly the djangorestframework has another handy permission that comes with it by default just called IsAuthenticated so we can just remove this OrReadOnly from the end and then that is the permission we want to import so we just want to use the is authenticated permission which blocks access to the entire endpoint unless the user is authenticated.
		
		![[Screenshot 2024-01-25 at 4.20.47 AM.png]]
		Let's scroll to the bottom of the file and update our permission classes accordingly so let's remove the OrReadOnly from this as well and then we can actually reformat this because the length is shorter now, so we'll reformat it into one line to keep it neat and tidy.
	Test new private feed:
		Now that we've updated the permissions on our feed API, let's go ahead and test that they're working okay in the browser.
		
		![[Screenshot 2024-01-25 at 4.26.54 AM.png]]
		Then let's open up the Google Chrome browser we can see that we're currently authenticated and listing items in the feed API so what happens if we uncheck the authorization header in the mod headers Chrome extension and refresh the page.
		
		![[Screenshot 2024-01-25 at 4.27.34 AM.png]]
		
		![[Screenshot 2024-01-25 at 4.27.56 AM.png]]
		If we hit that we can see that it returns authentication credentials were not provided this is because this endpoint is now locked down to authenticated users only. So we can see that the permission classes are working as expected now.

Deploying our API to a server on AWS:
	Introduction to deploying our app on AWS:
		We're going to be creating a new server on AWS, deploying our code and configuring the server to make it available on the internet.
	Add key pair to AWS:
		Now we're going to add a SSH key pair to AWS the reason we do this is so that when we create our server we can connect to it using ssh authentication this is the same method of authentication that we use to connect to github.
		We're going to start by outputting the content of our SSH key pair public file, so open up the git bash or the terminal window and we want to get a terminal window on our local machine not on the vagrant server it's very important that it's running on our local machine otherwise we won't be able to access the SSH key we need to set up the authorization.
		So we're going to output it by typing: cat ~/.ssh/id_rsa.pub. It's very important that we add the pub for public because we want to output the public file for our key so hit enter there and then we can copy the contents right from the beginning ssh RSA all the way to the end where the comment ends let's right-click that and copy and then open up the Google Chrome browser and we want to make sure that we are logged in to our AWS console.
		
		![[Screenshot 2024-01-30 at 2.57.30 PM.png]]
		We're going to click on services we're going to head over to EC2. EC2 is where the key pairs can be added for use on our server instances so on the left-hand side here let's scroll down and find the bit that says key pairs here underneath network and security click on key pairs to open up the key pair page. What we're going to do is we're going to import a key pair because we already have a key pair created that is our private key and our public key and we're just going to click import here and we'll give it the name.
		Recommended name to be given a name that matches the laptop or computer that we are authenticating then under the public key contents box we're going to paste the contents of our public key.
		
		![[Screenshot 2024-01-30 at 3.00.36 PM.png]]
		Now all we need to do is hit import and this will import our public key into AWS.
		(Note: iff ssh key isn't created prior use the instructions given below.)
		We need to creating a public/private key pair let's start by typing in our terminal or git bash window: ls ~/.ssh, and hit enter just to make sure we don't have any existing keys in our SSH directory. By default the SSH directory is where all public private SSH keys are created on the system and this should be the same for Mac or if we're using a Windows and we're using the git bash since we don't have any existing keys we're going to go ahead and create a new key by typing: ssh-keygen -t rsa -b 4096 -C, and then our email address, hbret@gmail.com. What this command does is it runs the SSH key gen tool and then it says we want to create a new key with a type RSA that's the type of key that we're creating and we want to create a key that is 4096 bytes then this -C and this message here is just the comment so we can identify what key this is for if we ever need to check it.
		If we hit enter it will generate the key pair and by default it will create it in our home directory(in Users/'username'/.ssh/id_rsa)/.ssh/id_rsa this is the default key for our system.
		Now we can create an optional passphrase for our key and it is recommended to create a, passphrase this adds an extra layer of security on our key so if somebody manages to steal the key from our computer they won't be able to use it without the passphrase.
		
		![[Screenshot 2024-01-30 at 2.53.30 PM.png]]
		Now we can see that our key has been created and we have these two new files created in our SSH directory, let's just type ls ~/.ssh again and let's check that these files exist. Okay so the id_rsa file here is the private key, now we want to make sure we never share the contents with this key or the file with anyone else we want to keep this safe at all times because this is basically like our password, the id_rsa.pub key is the public key this is the key that we can upload to services like github in order to authenticate.
		
		![[Screenshot 2024-01-30 at 2.54.45 PM.png]]
	Create EC2 server instance:
		Next we're going to create an EC2 server instance to run our project. Open up the AWS console and select services and EC2 underneath the compute option, this is where all of our EC2 server instances are in AWS. An EC2 server instance is simply just a virtual machine that we can spin up and connect to to deploy our application. Once we're on the EC2 page click on launch instance to create a new instance, if we're in the 12 month free tier period then we shouldn't be charged for following the steps in this course as long as we choose all of the options for the free tier so what we're going to do is we're going to use the Ubuntu operating system with the ami version that is put in the resources of this video so if we click the link in the resources and then copy the ami ID just to make sure we get the specific version that we did for the steps in this course, copy the ami and then head back to the choose an Amazon machine image page and enter the ami into the search box here and hit enter so we're going to be using this Ubuntu 18.04 LTS SSD volume type image as we can see here it's eligible for the free tier so if we're in the 12-month free tier period then we shouldn't be charged. Once we've found this click on select to select this as our server instance and then we're going to choose the micro instance which is the second one down and is also in the free tier then click on configure instance details and we're going to make some changes to the instance and the changes that we're going to make is we're going to add a or allow HTTP access to the instance, by default when AWS creates an instance the only port that's open is port 22 for SSH access, we also want to open port 80 so that we can connect to our web server once we create it so click on this option 6 here which is configure security group and then we're going to add a new rule and we're going to choose HTTP and then we're going to click review and launch. This will let us review the settings of our instance so just have a check here and then click on launch.
		Next we're going to be prompted to choose the SSH key that we want to set up on the server the SSH key is what we're going to use to connect to the server once it's created so make sure we choose the right one so we're going to select the key pair for mark desktop(the name of the dektop) and then check the box that acknowledges we have access to this key then click Launch instance and our instance will be created in AWS.
	Add deployment scripts and configs to our project:
		While we're waiting for our server to start in AWS let's go ahead and configure our project for deployment, start by downloading the deployed.zip file that is added as a resource to this video, this file contains a zip of all the scripts and configuration files that we need to deploy our project, we're going to add the contents of this to our project and then we're going to see what these scripts do. So once it's been downloaded unzip the deployed.zip file and copy the deploy directory into our profiles REST API project then open up the atom editor.
		So here we have a setup.sh script, this is the script that we're going to use to set up our server when it's first created, before we can run this we need to update the project git URL to the URL of our github project, this is because the script is going to clone the contents of our project to the server when we run it so we need to make sure that this is correct with the project URL for our project so open up the browser and open up github to our project and then we're going to click this clone or download button and we want to make sure we are cloning with HTTPS and we're going to copy the link of this HTTPS URL then head over to the atom editor and paste the contents in the project git url variable.
		
		![[Screenshot 2024-01-30 at 3.54.24 PM.png]]
		
		![[Screenshot 2024-01-30 at 3.54.41 PM.png]]
		So at the top of the script we set some variables this is the URL of the github project which we've just set and then we have the base path which is the directory we're going to store our project on the server, we're going to store our project in USR/local/apps/profiles-rest -api, this is where we're going to clone the project to the server and it's where all of our source code is going to be kept. Next we install some dependencies which we need to run our application on a server so we need Python Python 3 and then we need the Python 3 virtual environment and we also need sqlite Python pip supervisor nginx and git.
		So git is going to be used to clone the project, nginx is the webserver that is going to serve the static files and act as a proxy to our uWSGI service that is going to run in supervisor and then of course we have Python pip which is the package manager that we're going to use to install the packages and we have, sqlite which we're going to use for the database and then we have Python 3 virtual environment which is going to be used to set up our virtual environment, finally we have Python 3 dev which is going to be used to run Python on the server.
		The next thing we do is we create a directory to the project URL or the location on the server that we want to create or store the project files so we need to create the project before we can clone it because the next thing we do is we use git to clone the project from our git URL to the base location where we want to store the code so this is going to do a git clone and pull the source code down to the server.
		Next we create the virtual environment on the server so this creates a new directory in our project/env to create a virtual environment for Python.
		Next we install the Python packages which are everything within our requirements.txt file and additionally this uWSGI which is a Python daemon for running Python code as a webserver.
		Next we run the migrations which we've done a number of times every time we change our migrations or our models and then we run this collect static command collect static will gather all of the static files for all of the apps in our project into one directory.
		
		![[Screenshot 2024-01-30 at 4.09.07 PM.png]]
		When we use the Django management server it does this automatically for us but since we're not going to be using the Django development server on production we need to create a location with all of the static files that we can use to serve the CSS and JavaScript for the Django admin and the Django rest framework browsable api.
		Next we're going to configure the supervisor, supervisor is an application on linux that allows us to manage processes, this is what's going to manage our Python process or our uWSGI server.
		So what we do here is we copy the supervisor_profiles_api configuration.config file into the location on the server where the supervisor is kept then we run reread to update these supervisor configuration files and then we run update to update all the processes next we restart our profiles API to make sure that our service is started.
		
		![[Screenshot 2024-01-30 at 4.14.06 PM.png]]
		Finally we configure out nginx server this is the webserver that's going to be used to serve the static files so we need to create a location for the configuration file and we copy the configuration file that we've added here nginx_profiles_api.conf to the sites available directory in nginx, then we remove the default configuration that's provided when we install nginx and we add a symbolic link from our sites available to our sites enabled to enable our site. Finally we restart the nginx service and then the script exits with this message here saying done so that's a setup script.
		
		![[Screenshot 2024-01-30 at 4.17.49 PM.png]]
		Here we also have an update script which is going to be used to update the code on the server whenever we make a change so the setup script will be used the first time we set up the server but it will only work once, once the server setup we need to use the update script to pull updates or changes from git on to the server.
		So again we have the project based path which is the location on the server where the source code is going to be kept then we run git pull and then we run migrate in our virtual environment and then we run the collect static in case we've added any new dependencies that add anymore static files and finally we restart our supervisor process to make the changes come into effect.
		
		![[Screenshot 2024-01-30 at 4.42.49 PM.png]]
		Ok so that's all we need to do for the deploy configuration, next we're going to make some changes to our settings file for it to run better on the server.So open up settings.py within the profiles_project and the first change we're going to make is we're going to disable this debug mode, it's best practice never to run the server in debug mode when it's publicly accessible it's fine when we're running it on our local machine because it's unlikely that anyone else is going to be able to connect to the server but we should never run it when it's on a publicly accessible server because it opens us up to vulnerabilities when we run the server in debug mode that means that if there's any errors or exceptions in the API it will return a full stack trace on the screen this can reveal secret information like the Django secret file or other things that may make our server vulnerable so it's best practice to always disable this in production.
		Because we want to run debug mode when we run the server on our vagrant server but we want to disable it when we run it on the live server we're going to add some logic here to pull in the configuration from an environment variable so type: bool(int(os.environ.get('DEBUG',  1))). What this does is it pulls in the value of the environment variable called debug we set this environment variable here in the supervisor file so we can see in the supervisor at the top of the configuration we set environment equals debug equals zero.
		
		![[Screenshot 2024-01-30 at 4.48.28 PM.png]]
		This sets the debug environment variable to zero when we run our application, so when we pull in this debug variable we'll get a zero and then by default all environment variables are strings so there's no way to specify an integer as an environment variable so we need to use this int function to convert our string of a 1 value or a 0 value to an integer of a 0 and then we use the bool function to convert this to a boolean, the way Python booleans work is a 0 will convert into a false and a 1 will convert into a true. That's why we have this one here because this is the default value if the debug setting doesn't exist, so when we run our application on our vagrant server we're not going to specify debug equals zero so it's going to default to 1 which is going to be converted to true that means when we run our server on our local machine it's going to be in debug mode but then when it's running on our server debug mode is going to be disabled.
		The next change we need to do is add a STATIC_ROOT to the bottom of our configuration so type STATIC_ROOT= 'static/'. The static root is the location where Django will store all of the static files when we run our collect static command.
		Then let's just open up the setup again and we can see we run this collect static command, now we need to tell Django where to store the static files when we run this command we do this by setting the static root.
		
		![[Screenshot 2024-01-30 at 5.00.45 PM.png]]
		
		![[Screenshot 2024-01-30 at 5.04.52 PM.png]]
		We need to run one more command to make sure that these setup scripts are executable so when we send a file to a server the file needs to have the permissions to be executable if we want to run it as an executable script we can do that by opening up the terminal or the git bash window making sure we're on our project and then running: chmod +x deploy/*(Note: star the file hides it shows everything italic).sh.
		What this does is it runs the chmod command to set executable to any file that ends in .sh in our deployed directory. So that is our setup and our update commands.*
	Deploy to server:
		Next we're going to SSH to our server and run our deploy script, open up the Google Chrome and load up the Amazon console page then head over to services and EC2 under the compute option we're going to choose running instances where our instance should be up and running from the previous steps, what we need to do is we're going to SSH to our server in order to do that we need this Public DNS ipv4.
		
		![[Screenshot 2024-01-30 at 5.21.34 PM.png]]
		So hover over this entry here and click on this copy to keyboard button then open up the terminal and we're going to use SSH to connect to our server. The way we do that is we type: ssh ubuntu@ and then paste the URL for the server.
		
		![[Screenshot 2024-01-30 at 5.23.38 PM.png]]
		
		![[Screenshot 2024-01-30 at 5.24.37 PM.png]]
		Ubuntu is the user that we're going to connect to and the authentication should automatically happen via our public key so hit enter and we may be prompted with this authenticity of hosts and just type on or hit yes and hit enter and then we should be connected to the server.
		
		![[Screenshot 2024-01-30 at 5.26.13 PM.png]]
		Once we're connected to the server we need to download and run the script that we created to setup our server so if we head over to the github project and refresh the page we should see that since we've last pushed our changes, we have the deployed directory.
		And then click on deploy and we need to get the URL for the raw data file for our setup script what we're going to do is we're going to pull the script from the internet on to our server and we're going to run the script and that script should set up our server for the deployment, the way we get the raw file in github is we select the file and then we click on this raw button here and this will take us to the raw text page for the setup script. 
		
		![[Screenshot 2024-01-30 at 5.34.36 PM.png]]
		So copy the URL that's in the browser and then head back into the terminal that's connected to our server and we're going to run the following command: curl -sL and then paste the URL and then add the pipe(|) which is the line sudo bash -.
		
		![[Screenshot 2024-01-30 at 5.37.08 PM.png]]
		What this does is it runs the curl command to download the file and then it passes it into sudo bash, so this curl command is used to retrieve contents from a URL, so it's basically an HTTP client in Linux, the -s is for running in silent mode which means it won't update us with all of the steps when it's downloading the file the L is for following redirects so if there's any redirects of this URL then it will automatically follow them to the final destination and download the contents. The pipe is used to pipe the output of one command into another command so we're going to take the output of this curl command and we're going to pass it into sudo bash, sudo is used to run commands as administrator on Linux and bash is what we're going to use to run our script, the hyphen is used to signal the end of the options provided for bash so that it knows anything we pass in is to be ran on bash and not an option to configure bash. Okay so enter that into the console and hit enter and this should go ahead and run our script so we're going to wait for the script to finish it should take a few minutes to install all the dependencies and set up our project.
		
		![[Screenshot 2024-01-30 at 5.52.52 PM.png]]
		
		![[Screenshot 2024-01-30 at 5.53.51 PM.png]]
		Once the script is finished running head over to the Amazon Web Services console and copy the hostname again and then enter it into the browser, we should see this bad request 400 and that's because we haven't added the host name to the allowed hosts on our settings.py file.
	Update allowed hosts and deploy changes:
		
		![[Screenshot 2024-01-30 at 5.58.14 PM.png]]
		Next we're going to update the allowed host setting in our Django configuration to fix this bad request error that we see, so load up the settings.py file in our project then scroll up to the top of the file and find the allowed host setting, here allowed hosts is a setting that allows us to enable access via specific domain names it's a security feature to make sure that if somebody just finds a random IP address for our server they can't access the application unless they use a valid host name so we need to specify the host names that we want to allow to connect to our server in the allowed host option, the host name that we need to add is the host name for our server which is in the EC2 configuration here and is the public dns option.
		
		![[Screenshot 2024-01-30 at 6.00.57 PM.png]]
		So copy the contents of that and then we're going to paste it as a string into this list here, we also need to add the local host so that it still works on our vagrant server, so in a second item in this list type 127.0.0.1. We're going to break this out into separate lines to keep it within the character limit and then make sure we save the file.
		Now that we've made a change to the project we can demonstrate how to update changes on our server after we push them to github let's start by committing and pushing this change to github.
		
		![[Screenshot 2024-01-30 at 6.08.08 PM.png]]
		So open up the terminal and make sure we have a window open that is on a local machine and not connected to our server, select our project directory then type: git add ., to add any additional files and then type git commit - am, and we'll add the docstring, "Added allowed hosts."
		Then type git push origin to push the changes up to github.
		
		![[Screenshot 2024-01-30 at 6.18.08 PM.png]]
		Now that the changes are on github we can run our update script on the server to pull the latest changes so go back to the server that is connected via SSH, if it's disconnected then just run the SSH command again to connect back to the server and we're going to navigate to the location on the server where our project files are stored so type cd /usr/local/apps/profiles-rest-api and hit enter if we type ls, we should see all of the project files here and what we're going to do is we're going to run sudo sh ./deploy/update.sh, this is the command that will run the update script that will update the application based on the latest github changes, hit enter on that and it should pull the latest changes down and then run all of the commands necessary to restart the server.
		
		![[Screenshot 2024-01-30 at 6.22.17 PM.png]]
		Okay we can see that the script has finished running so let's go to our browser and let's open up the tab that we got the bad requests on and hit refresh. Now we can see it says not found because there's no root mapped to the base of the URL so we're going to just add: /API/, and we should see the root of our API, we should also see if we put /admin, the admin page.
		
		![[Screenshot 2024-01-30 at 6.28.32 PM.png]]
		
		![[Screenshot 2024-01-30 at 6.28.57 PM.png]]
		
		![[Screenshot 2024-01-30 at 6.33.47 PM.png]]
		The only thing left to do now is to create a super user on our server so that we can log into it using our user account so open up the terminal and make sure that we are in the /usr/local/apps/profiles-rest-api and then we're going to run the following command to add a super user, we're going to run sudo env/bin/python, and then we're going to run manage.py create super user and hit enter then enter an email address, then a name, and then the password. Make sure to put a secure password when creating this because our site will be publicly accessible which will open it up to be attacked, so once we've entered the password hit enter we're going to re enter the password hit enter. Now we can see the super user has been created so let's test this.
		
		![[Screenshot 2024-01-30 at 6.37.58 PM.png]]
		We can see that we've logged into the Django admin and now our app is working as expected so that's how we deploy the app to AWS on an EC2 instance.
		
		![[Screenshot 2024-01-30 at 6.39.45 PM.png]]
	