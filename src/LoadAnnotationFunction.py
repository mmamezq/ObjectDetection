import json

def LoadAnnotations(annotation_path):
    # Opening JSON file
    f = open(annotation_path)
    data = json.load(f)
    # Closing file
    f.close()
    return data