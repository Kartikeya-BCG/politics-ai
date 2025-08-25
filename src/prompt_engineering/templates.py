from utils.config import Config

class PromptTemplate:
    def __init__(self):
        prompt_template = "./config/prompt_template.yaml"
        config = Config(prompt_template)
        config = config.to_dict()
        
        self.input_format = [
            {
                "role": "developer",
                "content": f"""
                            You are a political expert. You job is to answer only politics related questions asked by the user.
                            If question is not related to politics & diplomacy, then don't answer the questions and respond with the following message:
                            {config["system_static_prompts"]["no_answer"]}\n
                            Close the response by below sentence:
                            {config["system_static_prompts"]["closing_sentence"]}.
                            """
            },
            {
                "role": "assistant",
                "content": f"""{config["system_static_prompts"]["starting_sentence"]}"""
            }
        ]

# Example Usage
# prompt_template = PromptTemplate()
# print(prompt_template.input_format)