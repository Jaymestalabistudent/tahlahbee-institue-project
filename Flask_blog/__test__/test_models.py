import unittest
from unittest.mock import patch, MagicMock
from flaskblog import create_app
from flaskblog.models import User, Post, Story, Contribution

class TestConfig:
    SECRET_KEY = 'mysecret'

class BasicTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app(TestConfig)
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        cls.client = cls.app.test_client()

    @classmethod
    def tearDownClass(cls):
        cls.app_context.pop()

    # Test Post Creation without Database
    def test_post_creation(self):
        with patch('flaskblog.models.Post.query') as mock_query:
            mock_post = MagicMock()
            mock_post.title = 'Test Post'
            mock_post.content = 'This is a test post'
            mock_query.first.return_value = mock_post
            post = Post(title='Test Post', content='This is a test post', user_id=1)
            self.assertEqual(post.title, 'Test Post')
            self.assertEqual(post.content, 'This is a test post')


    # Test Story Creation without Database
    def test_story_creation(self):
        with patch('flaskblog.models.Story.query') as mock_query:
            mock_story = MagicMock()
            mock_story.title = 'Test Story'
            mock_query.first.return_value = mock_story
            story = Story(title='Test Story', description='This is a test story.')
            self.assertEqual(story.title, 'Test Story')

    # Test Contribution Creation without Database
    def test_contribution_creation(self):
        with patch('flaskblog.models.Contribution.query') as mock_query:
            mock_contribution = MagicMock()
            mock_contribution.content = 'This is a contribution'
            mock_query.first.return_value = mock_contribution
            contribution = Contribution(content='This is a contribution', story_id=1, user_id=1)
            self.assertEqual(contribution.content, 'This is a contribution')

if __name__ == '__main__':
    unittest.main()
