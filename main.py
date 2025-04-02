from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

client = OpenAI(
    api_key="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"
)

@app.post("/ask")
async def ask_openai(question_data: Question):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {"role": "user", "content": question_data.question}
        ]
    )
    return completion.choices[0].message.content