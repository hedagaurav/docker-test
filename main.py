from fastapi import FastAPI


app = FastAPI(debug=True)

@app.get()
async def index():
  return {"message":"docker test project running"}