# test_assessment.py
import unittest
from assessment import (
    calculate_rectangle_area,
    sum_even_numbers,
    find_first_occurrence,
    safe_string_to_int,
    reverse_string_list_comprehension,
    count_characters_above_threshold
)

class TestAssessmentFunctions(unittest.TestCase):

    def test_calculate_rectangle_area(self):
        self.assertEqual(calculate_rectangle_area(5, 10), 50)
        self.assertEqual(calculate_rectangle_area(3.5, 2), 7.0)
        self.assertEqual(calculate_rectangle_area(0, 100), 0)
        self.assertEqual(calculate_rectangle_area(10, 0), 0)
        self.assertEqual(calculate_rectangle_area(-5, 10), 0) # Negative length
        self.assertEqual(calculate_rectangle_area(5, -10), 0) # Negative width
        self.assertEqual(calculate_rectangle_area(-5, -10), 0)# Both negative

    def test_sum_even_numbers(self):
        self.assertEqual(sum_even_numbers([1, 2, 3, 4, 5, 6]), 12) # 2+4+6
        self.assertEqual(sum_even_numbers([10, 1, 22, 3, 40]), 72) # 10+22+40
        self.assertEqual(sum_even_numbers([1, 3, 5, 7]), 0)      # No even numbers
        self.assertEqual(sum_even_numbers([]), 0)                 # Empty list
        self.assertEqual(sum_even_numbers([-2, 0, 2, -4]), -4)   # Including negatives and zero: -2+0+2-4

    def test_find_first_occurrence(self):
        self.assertEqual(find_first_occurrence([1, 2, 3, 4, 3, 5], 3), 2)
        self.assertEqual(find_first_occurrence(["apple", "banana", "cherry"], "banana"), 1)
        self.assertEqual(find_first_occurrence([10, 20, 30], 40), -1) # Not found
        self.assertEqual(find_first_occurrence([], "anything"), -1)    # Empty list
        self.assertEqual(find_first_occurrence([5, 5, 5, 5], 5), 0)   # First occurrence

    def test_safe_string_to_int(self):
        self.assertEqual(safe_string_to_int("123"), 123)
        self.assertEqual(safe_string_to_int("-45"), -45)
        self.assertEqual(safe_string_to_int("0"), 0)
        self.assertIsNone(safe_string_to_int("abc"))
        self.assertIsNone(safe_string_to_int("12.34"))
        self.assertIsNone(safe_string_to_int(""))

    def test_reverse_string_list_comprehension(self):
        self.assertEqual(reverse_string_list_comprehension("hello"), "olleh")
        self.assertEqual(reverse_string_list_comprehension("Python"), "nohtyP")
        self.assertEqual(reverse_string_list_comprehension(""), "")
        self.assertEqual(reverse_string_list_comprehension("a"), "a")
        self.assertEqual(reverse_string_list_comprehension("madam"), "madam")

    def test_count_characters_above_threshold(self):
        self.assertEqual(count_characters_above_threshold("aabbc", 1), 2) # a, b, c (a:2, b:2, c:1. All > 1? No, c is not. a,b are. This needs to be >= threshold for count to be included in the count for the character)
        # Let's redefine: count of unique characters whose own count is > threshold
        # a:2, b:2, c:1. threshold=1. Chars > 1 are 'a' and 'b'. So result is 2.
        self.assertEqual(count_characters_above_threshold("aaabbc", 2), 1) # a:3, b:2, c:1. threshold=2. Chars > 2 are 'a'. So result is 1.
        # Wait, if the char count is 3, and threshold is 2, then 3 > 2. 'a' counts.
        # if char count is 2, and threshold is 2, then 2 is not > 2. 'b' does not count.
        # This interpretation means the example was: text="aaabbc", threshold=2 -> 'a' is 3, so 'a' counts. Output 1.
        # Re-evaluating examples for count_characters_above_threshold based on "more times than a given threshold"
        # text="aabbc", threshold=1. Counts: {'a':2, 'b':2, 'c':1}.
        # 'a': 2 > 1 (True). 'b': 2 > 1 (True). 'c': 1 > 1 (False).
        # Unique characters meeting criteria: 'a', 'b'. Count = 2.
        self.assertEqual(count_characters_above_threshold("aabbc", 1), 2)

        # text="aaabbc", threshold=2. Counts: {'a':3, 'b':2, 'c':1}.
        # 'a': 3 > 2 (True). 'b': 2 > 2 (False). 'c': 1 > 2 (False).
        # Unique characters meeting criteria: 'a'. Count = 1.
        self.assertEqual(count_characters_above_threshold("aaabbc", 2), 1)

        self.assertEqual(count_characters_above_threshold("Hello World", 0), 8) # h:1,e:1,l:3,o:2, :1,w:1,r:1,d:1. All > 0. Unique: h,e,l,o, ,w,r,d (8 chars)
        self.assertEqual(count_characters_above_threshold("Hello World", 1), 2) # l:3, o:2. Unique: l, o (2 chars)
        self.assertEqual(count_characters_above_threshold("Hello World", 2), 1) # l:3. Unique: l (1 char)
        self.assertEqual(count_characters_above_threshold("hello", 10), 0)      # No char appears > 10 times
        self.assertEqual(count_characters_above_threshold("", 0), 0)            # Empty string
        self.assertEqual(count_characters_above_threshold("MiSsIsSiPpI", 3), 2) # s:4, i:4, p:2, m:1. Case-insensitive: M:1, I:4, S:4, P:2. counts: i:4, s:4, p:2, m:1. >3 are i,s. Result 2.
        # Correcting case-insensitive test for "MiSsIsSiPpI", threshold=3
        # Lowercase: "mississippi"
        # Counts: m:1, i:4, s:4, p:2
        # Characters with count > 3: 'i' (4 times), 's' (4 times).
        # Number of such unique characters = 2.
        self.assertEqual(count_characters_above_threshold("MiSsIsSiPpI", 3), 2)


if __name__ == '__main__':
    unittest.main(verbosity=2) # verbosity=2 gives more detailed output