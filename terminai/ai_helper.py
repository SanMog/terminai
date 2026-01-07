import json
import os
from openai import OpenAI
from typing import Optional


class AIHelper:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("API key not found.")

        # НАСТРОЙКА ПОД GROQ
        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.groq.com/openai/v1"
        )
        self.model = "llama-3.3-70b-versatile"

    def analyze_error(self, command: str, exit_code: int, stdout: str, stderr: str) -> dict:
        prompt = self._build_prompt(command, exit_code, stdout, stderr)

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a DevOps expert. Analyze errors and provide fixes in JSON."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)

        except Exception as e:
            return {"explanation": f"AI Error: {str(e)}", "fix_command": None}

    def _build_prompt(self, command: str, exit_code: int, stdout: str, stderr: str) -> str:
        # (Тут оставь тот же код метода _build_prompt, который был раньше)
        return f"""
Analyze this failed command.
Command: {command}
Error: {stderr[-1000:]}
Return JSON: {{"explanation": "...", "fix_command": "..."}}
"""