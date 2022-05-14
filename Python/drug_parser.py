#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

#Create Connection
cnx= mysql.connector.connect(user= 'cdimapa1', password= 'password', host= 'localhost', database= 'cdimapa1')

#Create Cursor object
cursor= cnx.cursor()

#Parse File

with open('drug.txt', 'rb') as f:
    for line in f:
        line= line.decode('ISO-8859-1')
        line= line.rstrip()
        cols= line.split("\t")
   
    #Extract Drug Name and Descriptions
        drug_name= cols[0]
        drug_info= cols[-1]

    #Insert into SQL Database
        query= "INSERT INTO drug_info VALUES (%s, %s)"
        list= (drug_name, drug_info)

    #Execute Query
        cursor.execute(query, list)
        cnx.commit()

#Close Connection
cnx.close()
cursor.close()
