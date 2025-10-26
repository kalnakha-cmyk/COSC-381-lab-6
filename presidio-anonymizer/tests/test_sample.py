import pytest
from presidio_anonymizer.sample import sample_run_anonymizer

def test_sample_run_anonymizer():
    text = "My name is Bond."
    entities = [{"entity_type": "PERSON", "start": 11, "end": 15}]

    result = sample_run_anonymizer(text, entities)

    # Check anonymized text
    assert result.text == "My name is BIP."

    # Check items structure
    assert len(result.items) == 1
    item = result.items[0]

    assert item.entity_type == "PERSON"
    assert item.text == "BIP"
    assert item.start == 11
    assert item.end == 14  
    assert item.operator == "replace"