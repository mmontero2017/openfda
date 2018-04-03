import http.client #Library http, we create a client
import json # object notation (It is a format that marks the different fields with different signals)
# Dictionary of python can be converted to a json format. It is a python list that has some items, in this case a dictionary

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov") # http protocol and then we need the url where the info is available
conn.request("GET", "/drug/label.json?limit=10", None, headers) # code asking for github to  show us all the content from this user
r1 = conn.getresponse() # request the client sends a request
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8") #
conn.close()

repos1 = json.loads(repos_raw) # download a string a convert it

repos1 = repos1["results"] # first item in the list

for element in range(0,10):
    print("The id of the", element+1, "drug is: ", repos1[element]["id"])