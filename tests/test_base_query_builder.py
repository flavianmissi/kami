from unittest import TestCase
from kami import Q


class BaseQueryBuilderTestCase(TestCase):

    def test_should_concatenate_two_queries_with_and(self):
        self.assertEqual('title: "Mein Teil" AND album: "Reise, Reise"', Q(title='Mein Teil') & Q(album='Reise, Reise'))

    def test_should_concatenate_two_queries_with_more_than_one_param_for_each_call_to_Q(self):
        # Q(title='Mein Teil', artist='Rammstein') & Q(album='Reise, Reise')
        pass
