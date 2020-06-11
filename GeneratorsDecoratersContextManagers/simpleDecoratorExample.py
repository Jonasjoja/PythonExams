def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite #Is essentially the same as having greet = be_polite(greet)
def greet():
    print("My name is Svend.")


@be_polite
def rage():
	print("I HATE YOU!")


greet()
rage()