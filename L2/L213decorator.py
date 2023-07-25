#Funtion that takes a funtion as input and returns a modified version of it by adding additional capabilities
#Another use case is checking if a user is always logged in

def announce(f):
    def wrapper():
        print("About the run the funtion")
        f()
        print("Funtion ran")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()