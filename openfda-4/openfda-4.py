Handler = testHTTPRequestHandler

httpd = socketserver.TCPServer((IP, PORT), Handler)

Handler = socketserver.TCPserver(("", PORT), Handler)
print("Serving at port", PORT)
httpd.server_forever()