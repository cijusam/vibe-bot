# Medical Prognosis Chatbot

This is a simple proof-of-concept chatbot that provides a potential medical prognosis and service suggestion based on user-reported symptoms.

## How It Works

The chatbot uses a predefined knowledge base of medical conditions and their associated symptoms. When a user enters their symptoms, the chatbot attempts to find the best match in its knowledge base and provides the corresponding prognosis and suggested action.

## Project Structure

- `data/knowledge_base.json`: The knowledge base containing medical conditions.
- `src/main.py`: The main entry point for the command-line interface.
- `src/chatbot.py`: Contains the core logic for the chatbot.
- `src/knowledge_base.py`: A module for loading the knowledge base.

## Getting Started

### Prerequisites

- Python 3.6+

### Installation

No external libraries are needed for the current version.

### Running the Chatbot

To run the chatbot, execute the following command from the root of the project:

```bash
python -m src.main
```

## Disclaimer

This chatbot is for informational purposes only and is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.