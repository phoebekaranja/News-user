import unittest
from app.models import Sources,Articles


class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the classes
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('Citizen',"Citizen",'news from around the world',"english")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_init(self):
        '''
        test_init to ensure objects are instantiated correctly
        :return:
        '''
        self.assertEqual(self.new_source.id, "Citizen")
        self.assertEqual(self.new_source.name, "Citizen")
        self.assertEqual(self.new_source.description, "news from around the country")
        self.assertEqual(self.new_source.language, "english")


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('mark',"bitcoin review",'bitcoin news from relevant authorities',"en","2018-09-01T06:27:00Z","http://foxnews.com/img345.jpg")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_init(self):
        '''
        test_init to ensure objects are instantiated correctly
        :return:
        '''
        self.assertEqual(self.new_article.author, "mark")
        self.assertEqual(self.new_article.title, "bitcoin review")
        self.assertEqual(self.new_article.description, "bitcoin news from relevant authorities")
        self.assertEqual(self.new_article.url, "english")
        self.assertEqual(self.new_article.publishedAt, "2018-09-01T06:27:00Z")
        self.assertEqual(self.new_article.urlToImage, "http://foxnews.com/img345.jpg")


import unittest
from app.models import Sources,Articles


class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the classes
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('Citizen',"Citizen",'news from around the Country',"english")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_init(self):
        '''
        test_init to ensure objects are instantiated correctly
        :return:
        '''
        self.assertEqual(self.new_source.id, "Citizen")
        self.assertEqual(self.new_source.name, "Citizen")
        self.assertEqual(self.new_source.description, "news from around the country")
        self.assertEqual(self.new_source.language, "english")


class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('mark',"bitcoin review",'bitcoin news from relevant authorities',"en","2018-09-01T06:27:00Z","http://foxnews.com/img345.jpg")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_init(self):
        '''
        test_init to ensure objects are instantiated correctly
        :return:
        '''
        self.assertEqual(self.new_article.author, "mark")
        self.assertEqual(self.new_article.title, "bitcoin review")
        self.assertEqual(self.new_article.description, "bitcoin news from relevant authorities")
        self.assertEqual(self.new_article.url, "english")
        self.assertEqual(self.new_article.publishedAt, "2018-09-01T06:27:00Z")
        self.assertEqual(self.new_article.urlToImage, "http://foxnews.com/img345.jpg")
if __name__ == '__main__':
    unittest.main()
