from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def home():
  return {"message" : "Hellllo"}

@app.get("/skill")
def skill(name : str):
  return {"skill" : name}
