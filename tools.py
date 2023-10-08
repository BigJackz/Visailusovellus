
#Transforms input gotten from database to string with no extra characters
def make_string(input):
    input = str(input).strip('(' + ')' + ',' + "'" + '"')
    return input

#return False if string is not inbetween min and max, otherwise returns True
def check_length(string, min, max):
    if len(string) > max or len(string) < min:
        return False
    return True