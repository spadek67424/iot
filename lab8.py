from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import grovepi
R=0
G=0
B=0
class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        global R
        global G
        global B
        print 'Get path:', self.path
        st=self.path
        out=st.split("/")
        self._set_headers()
        if "status" in out:
            self.wfile.write(R)
            self.wfile.write(G)
            self.wfile.write(B)
        if "set" in out:
            if "r" in out:
                R=out[3]
            if "g" in out:
                G=out[3]
            if "b" in out:
                B=out[3]
        grovepi.analogWrite(3,int(B))
        grovepi.analogWrite(5,int(R))
        grovepi.analogWrite(6,int(B))
def run(server_class=HTTPServer, handler_class=Server, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Server start on:', port
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
