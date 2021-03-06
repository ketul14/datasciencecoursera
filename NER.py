#########################################################################
# Title: Name Entity Recognize Using spaCy
#########################################################################

#########################################################################
# Loading packages
#########################################################################
import spacy
import pandas as pd
from spacy import displacy


#########################################################################
# Load Model
#########################################################################
nlp = spacy.load('<Your path to model or model name>')

#########################################################################
# Read from single string from Local File
#########################################################################
local = 1

if local == 1:
    path = '<Your directory path containing text file>'
    try:
        text = open(path).read()
    except UnicodeDecodeError:
        import codecs
        text = codecs.open(path, encoding='utf-8').read()

#########################################################################
# Read from multiple string from database
#########################################################################
local = 2
if local ==2:
    data = pd.read_csv("< CSV File containing dataframe")


#########################################################################
# Create empty dataframe
#########################################################################
df_ner = pd.DataFrame()
df_ner['Word'] = None
df_ner['Start_Char'] = None
df_ner['End_Char'] = None
df_ner['Label'] = None
df_ner['ID'] = int()
dd = {}
i = 0

#########################################################################
# Extract NER and append in dataframe
#########################################################################

if local ==2:
    for a in range(data.shape[0]):
        doc = nlp(data.C[a])
        for ent in doc.ents:
            if '\n' in ent.text:
                continue
            else:
                print(data.id[a])
                dd['ID'] = data.id[a]
                dd['Word'] = ent.text
                dd['Start_Char'] = ent.start_char
                dd['End_Char'] = ent.end_char
                dd['Label'] = ent.label_
                data = pd.DataFrame(dd, index=[i])
                df_ner = df_ner.append(data)
                i = i + 1
else:
        doc = nlp(text)
        for ent in doc.ents:
            if '\n' in ent.text:
                continue
            else:
                dd['ID'] = i
                dd['Word'] = ent.text
                dd['Start_Char'] = ent.start_char
                dd['End_Char'] = ent.end_char
                dd['Label'] = ent.label_
                data = pd.DataFrame(dd, index=[i])
                df_ner = df_ner.append(data)
                i = i + 1

#########################################################################
# Visualize ent
#########################################################################
if local ==1:
    displacy.serve(doc, style='ent')

#########################################################################
# Export back to CSV
#########################################################################
df_ner.to_csv("NER.csv")


#########################################################################
# Ends
#########################################################################
