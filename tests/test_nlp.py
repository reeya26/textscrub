import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from textscrub import nlp
import unittest


class TestingNLPCleaning(unittest.TestCase):

    def test_convert_emoji(self):

        a = 'I’m convinced that 😭😭😭 is the most expressive emoji combo '
        b = 'I’m convinced that  is the most expressive emoji combo '

        mssg =  'Values are not equal'

        #Enter second input as Remove or Replace
        clean_text = nlp.remove_emoji(a,"Remove")
        self.assertEqual(clean_text, b, mssg)


    def test_stopwords(self):

        a = 'I’m convinced that the crying face is the most expressive emoji combo'
        b = 'I’m convinced crying face expressive emoji combo'

        mssg =  'Values are not equal'

        #Enter second input as Remove or Replace
        clean_text = nlp.stopword_removal(a)
        self.assertEqual(clean_text, b, mssg)

    


if __name__ == '__main__':
    unittest.main()