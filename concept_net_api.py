import requests
import random

def main():
    """
    Used for testing the API
    """
    # # print the animals that are related to this thing
    # print(get_related_to("donkey"))
    # # call this if we need to categorize the current animal
    # print(get_classes_from_animal("cat"))
    # # call this if we need to find some new animal
    # #print(get_animals_from_class(get_classes_from_animal("donkey")[2]))

    # print(get_related_to("horse"))
    # # call this if we need to categorize the current animal
    # print(get_classes_from_animal("horse"))
    # # call this if we need to find some new animal
    # print(get_animals_from_class(get_classes_from_animal("horse")[0]))
   
    # print(get_object_from_class('big cat',[]))

    x = 'elephant'
    print(x)
    x = get_class_of_object(x,{})
    print(x)
    print(get_class_of_object(x,{}))
    print('##########')
    for i in ['dog','eagle','wolf','cat','insect','hawk','tiger','wolf']:
        print(get_class_of_object(i,{}))
        print(get_object_from_class(get_class_of_object(i,{}),{}))
        print(';;;;;;;;;')


    # x= get_class_of_object('lion')[0] 
    # print(get_object_from_class(x,[]))


def get_related_to(arg: str) -> list:
    """
    Given some animal, return animals that are related. This usually returns more specific animals.
    """
    lower_arg = arg.lower()
    response = requests.get(
        f"http://api.conceptnet.io/query?end=/c/en/{lower_arg}&rel=/r/IsA&limit=1000"
    )
    obj = response.json()
    animals = [edge["start"]["label"] for edge in obj["edges"]]
    return animals


def get_animals_from_class(cls: str) -> list:
    """
    Given some class, return the animals that belong to this class
    """
    lower_type = cls.lower()
    response = requests.get(
        f"http://api.conceptnet.io/query?end=/c/en/{lower_type}/n/wn/animal&rel=/r/IsA&limit=1000"
    )
    obj = response.json()
    animals = [edge["start"]["label"] for edge in obj["edges"]]
    return animals


def get_classes_from_animal(animal: str) -> list:
    """
    Given some animal, return the types
    """
    lower_type = animal.lower()
    response = requests.get(
        f"http://api.conceptnet.io/query?start=/c/en/{lower_type}/n/wn/animal&rel=/r/IsA&limit=1000"
    )
    obj = response.json()
    animals = [edge["end"]["label"] for edge in obj["edges"]]
    return animals

def get_class_of_object(object: str, dictofsaid):
    dictofsaid[object] = object
    obj = object.lower()
    objsearch = obj.replace(' ','_') 
    response = requests.get(f"http://api.conceptnet.io/c/en/{objsearch}?rel=/r/IsA&limit=1000")

    

    file = response.json()
    
    edges = list(filter(lambda edge: not(edge['surfaceText'] == None) and ("[[" + obj + "]] is related to " in edge['surfaceText'] or \
    "[[" + obj + "]] is a type of " in edge['surfaceText']),
     file['edges']))

    # second_label = None

    # for edge in edges:
    #     if 'sense_label' in edge['start'].keys() and edge['start']['label'] == obj and len(edge['start']['sense_label'].split(', ')) > 1:
    #         second_label = edge['start']['sense_label'].split(', ')[1]
    #         break

    #     if 'sense_label' in edge['end'].keys() and edge['end']['label'] == obj and len(edge['end']['sense_label'].split(', ')) > 1:
    #         second_label = edge['end']['sense_label'].split(', ')[1]
    #         break
    
    # labels = {}
    # for edge in edges: 
    #     if "sense_label" in edge["start"] and edge['start']['label'] == obj.lower():
    #         #print(edge["start"]["sense_label"])
    #         for label in edge["start"]["sense_label"].split(', '):
    #             if label in labels:
    #                 labels[label] += 1
    #             else:
    #                 labels[label] = 1

    #     if "sense_label" in edge["end"] and edge['end']['label'] == obj.lower():
    #         #print(edge["end"]["sense_label"])
    #         for label in edge["end"]["sense_label"].split(', '):
    #             if label in labels:
    #                 labels[label] += 1
    #             else:
    #                 labels[label] = 1



    #print('labels', labels.items())
    #classes = [(edge['end']['label'], edge['end']['sense_label']) if 'sense_label' in edge['end'].keys() else ('NOT NEEDED', 'NOT NEEDED') for edge in edges]
    weights = [edge['weight'] for edge in edges]
    #print('weights', weights)
    classes = [edge['end']['label'] for edge in edges]

    clss_labels = [edge['end']['sense_label'] if 'sense_label' in edge['end'].keys() else None for edge in edges]

    #print(classes)
    clss = classes[weights.index(max(weights))]

    curr_label = clss_labels[weights.index(max(weights))]

    #labels = dict(sorted(labels.items(), key = lambda x: x[1], reverse= True))
    
    
    ###IMPORTANT: the commented section above are multiple of Daniel's tries to make it more generalized using different attributes. Issues that keep on getting
    ###           run into are weird domain changes like eagle -> score (from golf)
    while (clss in dictofsaid or clss  == obj or curr_label is None or (not (clss == 'animal')) and (not 'animal' in curr_label)):# or (not first in curr_label) or (not second in curr_label)):
        weights.pop(weights.index(max(weights)))
        classes.pop(weights.index(max(weights)))
        clss_labels.pop(weights.index(max(weights)))
        curr_label = clss_labels[weights.index(max(weights))]
        clss = classes[weights.index(max(weights))]

    if clss[0:2] == "a " or clss[0:2] == "A ":
        clss = clss[2:]
    elif clss[0:3] == "an " or clss[0:3] == "An ":
        clss  = clss[3:]

    dictofsaid[clss] = clss
    
    return clss

def get_object_from_class(clss: str, dictofsaid):
    domain = clss.lower()
    file = requests.get(f"http://api.conceptnet.io/c/en/{domain.replace(' ','_')}?rel=/r/IsA&limit=1000")

    file = file.json()
    #str1 = "is related to " +  "[[" + domain + "]]"
    str2 = "is a type of " +  "[[" + domain + "]]"
    
    edges = list(filter(lambda edge: not(edge['surfaceText'] == None) and ('sense_label' in edge['start'].keys()) and 'animal' in edge['start']['sense_label'] 
    and not(edge['start']['label'] in dictofsaid.values()) and #(str1  in edge['surfaceText'] or \
    (str2 in edge['surfaceText']), file['edges']))
    lstofobjects = list(map(lambda edge: edge['start']['label'], edges))
    object_to_return = random.choice(lstofobjects)
    
    dictofsaid[object_to_return] = object_to_return
    
    return object_to_return

if __name__ == "__main__":
    main()