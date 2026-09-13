# 🔍 CodeLens



### Interactive Python Code Explanation Platform



CodeLens is a simple interactive platform that helps users understand Python code one line at a time.



**Paste → Click → Understand**



Select any line of Python code and get a clear explanation of what it does, why it is used, and its important parts.



---



## ✨ Features



- Interactive Python code editor

- Click any line to select it

- Selected-line highlighting

- Line-by-line explanations

- Explanation of common Python constructs

- Simple and beginner-friendly explanations

- FastAPI backend



Currently supports:



- `if` conditions

- `for` loops

- Function definitions

- `return` statements

- Variable assignments



---



## ⚙️ How It Works



```text

Python Code

&#x20;    ↓

Select a Line

&#x20;    ↓

React + Monaco Editor

&#x20;    ↓

FastAPI Backend

&#x20;    ↓

Explanation Engine

&#x20;    ↓

Explanation
```



## 🛠️ Tech Stack



Frontend



- React

- Vite

- Monaco Editor



Backend



- Python

- FastAPI

- Uvicorn

## 📁 Project Structure

codelens/

├── backend/

│   ├── explanation\_engine.py

│   └── main.py

│

├── frontend/

│   ├── public/

│   └── src/

│       ├── App.jsx

│       ├── App.css

│       ├── index.css

│       └── main.jsx

│

├── .gitignore

└── README.md

## 🚀 Run Locally

Backend

cd backend

.\\venv\\Scripts\\activate

uvicorn main:app --reload



Backend:



http://127.0.0.1:8000



API documentation:



http://127.0.0.1:8000/docs

Frontend



Open another terminal:



cd frontend

npm install

npm run dev



Then open the URL provided by Vite.



## 💡 Example

def is\_prime(n):

&#x20;   for i in range(2, n):

&#x20;       if n % i == 0:

&#x20;           return False

&#x20;   return True



Selecting:



if n % i == 0:



gives an explanation such as:



Checks whether n is divisible by i without a remainder.



CodeLens also explains important operators such as % and ==.



## 🧠 Explanation Engine



CodeLens currently uses a rule-based Python explanation engine.



It identifies common Python constructs and generates a structured explanation containing:



What — what the line does

Why — why the line is used

Parts — important syntax and operators

Simple Explanation — an easier way to understand the line



CodeLens does not execute the user's code or use an external AI API.



## 🎯 Goal



CodeLens is designed to make learning and understanding source code easier by allowing users to focus on one line at a time.



Understand code, one line at a time.



## 👨‍💻 Author



Akshaya Naidu



## 📄 License



This project is developed as a learning and portfolio project.

