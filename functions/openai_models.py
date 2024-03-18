# Os and system imports
import os
import sys
sys.path.insert(0, '../')  # Go up one level from 'ats' to the 'source' folder
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv()) # read local .env file

# AI imports
from openai import OpenAI
from openai import APIConnectionError
client = OpenAI(api_key = os.environ['OPENAI_API_KEY'])


def generate_chat_completion(api_params):
    """
    Generates a chat completion using OpenAI's ChatGPT API.

    Parameters:
    - api_params (dict): All the parameters that the function should receive including optional values.

    Returns:
    - The response from the ChatGPT model or None if an error occurred.
    """

    try:
        # Call the OpenAI API with the dynamically constructed parameters
        chat_completion = client.chat.completions.create(**api_params)
        return chat_completion
    except APIConnectionError as e:
        print(f"An error occurred with the OpenAI API: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    return None


def calculate_embedding_original(input_text, model_type="small"):
    """
    Calculates the embedding of the given text input using a specific model based on the model type specified.
    
    Parameters:
    - input_text (str): The text input for which the embedding will be calculated.
    - model_type (str): The type of the model to be used for calculating embeddings. 
                        Accepts 'long' for larger models and 'short' for smaller models. Defaults to 'long'.
    
    Returns:
    - Dict[str, Any]: A dictionary containing the embedding data.
    
    Raises:
    - Exception: If an error occurs during the embedding process.
    """
    
    # Determine the model based on the model_type parameter
    model = "text-embedding-3-small" if model_type == "small" else "text-embedding-3-large"
    
    try:
        embedding = client.embeddings.create(
            input=input_text,
            model=model
        )
        return embedding.data[0].embedding
    except Exception as e:
        # Log the exception or handle it as needed
        raise Exception(f"Failed to calculate embedding: {e}")


def openai_embedding(input_text, model_type="small"):
    """
    Calculates the embedding of the given text input using a specific model based on the model type specified.
    
    Parameters:
    - input_text (str): The text input for which the embedding will be calculated.
    - model_type (str): The type of the model to be used for calculating embeddings. 
                        Accepts 'long' for larger models and 'short' for smaller models. Defaults to 'long'.
    
    Returns:
    - Dict[str, Any]: A dictionary containing the embedding data.
    
    Raises:
    - Exception: If an error occurs during the embedding process.
    """
    # Determine the model based on the model_type parameter
    model = "text-embedding-3-small" if model_type == "small" else "text-embedding-3-large"
    
    try:
        embedding = client.embeddings.create(
            input=input_text,
            model=model
        )
        return embedding
    except Exception as e:
        # Log the exception or handle it as needed
        raise Exception(f"Failed to calculate embedding: {e}")


def calculate_embedding(input_text, model_type="small"):
    return openai_embedding(input_text, model_type="small").data[0].embedding