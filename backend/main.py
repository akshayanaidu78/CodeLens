from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from explanation_engine import explain_line


app = FastAPI(title="CodeLens API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class CodeRequest(BaseModel):
    code: str
    line_number: int


@app.get("/")
def home():
    return {
        "message": "CodeLens backend is running"
    }


@app.post("/explain")
def explain_code(request: CodeRequest):
    lines = request.code.splitlines()
    line_index = request.line_number - 1

    if line_index < 0 or line_index >= len(lines):
        return {
            "error": "Invalid line number"
        }

    selected_line = lines[line_index].strip()

    explanation = explain_line(
        selected_line,
        lines
    )

    return {
        "line_number": request.line_number,
        "selected_line": selected_line,
        "explanation": explanation
    }