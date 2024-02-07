Introduction:
	Course Structure:
	
		![[Screenshot 2024-01-31 at 6.19.09 AM.png]]

Test Driven Development:
	What is Test Driven Developmaent?:
		Unit Tests:
		- Sets up conditions/inputs
		- Runs a piece of code
		- Checks outputs with "assertions"
		Many Benefits:
		- Ensures code runs as expected
		- Catches bugs
		- Improves Reliability
		- Provides confidence
		Since we're notified of any errors/bugs whenever we run the code it means that we have good test coverage, this is another benefit of Unit Tests.
		What is TDD?:
		Test driven development is a development practice.
		Often when people write unit tests, they start by writing the code that performs a certain piece of functionality. And then after they've written the code, they write the unit test to test that code. This is a perfectly fine way to do it as long as we're adding unit tests. But it's not the recommended approach.
		The way that we're going to do it is we're going to start by writing a test, that test the functionality that we want to add to the project, and then we're going to write the code that makes that test pass.
		So the TDD process works like this:
		- We start by writing a test to test a certain piece of functionality.
		- Then we run the test.
		- And because we haven't implemented the feature yet, the test should fail.
		- And then we add the feature which makes the test pass.
		- After we've done that, we run the test again and it should pass, and then we can go ahead and refactor the code that we wrote to make the test pass.
		- And after we refactor it, we go ahead and run the test again to make sure it's still passing as expected.
		Why use TDD?:
		- Better understanding of code.
		- Make changes with confidence.
		- Reduces bugs.
		So why should we use this process instead of just writing unit tests after we create the code?
		Well, there are many benefits to this:
		- It gives a much better understanding of the code that we're creating because we're not just thinking about how to add the feature in code.
		- We're actually thinking about how we would test that feature using code. So we have to put a lot of thought into the output of the APIs that we create.
		- This helps us make changes with confidence in our code.
		- Because we're using TDD, we should have a good test coverage in our project, which means that all of our code is covered by unit tests. This in turn helps us to reduce bugs in our project, and everybody likes to reduce bugs when they're working with software.

Project Setup:
	New project overview:
		Why use Docker?:
		There are many benefits to using Docker for development:
		- One of them is that we have a consistent development and production environment. So with Docker we can use the same image for our development as we use for production. This means that we're using exactly the same code on production and it eliminates all of those issues where we might have a problem that occurs on the production server, but we can't reproduce it locally because we're using the same image and the same set of based dependencies. We should have a consistent environment on our local development machine and on the server we deploy the application to.
		- Another benefit is easier collaboration. Often we'll be working on projects with other developers and there are so many times that we can think of where we've been sharing our project with a developer. And what happens is it works perfectly fine on our machine and everything works normally. However, when we go to run the project on the other developers machine, they run into a whole world of issues. And this often happens because the dependencies that we run our machine. So dependencies are any software that our project depends on are different from the dependencies on the other developers machine, for example, they might have a different version of Python or they might have a different version of the database we're using, or a different version of some SDK tool that we're using on the software. And this means that we have a whole load of issues to sort out because we basically need to make sure all the dependencies are exactly the same on both machines. However, when we use Docker, this eliminates all of those problems because all our dependencies are inside the Docker image, which is defined in our project. So when the other developer runs our project that is set up to use Docker in almost all cases, it just works. They just run the Docker images and it just works fine.
		- Another benefit is that using Docker allows us to capture all of the dependencies in the source code of our project. We don't need to install things manually on our machine and configure them to work with our project. It can all be done in the code. We can define every single dependency that our project needs inside the source code. This again helps with easier collaboration. For example, we can have all of the requirements, our python requirements defined in our project, and we can also add all of the operating system level dependencies in our Docker file.
		- Another benefit is easier cleanup. So if we're working as a professional developer, we'll often be working on various different projects and we might be just working on a project for a set period of time. So let's say we need to spend a couple of weeks working on a particular project. When we use Docker, when we're finished using that project, we can simply just delete the project files and delete all of the Docker images, and then our system is completely cleared of the dependencies that were needed for that project. We don't need to go through and manually remove any SDK or any databases that might be new in our system. It was all contained inside the Docker configuration for that project.
		How we'll use Docker?:
		- We'll define a doc of all the Docker files, its going to contain all of the operating system level dependencies that our project needs.
		- Then we'll create a Docker compose configuration. This will tell Docker how to run the images that are created from our Docker file configuration.
		- We're going to run all the commands that we need for this project through Docker Compose.
		Docker on GitHub actions:
		There's one thing to keep in mind when we using Docker with GitHub actions. Docker has something called Docker Hub. Docker Hub is where we can pull shared public images down to reuse them for our project. For example, there's an image for Python, like a Python base image for Docker, and that would come from Docker Hub. However, Docker Hub has introduced some rate limits, and a rate limit is basically limiting the amount of access that we have so that we need to upgrade to pay for that paid plan if we want to use more. So it's a way for them to monetize and also to prevent abuse of their platform. So the rate limit that they've introduced is 100 pulls for every 6 hours for unauthenticated users. So an unauthenticated user is just a user that is pulling a Docker image from Docker Hub that hasn't logged in with that Docker hub credentials. If we do log in, then we get 200 pulls for every 6 hours. So it doubles the limit. And this should be more than enough for now. So we shouldn't need to upgrade to a different plan. We should be able to manage, with just 200 pulls for every 6 hours. In fact, both of these rate limits would normally be fine for a project like this. However, the problem is that we're going to be running Docker on GitHub actions, which is a shared service, so we're not going to be the only developers in the world using GitHub actions. GitHub actions works by running our code on shared servers, which are used by many other projects and many other developers. So this means that this hundred pulls for every 6 hours is applied for every single person using the servers that are shared between all of the different developers on GitHub actions. This is a problem because this means that there's 100 pools every 6 hours gets quickly used up. So the way that we're going to get around this problem is we're going to authenticate with Docker Hub. So to authenticate with Docker Hub we'll start by creating a Docker Hub account. Then we're going to set up credentials that are used by our project in order to login before we run a job that pulls docker images. This means we can take advantage of the 200 pools for every 6 hours, which should be more than enough for now.
	Create GitHub project:
		
		![[Screenshot 2024-01-31 at 7.27.28 PM.png]]
		These secrets are things that can be used during our GitHub action jobs that we're going to add later to the project. So when we need to retrieve the username, we can retrieve it using the secret that we just added.
		Next, we're going to add our token. So click on New Repository Secret. We're going to add a second secret here. We're going to call this DOCKERHUB_TOKEN. It's very important that we call the names exactly as we're defining here, because we're going to be using them in our code a bit later on. So Docker Hub Token, what we're going to do for the value that is, we're going to head back to the page that we created the token with. Click on the copy icon to copy it to the clipboard, and we're going to paste that into the value here so that we'll paste this token into the secret, then click Add Secret, and this should add the second secret to the repository. So now we have two secrets here we have the Docker Hub Token and the dock hub user, and we can use both of these secret values in order to authenticate with Docker Hub.
	Docker and Django:
		Using Docker and Django has many benefits:
		- Consistent development and production environment.
		- Easier collaboration.
		- Capture all dependencies as code.
		- Easier cleanup.
		- Save a lot of time.
		However, all of these benefits don't come without their drawbacks:
		- VScode unable to interpreter.
		And that means it's difficult to configure our editor to use the integrated features that work with Python and other things such as the interactive debugger and also the learning tools that come with Visual Studio code
		- More difficult to use integrated features.
		- Suggest using Terminal.
		Using the terminal to run all of the linting and any debugging now we want to do to our project.
		How to configure Docker to work with Django?:
		So we start by defining a Docker file that has all of the operating system level dependencies needed for our project.
		Docker file is simply just a list of steps that Docker uses to create an image for our project.
		We start by choosing the base image because we were going to be building a Python project.
		We're going to use the Python base image that is provided for free on Docker hub.
		Then we install dependencies in our image.
		So these are operating system level dependencies, we then set up users.
		So these are the Linux users that are needed to run our application and these users are created inside our Docker container.
		Docker Compose:
		Docker compose defines how Docker images should be used to run our development server.
		We basically define the images as different services and every service has a name.
		For example, we're going to be using the name app.
		We can define various port mappings which make ports accessible on our local machine, and this is how we're going to actually connect to the containers that are running our application.
		And we can set up volume mappings. Volume mappings is important because it's how the code in our project gets into the Docker container.
		Using Docker Compose:
		So we're going to run all of the commands through Docker Compose, and the commands are going to look like this:
		docker-compose run --rm app sh -c "python manage.py collectstatic", Here's an example of running the collect static Django command through Docker Compose.
		We start by typing docker hyphen compose which will run the Docker Compose application.
		Then we pass in the run command which says that we wish to run a container and a single command on that container.
		Then we specify this hyphen hyphen rm. This is optional. However, it tells Docker Compose to remove the container once it's finished running, it's recommended that we add this any time we're running a single command because that means we don't have a build up of lingering containers on our system.
		Then we specify the name of the app that we defined inside our Docker compose configuration.
		The app that we're going to be using is going to be called app. Then we pass in sh hyphen c.
		So this is the command that is going to be passed into the container when it runs.
		This command basically says we want to run a single command on our container.
		Finally we pass in the Django command that we want to run inside quotations.
		So in this particular example we're running python manage.py collectstatic, which is the Django command for collecting static files.
		So the first part of this is the Docker compose syntax. That's everything up until the app. And this is basically the part that we need to add before every command that we run.
		Then the second part of this is the command that is actually going to be run on the container. We always start with sh hyphen c if we're going to be running a single command in the container just so we can wrap our command in quotes and easily understand which part of the command is going to be running in the container.
	Create project Dockerfile:
		So in the project file navigation here, we're going to create a new file in the route of the project.
		We're going to call it Docker file. Then we're going to define the steps that Docker needs in order to build our image. So the first step is to define the name of the image that we're going to be using. So that's the base image that we're going to pull from Docker Hub that we're going to build on top of to add the dependencies that we need for our project. 
		So we do that by typing from and then the name of the image. So we'll be using Python code on 3.9, hyphen Alpine 3.13. We can find the different versions if we head over to the browser and we go to hub.docker.com. Once we're on that page, there's a search functionality where we can search through all of the base images. So if we search for Python. We should see the official Python image here, and it will have a list of all the different image tags that are available. The one that we're using is the Alpine image tag for version 3.9. So Python is the name of the Docker image that is on Docker Hub 3.9 Hyphen Alpine 3.13 is the name of the tag that we're going to be using. And what this does is it ensures that we are using Python 3.9 and we're using the Alpine version. So Alpine is a lightweight version of Linux, and it's ideal for running Docker containers because it is very stripped. It doesn't have any unnecessary dependencies that we would need. Everything that it comes with is just the bare minimum and it's an extremely lightweight and efficient image to use for Docker. 
		Next we define the maintainer, so we label maintainer equals. And then we can specify our name or the name of the website, just basically whoever is going to be maintaining this Docker image and it's best practice to define this. So if other people work on the project, they know who the maintainer is.
		Then we're going to specify ENV PYTHONUNBUFFERED 1. And this is recommended when we are running Python in a Docker container. What it does, it tells Python that we don't want to buffer the output. The output from Python will be printed directly to the console, which prevents any delays of messages getting from our Python running application to the screen so we can see the logs immediately in the screen as they're running.
		Next, we'll type COPY ./requirements.txt /tmp/requirements.txt. And then below that we're going to type COPY ./app /app, and then work the WORKDIR /app and then expose 8000. So what this block does is it says copy our requirements.txt file from our local machine to /tmp/requirements.txt. And this copies the requirements file that we added earlier into the Docker image. We can then use that to install the Python requirements in a moment. Then what we do is we copy the app directory, which we're going to create in a moment, and that's the directory that's going to contain our Django app and we copy it to /app inside the container. Next we set the workdir. So to workdir is the working directory and it's the default directory that where commands are going to be run from when we run commands on our Docker image. And basically we're setting it to the location where our Django project is going to be sent to so that when we run the commands, we don't need to specify the full path of the Django Management Command. It will automatically be running from the /app directory. Next we set expose 8000, which says we want to expose Port 8000 from our container to our machine when we run the container. And what this does is it allows us to access that port on the container that's running from our image. And this way we can connect to the Django Development Server.
		Next, we're going to add a run command that is going to install some dependencies on our machine.  So type RUN python -m venv /py && backslash(\) and then an indentation under that will do /py/bin/pip install python --upgrade pip && backslash(\), in the next line, /py/bin/pip install -r /tmp/requirements.txt  && backslash(\), in the next line, rm -rf /tmp && backslash(\), in the next line, adduser backslash(\) and then another indentation --disabled-password backslash(\) --no-create-home backslash(\) and then django-user.
		Then under that we're going to type ENV PATH= and then in quotes  "/pi/bin:$PATH". And then finally, the last line we're going to add is, USER django-user.
		So what this does is we run the run command. So this runs a command on the alpine image that we are using when we're building our image. So we've broken the commands down onto one run block, so we could technically specify run, and then each one of these lines individually, however what happens in that case is it creates a new image layer for every single command that we run, and we want to avoid doing that to keep our images as lightweight as possible. So what we do is we specify a single run command and we break it down onto multiple lines using this double ampersand(&&) backslash(\) syntax.
		So it looks a little bit confusing, but it does make the building of our images a bit more efficient because it doesn't create so many layers on our system.
		The first command we run is python - m venv  /py. This creates a new virtual environment that we're going to use to store our dependencies.
		Now, lots of people have conflicting opinions on this. Some people think that we don't need to use a virtual environment when we're working with Docker, and this is probably the case in most cases. However, there may be some edge cases where there are some python dependencies on the actual base image that might conflict with our python dependencies for our project. So the way to avoid this happening and to reduce any risk, we can create a virtual environment in the Docker image and it doesn't really add that much overhead. So there's not really that much downside to it, but it just safeguards against any conflicting dependencies that may come in the base image that we're using.
		The next command we run is we're specifying the full path of our virtual environment. So we want to upgrade PIP for the virtual environment that we just created. So we specify the full path by doing /py/bin/pip install --upgrade pip. So this upgrades the python package manager inside our virtual environment.
		Next, we install our requirements files. So this /tmp/requirements is what we copied here in line 6. And basically we install that list of requirements inside the Docker image. So this will install it inside our virtual environment because we're specifying the full path to PIP inside our virtual environment /py/bin/pip.
		Then we remove the tmp directory. The reason we do this is because we don't want any extra dependencies on our image. Once it's being created, it's best practice to keep Docker images as lightweight as possible. So if there are any files that we don't need on the actual image, we want to make sure they're removed as part of our build process. So any file we just need temporarily, we add it, use it inside the Docker file and then remove it before the end of the Docker file. And this just helps make sure that the Docker image is as lightweight as possible so it saves a lot of space and speed when we're deploying our application.
		Then we have this adduser block here. So what this does is it calls the adduser Command, which adds a new user inside our image. So the reason we do this is because it's best practice not to use the root user. If we didn't specify this bit, then the only user available inside the alpine image that we're using would be the root user. The root user is the user that has the full access and permissions to do everything on the on the server. So any thing that we can do can be done by the root user. It has no restrictions or limitations. It's not recommended that we run our application using the root user, because this means that if our application gets compromised, then the attacker may have full access to everything on that Docker container. However, if we run our application using a user that doesn't have full privileges, then that means if our application does get compromised, the attacker will only be able to do what that limited user can do. So that might just be accessing the code, and it's still not good that it's being compromised but at least they don't have full access to everything in that container. So that's why we do add user, we specify and disable password because we're not going to be using a password to log on to this. We don't want people to be able to log on to our container using a password. We just want to do it by default. When we run the application, use that user. 
		We do no-create-home, so it doesn't create a home directory for that user because again, it's not necessary and we want to keep the Docker images light where it's possible.
		Finally we specify the name of the user, so we're just going to call it django-user.
		We could call it app. We can basically call it whatever we want. We're using django-user just so we explicitly know what that user's for in the container.
		Now we have the ENV line. So this updates the environment variable inside the image and we're updating the path environment variable. So the path is the environment variable that's automatically created on Linux operating systems. And what it does is it defines all of the directories where executables can be run. So when we run any command in our project, we don't want to have to specify the full path of our virtual environment. So we don't want to specify /py/bin every time. So the way we can avoid that is we can add this line here which will add a /py/bin to the system path. So whenever we run any Python commands, it will run automatically from our virtual environment.
		Finally, we have the user line, which should be the last line of our Docker file, and this specifies the user that we're switching to. So until we run this line here, everything else is being done as the root user and the containers are made out of this image. We'll run using the last user that the image switched to. So because we are switching to USER django-user, any time that we run something from this image, it's going to run as the django-user. So it's not going to have that full root privileges that we need for setting up the Docker image. So that's everything we need to do to create a Docker file. Now we save the file and next we're going to add a Docker ignore file.
		
		![[Screenshot 2024-02-01 at 6.36.16 PM.png]]
		DockerIgnore:
		So in the root of the project, create a new file and call it .dockerignore. And what this is, is it allows us to specify a list of files that are going to be excluded from the Docker context. So when we run the doc image, it uses something called the Docker context, which is the directory that we're running from. And all of the files are passed into the context except for the files that we list in Docker ignore. So basically in this file we want to exclude any files that Docker doesn't need to be concerned with. So that's files we want to exclude from our Docker file and from whenever we run our commands.
		
		![[Screenshot 2024-02-01 at 6.42.44 PM.png]]
		So the top 2 are git files and directories. So .git is a hidden directory for git, we don't need that copied into our doc file and that can actually be quite huge because it contains all the git history. So we exclude that in the doc file. We also exclude the .gitignore because we don't need that inside our docker file.
		And then we exclude .docker which is a Docker hidden file that might be created in our project that doesn't need to be used by our actual Docker file. So it just contains some Docker working files that we use specifically on our local machine. They don't need to be copied into our Docker image when we build it.
		Then we have Python. So these are the python exclusions here. When we run python code, it creates a cache and it puts that inside pycache. This isn't needed on our Docker container and in fact it can actually create problems if it does because the pycache that would be created on our local machine would maybe be specifically for our operating system and not for the Alpine operating system. So we just exclude them from the context just to make building our container a bit faster. The reason why we do this Asterix(*)* here is just to make sure that all of the different pycache files may be removed. Unfortunately, the Docker ignore file doesn't support things like doing a double asterix to do all subdirectories. So we need to specify each subdirectory individually.
		Then we remove .env .venv and just venv and this is the virtual environment. So we want to remove any virtual environments that we may create locally in our projects from the context because they don't need to be copied over. We already have a virtual environment that we add in our Docker file.
		(Note: Make sure to create a folder named app otherwise build of the image may fail, because it couldn't copy the directory, since it at least needs that empty directory, because we have this line here where we copy the app, in which we we're going to be adding our django project eventually)
		Now we go to the terminal and type: docker build ., this runs a command for building our Dockder image.
		What happens is it goes through each of the steps that we define inside our Docker file. And it will run that to create an image. And it uses caching behind the scenes. So the first time we run it, it might take a while, a few minutes for it to download any dependencies and to build our image. However, the second time we run it, it should be a lot faster because it caches each layer that is needed to build our docker image.
	Create docker compose configuration:
		
		![[Screenshot 2024-02-03 at 12.11.09 AM.png]]
		So we have the version at the top. So this is the version of the Docker compose syntax that we're going to be using. And this is just in case Docker compose, release new versions of the syntax. And it's a version mechanism to make sure that the syntax we use here matches the specific version. And if they were to release new versions, it wouldn't break out configuration.
		Then we specify services. So this is the main block inside the Docker compose file. Docker Compose files typically consist of one or more service that's needed for our application. So on the services, we have app as the name of our service and this is just the service that is going to run our Docker file. 
		We have build context and the current directory(.). And what this does is it says we want to build the Docker file inside our current directory. So the context that we're going to use for app service is the root directory that we're running the command from. That's what the dot here means. It means just use the current directory that we're currently running Docker compose from.
		Then we have the port mappings. So this maps port 8000 on our local machine to port 8000 inside our Docker container. This is how we can access the network when we want to connect to our server. Next we have volumes, volumes are the way of mapping directories from our system into the Docker container. So we're mapping the app directory that we created in the project to /app inside our container. The reason we add this is because we want the updates that we make to our code in our local project to be reflected in the running container in real time. So we don't want to have to rebuild the container. Every time we change a line of code, we want to automatically sync the code in our project to the cloud running in the container.
		Finally we have the command. So this is going to be the command that's used to run the service. We can override this command when we run Docker compose, run, which we're going to be doing a lot. However, by default, if we don't specify a command, it's going to use the command we define inside our Docker compose file.
		
		![[Screenshot 2024-02-02 at 9.59.32 AM.png]]
		Then inside terminal we can start: docker-compose build, and this will build our Docker image. So it effectively does the same as Docker build. However it does it via the Docker file, so it builds and tags the images appropriately for running our Docker compose configuration.
	Linting and Tests:
		Linting:
		- It is simply running a tool to check code formatting.
		- highlights errors(like syntax errors), typos, formatting issues.
		How we'll handle linting:
		- Install flake8 package. Flake8 is a nice simple to use linting tool.
		- Run it(flake8 tool) through Docker Compose.
		-docker-compose run --rm app sh -c "flake8", We'll do it like this. So first we'll specify the syntax for running our app service with Docker Compose. Then we'll specify sh -c "flake8". This will run the flake8 tool on our code. When we run the flag flaky tool, we're going to see an output like this:
		.recipe/serializers.py:12:1: E302 expected 2 blank lines, found 1
		.recipe/serializers.py:19:1: E302 expected 2 blank lines, found 0
		.recipe/serializers.py:57:40: E231 expected missing whitespace ','.
		ERROR: 1
		So the output like this means that we have some linting issues with our code. If we don't see this output and we don't see any help at all, then that means there's no linting issues and there's nothing to worry about. So here we have three different issues listed.
		If we look at the bottom one, we can see it specifies the path of the file that it found the issue in. So if we look at our recipe/serializer.py, we can see that on line 57. We are missing the whitespace after a comma. So what this says is that we have a comma here and it's expecting to find a white space, so a blank space after the comma. But we missed out, so we got the linting error so we can use this information to go and locate where the error is in our code, fix it and then run the tool again. If we have multiple linting errors like we can see here, we work from the bottom up.
		So we take the bottom arrow and we fix that, and then we go ahead and do the one above it. So the reason we go from the bottom up is because sometimes when we are fixing the linting errors, it involves adding new lines to the code. And if we work from the top down, then it's going to mess up the line numbers so the line number in the linting errors is below the one we're looking at may not be the same as the one output in the console. So if we went from the bottom up, this solves this error because we go from the bottom of the file up and it doesn't affect the line numbers listed in the linting output. So that's just a little tip when we're fixing issues generated by flake8.
		So whenever we see a flake8 output like this, we go through each one and we fix the issues one by one.
		Testing:
		- For the unit testing of our project, we're going to be using the Django test suite. So there's a framework that comes with Django specifically for running tests on the Django project. 
		- We're going to set up the tests for each different Django app that we create.
		- And then we're going to run the tests using Docker, compose using a command like this:
		docker-compose run --rm app sh -c "python manage.py test", So we'll have the same Docker syntax: docker-compose syntax at the beginning and we're going to run python manage.py test. This will run the unit test for our application.
	Configure flake8:
		
		![[Screenshot 2024-02-02 at 5.47.51 PM.png]]
		Like we did with Django and the other dependencies, we're installing the latest patch version to get any security fixes and things like that. But we're going to be pinning it to version 3.9. So if they release a new version of flake8 that has breaking changes, it doesn't break the steps or break the project.
		The reason why we created a new requirements file is because we're going to add a custom step to our build so that we only install these development requirements when we're building an image for our local development server.
		The reason we do this is because we don't need the flake8 package when we're running our deployed application because we don't need to run the linting tool on the application that we deployed to the server. We only need it for development, so it's useful sometimes to be able to separate our development dependencies from our actual project dependencies so we don't introduce unnecessary packages into the image that we're deploying on our actual server.
		
		![[Screenshot 2024-02-03 at 12.10.47 AM.png]]
		So the way we'll handle this is we're going to add a build argument. So what this does is it says we're running using this Docker compose, which we're only going to be using for development, set a build argument called DEV and set the value to true.
		
		![[Screenshot 2024-02-02 at 11.43.57 PM.png]]
		COPY ./requirements.dev.txt /tmp/requirements.dev.txt: So just like we did with our other requirements file, we're copying it to the temp directory so that we have it available during the build phase.
		ARG DEV=false: So this defines a build argument called DEV and sets the default value to false. We're overriding this inside our docker compose file by specifying args DEV=true. So when we use this docker file through this docker compose configuration, it's going to update this dev to true. Whereas when we use it in any other Docker compose configuration, it's going to leave it as false. So by default, we're not running in development mode.
		if [ $DEV = "true" ]; \
		then /py/bin/pip install -r requirements.dev.txt ; \
		fi && \
		: So it's quite confusing, but this is basically a shell script, so a little bit shell code that does an if statement. So if DEV=true, which is if the dev environment variable, which is a build argument here is set to true, then run this bit of code here on line 17 and then it's not actually a typo with the shell script if we're not familiar with it. When we do an if statement, the way we end the statement is we write it backwards by putting fi.
		This is basically how we run a shell command condition. So the condition, is that  if dev equals true, it's going to install the dev dependencies. Otherwise it's not. So otherwise we uninstall these requirements. So when we run our docker file with dev equals true, it's going to install the actual dependencies here with the requirements.txt because that's outside the block that happens regardless, but it will also install the dev dependencies. However, if we build it without dev being true, then these dev dependencies are not installed on our docker image, which saves that little bit of space and also adds a little bit of extra security because we don't need to worry about bugs and things in the development dependencies if we don't install them on our production image.
		
		![[Screenshot 2024-02-02 at 11.46.37 PM.png]]
		So now that we've added that, we can save the Docker file and we can just go ahead and test it. If this builds successfully, then we know that it's correct. If it doesn't, it should tell us if there's any errors in the syntax.
		
		![[Screenshot 2024-02-02 at 11.51.25 PM.png]]
		So once the docket image has been rebuilt, we can go ahead and add the configuration needed for our linting tool. So we need to add a configuration for flake8 to tell it what directories and files to exclude from the linting. And we do this because there are a lot of linting errors in the default Django settings file and things like that. So we just want to exclude them because we didn't create those files, they were created from a template and we only want to add the linting to the code that we create in the project.
		So let's open up the Explorer here and then we're going to add a new file inside the app directory. So it's very important that we place this file inside the app directory here and not inside the root of the project, because otherwise it's not going to be picked up by our linting tool. So inside the app directory, we're going to create a new file, and name it .flake8. .flake8 is the name of the default flake8 configuration file.
		All flake8 files start with: [flake8].
		exclude: So what this does is it tells flake8 to exclude these following directories and files from the linting. And we do migrations because migrations are auto generated by Django. So we don't need to lint those, pycache doesn't need to be linted because it's just the cache files that are automatically generated by Python when we run code manage.py is a script file that. Django includes that again, we don't need to change the code in there, so we just don't want to apply the linting to it, and settings.py has lots of long lines and things like that that we want to exclude from the linting because we don't necessarily want to update all of the settings.py lines because most of them are also generated by Django.
	Create Django project:
		
		![[Screenshot 2024-02-03 at 9.11.43 AM.png]]
		So what this does is we run Docker, compose, run --rm app to run our app service and the command we're passing in is the Django cli command for creating a new project. Now, because Django is installed inside our Docker image, we can run the cli commands just as if they were on our local machine. What's going to happen here is it's going to create a new project called App and we specify the dot(.) here to say create it in the current directory. This little dot(.) is very important because if we miss it, then what it's going to do is create a new subdirectory inside our app directory, which is then going to have our projects and it's going to mess up all of the commands and everything that we run.
		Once we type the command, we can hit enter and this will go ahead and spin up a container from an image and run the django-admin startproject app ., Command. We can see when it's finished running it automatically adds the Django project files to the root of the project.
		So if we didn't specify the little dot at the end of the command, what it would do is it would put all of these files inside another app directory, which is just going to add too many app directories to our project and make it confusing. So here we have the new Django project added to our code. The way that it was able to sync was through the volume that we defined in Docker Compose. So because we have the app directory mapped, then what it does is anything we create inside the container gets mapped to our project and anything we create inside the project, our directory gets mapped to the container. So it's like a two way relationship thing where we can create files in the container and access them in the project and we can create files in the project and access them in the container.
	Run the project with Docker Compose:
		
		![[Screenshot 2024-02-03 at 9.27.12 AM.png]]
		So this is the Docker compose command for starting out services.
		So what we have here is the Docker Compose App Command and it's going to run our services. So we can see that it started by running the app and we only have one service, which is why we just running the app service and it says that it started the development server.
		If we go over to our browser and we head over to 127. 0.1:8000 hit enter. We should see the Django launch page.
		
		![[Screenshot 2024-02-03 at 9.29.47 AM.png]]
		This is the template that is added for all default Django projects. This basically means that our project is working correctly and that we've configured everything with Docker. We are running the services inside Docker.

Configure GitHub Actions:
	What is Github Actions?:
		Now, we're going to be configuring GitHub actions to run some automated tasks whenever we push changes to our project.
		So what is GitHub actions?
		- Well, GitHub Actions is an automation tool.
		- It's a similar tool to things such as Travis-CI, GitLab, CI/CD and Jenkins.
		- Automate Tasks
		Simply put, it allows us to run jobs any time our code changes. These jobs allow us to automate certain tasks.
		The common uses for GitHub actions are to:
		- Handle deployment.
		- Handle code linting.
		- Run unit tests.
		So we would automate these tasks whenever we make changes to our code.
		For now, we're only going to be using it for running our code linting and also running our unit tests.
		We're not going to be covering the deployment part because that's quite a complex process.
		So how does GitHub actions work?
		Well, we start by setting up triggers. So triggers can be anything that happens to our project on GitHub. There are various different trigger options. They're all documented on the GitHub actions website. The trigger that we're going to be using is whenever code is pushed to GitHub. So that is the push trigger.
		When this trigger occurs, for example, when the code is pushed to GitHub, we then set up jobs that run when that trigger is hit. So for example, the job that we're going to be setting up is going to be to run unit tests. Then when the job runs, there will be an output of that job and the output is either going to be successful or fail. If it's successful, then we get a green tick and everything is fine. If it fails, then we can get notified via email or we can just see it in the GitHub actions console that something has failed and there are some changes that we need to make to our code.
		Pricing:
		- Charged per minutes.
		- 2000 free minutes for all free GitHub accounts.
		- Various plans available(If more than 2000 minutes are needed).
		But we shouldn't need to do this unless we're running a big team or we have a project that is very development intensive that's running a lot of CI minutes on GitHub actions.
	Configuring GitHub Actions:
		How we'll configure GitHub Actions?:
		- Create a config file at github/workflows/checks.yml, the last part checks.yml can be named anything as long as it ends with: .yml, so that we know its a YAML file. Once we've created that file, we're then going to:
			- Set some triggers in that config.
			- Add some tests for running and linting on the project.
		- We're also going to setup/configure Docker Hub auth(authentication)
		Docker Hub:
		- Needed to pull base images: Docker Hub is a platform that allows us to pull base images from Docker. It's basically a hosted service that allows us to pull Docker images down to our local machine. Any time we run a Docker container on our local machine, unless we specify otherwise, it's going to automatically pull that image from Docker Hub.
		- Rate limits:
			-Anonymous: 100/6h
			-Authenticated: 200/6h
			The thing about Docker Hub is it has some rate limits. Rate limits basically mean we're limited to the number of images that we're allowed to pull in a certain time frame. So for anonymous users of Docker Hub, we would get 100 pulls for every 6 hours. That means we can pull 100 different images within any 6 hour time frame. It identifies anonymous users by their IP address. So basically it's limited to 100 pulls per 6 hours for the specific IP address that we're using. Authenticated users, that is, users are logged into Docker Hub. They get 200 pools for every 6 hours, so the limit doubles.
		- GitHub Actions uses shared IP addresses: However, the key thing to remember is that it doesn't use our IP address, its using our authenticated credentials. So because GitHub actions that we're going to be running our code on, which is going to be pulling Docker images to build our base image that uses a shared IP address, which means that the anonymous limit is applied for all GitHub actions users that are using that specific IP address and that could be hundreds or thousands of different users. This means that this rate limit of anonymous users getting 100 pulls for every 6 hours gets used up very quickly when we're using shared IP addresses.
		- Authenticate with Docker Hub: So to get around this, we need to authenticate with Docker Hub so that we know that we can use the 200 pools for every 6 hours which should be more than enough for most projects. Once we authenticate with Docker Hub, we get the 200 pulls for every 6 hours all to ourselves. So it doesn't matter how many other users are using the same IP address because we authenticated, we always will get the 200 pause for every 6 hours. This is more than enough for most projects.
		However, if we do need to upgrade because we have a project that uses lots and lots of different Docker pulls, then there are different plans available on the Docker Hub website that allow us to upgrade and get more pulls for some money.
		How to authenticate with Docker Hub?:
		- Register account on https://hub.docker.com/
		- Use docker login during our job.
		- Add secrets GitHub project.
		- Secrets are encrypted.
		- Decrypted when needed in actions.
		Once we've signed up, we're going to be using Docker log in during our job and this is going to authenticate us with our docker hub account.
		We're going to need to add something called Secrets to our GitHub project, which contains the credentials for authenticating with Docker Hub. So secrets basically allow us to add encrypted variables to the project so that we can store variables that can be used in our jobs. Basically, we set them up in the GitHub interface and then they're encrypted when we save them. So nobody can actually access them except for us. And then they're decrypted automatically when they're needed for the jobs that we run in GitHub actions.
	Create GitHub config:
		
		![[Screenshot 2024-02-04 at 4.56.06 PM.png]]
		Now we've called it checks because it's going to be the action that performs various different checks on our code. If we were to add deployment to the project, then we might add a separate file called Deployment. And we might have both checks and deployment inside workflows.
		And there's various different ways that we can organize our different GitHub actions project.
		We're going to start by adding three dashes at the top, because this signifies that it is a YAML file.
		Then we're going to type name: Checks. So this is the name as it's going to appear in GitHub actions. Now we'll type on: and then [push]. This is the trigger. So we're saying we want this particular GitHub actions to run on push, which means any push of changes to our project. So any time we do git commit and then push it up to GitHub, it's going to run the jobs that we specify inside this text of YAML file.
		jobs:
		  test-lint:
		    name: Test and Lint
		    runs-on: ubuntu-20.04
		So what this does is it defines a new job called test lent. And this(test-lint) is actually the id of the job. And we want to use an id like this because it might need to be referenced somewhere else inside of actions. We're not going to need to use it here. But there are certain things like we might want to ensure the order of the jobs runs in a certain way. We might want to wait on certain jobs to complete before other jobs continue. And this would be the we that we would use for that.
		Then we have the name. So this is the kind of human friendly name that we're going to see within the GitHub actions interface. Underneath this, we have runs on. Runs on is the runner that we're going to be running our job on. So there are various different runners available on the GitHub actions website. We're going to be using the Ubuntu 20.04 runner. The runner is basically the operating system that we're going to be running the job on. So they have different operating systems available for our different needs in most cases, especially for Python projects. We're going to want something like Ubuntu that that's just a basic Linux operating system because that's going to be all we need to run our jobs. And other runners have different costs, like if we use a Windows Runner, that might cost more. But this would all be documented on the GitHub actions website. 
		Next, what we're going to do is we're going to add the steps. So the steps are the different things that run for the job.
		steps:
	      - name: Login to Docker Hub
	        uses: docker/login-action@v1
		    with:
		      username: ${{secrets.DOCKERHUB_USER}}
		      password: ${{secrets.DOCKERHUB_TOKEN}}
		So this name is going to be log into Docker Hub.
		So what this does is it defines our first step of our job. The name is the name that we want to give to this particular step. And again, this is the human readable name that we're going to see in the GitHub actions interface. Then we have uses. Uses allows us to use another pre-made action that's provided in the GitHub actions repository. So GitHub Actions, the way it works, is we can actually create our own actions. we can reuse existing actions that are used for particular jobs. And action is basically just a Docker container and a Docker configuration that's set up to perform a certain task. So this particular action is the docker/login-action. This action is used to log in to Docker. So it's officially provided in the Docker repository. And the '@' symbol is basically just to specify the version of this action that we want to use. We're going to be using the version one. Then we pass in the parameters. So we do with and we're passing in the username and password which is going to be passed in to the Docker log in action that's going to log into Docker with these credentials. Once that's done, we can define the next step and the next step is going to be Checkout.
		- name: Checkout
		   uses: actions/checout@v2
		So this step is the next step that's going to be performed if this Docker log in step is completed successfully. The steps are all executed in order. So first it's going to do log in, then it's going to do this checkout. Well, the checkout one does is its an action that's provided by GitHub automatically or provided by GitHub premade for free. And basically it checks our code out inside our GitHub actions job. The reason we need to do this is because by default the code is not checked out inside the job that we're running. The reason for this is because sometimes we may not need to check out the code, so there might be certain jobs that we want to perform that don't require the code in order to perform those jobs. However, in our case, we need to access the code because we need to run test and linting on the code. So we need to use this check out step here to make sure the code is available for us to run the next step on. So once that's done, we're going to go ahead and add the test step.
		- name: Test
		   run: docker-compose run --rm app sh -c "python manage.py test"
		So this is the command that runs the unit tests on our project. If we were to go ahead and copy this command and run it inside our terminal, it should go ahead and run the unit test for the project that we've created so far.
		
		![[Screenshot 2024-02-05 at 5.52.01 PM.png]]
		So we can see here that it ran a unit test. So this is basically the command we want to run next inside our job actions job. Next we're going to run the linting.
		We can call this lint lifting whatever we want to call it. Again, this is just a name that's used for us to view the different steps of the job inside the GitHub actions console.
		- name: Lint
		   run: docker-compose run --rm app sh -c "flake8"
		So now what we have is a complete set of steps for our job. The first step logs into Docker Hub. Then we check out using the check out action and then we run the tests using Docker Compose and then we run the listing using Docker compose as well. So if any of these steps fail, that means they return anything other than exit 0, which is the Linux exit signal for successful exit. If any of these fail, then the job that is running is going to fail.
		Docker compose comes preinstalled on the Ubuntu 20.04 runner. So if we're using this, run it then it should already have docker compose and docker installed and available. So you don't need to do anything like install it inside the container that we're running the job on. It should already be there ready for us to use.
	Configure Docker Hub credentials:
		The next step is to set up Docker Hub credentials and then add them to our get project so they can be used in the jobs.
		What are access tokens?
		So to authenticate with Docker, we can do it in two different ways. One way is we can just use the username and password that we used when we registered for the Docker Hub account. The problem with this is that it's good for our local machine and anything that we're logging into as a user. However, when we have automated tasks such as CI CD tools, that is like jobs running inside GitHub actions, we don't necessarily want to store our personal credentials with the account that's being used for that project. The reason for this is we shouldn't really share our credentials with anyone. We should only really use them for ourselves to log in and if we wanted to disable access to that particular tool. So let's say our project was hacked or we lost access to it or something. We might want to disable access to that account without having to change the credentials that we log in with ourselves. So the way we can do that is we can use something called access tokens. Access tokens are essentially just a username and password that are set up specifically for automated tasks. And we can go ahead and create access tokens as we need them and then we can remove them if we want to revoke access to whatever is using the access token. So we're going to go ahead and create an access token here inside our hub account.
		And then we can use that as our credentials instead of using our own username and password to log in with Docker Hub.
		
		![[Screenshot 2024-02-05 at 6.11.46 PM.png]]
		After creating the token we add our username and token as secrets for GitHub actions. 
		Now once we've added the secret, we can't actually retrieve the value, so we can't see what the secret is. We can only update it or remove it. And this is for security reasons.
		We should only have one token for every different account that we authenticate with. So best practice is not to share the same token with multiple different services. If we wanted to set up a different service that accesses Docker Hub, then we should create a new access token for that particular service. And the reason for this is that we can revoke the access as we need without having to change the access for every single service that we're using.
		So we have a hub user here, which should match up here in our YAML file and Docker Hub Token should match up too. All this stuff here, it pulls in the secrets from our project into the job. So we do the syntax. 
		
		![[Screenshot 2024-02-05 at 6.21.11 PM.png]]
		It's going to take whatever we have in the secrets and it's going to put it in the bit inside the job that we're running.
		That's all we need to do to set up Docker hub authentication in our GitHub actions jobs.
	Test GitHub Actions:
	
		![[Screenshot 2024-02-05 at 6.30.29 PM.png]]
		So now we have set up our GitHub actions job. Let's go ahead and test this and see that it works. So to test it, all we need to do is head over to our git project. And we're going to click on the actions page. And we can see here that there's no action created. So it basically has some automated steps to set up workflows and things like that. We don't need to do that because we've already set up our workflow. All we need to do is head back to our terminal, and commit our changes.
		
		![[Screenshot 2024-02-05 at 6.31.30 PM.png]]
		 What this will do is it will push our code to GitHub and because we have set up a new GitHub actions config and we have a trigger for on push, it should in theory run our job. So if we just refresh the page here.
		 
		![[Screenshot 2024-02-05 at 6.43.29 PM.png]]
		We have our workflow. So this is the checks workflow that is referencing the checks name of the file.
		
		![[Screenshot 2024-02-05 at 6.43.45 PM.png]]
		
		![[Screenshot 2024-02-05 at 6.44.52 PM.png]]
		If we click on that, we can see that it's running the job here and it uses the name for the commit that we added. So whatever the last commit was will be the name here in the workflow run. And we can see it's running off the main branch. So here we can see we got a tick. So if we click on the job, so this is the job that makes up our workflow. We click on test and lint. We should see the different steps.
		Setup job is added automatically by GitHub actions, but the rest of them down to here(Lint) should match up with what we have inside our config.
		Post Checkout, Post Login to Docker Hub and Complete job. These are added automatically.
		
		![[Screenshot 2024-02-05 at 6.45.27 PM.png]]
		
		![[Screenshot 2024-02-05 at 6.45.44 PM.png]]
		So if we expand the test. We should see the log output here and we can see that it ran our unit test and it said test zero tests because we haven't added any tests yet, but we know that it is running the test successfully. And then if we click on lint, we should see that there's not much here because there were no limiting errors with that code.
		
		![[Screenshot 2024-02-05 at 6.49.28 PM.png]]
		Now we go back to the code and let's say we make a change that would break the tests or break the linting.
		So this will break the line because we're supposed to have some spaces on the either side of the equals sign here. So if we save that and we go ahead and do git add, git commit and git push origin.
		
		![[Screenshot 2024-02-05 at 6.49.44 PM.png]]
		
		![[Screenshot 2024-02-05 at 6.50.13 PM.png]]
		So if we click on actions, you should see the new one runs, we can click it. So we click Test and Lint.
		We should see that the job fails.
		
		![[Screenshot 2024-02-05 at 6.50.35 PM.png]]
		So you see here we have the red X. If we go back to actions, you can see that the job failed because we have the "X" here.
		We should be able to click on the workflow and then the step in the job. And we can see here says that we have a couple of errors, the missing whitespace here and no new line and a file. And this is because we broke the linting here. So we didn't have the new line and we had this syntax that doesn't work here. So we need the whitespaces spaces here(before and after "="). This would be this would be correct. If we ran this, it should work.
		
		![[Screenshot 2024-02-05 at 6.51.24 PM.png]]
		But what we're going to do is because we don't need this variable, we're going to delete this and then we commit again, and push to origin and then the job should run again. And this time it should pass.
		![[Screenshot 2024-02-05 at 6.52.07 PM.png]]
		So we can see that the job completed successfully this time.
		If we look under lint and test, we can see that there are no issues and we got the green tick. So we know that the job is now completing successfully.
		
		![[Screenshot 2024-02-05 at 6.52.35 PM.png]]

Test Driven Development with Django:
	Testing in Django:
		Django test framework:
		- Based on unittest library.
		- Django adds features:
			- Test client- dummy web browser
			- Simulate authentication
			- Temporary database
		- Django REST Framework adds features:
			- API test client
		So when we test in Django, Django has something called the Django Test Framework, which is built into Django and comes out of the box. This is what we're going to be using to write the unit tests.
		The Django test framework is built on top of the unit test library.
		The unit test library comes out of the box with Python, but the Django test framework adds some additional features to this library. That's useful when we're testing Django projects.
		Some of these additional features include things like the test client, which is a dummy web browser that we can use to make requests to our project.
		It also allows us to simulate authentication so we can handle authentication by overriding it for our unit tests, which is useful when we're running tests because we don't always want to have to handle the log in and registration process for our test. The Django test framework also comes with database integration. It automatically creates a temporary database for us and then it will automatically clear the data from that database. Once we've finished running each test on top of Django, we have the Django Rest framework, which also adds some additional testing features specifically useful for testing rest APIs.
		The main one that we'll be using is the API test client, which is just like the test client that Django provides, except it's specifically used for testing API requests.
		Where do we put tests?
		- Placeholder tests.py added to each app.
		- Or create tests/ subdirectory to our app.
		- Keep in mind:
			- We can only use tests.py or tests/ directory(not both).
			- Test modules must start with test_.
			- Test directories must contain __init__.py.
		When we create a new app in Django, it automatically adds a tests.py module, which is a placeholder where we can add tests.
		Alternatively, we can create a test subdirectory inside our app, which allows us to split our tests up into multiple different modules.
		It's important to remember that we can only use either the tests.py module or the test/ subdirectory. We can't use them both.
		And if we do create tests inside our test directory, we need to make sure that each module is prefixed by the test_.
		Also make sure that when we have tests inside a directory, we have the __init__.py file added to that test subdirectory because this is what allows Django to pick up the tests in the test run.
		Test Database:
		- Test code that uses the database.
		- Specific database for tests.
		- So Django will actually automatically create a specific database just for our tests. And it does this automatically. And the way it works is we run the test and then it will clear any data that was created by the test and then run the next test. So every test that we run inside the Django test framework will have a fresh database to use.
		- Happens for every database(by default).
		So it's often useful to be able to test code that reads and writes data to database. And the problem we often have is that we want to have a separate database for our tests compared to our actual application because we don't want to be creating test data inside the real database.
		(For the last point) However, we can override this behavior, although we don't do it very often. It is possible to override the behavior so that wehave consistent data for all of our tests. However, it's not really recommended unless there's a specific reason to do that because it's ideal to have a clean data set for every test that we run.
		Test Classes:
		- SimpleTestCase:
			- No database integration.
			- Useful if no database is required for our test.
			- Save time executing tests(because we don't need to clear the database and set up the database for every test that we run.).
		- TestCase(most common class that we'll be using):
			- Database integration.
			- Useful for testing code that uses database(it's useful we need to test code that needs to write or read data to our database).
		