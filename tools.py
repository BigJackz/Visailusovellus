
#Transforms input gotten from database to string with no extra characters
def make_string(input):
    input = str(input).strip('(' + ')' + ',' + "'" + '"')
    return input
