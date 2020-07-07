# Yin Song
# July 7 2020

###### Please close all the linkedin tabs before running this ######

import requests
import pprint
import csv
import json
from bs4 import BeautifulSoup


def findKeysLocation(s, key, pos):
    # return the location of a tag in the html
    locs = []
    while(pos!=-1):
        pos = s.find(key,pos+1)
        locs.append(pos)
    locs=locs[:-1]
    return locs


def findTitleValue(s,key_start,key):
    # return the work title based on tag location
    start=key_start+len(key)+1
    end=s.find('"',start,start+200)
    val = s[start-1:end]

    #get rid of fellowship
    if(s[end:end+50].find("companyUrn")!=-1):
        #get rid of special chara
        val=val.replace('&amp;','&')
        return(val)
    return -1

def findValue(s,key_start,key):
    # return a key value based on tag location
    start=key_start+len(key)+1
    end=s.find('"',start,start+300)
    val = s[start-1:end]
    return(val)

def findConnectionValue(s,key):
    # return the number of connections
    loc=s.find(key)
    start = loc+len(key)+1
    end = s.find(',',start,start+10)
    val = s[start-1:end]

    #handle 500+ case
    if(val=='500'):
        val=val+"+"

    return(val)

def findDegrees(s):
    # return a dict of degrees
    degree = {}
    degree['undergrad']=""
    degree['grad']=""
    degree['phd']=""
    degree['other_degree']=""
    locs=findKeysLocation(s,'"degreeName":"',0)

    # sort degrees by type
    for loc in locs:
        deg = findValue(s,loc,'"degreeName":"')
        if(deg.find("Master")!=-1 or deg.find("master")!=-1):
            degree['grad']=deg
        elif(deg.find("Bachelor")!=-1 or deg.find("bachelor")!=-1):
            degree['undergrad']=deg
        elif(deg.find("phd")!=-1 or deg.find("PhD")!=-1 or deg.find("PHD")!=-1 or deg.find("Doctor")!=-1):
            degree['phd']=deg
        else:
            degree['other_degree']=deg
    return degree

def grad_year(data):
    # return graduate year, if any
    return "Need implement"

def undergrad_year(data):
    # return undergraduate year, if any
    return "Need implement"

def ifNEU(data):
    # decide this person's relation with NEU
    return "Need implement"

def current_emp(data):
    # return the current employer
    return "Need implement"

def past_emps(data):
    # return past employers, if any
    return "Need implement"


def extractData(client,URL):
    # extract person info from linkedin page
    data_dic = {}

    #open the html with soup object
    html = client.get(URL).content #opens connections_url
    soup = BeautifulSoup(html , "html.parser")

    # extract name
    person_data = soup.find_all('code')[32].get_text()
    person_dict = json.loads(person_data)
    fn = person_dict["data"]["firstName"]
    ln = person_dict["data"]["lastName"]
    data_dic['fname']=fn
    data_dic['lname']=ln

    # current position/title
    occupa = person_dict["data"]["occupation"]

    #connect_dict = json.loads(soup.find_all('code')[24].get_text())
    #connects = connect_dict["data"]["connectionsCount"]

    # extract work experience
    pretty_soup = soup.prettify()
    #print(pretty_soup)
    title_indexes = findKeysLocation(pretty_soup, '"title":"', 0)
    titles = []
    for t in title_indexes:
        title=findTitleValue(pretty_soup,t,'"title":"')
        if(title != -1):
            titles.append(title)
    data_dic['works']=titles

    # extract number of connections 
    connects = findConnectionValue(pretty_soup, '"connectionsCount":')
    data_dic['connects']=connects

    degrees = findDegrees(pretty_soup)
    data_dic['undergrad']=degrees['undergrad']
    data_dic['grad']=degrees['grad']
    data_dic['phd']=degrees['phd']

    pprint.pprint(data_dic)

    return data_dic


def writeCSV(data):
    # write data to a csv
    # need to discuss how data are used, visualized, and stored

    filename = 'LinkedIn_Extract.csv'
    headers = ['Name','NEU Link','Undergrad Degree','Undergrad Year','Grad Degree','Grad Year','Current Employer','Current Position','STEM/Tech/Engineering Related','Past Employer(s)','Connections' ]

    # only write one row at this point
    #rows = []
    
    # create single record
    row = [data['fn']+' '+data['ln'],data['neu'],data['undergrad'],data['undergrad_yr'],data['grad'],data['grad_yr'],data['current_emp'],data['current_pos'],data['stem'],data['past_emp'],data['connects']]

    # writing to csv file  
    with open(filename, 'w') as csvfile:  
        # creating a csv writer object  
        csvwriter = csv.writer(csvfile)  
            
        # writing the fields  
        csvwriter.writerow(headers)  
            
        # writing the data rows  
        csvwriter.writerows(row) 


def setup():
    #create a session
    client = requests.Session()

    #create url page variables
    HOMEPAGE_URL = 'https://www.linkedin.com'
    #URL = 'https://www.linkedin.com/in/alex-bonacum-55a83b51/'
    #URL = 'https://www.linkedin.com/in/jason-toby-9b435272/'
    URL='https://www.linkedin.com/in/kevin-b-707b29/'
    LOGIN_URL = 'https://www.linkedin.com/uas/login-submit'

    #get url, soup object and csrf token value
    html = client.get(HOMEPAGE_URL).content
    soup = BeautifulSoup(html, "html.parser")
    csrf = soup.find('input', dict(name='loginCsrfParam'))['value']

    #create login parameters
    login_information = {
        'session_key':'songyin79@qq.com',
        'session_password':'testuseonly',
        'loginCsrfParam': csrf
    }

    #try and login
    try:
        client.post(LOGIN_URL, data=login_information)
    except:
        print("Failed to Login")

    return extractData(client,URL)

data = setup()
#writeCSV(data)
