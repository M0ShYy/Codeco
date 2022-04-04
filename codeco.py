from fonctions import *
import sys
import getopt

"""from timeit import default_timer as timer"""
global info
# Options
options = "hedm:i:"
# Long options
long_options = ["help", "encode", "decode", "methode =", "input ="]


# list of the characters available


def infos():
    global info
    info = True
    return ("codeco.py\n"
            "OPTION\n"
            "-h   --help      <Show this page>\n"
            "-e   --encode    <if you want to encode>   \n"
            "-d   --decode    <if you want to encode>       \n"
            "-m   --methode   <methode of decode/encode>\n"
            "-i   --input     <the secret or the code>\n"
            "\n"
            "\n"
            "EXAMPLES:\n"
            "codeco.py -e -m caesar -i secret\n"
            "codeco.py -h\n"
            "\n"
            "SEE THE MAN PAGE https://github.com/M0ShYy/Codeco FOR MORE OPTIONS AND EXAMPLES\n")


def main(argumentlist):
    global info, encode, decode, text, method
    info = False
    encode = False
    decode = False
    try:
        arguments, values = getopt.getopt(argumentlist, options, long_options)

        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):  # test if there is -h or --help
                print(infos())  # print help

            elif currentArgument in ("-e", "--encode "):  # test if there is -e or --encode
                encode = True

            elif currentArgument in ("-d", "--decode "):  # test if there is -d or --decode
                decode = True

            elif currentArgument in ("-m", "--method "):  # test if there is -m --method
                method = currentValue  #
            elif currentArgument in ("-i", "--input "):  # test if there is -i or --input
                text = currentValue  #
        if not info:  # if the help was not printed then
            if encode != decode:
                print('commenceon le script avec: ' + method + " pour : " + text)
            else:
                print("You can't have decode and encode ON")
    except getopt.error as err:  # if there is an error
        # output error, and return with an error code
        print(str(err))  # print it
        infos()  # and print the help
        sys.exit()


# argumentList = (sys.argv[1:])                               # make a list of all the option wrote by the user
# main(argumentList)

if __name__ == '__main__':
    argument = " -d -m hexa -i test"
    argumentList = (argument.split())
    print(argumentList)
    main(argumentList)
