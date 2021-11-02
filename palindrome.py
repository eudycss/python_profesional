def is_palindrome(string: str)-> bool:
    string=string.replace(" ","").lower()
    return string==string[::-1] #""" ::-1 nos permite dar la vuelta al string """

def run():
    print(is_palindrome(1000))


""" Entry point """
if __name__=='__main__':
    run()
