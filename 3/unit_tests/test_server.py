import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.getcwd(), '..'))
from server import process_client_message
from common.variables import ACTION, TIME, USER, ACCOUNT_NAME, PRESENCE, RESPONSE, ERROR


class TestServer(unittest.TestCase):

    ok_dict = {RESPONSE: 200}
    err_dict = {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }

    def test_process_client_message_ok(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}}), self.ok_dict)

    def test_process_client_message_no_action(self):
        self.assertEqual(process_client_message(
            {TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_process_client_message_wrong_action(self):
        self.assertEqual(process_client_message(
            {ACTION: 'Wrong', TIME: '1.1', USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_process_client_message_no_time(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, USER: {ACCOUNT_NAME: 'Guest'}}), self.err_dict)

    def test_process_client_message_no_user(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: '1.1'}), self.err_dict)

    def test_process_client_message_unknown_user(self):
        self.assertEqual(process_client_message(
            {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest1'}}), self.err_dict)


if __name__ == '__main__':
    unittest.main()
