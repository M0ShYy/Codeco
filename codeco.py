from fonctions import *
import sys
import getopt

"""from timeit import default_timer as timer"""
global info, encode, decode, text, method, key
# Options
options = "ha:m:i:k:"
# Long options
long_options = ["help", "action =", "methode =", "input =", "key ="]


# list of the characters available


def infos():
    global info
    info = True
    return ("codeco.py\n"
            "OPTION\n"
            "-h   --help      <Show this page>\n"
            "-a   --action    <encode/decode>      \n"
            "-m   --methode   <methode of decode/encode>(ascii_key, ascii, keyed, alphanumeric, caesar)\n"
            "-i   --input     <the secret or the code>\n"
            "-k   --key       <key if necessary>\n"
            "\n"
            "\n"
            "EXAMPLES:\n"
            "codeco.py -e -m caesar -i secret\n"
            "codeco.py -h\n"
            "\n"
            "SEE THE MAN PAGE https://github.com/M0ShYy/Codeco FOR MORE OPTIONS AND EXAMPLES\n")


def main(argumentlist):
    global info, encode, decode, text, method, key
    info = False
    try:
        arguments, values = getopt.getopt(argumentlist, options, long_options)

        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):  # test if there is -h or --help
                print(infos())  # print help

            elif currentArgument in ("-a", "--action "):  # test if there is -a or --action
                if currentValue == "encode":
                    print("encode")
                    encode = True
                    decode = False
                elif currentValue == "decode":
                    print("decode")
                    decode = True
                    encode = False
                else:
                    print('please input ONLY encode or decode')
            elif currentArgument in ("-m", "--method "):  # test if there is -m --method
                method = currentValue  #
            elif currentArgument in ("-i", "--input "):  # test if there is -i or --input
                text = currentValue  #
            elif currentArgument in ("-k", "--key "):  # test if there is -i or --input
                key = currentValue  #
        if not info:  # if the help was not printed then
            if encode != decode:
                if method == "alphanumeric":
                    if encode:
                        print('coded text: ' + str(code_alphanumeric(text)))
                    elif decode:
                        print('decoded text: ' + str(decode_alphanumeric(text)))
                elif method == "caesar":
                    if encode:
                        print('coded text: ' + code_caesar(text))
                    elif decode:
                        print('decoded text: ' + decode_caesar(text))
                elif method == "keyed":
                    if encode:
                        print('coded text: ' + code_keyed(text, key))
                    elif decode:
                        print('decoded text: ' + code_keyed(text, key))
                elif method == "ascii":
                    if encode:
                        print('coded text: ' + code_ascii(text))
                    elif decode:
                        print('decoded text: ' + decode_ascii(text))
                elif method == "ascii_key":
                    if encode:
                        print('coded textascii: ' + code_ascii_key(text, key))
                    elif decode:
                        print(decode_ascii_key(text, key))
            else:
                print("You have to chose ONLY ONE action")
    except getopt.error as err:  # if there is an error
        # output error, and return with an error code
        print(str(err))  # print it
        infos()  # and print the help
        sys.exit()


"""argumentList = (sys.argv[1:])                               # make a list of all the option wrote by the user
main(argumentList)"""
if __name__ == '__main__':
    argument = " -h"
    argumentList = (argument.split())
    print(argumentList)
    main(argumentList)
