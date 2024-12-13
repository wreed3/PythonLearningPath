import unittest
from unittest.mock import patch

from Hangman.hangman_game import user_guess


class TestHangmanGame(unittest.TestCase):
    # def testWordsArrayIsNotEmpty(self):
    #     list_length = len(words)
    #     self.assertGreater(list_length, 0)
    #
    # def testBlankArrayGeneratedWithSameLengthOfRandomWord(self):
    #     random_word_selection = 'mouse'
    #     random_word_length = len(random_word_selection)
    #     blanks_array = build_blanks_array(random_word_selection)
    #     blanks_array_length = len(blanks_array)
    #     self.assertEqual(random_word_length, blanks_array_length)
    #
    # def testUserStartsWithSixLives(self):
    #
    @patch('hangman_game.user_guess')
    def testUserInputIsLowercase(self, mock_guess):
        mock_guess.return_value = 'b'
        result = user_guess()
        self.assertEqual(result, 'b')

    # def testUserCanOnlyEnterLetters(self):
    #
    # def testUserWillGetFeedBackIfTheyEnterAnyOtherThanALetter(self):
    #
    # def testBlankArrayIsUpdatedWithCorrectGuess(self):
    #
    # def testUserCanOnlyGuessOneLetterAtATime(self):
    #
    # def testSingleLetterInMultipleIndexIsUpdatedCorrectly(self):
    #
    # def testIncorrectGuessAreNotAddedToBlankArray(self):
    #
    # def testUserLosesALifeForAnIncorrectGuess(self):
    #
    # def testUserLivesUpdateProperly(self):
    #
    # def testWhenUserWinsGameIsOver(self):
    #
    # def testWhenUserRunsOutOfLivesGameIsOver(self):
    #
    # def



if __name__ == '__main__':
    unittest.main()
