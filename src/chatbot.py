
from src.knowledge_base import load_knowledge_base

class Chatbot:
    """
    The main chatbot class.
    """
    def __init__(self):
        self.knowledge_base = load_knowledge_base()

    def get_prognosis(self, symptoms):
        """
        Finds a matching condition from the knowledge base.
        """
        symptoms = [symptom.strip().lower() for symptom in symptoms.split(",")]
        
        best_match = None
        max_matching_symptoms = 0

        for condition in self.knowledge_base["conditions"]:
            matching_symptoms = len(set(symptoms) & set(condition["symptoms"]))
            if matching_symptoms > max_matching_symptoms:
                max_matching_symptoms = matching_symptoms
                best_match = condition
        
        return best_match

