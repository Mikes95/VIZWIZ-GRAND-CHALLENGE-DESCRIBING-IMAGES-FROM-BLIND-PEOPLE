# VIZWIZ-GRAND-CHALLENGE-DESCRIBING-IMAGES-FROM-BLIND-PEOPLE

# Introduzione
L’obiettivo principale di questa challenge è quello facilitare alcuni aspetti della vitaquotidiana di persone cieche o ipovedenti. La challenge si articola in 3 punti principali:
•1. Dare didascalia ad immagini, scattate da persone cieche
•2. Rispondere a domande, poste da persone cieche, relative a foto da loro scattate.
•3. Riconoscere le differenze tra possibili risposte a domande relative a foto scattateda persone cieche.
## Installazione

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install skimage
pip install matplotlib
pip install pytesseract
pip install googlesearch
```

## Utilizzo

```python

with open('GLOBAL_PATH\val.json') as json_file:
    data = json.load(json_file)

pprint(data['images'][:1]) #Stampa la prima immagine nel file json con tutte le info contenute al suo interno
pprint(data['annotations'][:1]) #Stampa la prima didascalia nel json 

[founded.append(x) for x in data['annotations'] if x['image_id'] == selected_image['id']]#Cercare tutte le didascalie data un'immagine selezionata

#Estrarre il testo da un'immagine
text= pytesseract.image_to_string(brightness_contrast, config=custom_config)
d = pytesseract.image_to_data(brightness_contrast, output_type=Output.DICT)
print(text)
```
