import unittest

from mode_helper.args import parse_args, get_shortcuts_dict

class TestArgParser(unittest.TestCase):

    def test_template(self):
        result = parse_args(['-T'])
        self.assertTrue(result['template'])

    def test_config(self):
        result = parse_args(['-c', '/home'])
        self.assertEqual(result['config'], '/home')

    def test_shortcuts(self):
        result = parse_args(['-s','s1 s2','d1 d2'])
        shortcuts = { 's1': 'd1',
                      's2': 'd2'}
        self.assertFalse(result['config'])
        self.assertFalse(result['notification'])
        self.assertFalse(result['pass_dir'])
        self.assertFalse(result['r_shortcuts'])
        self.assertFalse(result['target_dir'])
        self.assertFalse(result['template'])
        self.assertFalse(result['gen_config'])
        self.assertEqual(result['shortcuts'],shortcuts)
        self.assertRaises(ValueError,get_shortcuts_dict,['s1 s2 s3', 'd1 d2'])

    def test_notification(self):
        result = parse_args(['-n'])
        self.assertTrue(result['notification'])

    def test_r_shortcuts(self):
        result = parse_args(['-r'])
        self.assertTrue(result['r_shortcuts'])

    def test_pass_dir(self):
        result = parse_args(['-p', '/pass'])
        self.assertEqual(result['pass_dir'], '/pass')

    def test_target_dir(self):
        result = parse_args(['-t', '/target_dir'])
        self.assertEqual(result['target_dir'], '/target_dir')

    def test_gen_config(self):
        result = parse_args(['-g'])
        self.assertTrue(result['gen_config'])

if __name__ == '__main__':
    unittest.main()
