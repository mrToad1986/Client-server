import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.getcwd(), '..'))
# sys.path.insert(0, os.path.join(os.path.dirname(__file__), os.path.pardir)) # так тоже импортируется верно
from client import create_presence, process_ans
from common.variables import ACTION, TIME, USER, ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR


class TestClient(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_create_presence(self):
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})

    def test_create_presence_action(self):
        test = create_presence()
        test[TIME] = 1.1
        self.assertIsNotNone(test[ACTION], 'Presence not created')

    def test_create_presence_account_name_type(self):
        test = create_presence()
        test[TIME] = 1.1
        # test[USER][ACCOUNT_NAME] = 1234
        self.assertIsInstance(test[USER][ACCOUNT_NAME], str, 'Account name must be a string')

    def test_create_presence_output_length(self):
        test = create_presence()
        test[TIME] = 1.1
        self.assertEqual(len(test), 3, 'Wrong output length')

    def test_create_presence_output_type(self):
        test = create_presence()
        test[TIME] = 1.1
        self.assertIsInstance(test, dict, 'Output type must be a dictionary')

    def test_create_presence_output_keys(self):
        test = create_presence()
        test[TIME] = 1.1
        self.assertIn('action', test.keys(), 'Wrong output content')

    def test_process_ans_200(self):
        self.assertEqual(process_ans({RESPONSE: 200}), '200 : OK')

    def test_process_ans_400(self):
        self.assertEqual(process_ans({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_process_ans_no_response(self):
        self.assertRaises(ValueError, process_ans, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
