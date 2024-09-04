from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/calculate/{operation}")
async def calculate(operation : str, num1 : float, num2 : float):
    if operation == "add":
        result = num1 + num2
    elif operation == "substract":
        result = num1 - num2
    else:
        return {"error" : "Invalid operation. Please use 'add' or 'substract'."}
    return {"operation" : operation, "num1" : num1, "num2" : num2, "result" : result}

import uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)