import json

# Opening JSON file
f = open(r'C:\Users\monic\mmdetection\mmtracking\data\tao\annotations-master\train_482_classes.json')
data = json.load(f)
for i in range(len(data['categories'])):
    print(json.dumps(data['categories'][i]['id'], indent=4))

print("Transformed TAO2COCO JSON Object Keys: ")
for key, value in data.items():
    print(key)


# Checking if all category_id in annotations belong to id in categories

category_id = []
id = []
for i in range(len(data['annotations'])):
    category_id.append(data['annotations'][i]['category_id'])

for i in range(len(data['categories'])):
    id.append(data['categories'][i]['id'])


incorrect_categories = []
for val in category_id:
    if (val not in id):
        print(val not in id)
        incorrect_categories.append(val)

# Closing file
f.close()