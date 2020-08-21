import unittest

def ReverseNested(input_value):

    is_first = 1
    is_done = 0
    temp_input_value = input_value
    output_value = {}

    while is_done == 0:
        key = list(temp_input_value.keys())[0]
        value = temp_input_value.get(key)
        try:
            key_2 = list(value.keys())
            if is_first == 1:
                output_value = dict.fromkeys(key_2, key)
            else:
                output_value = dict.fromkeys(key_2, output_value)
            temp_input_value = value
            is_first = 0
        except:
            output_value = dict.fromkeys(value, output_value)
            is_done = 1
    return output_value

input_value = {
  'hired': {
    'be': {
      'to': {
        'deserve': 'I'
      }
    }
  }
}

output_value = {
  'I': {
    'deserve': {
      'to': {
         'be': 'hired'
      }
    }
  }
}

class ExceptionTest(unittest.TestCase):

    def test_assert_raises(self):
        self.assertEqual(ReverseNested(input_value), output_value)



if __name__ == '__main__':
    unittest.main()