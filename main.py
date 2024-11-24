import playground as pg

def main():
    #name = input('What is your name?')
    #pg.hello(name)
    #eval converts string to number
    miles = eval(input("What is the distance?"))
    kms = miles * 1.61
    print("The distance is ",kms)

main()