from functions.get_files_info import get_files_info

def print_result(title, result):
    print(title)
    for line in result.split("\n"):
        print(" ", line)
    print()

if __name__ == "__main__":
    # Test 1
    print("get_files_info('calculator', '.'):")
    result = get_files_info("calculator", ".")
    print_result("Result for current directory:", result)

    # Test 2
    print("get_files_info('calculator', 'pkg'):")
    result = get_files_info("calculator", "pkg")
    print_result("Result for 'pkg' directory:", result)

    # Test 3
    print("get_files_info('calculator', '/bin'):")
    result = get_files_info("calculator", "/bin")
    print_result("Result for '/bin' directory:", result)

    # Test 4
    print("get_files_info('calculator', '../'):")
    result = get_files_info("calculator", "../")
    print_result("Result for '../' directory:", result)
