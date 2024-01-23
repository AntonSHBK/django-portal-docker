from django.test import TestCase
from django.contrib.auth.models import User

from blog.models import Post

USER = User.objects.get(id=0)
TITLE="Title"
CONTENT="Context"

class PostModelTest(TestCase):
    
    # setUpTestData: Run once to set up non-modified data for all class methods
    @classmethod
    def setUpTestData(cls):
        cls.post: Post = Post.objects.create(author=USER, title=TITLE, content=CONTENT)
        cls.post_id = cls.post.id
           
    # setUp: Run once for every test method to setup clean data.
    def setUp(self):
        pass

    def test_title_label(self):
        post = Post.objects.get(id=self.post_id)
        title = post._meta.get_field('title').verbose_name
        self.assertEquals(title,'Title')

    def test_title_max_length(self):
        post = Post.objects.get(id=self.post_id)
        max_length = post._meta.get_field('title').max_length
        self.assertEquals(max_length, 100)

    def test_get_absolute_url(self):
        post = Post.objects.get(id=self.post_id)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(post.get_absolute_url(),
                          'user/{username}/'.format(
                              username=self.post.author.username))



    # def test_false_is_false(self):
    #     print("Method: test_false_is_false.")
    #     self.assertFalse(False)

    # def test_false_is_true(self):
    #     print("Method: test_false_is_true.")
    #     self.assertTrue(True)

    # def test_one_plus_one_equals_two(self):
    #     print("Method: test_one_plus_one_equals_two.")
    #     self.assertEqual(1 + 1, 2)

    

