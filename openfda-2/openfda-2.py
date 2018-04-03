import http.client #Library http, we create a client
import json # object notation (It is a format that marks the different fields with different signals)
# Dictionary of python can be converted to a json format. It is a python list thjat has some items, in this case a dictionary

headers = {'User-Agent': 'http-client'}

conn = http.client.HTTPSConnection("api.fda.gov") # http protocol and then we need the url where the info is available
conn.request("GET", "/drug/event.json?search=salycilic", None, headers) # code asking for github to  show us all the content from this user
r1 = conn.getresponse() # request the client sends a request
print(r1.status, r1.reason)
repos_raw = r1.read().decode("utf-8") #
conn.close()

repos = json.loads(repos_raw) # download a string a convert it

repo1 = repos["results"] # We choose the dictionary "results" to find the information about the manufacturer
repo2 = repo1[0] # First element of the list, in this case, the first dictionary

for element in repo1: # For every element of the first dictionary

    print("The manufacturers that produce aspirin are: ", repo2["patient"]["drug"][1]["openfda"]["manufacturer_name"])
# With these parameters we are entering inside the different dictionaries and lists, making sure also that we go through all