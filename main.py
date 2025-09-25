from pprint import pprint
from components.text_parser import parse_text
from components.world_model import get_world_model
from components.relationship_analyser import analyze_relationships


text = "Apple is in the box and the box is in the house and Alice is in the park"
parsed = parse_text(text)

pprint(parsed)

world_model = get_world_model(parsed)

print("\n World model")
pprint(world_model)

relationships = analyze_relationships(world_model)

print("\n Relationships")
pprint(relationships)
