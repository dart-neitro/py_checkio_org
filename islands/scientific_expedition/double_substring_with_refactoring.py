class SearchDoubleStringUsingBruteForce:

    def __init__(self, original_text):
        self.length_of_the_longest_substring = 0
        self.original_text = original_text or ''
        self.searching_substring = ''
        self.text_for_searching = ''
        self.increased_searching_substring = ''
        self.reduced_text_for_searching = ''

    def check_initial_parameters(self):
        if len(self.original_text) < 2:
            return False
        return True

    def set_up_initial_values(self):
        self.searching_substring = self.original_text[:1]
        self.text_for_searching = self.original_text[1:]

    def update_searching_params(self):
        self.searching_substring = self.searching_substring[-1] + self.text_for_searching[0]
        self.text_for_searching = self.text_for_searching[1:]

    def set_up_increased_params(self):
        self.increased_searching_substring = self.searching_substring
        self.reduced_text_for_searching = self.text_for_searching

    def is_increased_searching_substring_in_reduced_text_for_searching(self):
        return self.increased_searching_substring in self.reduced_text_for_searching

    def update_length_of_the_longest_substring(self):
        new_length_of_the_longest_substring = len(self.increased_searching_substring)
        if new_length_of_the_longest_substring > self.length_of_the_longest_substring:
            self.length_of_the_longest_substring = new_length_of_the_longest_substring

    def update_increased_searching_params(self):
        self.increased_searching_substring = self.increased_searching_substring + self.reduced_text_for_searching[0]
        self.reduced_text_for_searching = self.reduced_text_for_searching[1:]

    def search_increased_substring(self):
        self.set_up_increased_params()
        while self.is_increased_searching_substring_in_reduced_text_for_searching():
            self.update_length_of_the_longest_substring()
            self.update_increased_searching_params()

    def is_search_in_progress(self):
        return len(self.searching_substring) <= len(self.text_for_searching)

    def is_searching_substring_in_text_for_searching(self):
        return self.searching_substring in self.text_for_searching

    def search_double_substring(self):
        while self.is_search_in_progress():
            if self.is_searching_substring_in_text_for_searching():
                self.search_increased_substring()
            self.update_searching_params()

    def get_length_of_the_longest_substring(self):
        if self.check_initial_parameters():
            self.set_up_initial_values()
            self.search_double_substring()
        return self.length_of_the_longest_substring


def search_double_string_using_brute_force(original_text):
    return SearchDoubleStringUsingBruteForce(original_text).get_length_of_the_longest_substring()


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

