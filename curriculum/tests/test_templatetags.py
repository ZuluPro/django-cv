from django.test import TestCase
from curriculum.templatetags import curriculum


class TagDaterangeDisplayTest(TestCase):
    def test_start_year(self):
        result = curriculum.daterange_display(2015)
        self.assertTrue(result)

    def test_start_year_and_month(self):
        result = curriculum.daterange_display(2015, 9)
        self.assertTrue(result)

    def test_start_year_and_end_year(self):
        result = curriculum.daterange_display(2015, None, 2016, None)
        self.assertTrue(result)

    def test_start_year_month_and_end_year(self):
        result = curriculum.daterange_display(2015, 2, 2016, None)
        self.assertTrue(result)

    def test_start_year_month_and_end_year_month(self):
        result = curriculum.daterange_display(2015, 2, 2016, 3)
        self.assertTrue(result)


class TagShorlinkTest(TestCase):
    def test_filter(self):
        url = 'http://www.ricehintz.org/'
        result = curriculum.shortlink(url)
        self.assertIn(url, result)

    def test_with_text(self):
        url = 'http://www.ricehintz.org/'
        result = curriculum.shortlink(url, 'foo')
        self.assertIn('foo', result)

    def test_no_value(self):
        result = curriculum.shortlink(None)
        self.assertFalse(result)
