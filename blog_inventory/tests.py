import unittest
from models import Blogs


class TestBlogPosts(unittest.TestCase):
    """Tests for the class BlogAPICalls"""

    def setUp(self):
        """Create a list of comma seperated tags for use in test methods"""
        self.tags = ['tech', 'history']
        print(f"this is the tags {self.tags}")

    def test_single_tag(self):
        """Test that a single tag is stored properly"""
        
        my_test1 = Blogs([self.tags[0]])
        my_test1.fetch_posts()
        my_test1.check_tags()

        self.assertIn(self.tags[0], my_test1.tag_list)

    def test_multiple_tags(self):
        """Test that multiple tags are stored properly"""

        my_test2 = Blogs(self.tags)
        my_test2.fetch_posts()
        my_test2.check_tags()

        for tag in self.tags:
            self.assertIn(tag, my_test2.tag_list)

unittest.main() 