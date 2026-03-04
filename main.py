from fastapi import FastAPI
import random

app = FastAPI()

questions = [
    "Mi volt a legkínosabb pillanatod?",
    "Ki tetszik most titokban?",
    "Mi a legnagyobb félelmed?",
    "Mi volt a legfurcsább álmod?"
]

dares = [
    "Írj egy szerelmes üzenetet valakinek.",
    "Küldj egy random emojit.",
    "Írj egy vicces mondatot."
]

@app.get("/")
def home():
    return {"message": "Truth or Dare API működik"}

@app.get("/random-question")
def random_question():
    return {"question": random.choice(questions)}

@app.get("/random-dare")
def random_dare():
    return {"dare": random.choice(dares)}