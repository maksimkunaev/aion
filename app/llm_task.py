import json

from app.llm_client import LLMClient


class LLMTask:
    def __init__(self, client: LLMClient):
        self.client = client

    def run_json_task(
        self, instruction: str, example_schema: dict, model="llama-3.3-70b-versatile"
    ):
        """
        instruction: текстовое задание (например, 'Извлеки граф из текста')
        example_schema: пример JSON-ответа (dict), чтобы LLM понимала формат
        """
        prompt = f"""
Ты должен вернуть только JSON в следующем формате:
Пример:
{json.dumps(example_schema, ensure_ascii=False, indent=2)}

Задание: {instruction}
"""
        messages = [{"role": "user", "content": prompt}]
        output = self.client.chat(
            messages, model=model, response_format={"type": "json_object"}
        )
        try:
            return json.loads(output)
        except json.JSONDecodeError:
            raise ValueError("LLM вернула невалидный JSON")
