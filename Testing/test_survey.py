import unittest
from survey import AnonSurvey

class TestSurvey(unittest.TestCase):
    def test_store_response(self):
        question = "What language do you speak?"
        my_survey = AnonSurvey(question)
        my_survey.store_response('English')
        
        self.assertIn('English', my_survey.responses)
        
unittest.main()