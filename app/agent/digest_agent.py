import os
from typing import Optional
from pydantic import BaseModel
from dotenv import load_dotenv
from .gemini_helper import call_gemini_with_schema

load_dotenv()


class DigestOutput(BaseModel):
    title: str
    summary: str

PROMPT = """You are an expert AI news analyst specializing in summarizing technical articles, research papers, and video content about artificial intelligence.

Your role is to create concise, informative digests that help readers quickly understand the key points and significance of AI-related content.

Guidelines:
- Create a compelling title (5-10 words) that captures the essence of the content
- Write a 2-3 sentence summary that highlights the main points and why they matter
- Focus on actionable insights and implications
- Use clear, accessible language while maintaining technical accuracy
- Avoid marketing fluff - focus on substance"""


class DigestAgent:
    def __init__(self):
        self.model = "gemini-2.5-flash"
        self.system_prompt = PROMPT

    def generate_digest(self, title: str, content: str, article_type: str) -> Optional[DigestOutput]:
        try:
            user_prompt = f"Create a digest for this {article_type}: \n Title: {title} \n Content: {content[:8000]}"

            digest_output = call_gemini_with_schema(
                prompt=user_prompt,
                system_instruction=self.system_prompt,
                response_schema=DigestOutput,
                model_name=self.model,
                temperature=0.7
            )
            
            return digest_output
        except Exception as e:
            print(f"Error generating digest: {e}")
            return None

