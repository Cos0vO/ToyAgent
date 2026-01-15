from functions.get_files_info import get_files_info

def main():
    test_ls = [".", "pkg", "/bin", "../"]
    for test in test_ls:
        if test == '.':
            file_name = "current"
        else:
            file_name = f"'{test}'"
        print(f"Result for {file_name} directory:")
        print(get_files_info("calculator", test))

if __name__ == "__main__":
    main()
