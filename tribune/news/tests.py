from django.test import TestCase
from .models import Editor, Article, tags
import datetime as dt
# Create your tests here.

class EditorTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.newton = Editor(first_name='newton', last_name='bii', email='biinewtondev@gmail.com')

    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.newton, Editor))

    #test save method
    def test_save_method(self):
        self.newton.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)

    #test delete method
    # def test_delete_method(self):
    #     self.newton.delete_editor()


# class ArticleTestClass(TestCase):
#     #Set up method
#     def setUp(self):
#
#         editor = Editor(first_name='newton', last_name='bii', email='biinewtondev@gmail.com')
#         date = dt.date.today()
#
#         self.article = Article(title = 'Article', post = 'I like to pray everyday',
#         editor = editor, tags= 'pray', published_date=date)
#
#     #testing of artcile object is an instance of Article Class
#     def test_instance(self):
#         self.assertTrue(isinstance(self.article, Article))
#
#     #test the save article method in article class
#     def test_save_method(self):
#         self.article.save_article()
#         articles = Article.objects.all()
#         self.assertTrue(len(articles)>0)
