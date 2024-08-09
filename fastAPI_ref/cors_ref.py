from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS : Cross Origin Resource Sharing


app = FastAPI()

# Define the origins that should be allowed to make requests to your API
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://example.com",  # Replace with your frontend's origin
]
# origins = ['*']  # Allows all origins to be allowed


# Add the CORS middleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from the listed origins
    allow_credentials=True,  # Allows cookies to be included in requests
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get('/')
async def index():
    return {"message": "Learning about cors"}
