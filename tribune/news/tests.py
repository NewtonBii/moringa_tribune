from django.test import TestCase
from .models import Editor, Article, tags
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
