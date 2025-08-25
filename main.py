# Execution trigger
from src.llm.gpt_client import Config, OpenaigptClient

if __name__ == '__main__':
    model_conf = "./config/model_config.yaml"
    config = Config(model_conf)
    config = config.to_dict()

    instructions = ""
    model = config["chat_models"]["gpt-4o"]
    temperature = config["model_params"]["temperature"]

    openai_chat = OpenaigptClient(
        model=model,
        instructions=instructions,
        temperature=temperature
    )
    openai_chat.initialize_model()
    response = openai_chat.initialize_response()