import LoadAnnotationFunction as laf

data = laf.LoadAnnotations(r'../data/annotations/train_482_classes.json')
print("Display First Category \n", data['categories'][0])
print("Display First Annotation: \n",data['annotations'][0])

