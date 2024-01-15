![[Screenshot 2024-01-02 at 7.31.00 PM.png]]

In the above example, in basicConfig we are supplying a very basic configuration of logging, in this case supplying the level which is the warning

The others are different types of log messages.

What level does is that it determines which level of logging we want to print.

![[Screenshot 2024-01-02 at 7.35.11 PM.png]]

If we want to show any other level along with the 3(warning, error and critical) we need to simply change basicConfig to that level e.g.: logging.basicConfig(level=logging.INFO): will also show info message along with the other messages, according to their levels, similar for debug message.

Being able to control logs is really helpful because then throughout our application we can use these severity levels to print things, and we only have one place where we are defining how detailed the logs should be. we don't have to go through our code and enable and disable log messages just because we don't want to show them, we simply define in our basic config which level we want to see, from only critical errors to  all the levels of messages from debugging to critical messages.

![[Screenshot 2024-01-02 at 7.54.27 PM.png]]

We can even imagine that this level is something that you might want to be able to set from, let's say, a database, so that even when our application has already deployed, we can, in principle, change the database logging level, and then that's going to change the way that our application logging happens. So basic config has other arguments as well. For example, we can set the file name, if we want to write logs to a file, or we can change the way that logging is formatted.

![[Screenshot 2024-01-02 at 8.17.57 PM.png]]

Here, we formatted according to the time and name of the level and then the message, and we have also provided a string formatting how date and time should look like in these log messages.

This type of formatting is really helpful and easy to change. If we change it in one place it gets applied everywhere throughout our application.

Default logging writes the logs to the console. To write it to a file we can simply do that by adding a filename argument, in this case basic.log.

![[Screenshot 2024-01-02 at 8.28.05 PM.png]]

Now if we run this we don't get basic console logs anymore, instead these log messages are contained a log file named 'basic.log' that was generated. And logging adds to the existing log file. So if we run the log again we can see that basic.log contains these logs twice. Now simply writing log to a console or file is fine. But if we're developing more complex applications, we generally want to have more control over how logging happens, and it can be helpful to use a logging service. What log services do is that they give us an easier way to visualise logs, search logs, have overall more control over how long logs are being saved, and backups and things like that. And they also are helpful sometimes if we want to give somebody else in our team, maybe somebody's not a developer access to the logs, because that might sometimes be useful. There are several companies that offer logging services.

![[Screenshot 2024-01-02 at 8.41.15 PM.png]]

To integrate a logging service the only thing we need to to do is supply a host and a port. that basically tells the logging system where to send the logs.

In the above example, we have our main function where we use the logging module to create a logger object. Unlike before where we were using logging directly, here we are creating a logger object, to which we can also assign a name. We can have different logger objects for different parts of the application