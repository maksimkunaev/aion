from pprint import pprint
from app.llm_client import LLMClient
from app.llm_task import LLMTask


client = LLMClient()
task = LLMTask(client)

example_graph = {
    "nodes": [{"id": "Алиса", "type": "person"}],
    "edges": [{"source": "Алиса", "relation": "заметила", "target": "Кролик"}],
}

text = "Алиса заметила Кролика с часами."
result = task.run_json_task(f"Построй граф знаний из текста: {text}", example_graph)

pprint(result)
