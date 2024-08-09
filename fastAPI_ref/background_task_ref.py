from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()


# Define the background task function
def background_task(name: str):
    time.sleep(5)  # Simulate a time-consuming task
    print(f"Hello {name}, your background task is complete!")


# Define the endpoint that triggers the background task
@app.post("/send-email/")
async def send_email(email: str, background_tasks: BackgroundTasks):
    # Add the background task
    background_tasks.add_task(background_task, email)
    return {"message": "Email will be sent in the background"}
