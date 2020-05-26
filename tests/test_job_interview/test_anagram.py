import unittest

from esme_lessons.job_interview.anagrams import anagram


class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        # Given
        n ='68169'
        expected_output=98661
        pass
        # When
        output = anagram(n)
        # Then
        self.assertEqual(expected_output,output)

