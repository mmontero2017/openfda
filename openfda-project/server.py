import http.server
import socketserver
import http.client
import json

# We stablish the IP and the port which we are going to use
IP = "localhost"  # Localhost means "I": your local machine
PORT = 8000

socketserver.TCPServer.allow_reuse_address = True  # This determines whether the server will allow or not the reuse of an address.


# This defaults to the value False, and can be set in subclasses to change the policy


# HTTPRequestHandler class: this module is used as a basis for building functioning Web servers

class testHTTPRequestHandler(
    http.server.BaseHTTPRequestHandler):  # This class is usually used to handle the requests that arrive to the server
    # do_METHOD, in this case GET with the argument "self". We do this in order to return a response to the client

    def do_GET(self):
        # Send response status code
        self.send_response(200)
        # Send headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        def drugs_active_ingredient():  # Inside the class testHTTPRequestHandler and also the definition of do_Get
            # we make a definition without any argument in order to search drugs taking into account the active ingredient parameter with a limit in the url where the info is available (api.fda.gov)
            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            information1 = self.path.strip('/search?').split('&')  # We remove '/search?' and separate the rest at '&'
            drugs = information1[0].split('=')[1]
            if "limit" in self.path:  # If we introduce in our request as clients a limit, is because we want to know a concrent number of drugs so as programmers we have to impliment that option for the client
                limit_1 = information1[1].split('=')[1]
                if limit_1 == "":
                    limit_1 = "20"
            else:
                limit_1 = "20"
            print("The client has made the request correctly :)")

            information2 = "/drug/label.json?search=active_ingredient:" + drugs + '&' + 'limit=' + limit_1  # Means the url we are searching as a client with the limit and the active ingredient include
            print(information2)

            conn.request("GET", information2, None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            list_1 = []  # We create an empty list
            i = 0  # Starting point at 0
            list_2 = "<head>" + "<font face='courier' align='center' size='6' color='black'>" + "Here you can find the brand names of the drugs you are looking for:" + '<body style="background-color: #81F7BE">' + "</font>" + "</head>" "<ol>" + "\n"
            limit_2 = int(limit_1)  # limit_2 is the limit_1 convert into a integrer number

            while i < limit_2:  # We create a while loop in order to append the results of the search of the client one by one until we reach the value of the limit
                try:
                    list_1.append(repos["results"][i]["openfda"]["brand_name"][0])  # We put all the new information about the drugs in the first list
                    i += 1
                except:  # In order to detect drugs that are not in url, we create a try-except "program"
                    list_1.append("Not known")
                    print("We cannot find drugs with this active ingredient. Please, try again!")
                    i += 1

            with open("data_drugs.html", "w") as file:  # We write all the info in the html file "manufacturers_list"
                file.write(list_2)
                for u in list_1:
                    list_3 = "<font face='courier'>" + "<t>" + "<li>" + u + "</font>"
                    file.write(list_3)

        def drugs_manufacturer_name():  # We make a definition without any argument in order to search drugs taking into account the manufacturer name parameter with a limit in the url where the info is available (api.fda.gov)

            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            information1 = self.path.strip('/search?').split('&')  # We remove '/search?' and separate the rest at '&'
            manufacturer = information1[0].split('=')[1]
            if "limit" in self.path:
                limit_1 = information1[1].split('=')[1]
                if limit_1 == "":
                    limit_1 = "20"
            else:
                limit_1 = "20"
            print("The client has made the request correctly :)")

            information2 = "/drug/label.json?search=openfda.manufacturer_name:" + manufacturer + '&' + 'limit=' + limit_1  # Means the url we are searching as a client with the limit and the manufacturer name include
            print(information2)

            conn.request("GET", information2, None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            list_1 = []  # We create an empty list
            i = 0  # Starting point at 0
            list_2 = "<head>" + "<font face='courier' align='center' size='6' color='black'>" + "These are the manufacturer names of the drugs that you are looking for:" + '<body style="background-color: #81F7BE">' + "</font>" + "</head>" "<ol>" + "\n"
            limit_2 = int(limit_1)  # limit_2 is the limit_1 convert into a integrer number

            while i < limit_2:  # We create a while loop in order to append the results of the search of the client one by one until we reach the value of the limit
                try:
                    list_1.append(repos["results"][i]["openfda"]["brand_name"][0])  # We put all the new information about the drugs in the first list
                    i += 1
                except:  # In order to detect drugs that are not in url, we create a try-except "program"
                    list_1.append("Not known")
                    print("We cannot find drugs with this manufacturer name. Please, try again!")
                    i += 1

            with open("manufacturer_name.html",
                      "w") as file:  # We write all the info in the html file "manufacturers_list"
                file.write(list_2)
                for u in list_1:
                    list_3 = "<font face='courier'>" + "<t>" + "<li>" + u + "</font>"
                    file.write(list_3)

        def list_manufacturers():  # We make a definition without any argument in order to search drugs taking into account the company parameter with a limit in the url where the info is available (api.fda.gov)

            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            information1 = self.path.strip('/listCompanies?').split('=')  # We remove '/search?' and separate the rest at '&'
            limit_1 = information1[1]
            print("The client has made the request correctly :)")

            information2 = "/drug/label.json?limit=" + limit_1  # Means the url we are searching as a client with the limit include
            print(information2)

            conn.request("GET", information2, None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            list_1 = []  # We create an empty list
            i = 0  # Starting point at 0
            list_2 = "<head>" + "<font face='courier' align='center' size='6' color='black'>" + "This is the list of all manufacturers you are looking for:" + '<body style="background-color: #81F7BE">' + "</font>" + "</head>" "<ol>" + "\n"
            limit_2 = int(limit_1)  # limit_2 is the limit_1 convert into a integrer number

            while i < limit_2:  # We create a while loop in order to append the results of the search of the client one by one until we reach the value of the limit
                try:
                    list_1.append(repos["results"][i]["openfda"]['brand_name'][0])  # We put all the new information about the drugs in the first list
                    i += 1
                except:  # In order to detect drugs that are not in url, we create a try-except "program"
                    list_1.append("Not known")
                    print("We cannot find that drug in our list. Please, try again!")
                    i += 1

            with open("manufacturers_list.html","w") as file:  # We write all the info in the html file "manufacturers_list"
                file.write(list_2)
                for u in list_1:
                    list_3 = "<font face='courier'>" + "<t>" + "<li>" + u + "</font>"
                    file.write(list_3)

        def list_drugs():  # We make a definition without any argument in order to search drugs with a limit in the url where the info is available (api.fda.gov)

            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            information1 = self.path.strip('/listDrugs?').split(
                '=')  # We remove '/search?' and separate the rest at '&'
            limit_1 = information1[1]
            print("The client has made the request correctly :)")

            information2 = "/drug/label.json?limit=" + limit_1  # Means the url we are searching as a client with the limit include
            print(information2)

            conn.request("GET", information2, None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            list_1 = []  # We create an empty list
            i = 0  # Starting point at 0
            list_2 = "<head>" + "<font face='courier' align='center' size='6' color='black'>" + "Here you can find the list of all of the drugs you are looking for:" + '<body style="background-color: #81F7BE">' + "</font>" + "</head>" "<ol>" + "\n"
            limit_2 = int(limit_1)  # limit_2 is the limit_1 convert into a integrer number

            while i < limit_2:  # We create a while loop in order to append the results of the search of the client one by one until we reach the value of the limit
                try:
                    list_1.append(repos['results'][i]["openfda"]['brand_name'][0])  # We put all the new information about the drugs in the first list
                    i += 1
                except KeyError:  # In order to detect drugs that are not in url, we create a try-except "program"
                    list_1.append("Not known")
                    print("We cannot find that drug in our list. Please, try again!")
                    i += 1

            with open("drugs_list.html", "w") as file:  # We write all the info in the html file "drugs_list"
                file.write(list_2)
                for u in list_1:
                    list_3 = "<font face='courier'>" + "<t>" + "<li>" + u + "</font>"
                    file.write(list_3)

        def list_warnings():  # We make a definition without any argument in order to search drugs taking into account the warning parameter with a limit in the url where the info is available (api.fda.gov)

            headers = {'User-Agent': 'http-client'}
            conn = http.client.HTTPSConnection("api.fda.gov")
            information1 = self.path.strip('/listWarnings?').split('=')  # We remove '/search?' and separate the rest at '&'
            limit_1 = information1[1]
            print("The client has made the request correctly :)")

            information2 = "/drug/label.json?limit=" + limit_1  # Means the url we are searching as a client with the limit include
            print(information2)

            conn.request("GET", information2, None, headers)
            r1 = conn.getresponse()
            print(r1.status, r1.reason)
            repos_raw = r1.read().decode("utf-8")
            conn.close()
            repos = json.loads(repos_raw)

            list_1 = []  # We create a empty list (list_1)
            warnings = []  # We create an empty list (warnings)
            i = 0  # Starting point must be 0
            j = 0
            list_2 = "<head>" + "<font face='courier' align='center' size='6' color='black'>" + "This is the list of all warnings of the drugs you are looking for:" + '<body style="background-color: #81F7BE">' + "</font>" + "</head>" "<ol>" + "\n"
            limit_2 = int(limit_1)  # limit_2 is the limit_1 convert into a integrer number

            while i < limit_2:  # We create a while loop in order to append the results of the search of the client one by one until we reach the value of the limit
                try:  # We use a try and except structure in case one of the drugs doesn't have any brandname in it's description of the openfda
                    list_1.append(repos["results"][i]["openfda"]["brand_name"][0])
                    i += 1
                except:
                    list_1.append("Not known")
                    i += 1

            while j < limit_2:
                try:  # We use a try and except structure in case one of the drugs doesn't have any warning in it's description
                    warnings.append(repos["results"][i]["warnings"][0])
                    j += 1
                except:
                    warnings.append("Not known")
                    j += 1

            with open("warnings_list.html","w") as file:  # We create a html file with the information encode in the list_2
                file.write(list_2)
                i = 0

                while i < limit_2:  # Inside of this file, we create a while loop to create another list with the name of the drug and the warnings for each of the drugs
                    list_3 = "<font face='courier'>" + "<t>" + "<li>" + "The drug " + list_1[i] + "&nbsp; has this warnings: " + warnings[i] + "</font>"
                    file.write(list_3)
                    i += 1

        if self.path == "/":
            print("SEARCH: The client is searching a web")
            with open("search.html", "r") as file:
                message = file.read()
                self.wfile.write(bytes(message, "utf8"))

        elif "searchCompany" in self.path:  # If the client is searching specifically for a drug's Company, he/she must put searchCompany in order to enter into the file manufacturer_name we created previously with all the information the client needs
            drugs_manufacturer_name()  # Definition in which is inside the file manufacturer_name

            with open("manufacturer_name.html", "r") as file:
                message = file.read()
                self.wfile.write(bytes(message, "utf8"))

        elif "searchDrug" in self.path:  # If the client is searching specifically for a drug's active ingredient, he/she must put searchDrug in order to enter into the file data_drugs we created previously with all the information the client needs
            drugs_active_ingredient()  # Definition in which is inside the file data_drugs

            with open("data_drugs.html", "r") as file:
                message = file.read()
                self.wfile.write(bytes(message, "utf8"))


        elif "listDrugs" in self.path:  # If the client is searching specifically for a drug, he/she must put listDrugs in order to enter into the file drugs_list we created previously with all the information the client needs
            list_drugs()  # Definition in which is inside the file drugs_list

            with open("drugs_list.html", "r") as file:
                message = file.read()
                self.wfile.write(bytes(message, "utf8"))

        elif "listCompanies" in self.path:  # If the client is searching specifically for a drug's Company, he/she must put listCompanies in order to enter into the file manufacturers_list we created previously with all the information the client needs
            list_manufacturers()  # Definition in which is inside the file manufacturers_list

            with open("manufacturers_list.html", "r") as file:
                message = file.read()
                self.wfile.write(bytes(message, "utf8"))

        elif 'listWarnings' in self.path:  # If the client is searching specifically for a drug warning, he/she must put listWarnings in order to enter into the file warnings_list we created previously with all the information the client needs
            list_warnings()  # Definition in which is inside the file warnings_list

            with open("warnings_list.html", "r") as file:
                message = file.read()
                self.wfile.write(bytes(message, "utf8"))


# Handler = http.server.SimpleHTTPRequestHandler
Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)
print("serving at %s:%s" % (IP, PORT))
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print("")
print("Server stopped!")