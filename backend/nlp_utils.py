from transformers import pipeline

def analyze_statement(statement):
    nlp = pipeline("ner")  # Named Entity Recognition to identify policies or people
    results = nlp(statement)
    return results

if __name__ == "__main__":
    statement = "We will reduce taxes and increase infrastructure spending."
    print(analyze_statement(statement))
