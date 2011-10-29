from unittest import TestCase

from search import search


class SimpleSearchQueryTestCase(TestCase):

    def test_should_pass_title(self):
        self.assertEqual('title: "Mein Teil"', search(title='Mein Teil'))

    def test_should_pass_artist_and_title(self):
        query = search(title='Mein Teil', artist='Rammstein')
        self.assertEqual('artist: "Rammstein" AND title: "Mein Teil"', query)

    def test_should_have_one_AND_only_between_a_pair_of_statements(self):
        query = search(title='Mein Teil', artist='Rammstein', album='Reise, Reise')
        self.assertEqual('album: "Reise, Reise" AND artist: "Rammstein" AND title: "Mein Teil"', query)
