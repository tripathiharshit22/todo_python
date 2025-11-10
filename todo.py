import json

from http.server import BaseHTTPRequestHandler, HTTPServer

import os



TASKS_FILE = 'tasks.json'



# Ensure file exists

if not os.path.exists(TASKS_FILE):

    with open(TASKS_FILE, 'w') as f:

        json.dump([], f)





def load_tasks():

    with open(TASKS_FILE, 'r') as f:

        return json.load(f)





def save_tasks(tasks):

    try:

        with open(TASKS_FILE, 'w') as f:

            json.dump(tasks, f, indent=2)

        print("Tasks saved successfully.")

    except Exception as e:

        print(f"Error saving tasks: {e}")





class RequestHandler(BaseHTTPRequestHandler):

    # --- CORS fix ---

    def end_headers(self):

        self.send_header('Access-Control-Allow-Origin', '*')

        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')

        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

        super().end_headers()



    def do_OPTIONS(self):

        self.send_response(200)

        self.end_headers()



    def _send_json(self, data, status_code=200):

        self.send_response(status_code)

        self.send_header('Content-Type', 'application/json')

        self.end_headers()

        self.wfile.write(json.dumps(data).encode())



    # --- Handle GET ---

    def do_GET(self):

        if self.path == '/favicon.ico':

            self.send_response(204)

            self.end_headers()

        elif self.path == '/get-tasks':

            print("GET /get-tasks")

            tasks = load_tasks()

            self._send_json(tasks)

        else:

            self._send_json({'error': 'Not found'}, 404)



    # --- Handle POST ---

    def do_POST(self):

        if self.path == '/save-tasks':

            try:

                content_length = int(self.headers.get('Content-Length', 0))

                post_data = self.rfile.read(content_length)

                tasks = json.loads(post_data.decode('utf-8'))

                print("Received tasks:", tasks)

                save_tasks(tasks)

                self._send_json({'message': 'Tasks saved successfully'})

            except Exception as e:

                print(f"Error in POST /save-tasks: {e}")

                self._send_json({'message': 'Error saving tasks'}, 500)

        else:

            self._send_json({'error': 'Not found'}, 404)





def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):

    server_address = ('', port)

    httpd = server_class(server_address, handler_class)

    print(f"To-Do server running on http://127.0.0.1:{port}")

    print("Press Ctrl+C to stop.")

    httpd.serve_forever()





if __name__ == '__main__':

    run()