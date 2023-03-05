import unittest
from unittest.mock import patch

import pytest
from quiz import play_game, QUESTIONS_AND_ANSWERS, get_input


class PlayQuizTest(unittest.TestCase):

    @pytest.mark.task(taskno=1)
    @patch('quiz.get_input', side_effect=["Guido van Rossum", "bool", "94", "1991", "="])
    def test_all_correct_answers(self, input):
        actual_result = play_game(QUESTIONS_AND_ANSWERS)
        expected_result = 5
        self.assertEqual(expected_result, actual_result)
