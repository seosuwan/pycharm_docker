import unittest
from titanic.view.titanic_view import TitanicView


class TitanicViewTest(unittest.TestCase):


    def test_modeling(self):

        mock = TitanicView()
        this = mock.preprocessing()
        print(f'The Type of This is{type(this.train)}')
        print(f'The head of Train is\n {this.train.head(2)}')
        print(f'The head of Train is\n {this.test.head(2)}')


if __name__ == '__main__':
    unittest.main()



