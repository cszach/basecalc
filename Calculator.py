# Command dictionary, used for the help command and the ? command

cmd_dict = {
    "help": "Show help.",
    "?": "Get help on a command. 1 argument required: name of the command. Example: \"? dec\"",
    "dec": "Convert a number to decimal. 2 arguments required: one is the number itself, second is the base.",
    "bin": "Convert a number to binary. 2 arguments required: one is the number itself, second is the base.",
    "oct": "Convert a number to octal. 2 arguments required: one is the number, second is the base.",
    "hex": "Convert a number to hexadecimal. 2 arguments required: one is the number, second is the base.",
    "input": "Input a number with its base, save it for later conversion 2 arguments required: the number itself and its base.",
    "->": "Convert the number entered upon the input command to another base. One argument required: the type you want to convert to. Example: \"-> hex\"",
    "exit": "Exit the calculator."
            }


def convert(in_cmd):
    if len(cmd.split()) >= 3:
        number = cmd.split()[1]
    try:
        base = int(cmd.split()[2])
        try:
            if in_cmd == "dec":
                answer = str(int(number, base))
            elif in_cmd == "bin":
                answer = bin(int(number, base))[2:]
            elif in_cmd == "oct":
                answer = oct(int(number, base))[2:]
            elif in_cmd == "hex":
                answer = hex(int(number, base))[2:].upper()
            print(">> " + answer)
        except ValueError:  # Number is not valid in the given base. i.e. Base 2 number 294
            print("Number is not correspond to its base.")
    except IndexError:  # Missing parameter
        print("No base given.")
    except ValueError:  # Base is invalid
        print("Invalid base.")


cmd = None
while cmd != "exit":
    cmd = input("> ")
    cmd = cmd.lower()
    try:
        main = cmd.split()[0] # Get command
        if main == "help":
            for command in cmd_dict:
                print(command + ": " + cmd_dict[command])
        elif main == "?":
            try:
                if cmd.split()[1] in cmd_dict:
                    print(cmd.split()[1] + ": " + cmd_dict[cmd.split()[1]])
                else:
                    print("No such command.")
            except IndexError:
                print("An argument is required.")
        elif main == "dec" or main == "bin" or main == "oct" or main == "hex":
            convert(main)
        elif main == "input":
            try:
                in_base = int(cmd.split()[2])
                try:
                    in_num = cmd.split()[1]
                    test = int(in_num, in_base)
                    del test
                except ValueError:
                    print("Number is not correspond to its base.")
            except IndexError:
                print("No base given.")
            except ValueError:
                print("Invalid base.")
        elif main == "->":
            try:
                target = cmd.split()[1]
                try:
                    if target == "dec":
                        print(">> " + str(int(in_num, in_base)))
                    elif target == "bin":
                        print(">> " + bin(int(in_num, in_base))[2:])
                    elif target == "oct":
                        print(">> " + oct(int(in_num, in_base))[2:])
                    elif target == "hex":
                        print(">> " + hex(int(in_num, in_base))[2:].upper())
                    else:
                        print("Invalid argument \"" + target + "\".")
                except NameError:
                    print("No input has been defined.")
            except IndexError:
                print("An argument is required.")
        elif cmd != "exit":
            print("Invalid command.")
    except IndexError: # If empty
        print("Empty input.")
