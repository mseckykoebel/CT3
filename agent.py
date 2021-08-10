import random
from gpt_api import (
    get_animal,
    get_single_why,
    get_comparison_why,
    get_insane_comparison_why,
    random_name_generator,
)
from concept_net_api import (
    get_class_of_object,
    get_object_from_class,
    get_related_to,
    get_animals_from_class,
    get_classes_from_animal,
)


class Agent:
    def __init__(self) -> None:
        self.name = random_name_generator()
        if ":" in self.name:
            self.name = self.name[:-1]
        self.current_animal = None
        self.animal_dict = {}
        self.insane_comparison = False
        self.cn_loop_check = 0

    def _get_name(self) -> str:
        return self.name

    def _get_current_animal(self) -> None:
        return self.current_animal

    def _set_current_animal(self, animal: str) -> None:
        self.current_animal = animal

    def generate_what_gpt(self):
        while True:
            what_animal = "".join(get_animal().strip()).lower()
            if what_animal != None or len(what_animal) >= 5:
                if what_animal not in self.animal_dict:
                    # print("WHAT ANIMAL:", what_animal)
                    return what_animal
                self.animal_dict[what_animal] = what_animal
            continue

    def generate_what_concept_net(self, animal: str) -> str:
        """
        Generates an animal that is similar to the argument animal via concept net
        """
        #print('the animal is',animal)
        # print("animal:", animal)
        query = get_classes_from_animal("".join(animal.split()[-1]).strip())
        # print(query)
        #print('query', query)
        for i in range(len(query)):
            if query[i] is not None:
                # ASSUMES THAT THIS IS GOING TO RETURN SOMETHING
                if len(get_animals_from_class(query[i])) > 1:
                    concept_net_response: str = random.choice(
                        get_animals_from_class(query[i])
                    )
                    print("CN!")
                    self.insane_comparison = False
                    self.cn_loop_check += 1
                    if self.cn_loop_check > 10:
                        
                        self.cn_loop_check = 0
                        break

                    clss = concept_net_response.strip()
                    if clss[0:2] == "a " or clss[0:2] == "A ":
                        clss = clss[2:]
                    elif clss[0:3] == "an " or clss[0:3] == "An ":
                        clss  = clss[3:]

                    return clss
        
        try:
            print('going through class hierarchy!')
            #getting the class from the object
            clss = get_class_of_object(animal.split()[-1], self.animal_dict)
            print('curr class:', clss)
            clss = get_class_of_object(clss, self.animal_dict)
            print('higher class:', clss)
            obj = get_object_from_class(clss, self.animal_dict)
            
            try:
                obj2 = get_object_from_class(obj, self.animal_dict)
                print('lower class:', obj)
                
                if obj2[0:2] == "a " or obj2[0:2] == "A ":
                        obj2 = obj2[2:]
                elif obj2[0:3] == "an " or obj2[0:3] == "An ":
                    obj2  = obj2[3:]

                print('new object from lower class:', obj2)

                return obj2.strip()
            except:
            #print(f"animal: {animal}, class: {clss}, new obj: {obj}")
            #print('\n\n\n\n')
                

                if obj[0:2] == "a " or obj[0:2] == "A ":
                    obj = obj[2:]
                elif obj[0:3] == "an " or obj[0:3] == "An ":
                    obj  = obj[3:]

                print('new object from higher class:', obj)

                return obj.strip()
        except:
            pass
        
        
        # if this does not work, rely on GPT to get the next animal:
        
        fallback = self.generate_what_gpt()
        while (chr(65533) in fallback) or (not fallback.isalpha()):
            fallback = self.generate_what_gpt()
        # UN-COMMENT THIS TO MAKE MORE CREATIVE - MIGHT BACKFIRE SO USE w/ CAUTION
        # self.insane_comparison = True
        print("GPT!")
        clss = fallback
        if clss[0:2] == "a " or clss[0:2] == "A ":
            clss = clss[2:]
        elif clss[0:3] == "an " or clss[0:3] == "An ":
            clss  = clss[3:]

        return clss

    def generate_why_sentence(self) -> str:
        """
        Generate a why sentence based on the current animal
        """
        return get_single_why(self.current_animal)

    def generate_why_sentence_comparison(self, animal_1: str, animal_2: str) -> str:
        return get_comparison_why(animal_1, animal_2)

    def generate_insane_why_sentence_comparison(
        self, animal_1: str, animal_2: str
    ) -> str:
        return get_insane_comparison_why(animal_1, animal_2)
