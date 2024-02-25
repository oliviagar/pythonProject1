def test_husband_requirements():
    print("Hello, welcome to the husband requirements test\n")
    answer = input("Who's husband requirements would you like to be tested on?\n" + "Oli, Nati, Hanna or Vale?\n\n").lower()

    if answer in ["oli", "olivia", "o"]:
        tall = input("Are you taller than Oli?\n")
        if tall in ["yes", "Yes", "Y", "y"]:
            athletic = input("Are you athletic?\n")
            if athletic in ["yes", "Yes", "Y", "y"]:
                stable = input("Are you emotionally stable\n")
                if stable in ["yes", "Yes", "Y", "y"]:
                    rich = input("Are you rich AF?\n")
                    if rich in ["yes", "Yes", "Y", "y"]:
                        shoulders = input("Do you have broad shoulders?\n")
                        if shoulders in ["yes", "Yes", "Y", "y"]:
                            latino = input("Are you latino?\n")
                            if latino in ["yes", "Yes", "Y", "y"]:
                                print("Congrats, you qualify to be Oli's husband!!")
                            else:
                                print("Sorry, you don't qualify")
                        else:
                            print("Sorry, you don't qualify")
                    else:
                        print("Sorry, you don't qualify.")
                else:
                    print("Sorry, you don't qualify.")
            else:
                print("Sorry, you don't qualify.")
        else:
            print("Sorry, you don't qualify.")
    elif answer in ["nati", "n", "natalia"]:
        smoke = input("Do you smoke?\n")
        if smoke in ["no", "n"]:
            family = input("Are you close to your family?\n")
            if family in ["yes", "y"]:
                hoe = input("Are you a retired hoe?\n")
                if hoe in ["yes", "y"]:
                    jewelry = input("Do you wear jewelry (rings, bracelets, and necklaces?\n")
                    if jewelry in ["yes", "y"]:
                        gym = input("Do you workout?\n")
                        if gym in ["yes", "y"]:
                            print("Congrats, you qualify to be Nati's husband!!")
                        else:
                            print("Sorry, you don't qualify")
                    else:
                        print("Sorry, you don't qualify.")
                else:
                    print("Sorry, you don't qualify.")
            else:
                print("Sorry, you don't qualify.")
        else:
            print("Sorry, you don't qualify.")
    elif answer in ["hanna", "hann"]:
        european = input("Are you European?\n")
        if european in ["yes", "y"]:
            f1 = input("Are you an Formula One fan?\n")
            if f1 in ["yes", "y"]:
                coffee = input("Do you like coffee?\n")
                if coffee in ["yes", "y"]:
                    glasses = input("Do you wear glasses?\n")
                    if glasses in ["yes", "y"]:
                        cook = input("Are you a good cook?\n")
                        if cook in ["yes", "y"]:
                            print("Congrats, you qualify to be Hanna's husband!!")
                        else:
                            print("Sorry, you don't qualify")
                    else:
                        print("Sorry, you don't qualify.")
                else:
                    print("Sorry, you don't qualify.")
            else:
                print("Sorry, you don't qualify.")
        else:
            print("Sorry, you don't qualify.")
    elif answer in ["vale", "v"]:
        european = input("Are you European?\n")
        if european in ["yes", "y"]:
            f1 = input("Are you an Formula One fan?\n")
            if f1 in ["yes", "y"]:
                coffee = input("Do you like coffee?\n")
                if coffee in ["yes", "y"]:
                    glasses = input("Do you wear glasses?\n")
                    if glasses in ["yes", "y"]:
                        cook = input("Are you a good cook?\n")
                        if cook in ["yes", "y"]:
                            print("Congrats, you qualify to be Vale's husband!!")
                        else:
                            print("Sorry, you don't qualify")
                    else:
                        print("Sorry, you don't qualify.")
                else:
                    print("Sorry, you don't qualify.")
            else:
                print("Sorry, you don't qualify.")
        else:
            print("Sorry, you don't qualify.")
    else:
        print("Invalid input. Please choose Oli, Nati, Hanna, or Vale.")


def start_again():
    restart = input("Would you like to restart? Type 'start' to begin again, or any other key to exit.\n").lower()
    if restart == "start":
        test_husband_requirements()


# Call the main function to start the program
test_husband_requirements()
start_again()