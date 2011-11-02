Kami - solr queries made easy
=============================

Finding
-------

To make a simple query, just call the `find` method, passing the fields and values you want to retrieve::
    from kami import Kami
    kami = Kami()
    kami.find(title='Mein Teil', artist='Rammstein')

This will format and execute the query. To see the query mounted by kami, call the `raw_query` attribute::
    kami.find(title='Mein Teil', artist='Rammstein').raw_query

This will return something like that::
    'title: "Mein Teil" AND artist: "Rammstein"'

It is also supported to specify more than one value for each field::
    from kami import Kami
    kami = Kami()
    kami.find(title=('Mein Teil', 'Foo'), artist='Rammstein')

That will result in the following query::
    'title: ("Mein Teil" OR "Amerika")'


Excluding
---------

To exclude a field value from the search, use the `exclude` method::
    from kami import Kami
    kami = Kami()
    kami.exclude(title='Mein Teil')

And the resulting query::
    'NOT title: "Mein Teil"'


Nesting methods call
--------------------

Kami allows to nest method calls, so you are able to perform nested calls, e.g.::
    kami.find(title='Mein Teil').exclude(album='Mutter')

That will form the following query::
    'title: "Mein Teil" AND NOT album: "Mutter"'


Running tests
-------------

Use the make target `test` to run all tests. e.g.:
::
    $ make test

.. note::
    The test discovery uses built-in unittest2 auto discover, thus, to be able to use it, you must be running python 2.7
