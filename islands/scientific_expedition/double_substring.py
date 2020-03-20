def search_double_string_using_brute_force(original_text):
    result = 0
    original_text = original_text or ''

    if len(original_text) > 0:
        searching_substring = original_text[:1]
        text_for_searching = original_text[1:]
        while len(searching_substring) <= len(text_for_searching):
            if searching_substring in text_for_searching:
                increased_searching_substring = searching_substring
                reduced_text_for_searching = text_for_searching

                while increased_searching_substring in reduced_text_for_searching:
                    new_result = len(increased_searching_substring)
                    result = result if new_result < result else new_result

                    increased_searching_substring = increased_searching_substring + reduced_text_for_searching[0]
                    reduced_text_for_searching = reduced_text_for_searching[1:]

            searching_substring = searching_substring[-1] + text_for_searching[0]
            text_for_searching = text_for_searching[1:]

    return result


# Tests
def test_find_double_string_using_brute_force_1():
    assert search_double_string_using_brute_force('') == 0
    assert search_double_string_using_brute_force('a') == 0
    assert search_double_string_using_brute_force('aa') == 1
    assert search_double_string_using_brute_force('aaa') == 1
    assert search_double_string_using_brute_force('abc') == 0


def test_find_double_string_using_brute_force_2():
    assert search_double_string_using_brute_force('aaaa') == 2
    assert search_double_string_using_brute_force('aabaa') == 2
    assert search_double_string_using_brute_force('cabab') == 2
    assert search_double_string_using_brute_force('abcab') == 2
    assert search_double_string_using_brute_force('abcdabc') == 3
    assert search_double_string_using_brute_force('aghtfghkofgh') == 3  # fgh
    assert search_double_string_using_brute_force('aghtfghkofgh') == 3  # fgh


def test_find_double_string_using_brute_force_3():
    assert search_double_string_using_brute_force(None) == 0
    assert search_double_string_using_brute_force("arefhjaref!!") == 4
    assert search_double_string_using_brute_force("aa") == 1

