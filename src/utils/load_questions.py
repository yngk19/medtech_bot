import json
import asyncio

async def load_questions():
    with open("../db/questions.json", "r") as f:
        questions = json.load(f)
        questions_list = list(questions.values())[0]
    return questions_list