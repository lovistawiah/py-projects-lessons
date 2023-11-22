#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#


def main():
    x, y = 10, 100

    # conditional flow uses if, elif, else
    if x < y:
        result = "x is less than y"
    elif y == x:
        result = "x is the same as y"
    # conditional statements let you use "a if C else b"
    else:
        result = "x is greater than y"

    print(result)
    # match-case makes it easy to compare multiple values
    value = "43"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3,4)
        case _: 
            result =-1
    print(result)


if __name__ == "__main__":
    main()
