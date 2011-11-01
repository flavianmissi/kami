class Kami(object):

    def __init__(self):
        self.raw_query = ''

    def filter(self, **params):
        """ Simple key value search query """
        self._combine(Q(**params).to_query())
        return self

    def exclude(self, **params):
        """ Exclude a statement in the query """
        self._combine(~Q(**params))
        return self

    def _combine(self, query):
        if self.raw_query:
            self.raw_query = "%s AND %s" % (self.raw_query, query)
        else:
            self.raw_query = query


class Q(object):

    def __init__(self, **params):
        self.params = params

    def __and__(self, other):
        return '%s AND %s' % (self.to_query(), other.to_query())

    def __or__(self, other):
        return '%s OR %s' % (self.to_query(), other.to_query())

    def __invert__(self):
        return self.to_query(negate=True)

    def to_query(self, negate=False):
        query = []
        for key, value in self.params.items():
            query.append('%s: "%s"' % (key, value))

        if negate:
            query = ["NOT %s" % q for q in query]

        query = ' AND '.join(query)
        return query
