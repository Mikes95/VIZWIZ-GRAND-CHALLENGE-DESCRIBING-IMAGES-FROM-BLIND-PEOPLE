import json
from pprint import pprint

from skimage import io
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure




with open('D:\\universita\\MAGISTRALE\\2-SEMESTRE\\COMPUTER VISION\\2020\\Blind\\annotations\\val.json') as json_file:
    data = json.load(json_file)


print('image')
pprint(data['images'][:1])
print('\n')
print('annotations')
pprint(data['annotations'][:1])


w=10
h=10
fig=plt.figure(figsize=(15, 15))
columns = 3
rows = 3
for i in range(1, columns*rows +1):
    selected_image= data['images'][i]
    image = io.imread(selected_image['vizwiz_url'])
    img = image
    
    

    fig.add_subplot(rows, columns, i)
    plt.title('Id: '+str(data['images'][i]['id']),fontsize=18, y=1)
    plt.imshow(img)
plt.show() 
selected_image= data['images'][63]

image = io.imread(selected_image['vizwiz_url'])
figure(num=None, figsize=(10, 8), dpi=80, facecolor='w', edgecolor='k')
plt.title('Esempio di immagine contenuta nel dataset',fontsize=24, y=1)
plt.imshow(image)
plt.show()

founded=[]
[founded.append(x) for x in data['annotations'] if x['image_id'] == selected_image['id']]

selected_caption=[]
label_caption=""
for item in founded:
    selected_caption.append(item['caption'])
    label_caption+=item['caption']+'\n'
    pprint(item['caption'])

textstr = label_caption

plt.text(0, 0, textstr, fontsize=5)

plt.subplots_adjust(left=0)

plt.imshow(image)
plt.show()