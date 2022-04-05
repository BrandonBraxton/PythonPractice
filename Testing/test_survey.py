import unittest
from survey import AnonSurvey

class TestSurvey(unittest.TestCase):
    
    def setUp(self):
        question = "What language do you speak?"
        self.my_survey = AnonSurvey(question)
        self.responses = ['English', 'Spanish', 'Thai']
        
    def test_store_response(self):
        """question = "What language do you speak?"
        my_survey = AnonSurvey(question)
        my_survey.store_response('English')"""
        self.my_survey.store_response(self.responses[0])        
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_multiple_responses(self):
        """question = "What language do you speak?"
        my_survey = AnonSurvey(question)
        responses = ['English', 'Spanish', 'Thai']"""
        
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
            
unittest.main()