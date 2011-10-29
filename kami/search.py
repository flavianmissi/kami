class Kami(object):

    def search(self, **params):
        return self._mount_query(**params)

    def exclude(self, **params):
        return self._mount_query('NOT ', **params)

    def _mount_query(self, logical_operator='', **params):
        """
        Mount the query
        ``logical_operator`` must end with a blank space, it avoids white spaces
        when the query doesn't need them
        ``params`` field=value params
        """
        query = []
        for key, value in params.items():
            query.append('%s%s: "%s" AND' % (logical_operator, key, value))

        query = " ".join(query)[:-4]

        return query
