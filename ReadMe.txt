*Description*

Web front-end application containing gene annotation information and drug data for Diabetes using Python, Unix Commandline, Javascript, CSS, and HTML. The purpose of this webpage project was to generate a pipeline that would scrape relevant genetic and treatment data and combine both elements into one concise webpage. 

*Author*
Chris Dimapasok


*Data Scraped From:*

Gene Annotation Information
https://www.ncbi.nlm.nih.gov/gene/?term=diabetes (saved in tabular text format (tab-delimeted)

Drug Information
https://drugcentral.org/?q=diabetes (scraped directly from website and imported into Excel and formatted into txt file)

*File Locations*
All files are located in directory /var/www/html/cdimap1/project


*Detailed Usage*

#Downloading Data
1. Go to https://www.ncbi.nlm.nih.gov/gene and download gene data for disease of interest
2. Scroll to bottom and click send to file and select Tabular (text) for Format parameter
3. Open excel to download drug data from https://drugcentral.org. In excel click get Get Data from Web and input 
https://drugcentral.org URL. Load table into excel and save as txt file.

#Load Data into Database
4. To load gene data into database, execute python3 parser.py file to parse gene data and load into SQL database with python3 parser.py
5. Follow same steps for drug data, this time with python3 drug_parser.py

#Generate Webpage
6. Execute gene and drug cgi with ./drug2.cgi and ./query3.cgi respectively. 


*Open Webpage for Testing*
Navigate to webpage http://bfx3.aap.jhu.edu/cdimapa1/project/usersearch.html and type in gene of interest or just type any letter and get gene annotation information for the genes of interest. Additionally, at bottom of webpage there is a button functionality element that takes the user to another drug treatment page with significant treatment information for the disease. 
