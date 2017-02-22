import unittest, sys, os

sys.path.insert(0, os.path.abspath('.'))

from csv_map_converter.models.fields.base import *

class TestField(unittest.TestCase):

    def test_boolean_field(self):
        boolean_field = BooleanField()
        self.assertTrue(boolean_field.to_python('1'))
        self.assertTrue(boolean_field.to_python('True'))
        self.assertTrue(boolean_field.to_python('true'))
        self.assertFalse(boolean_field.to_python('0'))
        self.assertFalse(boolean_field.to_python('False'))
        self.assertFalse(boolean_field.to_python('false'))
        self.assertFalse(boolean_field.to_python(None))

    def test_long_field(self):
        long_field = LongField()

        if sys.version_info.major > 2:
            number = int
        else:
            number = long

        self.assertEqual(long_field.to_python('1'), number(1))
        self.assertEqual(long_field.to_python('0'), number(0))
        self.assertEqual(long_field.to_python('-1'), number(-1))

    def test_int_field(self):
        int_field = IntField()
        self.assertEqual(int_field.to_python('1'), int(1))
        self.assertEqual(int_field.to_python('0'), int(0))
        self.assertEqual(int_field.to_python('-1'), int(-1))

    def test_float_field(self):
        float_field = FloatField()
        self.assertEqual(float_field.to_python('1'), float(1))
        self.assertEqual(float_field.to_python('1.1231'), float(1.1231))
        self.assertEqual(float_field.to_python('0'), float(0))
        self.assertEqual(float_field.to_python('-1'), float(-1))
        self.assertEqual(float_field.to_python('-1.1'), float(-1.1))

    def test_string_field(self):
        string_field = StringField()
        texts = ['str1', 'str2', 'str3', '1', '0']
        for text in texts:
            self.assertEqual(string_field.to_python(text), text)


if __name__ == '__main__':
    unittest.main()

