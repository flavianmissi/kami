from unittest import TestCase

from kami import Kami, Q

#TODO test format equality by regex


class FilterQueryTestCase(TestCase):

    def setUp(self):
        self.kami = Kami()

    def test_should_pass_title(self):
        query = self.kami.filter(title='Mein Teil').raw_query
        self.assertEqual('title: "Mein Teil"', query)

    def test_should_pass_artist_and_title(self):
        query = self.kami.filter(title='Mein Teil', artist='Rammstein').raw_query
        self.assertEqual('artist: "Rammstein" AND title: "Mein Teil"', query)

    def test_should_have_one_AND_only_between_a_pair_of_statements(self):
        query = self.kami.filter(title='Mein Teil', artist='Rammstein', album='Reise, Reise').raw_query
        self.assertEqual('album: "Reise, Reise" AND artist: "Rammstein" AND title: "Mein Teil"', query)

    def test_should_support_calling_filter_method_with_Q_objects_as_params(self):
        query = self.kami.filter(Q(title='Mein Teil') & Q(artist='Rammstein')).raw_query
        self.assertEqual('title: "Mein Teil" AND artist: "Rammstein"', query)

    def test_should_call_filter_with_Q_objects_separeted_with_OR(self):
        query = self.kami.filter(Q(title='Mein Teil') | Q(artist='Rammstein')).raw_query
        self.assertEqual('title: "Mein Teil" OR artist: "Rammstein"', query)

    def test_should_call_filter_with_Q_objects_negating_an_parameter(self):
        query = self.kami.filter(~Q(title='Mein Teil') | Q(artist='Rammstein')).raw_query
        self.assertEqual('NOT title: "Mein Teil" OR artist: "Rammstein"', query)


class ExcludeSearchQueryTestCase(TestCase):

    def setUp(self):
        self.kami = Kami()

    def test_should_pass_a_title_and_get_its_negation(self):
        query = self.kami.exclude(title='Mein Teil').raw_query
        self.assertEqual('NOT title: "Mein Teil"', query)

    def test_should_negate_and_concatenate_when_receive_two_fields(self):
        query = self.kami.exclude(title='Amerika', album='Reise, Reise').raw_query
        self.assertEqual('NOT album: "Reise, Reise" AND NOT title: "Amerika"', query)

    def test_should_raise_an_error_when_trying_to_call_exclude_with_Q_objects_as_params(self):
        with self.assertRaises(ValueError):
            self.kami.exclude(Q(title='Mein Teil') | Q(artist='Rammstein')).raw_query

class ExcludeAndFilterMustWorkTogetherTestCase(TestCase):

    def setUp(self):
        self.kami = Kami()

    def test_should_search_for_field_title_and_negate_the_album(self):
        query = self.kami.filter(title='Mein').exclude(album='Mutter').raw_query
        self.assertEqual('title: "Mein" AND NOT album: "Mutter"', query)

    def test_glue_between_search_and_exclude_methods_should_be_AND_by_default(self):
        query = self.kami.filter(title='Mein').exclude(album='Mutter').raw_query
        self.assertNotIn('OR', query)
