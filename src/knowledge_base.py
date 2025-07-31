
import json
from pathlib import Path

def load_knowledge_base():
    """
    Loads the knowledge base from the JSON file.
    """
    base_path = Path(__file__).parent.parent 
    knowledge_base_path = base_path / "data" / "knowledge_base.json"
    with open(knowledge_base_path, "r") as f:
        return json.load(f)

