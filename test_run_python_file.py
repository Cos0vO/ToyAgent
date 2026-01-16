from functions.run_python_file import run_python_file

def main():
    test_ls = [
        ("main.py", None),
        ("main.py", ["3 + 5"]),
        ("tests.py", None),
        ("../main.py", None),
        ("nonexistent.py", None),
        ("lorem.txt", None)
    ]
    for test in test_ls:
        print(f"Result for {test[0]} directory:")
        print(run_python_file("calculator", test[0], test[1]))

if __name__ == "__main__":
    main()
