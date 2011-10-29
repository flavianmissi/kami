class Kami(object):

    def __init__(self):
        self.raw_query = ''

    def search(self, **params):
        """ Simple key value search query """
        self._filter_or_exclude(**params)
        return self

    def exclude(self, **params):
        """ Exclude a statement in the query """
        self._filter_or_exclude(prepend_operator='NOT', **params)
        return self

    def _filter_or_exclude(self, logical_operator='AND', prepend_operator='', **params):
        """
        Add AND, OR filters to a query or exclude prepending the NOT operator
        ``logical_operator`` The glue operator to the query. Default is ``AND``
        ``prepend_operator`` The operator that prepends each statement, in case of ``exclude``, it's NOT by default.
        ``params`` field=value params
        """
        query = []

        for key, value in params.items():
            query.append('%s: "%s"' % (key, value))

        if prepend_operator:
            query = ["%s %s" % (prepend_operator, query_statement) for query_statement in query]

        query = (" %s " % logical_operator).join(query)
        if self.raw_query:
            self.raw_query = "%s AND %s" % (self.raw_query, query)
        else:
            self.raw_query = query

        return self.raw_query
