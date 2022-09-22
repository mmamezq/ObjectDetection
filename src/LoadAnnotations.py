import json
import mmtracking as m

# Opening JSON file
f = open(r'C:\Users\monic\mmdetection\mmtracking\data\tao\annotations-master\train_482_classes.json')
data = json.load(f)

print(json.dumps(data, indent=4))

print("Transformed TAO2COCO JSON Object Keys: ")
for key, value in data.items():
    print(key)

#print(data)
# Closing file
f.close()
