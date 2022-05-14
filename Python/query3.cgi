#!/usr/local/bin/python3

import jinja2
import re
import cgi
import mysql.connector

# This line tells the template loader where to search for template files
templateLoader = jinja2.FileSystemLoader( searchpath="./templates" )
env = jinja2.Environment(loader=templateLoader)

#s creates your environment and loads a specific template
template = env.get_template('template.html')

#Get User Input
form= cgi.FieldStorage()
search= form.getvalue('search_term')


#Create connection
con= mysql.connector.connect(user= 'cdimapa1', password= 'password', host= 'localhost', database= 'cdimapa1')

#Create cursor object
cursor= con.cursor()

#Create Empty list to store information
#list= list()

#Query From Databse
query= "SELECT * FROM gene_info WHERE gene_info.GeneName LIKE %s"

cursor.execute(query, ('%' +str(search) +'%',))


#Get information
results=cursor.fetchall()

#Finish connection
cursor.close()
con.close()




#Print the output
print("Content-Type: text/html\n\n")
print(template.render(results= results,))
