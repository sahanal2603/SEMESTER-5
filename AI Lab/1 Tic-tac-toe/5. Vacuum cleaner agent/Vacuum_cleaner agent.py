# Locations: A and B
# Status of locations: 0 for clean and 1 for dirty
# Goal state: A -> 0 and B -> 0

def vacuum_world():
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    location_input = input("Enter location of Vacuum (A or B): ")
    print("")
    status_input = input("Enter status of " + location_input + " (0 ->clean and 1 ->dirty): ")
    print("")
    status_input_complement = input("Enter status of other room (0 ->clean and 1 ->dirty): ")
    print("")
    print("")


    if location_input == 'A':
        print("Vacuum is in Location A.")
        print("")
        if status_input == '1':
            print("Location A is Dirty.")
            print("")
            print("Action: Suck dirt")
            print("")
            goal_state['A'] = '0'
            cost += 1
            print("Cost: " + str(cost))
            print("")
            print("Location A is cleaned.")
            print("")

            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("")
                print("Action: Move Right to Location B")
                print("")
                cost += 1
                print("Cost: " + str(cost))
                print("")
                print("Action: Suck dirt")
                print("")
                goal_state['B'] = '0'
                cost += 1
                print("Cost: " + str(cost))
                print("")
                print("Location B is cleaned.")
                print("")
            else:
                print("Location B is already Clean.")
                print("")
                print("No action")
                print("")

        if status_input == '0':
            print("Location A is already clean.")
            print("")
            if status_input_complement == '1':
                print("Location B is Dirty.")
                print("")
                print("Action: Move Right to Location B")
                print("")
                cost += 1
                print("Cost: " + str(cost))
                print("")
                print("Action: Suck dirt")
                print("")
                goal_state['B'] = '0'
                cost += 1
                print("Cost: " + str(cost))
                print("")
                print("Location B is cleaned.")
                print("")
            else:
                print("Location B is already Clean.")
                print("")
                print("No action")
                print("")

        
    else:
        print("Vacuum is in Location B.")
        print("")
        if status_input == '1':
            print("Location B is Dirty.")
            print("")
            print("Action: Suck dirt")
            print("")
            goal_state['B'] = '0'
            cost += 1
            print("Cost: " + str(cost))
            print("")
            print("Location B is cleaned.")
            print("")

            if status_input_complement == '1':
                print("Location A is Dirty.")
                print("")
                print("Action: Move Left to Location A")
                print("")
                cost += 1
                print("Cost: " + str(cost))
                print("")
                print("Action: Suck dirt")
                print("")
                goal_state['A'] = '0'
                cost += 1
                print("Cost: " + str(cost))
                print("")
                print("Location A is cleaned.")
                print("")
            else:
                print("Location A is already Clean.")
                print("")
                print("No action")
                print("")

        if status_input == '0':
            print("Location B is already clean.")
            print("")
            if status_input_complement == '1':
                print("Location A is Dirty.")
                print("")
                print("Action: Move Left to Location A")
                print("")
                cost += 1
                print("Cost: " + str(cost))
                print("")
                print("Action: Suck dirt")
                print("")
                goal_state['A'] = '0'
                cost += 1
                print("Cost: " + str(cost))
                print("")
                print("Location A is cleaned.")
                print("")
            else:
                print("Location A is already Clean.")
                print("")
                print("No action")
                print("")


    print("")
    print("GOAL STATE: " + str(goal_state))
    print("")
    print("Performance measurement: " + str(cost))



vacuum_world()
    

        
