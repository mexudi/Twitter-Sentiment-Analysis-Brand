import spacy

# Load the large English NLP model
nlp = spacy.load('en_core_web_lg')

# Iterate through each row of the dataframe
for index, row in df.iterrows():
    # Get the text from the 'text_column' column
    text = row['content']

    # Parse the text with spaCy. This runs the entire pipeline.
    doc = nlp(text)

    # Print out all the named entities that were detected:
    for entity in doc.ents:
        print(f"{entity.text} ({entity.label_})")
