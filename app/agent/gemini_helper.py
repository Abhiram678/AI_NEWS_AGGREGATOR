import os
import json
from typing import Type, TypeVar, Optional
from pydantic import BaseModel
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

T = TypeVar('T', bound=BaseModel)


def call_gemini_with_schema(
    prompt: str,
    system_instruction: str,
    response_schema: Type[T],
    model_name: str = "gemini-2.5-flash",
    temperature: float = 0.7
) -> Optional[T]:
    """
    Call Gemini API with structured output using Pydantic schema.
    
    Args:
        prompt: The user prompt
        system_instruction: System instructions for the model
        response_schema: Pydantic model class for response validation
        model_name: Gemini model to use
        temperature: Temperature for generation
        
    Returns:
        Parsed Pydantic model instance or None on error
    """
    try:
        model = genai.GenerativeModel(
            model_name=model_name,
            generation_config={
                "temperature": temperature,
                "response_mime_type": "application/json"
            },
            system_instruction=system_instruction
        )
        
        # Create prompt with schema info
        schema_prompt = f"{prompt}\n\nRespond with JSON matching this schema: {response_schema.model_json_schema()}"
        
        response = model.generate_content(schema_prompt)
        
        # Parse JSON response into Pydantic model
        json_data = json.loads(response.text)
        return response_schema.model_validate(json_data)
        
    except Exception as e:
        print(f"Error calling Gemini API: {e}")
        return None
