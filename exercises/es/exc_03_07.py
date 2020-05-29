import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

nlp = spacy.load("es_core_news_sm")
animals = ["Golden Retriever", "gato", "tortuga", "rata"]
animal_patterns = list(nlp.pipe(animals))
print("animal_patterns:", animal_patterns)
matcher = PhraseMatcher(nlp.vocab)
matcher.add("ANIMAL", None, *animal_patterns)

# Define el componente personalizado
def animal_component(doc):
    # Aplica el matcher al doc
    matches = ____
    # Crea un Span para cada resultado y asignales el label "ANIMAL"
    spans = [Span(____, ____, ___, label=____) for match_id, start, end in matches]
    # Sobrescribe los doc.ents con los spans resultantes
    doc.ents = spans
    return doc


# Añade el componente al pipeline después del componente "ner"
____.____(____, ____=____)
print(nlp.pipe_names)

# Procesa el texto e imprime en pantalla el texto y el label de los doc.ents
doc = nlp("Tengo un gato y un Golden Retriever")
print([(____, ____) for ent in ____])
