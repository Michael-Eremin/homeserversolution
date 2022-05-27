from django.test import TestCase
from newscreation.datasite import *
from bs4 import BeautifulSoup

class DatasiteTestCase(TestCase):

    def test_date(self):
        result = make_format_date('2 may 2022')
        self.assertEqual('2022-05-02', result)
    
    def test_source(self):
        result = get_source('https://scitechdaily.com/news/biology/')
        self.assertEqual('scitechdaily.com', result)

    def test_path(self):
        result = convert_to_path('https://news.mit.edu/sites/default/files/styles/term_page__news_article/public/images/202204/MIT-AAAS-Members-01-press.jpg?itok=lY3DTd1s', 'math')
        self.assertEqual('images/MIT-AAAS-Members-01-press_math.jpg', result) 

    def test_math_data(self):
        with open('/home/michael/code/homeserversolution/homeservertest/newscreation/templates/newscreation/example_m.html') as fp:
            soup = BeautifulSoup(fp, "lxml")
        result = dict((get_math_news(soup)[:1][0]))
        checked_data = sorted(result.items(), key=lambda x: x[0])
        data = {"title":"Peter Shor receives 2022-2023 Killian Award","description":"The MIT professor is honored for extraordinary accomplishments in mathematics, computer science, and quantum physics.","img_link":"https://news.mit.edu/sites/default/files/styles/term_page__news_article/public/images/202205/MIT-Shor-Peter-01-press.jpg?itok=I8FjfyAJ","img_path":"images/MIT-Shor-Peter-01-press_math.jpg","content_link":"https://news.mit.edu/2022/peter-shor-receives-2022-2023-killian-award-0511","date_published":"2022-05-11","source":"news.mit.edu","cat_id":"1"}
        expected_data = sorted(data.items(), key=lambda x: x[0])
        self.assertEqual(expected_data, checked_data)

    def test_physics_data(self):
        with open('/home/michael/code/homeserversolution/homeservertest/newscreation/templates/newscreation/example_p.html') as fp:
            soup = BeautifulSoup(fp, "lxml")
        result = dict((get_physics_news(soup)[:1][0]))
        checked_data = sorted(result.items(), key=lambda x: x[0])
        data = {"cat_id":"2","title":"Pythagorean Astronomy: Routine Spaceflight?","description":"It’s not often that a new astronomical phenomenon is named, but this month we have a new one. The name might not be that original, but there have been the first observations of something known as a “micronova”. Lasting just a few hours, a micronova is much fainter than a typical “nova”, making them much","img_link":"https://blogs.cardiff.ac.uk/physicsoutreach/wp-content/uploads/sites/236/2022/05/micronova_eso2207a-170x96.jpg","img_path":"images/micronova_eso2207a-170x96_physics.jpg","content_link":"https://blogs.cardiff.ac.uk/physicsoutreach/2022/05/07/pythagorean-astronomy-routine-spaceflight/","date_published":"2022-05-07","source":"blogs.cardiff.ac.uk"}
        expected_data = sorted(data.items(), key=lambda x: x[0])
        self.assertEqual(expected_data, checked_data)
        

    def test_biology_data(self):
        with open('/home/michael/code/homeserversolution/homeservertest/newscreation/templates/newscreation/example_b.html') as fp:
            soup = BeautifulSoup(fp, "lxml")
        result = dict((get_biology_news(soup)[1:2][0]))
        checked_data = sorted(result.items(), key=lambda x: x[0])
        data = {"cat_id":"3","title":"Fly Researchers at Duke University Find Another Layer to the Code of Life","description":"Rare pieces of genetic code may serve as another way to control cellular machinery. A new investigation into the way different tissues read information from…","img_link":"https://scitechdaily.com/images/DNA-Map-Genetic-Code-Concept-260x146.jpg","img_path":"images/DNA-Map-Genetic-Code-Concept-260x146_biology.jpg","content_link":"https://scitechdaily.com/fly-researchers-at-duke-university-find-another-layer-to-the-code-of-life/","date_published":"2022-05-22","source":"scitechdaily.com"}
        expected_data = sorted(data.items(), key=lambda x: x[0])
        self.assertEqual(expected_data, checked_data)
        