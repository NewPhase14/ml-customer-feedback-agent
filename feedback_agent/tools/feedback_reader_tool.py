from csv import DictReader
from pathlib import Path
from typing import List, TypedDict

class Feedback(TypedDict):
    id: int
    text: str

CSV_PATH = Path(__file__).resolve().parents[1] / "feedback.csv"

def query_feedback() -> List[Feedback]:
 feedback_store: List[Feedback] = []

 with open(CSV_PATH, encoding="utf-8") as csvfile:
    reader = DictReader(csvfile)
    for row in reader:
        feedback_store.append(
        {"id": int(row["id"]),
        "text": row["feedback"],
         })

    return feedback_store