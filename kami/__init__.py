class Kami(object):

    def __init__(self):
        self.raw_query = ''

    def filter(self, **params):
        """ Simple key value search query """
        self._combine(Q(**params).to_query())
        return self

    def exclude(self, **params):
        """ Exclude a statement in the query """
        self._combine((~Q(**params)).query)
        return self

    def _combine(self, query):
        if self.raw_query:
            self.raw_query = "%s AND %s" % (self.raw_query, query)
        else:
            self.raw_query = query

class Q(object):

    OR = 'OR'
    AND = 'AND'

    def __init__(self, **params):
        self.params = params
        self.to_query()

    def __and__(self, other):
        self.query = '%s AND %s' % (self.query, other.query)
        return self

    def __or__(self, other):
        self.query = '%s OR %s' % (self.query, other.query)
        return self

    def __invert__(self):
        self.query = self.to_query(negate=True)
        return self

    def to_query(self, negate=False):
        query = []
        for key, value in self.params.items():
            query.append('%s: "%s"' % (key, value))

        if negate:
            query = ["NOT %s" % q for q in query]

        self.query = ' AND '.join(query)
        return self.query
