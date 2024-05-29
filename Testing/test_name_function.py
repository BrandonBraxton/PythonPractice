import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('Billy', 'Bob')
        self.assertEqual(formatted_name, 'Billy Bob')
        
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('Jack','Jill', 'And')
        self.assertEqual(formatted_name, 'Jack And Jill')
    
unittest.main()