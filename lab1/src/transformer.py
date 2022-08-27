"""
CSAPX Lab 1: Secret Messages

A program that encodes/decodes a message by applying a set of transformation operations.
The transformation operations are:
    shift - Sa[,n] changes letter at index a by moving it n letters fwd in the alphabet. A negative
        value for n shifts the letter backward in the alphabet.
    rotate - R[n] rotates the string n positions to the right. A negative value for n rotates the string
        to the left.
    duplicate - Da[,n] follows character at index a with n copies of itself.

All indices numbers (the subscript parameters) are 0-based.

author: Ryan Weiner
"""
def transform(opString, message):
    ops = opString.split(';')
    operation = ""
    for op in ops:
        operation = op[0]
        param = op[1:]
        params = param.split(',')
        words = {"R":"Rotate", "S":"Shift", "D":"Duplicate", "T":"Swap"}
        paramMessage = "Operation {} {} - Parameters: ".format(words[operation], operation)
        if len(params)> 1:
            paramMessage += "{}, {}".format(params[0], params[1])
        else:
            paramMessage+=params[0]
        print(paramMessage)
    print("\n\n")
    opList = []
    opList.append(op for op[0] in ops)
    print(o for o in opList)


def shift(message):
    pass
def rotate(message):
    pass
def duplicate(message, index):
    pass
def swap(message, index1, index2):
    pass
def encrypt(opString, message):
    pass
def decrypt(opString, message):
    pass

def main() -> None:
    """
    The main loop responsible for getting the input details from the user
    and printing in the standard output the results
    of encrypting or decrypting the message applying the transformations
    :return: None
    """

    while True:
        uChoice = (input("Would you like to encrypt (E), decrypt(D) or quit (Q)? ")).upper()
        if uChoice == "Q":
            print("GOODBYE!")
            break
        elif uChoice != "D" and uChoice != "E" and uChoice != "Q":
            print("Input not recognized, please try again.")
        else:
            message = (input("Enter the message: ")).upper()
            encryptOps = input("Enter the encrypting transformation operations: ")
            print("Generating output...")
            print("Transforming message: {}".format(message))
            print("Applying...")
            if uChoice == "D":
                decrypt(encryptOps, message)
            elif uChoice == "E":
                encrypt(encryptOps, message)
            transform(encryptOps, message)

if __name__ == '__main__':
    main()
