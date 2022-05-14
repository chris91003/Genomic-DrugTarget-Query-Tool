#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

#Create Connection
cnx= mysql.connector.connect(user= 'cdimapa1', password= 'password', host= 'localhost', database= 'cdimapa1')

#Create Cursor object
cursor= cnx.cursor()

#Parse ncbi gene file
for line in open('gene_result.txt'):
    line= line.rstrip()
    cols= line.split("\t")
    
    #Extract Specific Columns
    function= cols[7] #Gene Function
    name= cols[5]#Gene Names
    gene_id= cols[2]
    tax_id= cols[0]
   

    #Insert into SQL Database
    query = "INSERT INTO gene_info VALUES (%s, %s, %s, %s)"
    
    list= (name, gene_id, tax_id, function)
     
    #Execute query 
    cursor.execute(query, list)
    cnx.commit() 

#Close Connection 
cnx.close()
cursor.close()

