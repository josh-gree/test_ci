from my_module.my_module import *
from unittest import TestCase

class TestMyModule(TestCase):

    def test_df1(self):

        self.assertEqual(len(df1),100)

    def test_df2(self):
    
        self.assertEqual(len(df2),100)

    def test_random_df(self):
        
        columns = ['Bob','Steve']
        N = 1000

        df = random_df(N=N,columns=columns)

        self.assertTrue((df.columns == columns + ['other']).all())


    