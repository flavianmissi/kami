def search(**params):
    query = []
    for key, value in params.items():
        query.append('AND %s: "%s"' % (key, value))

    query = " ".join(query)[4:]

    return query
