
import json
from pathlib import Path

def load_questions() -> list[dict]:
    data_path = Path(__file__).resolve().parent.parent / "data" / "questions.json"
    
    with open(data_path, "r", encoding="utf-8") as file:
        return json.load(file)