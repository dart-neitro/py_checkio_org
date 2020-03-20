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


def test_SearchDoubleStringUsingBruteForce_check_initial_parameters_1():
    searcher = SearchDoubleStringUsingBruteForce()
    assert not searcher.check_initial_parameters()


def test_SearchDoubleStringUsingBruteForce_check_initial_parameters_2():
    searcher = SearchDoubleStringUsingBruteForce('aa')
    assert searcher.check_initial_parameters()


def test_SearchDoubleStringUsingBruteForce_set_up_initial_values():
    searcher = SearchDoubleStringUsingBruteForce('fd')
    searcher.set_up_initial_values()
    assert searcher.searching_substring == 'f'
    assert searcher.text_for_searching == 'd'


def test_SearchDoubleStringUsingBruteForce_update_searching_params():
    searcher = SearchDoubleStringUsingBruteForce('abcd123')
    searcher.set_up_initial_values()
    searcher.update_searching_params()
    assert searcher.searching_substring == 'ab'
    assert searcher.text_for_searching == 'cd123'
    searcher.update_searching_params()
    assert searcher.searching_substring == 'bc'
    assert searcher.text_for_searching == 'd123'


def test_SearchDoubleStringUsingBruteForce_set_up_increased_params():
    searcher = SearchDoubleStringUsingBruteForce('abcd123')
    searcher.searching_substring = '123'
    searcher.text_for_searching = '456'
    searcher.set_up_increased_params()
    assert searcher.increased_searching_substring == '123'
    assert searcher.reduced_text_for_searching == '456'


def test_SearchDoubleStringUsingBruteForce_is_increased_searching_substring_in_reduced_text_for_searching():
    searcher = SearchDoubleStringUsingBruteForce('')
    searcher.increased_searching_substring = '123'
    searcher.reduced_text_for_searching = '1234'
    assert searcher.is_increased_searching_substring_in_reduced_text_for_searching()
    searcher.increased_searching_substring = '123'
    searcher.reduced_text_for_searching = '1254'
    assert not searcher.is_increased_searching_substring_in_reduced_text_for_searching()


def test_SearchDoubleStringUsingBruteForce_update_length_of_the_longest_substring_1():
    searcher = SearchDoubleStringUsingBruteForce('')
    searcher.length_of_the_longest_substring = 4
    searcher.increased_searching_substring = '12345'
    searcher.update_length_of_the_longest_substring()
    assert searcher.length_of_the_longest_substring == 5


def test_SearchDoubleStringUsingBruteForce_update_length_of_the_longest_substring_2():
    searcher = SearchDoubleStringUsingBruteForce('')
    searcher.length_of_the_longest_substring = 4
    searcher.increased_searching_substring = '123'
    searcher.update_length_of_the_longest_substring()
    assert searcher.length_of_the_longest_substring == 4


def test_SearchDoubleStringUsingBruteForce_update_increased_searching_params():
    searcher = SearchDoubleStringUsingBruteForce('')
    searcher.increased_searching_substring = '1'
    searcher.reduced_text_for_searching = '234'
    searcher.update_increased_searching_params()
    assert searcher.increased_searching_substring == '12'
    assert searcher.reduced_text_for_searching == '34'


def test_SearchDoubleStringUsingBruteForce_search_increased_substring():
    searcher = SearchDoubleStringUsingBruteForce('')
    searcher.searching_substring = '12'
    searcher.text_for_searching = '3456123'
    searcher.search_increased_substring()
    assert searcher.length_of_the_longest_substring == 3
    assert searcher.increased_searching_substring == '1234'
    assert searcher.reduced_text_for_searching == '56123'


def test_SearchDoubleStringUsingBruteForce_is_search_in_progress_1():
    searcher = SearchDoubleStringUsingBruteForce('')
    searcher.searching_substring = '12'
    searcher.text_for_searching = '12'
    assert searcher.is_search_in_progress()


def test_SearchDoubleStringUsingBruteForce_is_search_in_progress_1():
    searcher = SearchDoubleStringUsingBruteForce('')
    searcher.searching_substring = '12'
    searcher.text_for_searching = '456'
    assert searcher.is_search_in_progress()


def test_SearchDoubleStringUsingBruteForce_is_search_in_progress_1():
    searcher = SearchDoubleStringUsingBruteForce('')
    searcher.searching_substring = '1222'
    searcher.text_for_searching = '456'
    assert not searcher.is_search_in_progress()


def test_SearchDoubleStringUsingBruteForce_is_searching_substring_in_text_for_searching_1():
    searcher = SearchDoubleStringUsingBruteForce('')
    searcher.searching_substring = '12'
    searcher.text_for_searching = '5123'
    assert searcher.is_searching_substring_in_text_for_searching()


def test_SearchDoubleStringUsingBruteForce_is_searching_substring_in_text_for_searching_1():
    searcher = SearchDoubleStringUsingBruteForce('')
    searcher.searching_substring = '12'
    searcher.text_for_searching = '513'
    assert not searcher.is_searching_substring_in_text_for_searching()

    def search_double_substring(self):
        while self.is_search_in_progress():
            if self.is_searching_substring_in_text_for_searching():
                self.search_increased_substring()
            self.update_searching_params()


def test_SearchDoubleStringUsingBruteForce_search_double_substring():
    searcher = SearchDoubleStringUsingBruteForce('zz1234asd123456')
    searcher.set_up_initial_values()
    searcher.search_double_substring()
    assert searcher.length_of_the_longest_substring == 4
    assert searcher.increased_searching_substring == '34a'
    assert searcher.reduced_text_for_searching == 'sd123456'
    assert searcher.searching_substring == '45'
    assert searcher.text_for_searching == '6'


def test_SearchDoubleStringUsingBruteForce_get_length_of_the_longest_substring():
    searcher = SearchDoubleStringUsingBruteForce('zz1234asd123456')
    searcher.get_length_of_the_longest_substring()
    assert searcher.length_of_the_longest_substring == 4
    assert searcher.increased_searching_substring == '34a'
    assert searcher.reduced_text_for_searching == 'sd123456'
    assert searcher.searching_substring == '45'
    assert searcher.text_for_searching == '6'
