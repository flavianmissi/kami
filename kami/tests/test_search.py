from unittest import TestCase

from search import Kami

#TODO test format equality by regex


class SimpleSearchQueryTestCase(TestCase):

    def setUp(self):
        self.kami = Kami()

    def test_should_pass_title(self):
        query = self.kami.search(title='Mein Teil').raw_query
        self.assertEqual('title: "Mein Teil"', query)

    def test_should_pass_artist_and_title(self):
        query = self.kami.search(title='Mein Teil', artist='Rammstein').raw_query
        self.assertEqual('title: "Mein Teil" AND artist: "Rammstein"', query)

    def test_should_have_one_AND_only_between_a_pair_of_statements(self):
        query = self.kami.search(title='Mein Teil', artist='Rammstein', album='Reise, Reise').raw_query
        self.assertEqual('album: "Reise, Reise" AND title: "Mein Teil" AND artist: "Rammstein"', query)


class SimpleExcludeSearchQueryTestCase(TestCase):

    def setUp(self):
        self.kami = Kami()

    def test_should_pass_a_title_and_get_its_negation(self):
        query = self.kami.exclude(title='Mein Teil').raw_query
        self.assertEqual('NOT title: "Mein Teil"', query)

    def test_should_negate_and_concatenate_when_receive_two_fields(self):
        query = self.kami.exclude(title='Amerika', album='Reise, Reise').raw_query
        self.assertEqual('NOT album: "Reise, Reise" AND NOT title: "Amerika"', query)


class ExcludeAndSimpleSearchMustWorkTogetherTestCase(TestCase):

    def setUp(self):
        self.kami = Kami()

    def test_should_search_for_field_title_and_negate_the_album(self):
        query = str(self.kami.search(title='Mein').exclude(album='Mutter').raw_query)
        self.assertEqual('title: "Mein" AND NOT album: "Mutter"', query)
