import unittest
from unittest.mock import patch
from io import StringIO
from task3_class_bank import Bank, Account, SavingsAccount, CurrentAccount


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()

    def test_open_account(self):
        account = Account.create_account('5001')
        self.bank.open_account(account)
        self.assertIn(account, self.bank.accounts)
        self.assertEqual(account.get_balance(), 0.0)
        self.assertEqual(account.get_account_number(), '5001')

    def test_update(self):
        account1 = SavingsAccount(2000, '2001', 5)
        account2 = CurrentAccount(-3000, '3001', 1000)

        self.bank.add_account(account1)
        self.bank.add_account(account2)

        self.assertEqual(account1.get_balance(), 2000)
        self.assertEqual(account2.get_balance(), -3000)
        # 1. Mocking print
        with patch('builtins.print') as mocked_print:
            self.bank.update()
            mocked_print.assert_called_once_with("Letter sent to account 3001:\
 You are in overdraft.")
        # 2. sys.stdout with io.StringIO
        capturedOutput = StringIO()
        import sys
        sys.stdout = capturedOutput

        self.bank.update()

        sys.stdout = sys.__stdout__

        expected_output = "Letter sent to account 3001: You are in overdraft."
        self.assertEqual(capturedOutput.getvalue().strip(), expected_output)

        self.assertEqual(account1.get_balance(), 2205)
        self.assertEqual(account2.get_balance(), -3000)


if __name__ == '__main__':
    unittest.main()
