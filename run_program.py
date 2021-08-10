from agent import Agent


def main():
    # define agents
    agent_1 = Agent()
    agent_2 = Agent()
    # keep track of iterations and animals mentioned
    iterations = 0
    num_iterations = 12
    animal_dict = {}
    while iterations < num_iterations:
        agent_1_name = agent_1._get_name()
        agent_2_name = agent_2._get_name()
        # if the first run
        if iterations == 0:
            # all of the while loops check for instances where the animal that has been brought up exists in the dict
            # and, if it does, just continue
            while True:
                # agent 1 gets a brand new animal. do the dictionary checks for all of these
                agent_1._set_current_animal(agent_1.generate_what_gpt())
                agent_one_animal = agent_1._get_current_animal()
                # print(agent_one_animal, "IS THE ANIMAL")
                if agent_one_animal not in animal_dict:
                    print(
                        f"{agent_1_name}: I think the best pet is the {agent_one_animal}.{agent_1.generate_why_sentence()}"
                    )
                    animal_dict[agent_one_animal] = agent_one_animal
                    break
                else:
                    continue
            while True:
                # give agent two some new animal. this is based on agent 1's previous animal
                agent_2._set_current_animal(
                    agent_2.generate_what_concept_net(agent_1._get_current_animal())
                )
                agent_two_animal = agent_2._get_current_animal()
                if agent_two_animal not in animal_dict:
                    if agent_2.insane_comparison:
                        print(
                        f"{agent_2_name}: Well I think the best pet is the {agent_two_animal}.{agent_2.generate_insane_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
                        )
                    else:
                        print(
                            f"{agent_2_name}: Well I think the best pet is the {agent_two_animal}.{agent_2.generate_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
                        )
                    animal_dict[agent_two_animal] = agent_two_animal
                    break
                else:
                    continue
        # if not we can just run through
        else:
            while True:
                # agent 1 gets a brand new animal
                # print("AGENT 1\n")
                agent_1._set_current_animal(
                    agent_1.generate_what_concept_net(agent_2._get_current_animal())
                )
                agent_one_animal = agent_1._get_current_animal()
                if agent_one_animal not in animal_dict:
                    if agent_1.insane_comparison:
                        print(
                            f"{agent_1_name}: How about the {agent_one_animal}.{agent_1.generate_insane_why_sentence_comparison(agent_2._get_current_animal(), agent_1._get_current_animal())}"
                        )
                    else:
                        print(
                            f"{agent_1_name}: How about the {agent_one_animal}.{agent_1.generate_why_sentence_comparison(agent_2._get_current_animal(), agent_1._get_current_animal())}"
                        )
                    animal_dict[agent_one_animal] = agent_one_animal
                    break
                else:
                    continue
            while True:
                agent_2._set_current_animal(
                    agent_2.generate_what_concept_net(agent_1._get_current_animal())
                )
                agent_two_animal = agent_2._get_current_animal()
                # print("AGENT 2\n")
                # give agent two some new animal. this is based on agent 1's previous animal
                if agent_two_animal not in animal_dict:
                    if agent_2.insane_comparison:
                        print(
                            f"{agent_2_name}: What about the {agent_two_animal}.{agent_2.generate_insane_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
                        )
                    else:
                        print(
                            f"{agent_2_name}: What about the {agent_two_animal}.{agent_2.generate_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
                        )
                    animal_dict[agent_two_animal] = agent_two_animal
                    break
                else:
                    continue
        # iterate
        iterations += 1


if __name__ == "__main__":
    main()

"""
while iterations < num_iterations:
        agent_1_name = agent_1._get_name()
        agent_2_name = agent_2._get_name()
        # if the first run
        if iterations == 0:
            # all of the while loops check for instances where the animal that has been brought up exists in the dict
            # and, if it does, just continue
            while True:
                # agent 1 gets a brand new animal. do the dictionary checks for all of these
                agent_1._set_current_animal(agent_1.generate_what_gpt())
                agent_one_animal = agent_1._get_current_animal()
                # print(agent_one_animal, "IS THE ANIMAL")
                if agent_one_animal not in animal_dict:
                    print(
                        f"{agent_1_name}: I think the best pet is the {agent_one_animal}.{agent_1.generate_why_sentence()}"
                    )
                    animal_dict[agent_one_animal] = agent_one_animal
                    break
                else:
                    continue
            while True:
                # give agent two some new animal. this is based on agent 1's previous animal
                agent_2._set_current_animal(
                    agent_2.generate_what_concept_net(agent_1._get_current_animal())
                )
                agent_two_animal = agent_2._get_current_animal()
                if agent_two_animal not in animal_dict:
                    if agent_2.insane_comparison:
                        print(
                        f"{agent_2_name}: Well I think the best pet is the {agent_two_animal}.{agent_2.generate_insane_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
                        )
                    else:
                        print(
                            f"{agent_2_name}: Well I think the best pet is the {agent_two_animal}.{agent_2.generate_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
                        )
                    animal_dict[agent_two_animal] = agent_two_animal
                    break
                else:
                    continue
        # if not we can just run through
        else:
            while True:
                # agent 1 gets a brand new animal
                # print("AGENT 1\n")
                agent_1._set_current_animal(
                    agent_1.generate_what_concept_net(agent_2._get_current_animal())
                )
                agent_one_animal = agent_1._get_current_animal()
                if agent_one_animal not in animal_dict:
                    if agent_1.insane_comparison:
                        print(
                            f"{agent_1_name}: How about the {agent_one_animal}.{agent_1.generate_insane_why_sentence_comparison(agent_2._get_current_animal(), agent_1._get_current_animal())}"
                        )
                    else:
                        print(
                            f"{agent_1_name}: How about the {agent_one_animal}.{agent_1.generate_why_sentence_comparison(agent_2._get_current_animal(), agent_1._get_current_animal())}"
                        )
                    animal_dict[agent_one_animal] = agent_one_animal
                    break
                else:
                    continue
            while True:
                agent_2._set_current_animal(
                    agent_2.generate_what_concept_net(agent_1._get_current_animal())
                )
                agent_two_animal = agent_2._get_current_animal()
                # print("AGENT 2\n")
                # give agent two some new animal. this is based on agent 1's previous animal
                if agent_two_animal not in animal_dict:
                    if agent_2.insane_comparison:
                        print(
                            f"{agent_2_name}: What about the {agent_two_animal}. {agent_2.generate_insane_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
                        )
                    else:
                        print(
                            f"{agent_2_name}: What about the {agent_two_animal}. {agent_2.generate_why_sentence_comparison(agent_1._get_current_animal(), agent_2._get_current_animal())}"
                        )
                    animal_dict[agent_two_animal] = agent_two_animal
                    break
                else:
                    continue
        # iterate
        iterations += 1
"""