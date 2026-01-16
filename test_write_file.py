from functions.write_file import write_file

def main():
    test_ls = [
        ("lorem.txt", "wait, this isn't lorem ipsum"),
        ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
        ("/tmp/temp.txt", "this should not be allowed")
    ]
    for test in test_ls:
        print(f"Result for {test[0]} directory:")
        print(write_file("calculator", test[0], test[1]))

if __name__ == "__main__":
    main()
