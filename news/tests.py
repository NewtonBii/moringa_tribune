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


class ArticleTestClass(TestCase):
    #Creating a nee editor and saving it.
    def setUp(self):
        self.newton = Editor(first_name='newton', last_name='bii', email='biinewtondev@gmail.com')
        self.newton.save_editor()

        #Creating a new tag and saving it
        self.new_tag = tags(name='testing')
        self.new_tag.save()

        self.new_article = Article(title = 'Test Article',post = 'A test post',editor = self.newton)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)


    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
