from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        file = open('db.json')
        obj = file.read()
        data = json.loads(obj)
        if len(self.path) == 1:
            self.wfile.write(str("Hello!").encode())
        else:
            list = self.path.split("/")
            if len(list) == 5:
                element = str(data["fructe"])
                element = element.replace("'", '"')
                js = json.loads(element)
                for j in range(len(js)):
                    if js[j].get("id") == list[2]:
                        element = str(js[j][list[3]])
                        element = element.replace("'", '"')
                        sb = json.loads(element)
                        for i in range(len(sb)):
                            if sb[i].get('id')==list[4]:
                                self.wfile.write(str(sb[i]).encode())
            elif len(list) == 4:
                element = str(data["fructe"])
                element = element.replace("'", '"')
                js = json.loads(element)
                for j in range(len(js)):
                    if js[j].get("id") == list[2]:
                        self.wfile.write(str(js[j][list[3]]).encode())
            elif len(list) == 3:
                element = str(data["fructe"])
                element = element.replace("'", '"')
                js = json.loads(element)
                for j in range(len(js)):
                    if js[j].get("id") == list[2]:
                        self.wfile.write(str(js[j]).encode())
            else:
                l = list[1].split('?')
                if len(l) == 1:
                    self.wfile.write(str(data[list[1]]).encode())
                else:
                    l = l[1].split('=')
                    print(l)
                    if l[0] == 'limit':
                        for i in range(int(l[1])):
                            self.wfile.write(str(data['fructe'][i]).encode())
                    elif l[0] == 'nume':
                        for i in range(len(data['fructe'])):
                            if data['fructe'][i].get('nume')==l[1]:
                                self.wfile.write(str(data['fructe'][i]).encode())


    def do_POST(self):
        self.send_response(201)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        file = open('db.json')
        obj = file.read()
        data = json.loads(obj)
        list = self.path.split("/")
        if self.path.endswith('/fructe'):
            content_length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(content_length))
            with open('db.json') as jsonfile:
                data = json.load(jsonfile)
                temp = data["fructe"]
                max = 1;
                for i in range(len(data['fructe'])):
                    if int(data['fructe'][i].get('id')) > max:
                        max = int(data['fructe'][i].get('id'))
                post_data["id"] = str(max+1)
                temp.append(post_data)
            with open('db.json', 'w') as f:
                json.dump(data, f, indent=4)
        elif len(list) == 4:
            content_length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(content_length))
            element = str(data["fructe"])
            element = element.replace("'", '"')
            js = json.loads(element)
            for j in range(len(js)):
                if js[j].get("id") == list[2]:
                    with open('db.json') as jsonfile:
                        data = json.load(jsonfile)
                        temp = data["fructe"][j]['cantitate']
                        temp.append(post_data)
                    with open('db.json', 'w') as f:
                        json.dump(data, f, indent=4)



    def do_PUT(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        with open('db.json') as jsonfile:
            data = json.load(jsonfile)
        content_length = int(self.headers['Content-Length'])
        put_data = json.loads(self.rfile.read(content_length))
        print(put_data)
        list = self.path.split("/")
        if len(list) == 3:
            for j in range(len(data["fructe"])):
                if data["fructe"][j].get("id") == list[2]:
                    data["fructe"].pop(j)
                    put_data["id"] = str(j+1)
                    data["fructe"].append(put_data)
                    break
            with open('db.json', 'w') as f:
                json.dump(data, f, indent=4)
        elif len(list) == 5:
            for j in range(len(data['fructe'])):
                if data['fructe'][j].get("id") == list[2]:
                    for i in range(len(data['fructe'][j]['cantitate'])):
                        if data["fructe"][j]['cantitate'][i].get("id") == list[4]:
                            data["fructe"][j]['cantitate'].pop(i)
                            data["fructe"][j]['cantitate'].append(put_data)
                            break
                    with open('db.json', 'w') as f:
                        json.dump(data, f, indent=4)


    def do_DELETE(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        file = open('db.json')
        obj = file.read()
        data = json.loads(obj)
        list = self.path.split("/")
        if len(list) == 5:
            element = str(data["fructe"])
            element = element.replace("'", '"')
            js = json.loads(element)
            for j in range(len(js)):
                if js[j].get("id") == list[2]:
                    element = str(js[j][list[3]])
                    element = element.replace("'", '"')
                    sb = json.loads(element)
                    for i in range(len(sb)):
                        if sb[i].get('id') == list[4]:
                            data['fructe'][j][list[3]].pop(i)
        elif len(list) == 3:
            element = str(data["fructe"])
            element = element.replace("'", '"')
            js = json.loads(element)
            for j in range(len(js)):
                if js[j].get("id") == list[2]:
                    data["fructe"].pop(j)
                    break
        else:
            data.pop("fructe")
        print(data)
        open("db.json", "w").write(json.dumps(data, indent=4))


def run():
    PORT = 5000
    server_adress = ('localhost', PORT)
    server = HTTPServer(server_adress, requestHandler)
    print('Server running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    run()
