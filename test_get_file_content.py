from functions.get_file_content import get_file_content

def main():
    res = get_file_content("calculator", "lorem.txt")
    test_ls = [
        "main.py",
        "pkg/calculator.py",
        "/bin/cat",
        "pkg/does_not_exist.py"
    ]
    for test in test_ls:
        print(f"Result for {test} file:")
        print(get_file_content("calculator", test))

if __name__ == "__main__":
    main()
