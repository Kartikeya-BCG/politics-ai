import os
from dotenv import load_dotenv
from openai import OpenAI
from utils.config import Config
from prompt_engineering.templates import PromptTemplate

load_dotenv()

class OpenaigptClient(PromptTemplate):
    def __init__(self, model: str, instructions: str, temperature: float):
        super().__init__()
        self.api_key = os.environ.get("OPENAI_API_KEY")
        self.model = model
        self.instructions = instructions
        self.input = self.input_format
        self.temperature = temperature

    def initialize_model(self) -> OpenAI:
        client = OpenAI(
            api_key=self.api_key,
            timeout=10
        )

        return client
    
    def initialize_response(self):
        client = self.initialize_model()
        conversation = self.input
        print("***** ", conversation[1]["content"], " *****\n")

        while True:
            
            user_inp = input("\n")

            # Exit condition
            if user_inp.strip().lower() == 'quit':
                print("Got it! Ending the conversation. It's nice talking to you. Have a great day!")
                break
            
            conversation.append({
                "role": "user",
                "content": user_inp
            })

            response = client.responses.create(
                model=self.model,
                instructions=self.instructions,
                input=conversation,
                temperature=self.temperature
            )
            
            # Extract assistant reply
            reply = response.output_text
            print(f"\nAssistant: {reply}")

            # Append assistant response to conversation
            conversation.append({"role": "assistant", "content": reply})
