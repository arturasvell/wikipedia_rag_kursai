import subprocess
import requests
from pydantic import BaseModel

class VerifiedResponse(BaseModel):
    enough_information:bool
    missing_concepts:list[str]
    confidence:float
    

def check_answer(query, answer):
    model_name = "gemma3"
    # Pull the desired model. WARNING: this implementation does not check your disk space, so be careful when running this
    print("Pulling %s model from Ollama...\n" % model_name)
    subprocess.run(["ollama", "pull", model_name], check=True)

    initial_prompt = f"You will get a query, and an answer. Please answer whether the information is enough. If it is not, list the missing concepts, and finally provide the confidence of your answer.\nQuery:{query}\nAnswer:{answer}"

    # prompting
    print("Running %s model...\n" % model_name)
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model_name,
            "prompt": initial_prompt,
            "stream": False,
            "format": VerifiedResponse.model_json_schema()
        }
    )

    if not response.ok:
        print("Error:", response.status_code)
        
    
    return VerifiedResponse.model_validate_json(response.json()["response"])