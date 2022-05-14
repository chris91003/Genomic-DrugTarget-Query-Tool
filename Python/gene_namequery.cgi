#!/usr/local/bin/python3

import jinja2
import re
import cgi
import mysql.connector
import json

# This line tells the template loader where to search for template files
#templateLoader = jinja2.FileSystemLoader( searchpath="./templates" )
#env = jinja2.Environment(loader=templateLoader)

#s creates your environment and loads a specific template
#template = env.get_template('template.html')

#Get User Input
form= cgi.FieldStorage()
search= form.getvalue('term')



#Create connection
con= mysql.connector.connect(user= 'cdimapa1', password= 'password', host= 'localhost', database= 'cdimapa1')

#Create cursor object
cursor= con.cursor()

#Create Empty list to store information
#list= list()

#Query From Databse
query= "SELECT GeneName FROM gene_info WHERE gene_info.GeneName LIKE %s"

cursor.execute(query, ('%' +str(search) +'%',))


#Get information
#results=cursor.fetchall()
results = [res[0] for res in cursor.fetchall()]
output= json.dumps(results)

#Finish connection
cursor.close()
con.close()




#Print the output
print("Content-Type: application/json\n\n")
print(output)
#print(template.render(results= results,))
