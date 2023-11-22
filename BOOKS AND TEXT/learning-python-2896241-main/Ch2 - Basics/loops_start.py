#
# Example file for working with loops
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x = 0
    # TODO: define a while loop
    # while (x < 5):
    #     print(x)
    #     x = x+1
    #     print("="*30)

    # TODO: define a for loop
    # for x in range(5, 12, 3):
    #     print(x)
    # print("="*30)

    # TODO: use a for loop over a collection
    # days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    # for day in days:
    #     print(day)
    # print("="*30)

# TODO: use the break and continue statements
    # for day in ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]:
    #     if day == "Fri":
    #         print("Hello")
    #     break
    # print("="*30)
    
    # for i in range(1, 20):
    #     if i % 2 == 0:
    #         continue
    #     print(i)
    # print("="*30)

    # TODO: using the enumerate() function to get index
    for i, d in enumerate(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]):
        print(i,d)
    

if __name__ == "__main__":
    main()
