
# Rasise keyword to set the mannual error
def calculateNum(num):
    if (num <= 0):
        raise ValueError('Number cant be 0 or less..')
    return 10/num


try:
    calculateNum(0)
except ValueError as error:
    print(error)
