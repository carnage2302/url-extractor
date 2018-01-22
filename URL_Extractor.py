#READ ME
#Download this file and open terminal. Navigate to your file's folder and run "python filename.py"
#Change the url for prefered target.
#Only for extracting informations of a website.
#Use this on your own risk.
import requests
r=requests.get('http://www.google.com')                                 #Change URL to extract information
print '\n' + "#################################################################"
print "######                                                      #####"
print "######            URL INFORMATION EXTRACTOR                 #####"
print "######                                                      #####"
print "#################################################################" + '\n'
print "TARGET URL :" + r.url
print "STATUS CODE:" + str(r.status_code) + '\n'
print "HEADERS"
print '**************************************************************'
for x in r.headers:
    print '\t' + x + ' : ' + r.headers[x]
print '**************************************************************\n'
print "CONTENTS :\n"
print r.text
