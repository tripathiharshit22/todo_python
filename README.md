## To-Do App (Python backend + Vanilla JS frontend)

A simple To-Do list with a static HTML frontend and a minimal Python HTTP server for persistence via tasks.json.

### Prerequisites
- Python 3.8+ installed and available in PATH (verify with python --version).
- A modern web browser (Chrome, Edge, etc.).

### Project Structure

New folder/
├─ index.html       # Frontend (open directly in your browser)
├─ todo.py          # Backend (Python HTTP server)
├─ tasks.json       # Data file (auto-created on first run)
└─ README.md


### Run the backend
1. Open PowerShell and navigate to the project folder:
   powershell
   Set-Location "C:\Users\Abhishek Yadav\OneDrive\Desktop\New folder"
   
2. Start the server:
   powershell
   python todo.py
   
3. You should see:
   
   To-Do server running on http://127.0.0.1:8080
   Press Ctrl+C to stop.
   

### Open the frontend
- Double-click index.html (or run start index.html in PowerShell).
- The page will load tasks from, and save tasks to, the running backend.

### Features
- Add, complete/undo, and delete tasks
- Auto-save to tasks.json via HTTP calls:
  - GET  /get-tasks → returns an array of tasks
  - POST /save-tasks → accepts an array of tasks and saves

### Troubleshooting
- Failed to fetch / 404
  - Ensure the backend is running: python todo.py
  - Verify the API:  
    powershell
    Invoke-WebRequest -Uri http://127.0.0.1:8080/get-tasks -UseBasicParsing
    
- UnicodeEncodeError on Windows console
  - The server logs were updated to ASCII-only; pull latest and rerun.
- Browser console shows 404 for /favicon.ico
  - Handled by the server; reload the page if you still see it.
- Python not found
  - Install Python from https://www.python.org/downloads/ and check “Add Python to PATH”. Reopen PowerShell.

### Notes
- The frontend uses fetch to http://127.0.0.1:8080. Update API_URL in index.html if you change the port/host.
- tasks.json is stored in the project directory. Deleting it resets the list.

### Stopping the server
- Press Ctrl + C in the PowerShell window running todo.py.
