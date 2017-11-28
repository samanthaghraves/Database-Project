#LOGS ANALYSIS PROJECT

Hey everyone!

So, this one is a bit of a doozy. This program reads a posgresql database via Python, and then prints out pieces of information based on the questions asked in the project.

###So let's get started!

In this repo, you'll find 3 files.

First, the README. It's awesome, and you are here.

Next up, there's the questions.py file. Thats where the _magic_ happens!

And finally there's the questions.txt file, which simply shows the output.

###Setting Up The Project

So, to begin, you need a database to access. We used newsdata.sql, however, any database will work. You enter the database name into the DB_NAME variable, so that the python program knows where to look.

Once you do that, you're all set. Just make sure that the database and this python script are in the same directory, and you just run "python3 questions.py". 

IF you want to use this program to run different queries or check a different database, you're going to want to check the below section. It will tell you what you need to know.

###HOW TO USE THIS THING

This script takes a database name, or DB_NAME, and that is the database that we are working on.

After that, you input 3 queries. For this program, I was attempting to answer 3 questions 
using the database I was provided. 

1. What are the three most popular articles of all time?

2. Who are the four most popular authors of all time?

3. What days had more than 1% of requests lead to errors?

That's where the queries come from. If you are wanting to use this code for your own projects, 
you can modify the queries to anything you would like. It's just a string that is passed to postgresql, 
so as long as you've formatted it correctly, you're fine.

The next block is: [query1_result = dict() and query_result['title']]. Those are where the tables are stored, 
and the title line is where you add the part printed above the information. So, if you are wondering 
the _least_ popular articles, and you write a query to find that, you'll want to change the title string to
reflect that.

Now, for some functions.

####FUNCTIONS ARE GREAT DON'T @ ME

So, the first function ([def get_query_result(query))]) is super important. It saves us from having 
to call the cursors three times here. Basically, all this function does is connect to the database, run
all of the queries, and place that information in results. Here's where the second one comes in.

The next two functions ([def print_query_results(query_results))]) and ([def print_error_query_results(query_result)])
are what make up the bulk of what this script does. They get passed the information from 
([def get_query_result(query)]) and then take that information and formats it.

Basically ([def get_query_result(query)]) passes the query to [(query1_result['results'])] because of [results], and then it gets passed to ([def print_query_results(query_results))]) and ([def print_error_query_results(query_result)])
so that the [(print_query_results(query#_result))] can do its job.

So, yeah.

The main things that would need to be changed is the amount of queries, and the actual queries. 

Hope you like!
