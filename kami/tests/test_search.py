from unittest import TestCase

from search import Kami


class SimpleSearchQueryTestCase(TestCase):

    def setUp(self):
        self.kami = Kami()

    def test_should_pass_title(self):
        self.assertEqual('title: "Mein Teil"', self.kami.search(title='Mein Teil'))

    def test_should_pass_artist_and_title(self):
        query = self.kami.search(title='Mein Teil', artist='Rammstein')
        self.assertEqual('title: "Mein Teil" AND artist: "Rammstein"', query)

    def test_should_have_one_AND_only_between_a_pair_of_statements(self):
        query = self.kami.search(title='Mein Teil', artist='Rammstein', album='Reise, Reise')
        self.assertEqual('album: "Reise, Reise" AND title: "Mein Teil" AND artist: "Rammstein"', query)


class SimpleExcludeSearchQueryTestCase(TestCase):

    def setUp(self):
        self.kami = Kami()

    def test_should_pass_a_title_and_get_its_negation(self):
        self.assertEqual('NOT title: "Mein Teil"', self.kami.exclude(title='Mein Teil'))

    def test_should_negate_and_concatenate_when_receive_two_fields(self):
        self.assertEqual('NOT album: "Reise, Reise" AND NOT title: "Amerika"', self.kami.exclude(title='Amerika', album='Reise, Reise'))
