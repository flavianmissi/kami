from unittest import TestCase
from kami import Q


class BaseQueryBuilderTestCase(TestCase):

    def test_should_concatenate_two_queries_with_and(self):
        q = Q(title='Mein Teil') & Q(album='Reise, Reise')
        self.assertEqual('title: "Mein Teil" AND album: "Reise, Reise"', q.query)

    def test_should_concatenate_two_queries_with_more_than_one_param_for_each_call_to_Q(self):
        q = Q(title='Mein Teil', artist='Rammstein') & Q(album='Reise, Reise')
        self.assertEqual('artist: "Rammstein" AND title: "Mein Teil" AND album: "Reise, Reise"', q.query)

    def test_should_concatenate_two_queries_with_or(self):
        q = Q(title='Mein Teil') | Q(album='Reise, Reise')
        self.assertEqual('title: "Mein Teil" OR album: "Reise, Reise"', q.query)

    def test_should_concatenate_two_queries_with_more_then_one_param_for_each_call_to_Q_using_AND_and_OR(self):
        q = Q(title='Mein Teil', artist='Rammstein') | Q(album='Reise, Reise')
        self.assertEqual('artist: "Rammstein" AND title: "Mein Teil" OR album: "Reise, Reise"', q.query)

    def test_should_negate_a_query_calling_tilde(self):
        q = ~Q(artist='Rammstein')
        self.assertEqual('NOT artist: "Rammstein"', q.query)

    def test_should_use_AND_with_negation(self):
        q = Q(title='Mein Teil') & ~Q(album='Mutter')
        self.assertEqual('title: "Mein Teil" AND NOT album: "Mutter"', q.query)

    def test_should_use_OR_with_negation(self):
        q = Q(title='Mein Teil') | ~Q(album='Mutter')
        self.assertEqual('title: "Mein Teil" OR NOT album: "Mutter"', q.query)

    def test_should_use_negation_with_OR(self):
        q = ~Q(title='Mein Teil') | Q(album='Mutter')
        self.assertEqual('NOT title: "Mein Teil" OR album: "Mutter"', q.query)
