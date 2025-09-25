from app.llm_client import LLMClient
from app.llm_task import LLMTask
from constants.relationships import ALLOWED_RELATIONS

example_graph = {
    "nodes": [{"id": "Алиса", "type": "person"}],
    "edges": [{"source": "Алиса", "relation": "заметила", "target": "Кролик"}],
}


def parse_text(
    text: str,
    example_graph: dict = example_graph,
    allowed_relations: list = ALLOWED_RELATIONS,
) -> dict:
    """
    TextParser: принимает текст и возвращает граф знаний
    с ограничением на список допустимых отношений.
    """
    client = LLMClient()
    task = LLMTask(client)

    # формируем Prompt с жёстким ограничением по отношениям
    allowed_str = ", ".join(allowed_relations)
    prompt = (
        f"Построй граф знаний из текста: {text}\n"
        f"Используй только следующие отношения: {allowed_str}.\n"
        f"Не придумывай других отношений."
    )

    result = task.run_json_task(prompt, example_graph)
    return result
