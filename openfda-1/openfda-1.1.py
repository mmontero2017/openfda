import http.client #Library http, we create a client
import json # object notation (It is a format that marks the different fields with different signals)
# Dictionary of python can be converted to a json format. It is a python list that has some items, in this case a dictionary

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov") # http protocol and then we need the url where the info is available
conn.request("GET", "/drug/label.json", None, headers) # code asking for github to  show us all the content from this user
r1 = conn.getresponse() # request the client sends a request
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8") #
conn.close()

repos1 = json.loads(repos_raw) # download a string a convert it

repo = repos1['results'] # first item in the list

print("The id of the drug is", repo[0]['id'])
print("The purpose of the drug is", repo[0]["purpose"])
print("The manufacturer name of the drug is", repo[0]["openfda"]["manufacturer_name"])
