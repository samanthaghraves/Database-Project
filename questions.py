#!/usr/bin/python3

import psycopg2
import sys

"""
This is my submission for the Logs Analysis Project.
The python file takes various queries and applies them to the database.
It then stores them in variables and formats the text, making it
much more readable.
"""

DB_NAME = 'news'

query1 = """SELECT articles.title, count(*) AS views
        FROM authors JOIN articles ON authors.id = articles.author
        JOIN log ON log.path LIKE CONCAT('%', articles.slug)
        GROUP BY articles.title ORDER BY views DESC
        LIMIT 3;"""

query2 = """SELECT authors.name, COUNT(log.path) AS views FROM authors
        JOIN articles ON authors.id = articles.author JOIN log ON
        log.path LIKE CONCAT('%', articles.slug) GROUP BY
        authors.name ORDER BY views DESC LIMIT 4;"""

query3 = """SELECT day, perc FROM (
        SELECT day, round((sum(requests)/(select count(*) FROM log WHERE
        substring(cast(log.time as text), 0, 11) = day) * 100), 2) AS
        perc FROM (select substring(cast(log.time as text), 0, 11) AS day,
        count(*) AS requests FROM log WHERE status LIKE '%404%' GROUP BY day)
        AS log_percentage group BY day ORDER BY perc desc) AS final_query
        WHERE perc >= 1"""


"""
Storing the variables
"""
query1_result = dict()
query1_result['title'] = """\n1. The three most popular articles
                        of all time are:\n"""

query2_result = dict()
query2_result['title'] = "\n2. The most popular authors of all time are:\n"

query3_result = dict()
query3_result['title'] = """\n3. Days where more than 1% of
                        requests lead to errors:\n"""


"""
Calls the queries to be applied to the database
"""


def get_query_result(query):
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

"""
Calls for the results to be printed
"""


def print_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print('\t' + str(result[0]) + ':	' + str(result[1]) + ' views')


def print_error_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ':	' + str(result[1]) + '%')

"""
Sets where the variables are stored.
"""

query1_result['results'] = get_query_result(query1)
query2_result['results'] = get_query_result(query2)
query3_result['results'] = get_query_result(query3)

print_query_results(query1_result)
print_query_results(query2_result)
print_error_query_results(query3_result)

