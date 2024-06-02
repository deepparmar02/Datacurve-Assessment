# main.py
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from pydantic import BaseModel
from CodeSubmission import CodeSubmissionModel
import subprocess
import uuid
import os

# Initialize the database
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Initialize fastapi backend service
app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend's origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DEFAULT_OUTPUT = "Code compiled successfully!"
DEFAULT_FILE_NAME = "python_code_executer"

class CodeRequest(BaseModel):
    code: str

@app.post("/api/execute")
async def execute_code(request: CodeRequest):
    print("hit")
    try:
        # Save code to a temporary file
        code_file = f"/tmp/{DEFAULT_FILE_NAME}.py"
        with open(code_file, "w") as file:
            file.write(request.code)
        
        # Execute the code and capture the output
        result = subprocess.run(["python3", code_file], capture_output=True, text=True, timeout=5)
        print(result)
        os.remove(code_file)  # Clean up the temporary file
            
        # Invalid code
        if result.returncode != 0:
            return {"result": result.stderr}
        
        result_output = result.stdout if len(result.stdout) > 0 else DEFAULT_OUTPUT
        return {"result": result_output}
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=400, detail="Code execution timed out")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/submit")
async def submit_code(request: CodeRequest, db: Session = Depends(get_db)):
    try:
        # Save code to a temporary file
        code_file = f"/tmp/{DEFAULT_FILE_NAME}.py"
        with open(code_file, "w") as file:
            file.write(request.code)
        
        # Execute the code and capture the output
        result = subprocess.run(["python3", code_file], capture_output=True, text=True, timeout=5)
        os.remove(code_file)  # Clean up the temporary file

        # Invalid code
        if result.returncode != 0:
            return {"result": result.stderr}

        # Create a new code submission record
        code_submission = CodeSubmissionModel(code=request.code, result=result.stdout)
        db.add(code_submission)
        db.commit()
        db.refresh(code_submission)

        return {"result": f"Code submitted successfully with ID: {code_submission.id}"}
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=400, detail="Code execution timed out")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))