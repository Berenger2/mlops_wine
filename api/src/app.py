from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse



app = FastAPI(
    title="FastAPI MLFlow",
    description="This is a simple FastAPI application with MLFlow.",
    version="0.1",
    docs_url="/docs",
    redoc_url=None
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.get("/hi", tags=["Root"])
def read_root():
    return {"message": "Hello World"}

