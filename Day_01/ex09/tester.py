# ft_package/tests/test_core.py

from ft_package.core import count_in_list

def test_count_in_list():
    # Test case 1
    result1 = count_in_list(["toto", "tata", "toto"], "toto")
    assert result1 == 2, f"Expected 2, got {result1}"

    # Test case 2
    result2 = count_in_list(["toto", "tata", "toto"], "tutu")
    assert result2 == 0, f"Expected 0, got {result2}"

if __name__ == "__main__":
    test_count_in_list()
    print("All tests passed.")
