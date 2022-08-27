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
def shift(message : str, index : int) -> str:
    '''shifts the message[index] forward in the alphabet num number of positions.  wraps around if past z'''
    newChar = chr(ord('A')+(ord(message[index])-ord('A')+1)%26)
    return message[:index]+newChar+message[index+1:]
def rotate(message : str, num : int) -> str:
    '''rotates characters in message forward num number of positions'''
    return message[-num:]+message[:len(message)-num]
def duplicate(message : str, index : int) -> str:
    '''duplicates character in message at index'''
    return message[:index]+message[index]+message[index:]
def swap(message : str, index1 : int, index2 : int) -> str:
    '''swaps characters in message at index1 and index2'''
    message = list(message)
    message[index1], message[index2] = message[index2], message[index1]
    return ''.join(message)
def unDuplicate(message : str, index : int) -> str:
    '''deletes the duplicated character in message at index'''
    return message[:index]+message[index+1:]
def unRotate(message : str, num : int) -> str:
    '''rotates message backward num positions'''
    return message[num:]+message[:num]
def getOpType(op : str) -> str:
    '''returns a single character value indicating the type of transformation'''
    return op[0]
def createOpList(opString : str) -> str:
    '''splits the parameters of the operation into a list to be used later'''
    return opString.split(',')
def callTransf(tType : str, message : str, encrypt : bool, params) -> str:
    '''calls the respective transformation function based on parameters.  returns the message post-transformation'''
    if tType == "T":
        message = swap(message, int(params[0]), int(params[1]))
    if encrypt:
        if tType == "R":
            message = rotate(message, params)
        if tType == "S":
            message = shift(message, int(params[0]))
        if tType == "D":

            message = duplicate(message, int(params[0]))
    if not encrypt:
        if tType == "R":
            message = unRotate(message, params)
        if tType == "S":
            message = shift(message, -int(params[0]))
        if tType == "D":
            message = unDuplicate(message, int(params[0]))
    return message
def printParamsMessage(op : str):
    '''prints the message describing which transformations are being used with which parameters.  returns the parameter list for later use'''
    operation = op[0]
    param = op[1:]
    params = param.split(',')
    words = {"R": "Rotate", "S": "Shift", "D": "Duplicate", "T": "Swap"}
    paramMessage = "Operation {} {} - Parameters: ".format(words[operation], operation)
    if len(params) > 1:
        paramMessage += "{}, {}".format(params[0], params[1])
    else:
        paramMessage += params[0]
    print(paramMessage)
    return params
def encrypt(opString : str, message : str) -> str:
    '''called if the user would like to encrypt a message.  takes operations to use and applies them to the message. returns encrypted message'''
    for op in opString.split(';'):
        message = execute(printParamsMessage(op), op[0], message, True)
    return message
def decrypt(opString: str, message : str) -> str:
    '''called to decrypt message with the operations that were used to encrypt it.  returns decrypted message'''
    for op in opString.split(';')[::-1]:
        message = execute(printParamsMessage(op), op[0], message, False)
    return message
def execute(params, operation , message, encrypt) -> str:
    '''executes the correct transformation functions, returns post transformation message'''
    for i in range(len(params)):
        if params[i] != '':
            params[i] = int(params[i])
        else:
            params = 1
            break
    message = callTransf(operation, message, encrypt, params)
    print(message)
    return message
print(rotate("HOESS", 1))
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
            print("Generating output...\nTransforming message: {}\nApplying...".format(message))
            if uChoice == "D":
                decrypt(encryptOps, message)
            elif uChoice == "E":
                encrypt(encryptOps, message)
if __name__ == '__main__':
    main()
