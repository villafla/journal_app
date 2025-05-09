from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def random_prompt_all():

    prompt = ["What happened today?", "What did I learn today?",
              "What was the most surprising thing that happened today?",
              "What was the most interesting thing I saw or heard today?",
              "What was the most surprising thing that happened today?",
              "What is one challenge or prompt that I can give myself to push myself creatively?",
              "Write a poem about a childhood memory that has stayed with you."
              "What are some things I would like to do differently tomorrow?",
              "Write about a character who wakes up one day with a superpower.",
              "Write a story about a character who discovers a mysterious book with a hidden message."
              ]
    num = random.randint(0, len(prompt) - 1)
    return prompt[num]


def random_prompt_daily():
    prompt = ["What happened today?", "What did I learn today?",
              "What was the most surprising thing that happened today?",
              "What was the most interesting thing I saw or heard today?",
              "What was the most surprising thing that happened today?",
              "What are some things I would like to do differently tomorrow?"
              ]
    num = random.randint(0, len(prompt) - 1)
    return prompt[num]


def random_prompt_creative():

    prompt = ["What is one challenge or prompt that I can give myself to push myself creatively?",
              "Write a poem about a childhood memory that has stayed with you.",
              "Write about a character who wakes up one day with a superpower.",
              "Write a story about a character who discovers a mysterious book with a hidden message.",
              ]
    num = random.randint(0, len(prompt) - 1)
    return prompt[num]


@app.get("/")
async def journal_prompt_all():
    return {"prompt": random_prompt_all()}


@app.get("/daily")
async def journal_prompt_daily():
    return {"prompt": random_prompt_daily()}


@app.get("/creative")
async def journal_prompt_creative():
    return {"prompt": random_prompt_creative()}
