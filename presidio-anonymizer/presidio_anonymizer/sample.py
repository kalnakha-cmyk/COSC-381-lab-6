from presidio_anonymizer import AnonymizerEngine
from presidio_anonymizer.entities import RecognizerResult, OperatorConfig


def sample_run_anonymizer(text: str, entities: list, operators: dict = None):
    """
    Run the Presidio anonymizer with provided parameters.

    Args:
        text (str): The input text.
        entities (list): A list of dicts containing entity info with keys:
            - entity_type (str)
            - start (int)
            - end (int)
            - score (float, optional, default=0.8)
        operators (dict, optional): Mapping of entity types to OperatorConfig.
            Defaults to replacing PERSON entities with "BIP".

    Returns:
        AnonymizerResult: The anonymized result object.
    """
    engine = AnonymizerEngine()

    if operators is None:
        operators = {"PERSON": OperatorConfig("replace", {"new_value": "BIP"})}

    analyzer_results = [
        RecognizerResult(
            entity_type=e["entity_type"],
            start=e["start"],
            end=e["end"],
            score=e.get("score", 0.8),
        )
        for e in entities
    ]

    result = engine.anonymize(
        text=text,
        analyzer_results=analyzer_results,
        operators=operators,
    )

    return result


if __name__ == "__main__":
    # Run with a predefined example (no input)
    text = "My name is Bond."
    entities = [{"entity_type": "PERSON", "start": 11, "end": 15}]

    result = sample_run_anonymizer(text, entities)
    print(result)
