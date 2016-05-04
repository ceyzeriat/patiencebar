patiencebar
===========

Terminal progress bar compatible with multi-threading

Built by `Guillaume Schworer <https://github.com/ceyzeriat>`_. Licensed under
the GNU General Public License v3 or later (GPLv3+) license (see ``LICENSE``).


Installation
------------

Just run

::

    pip install patiencebar

to get the most recent stable version.


Usage
-----

The main entry points are the ``patiencebar.Patiencebar`` and ``patiencebar.Patiencebarmulti`` classes. You'll just use it
like this:

::

    import patiencebar as PB

    n_calc = 34
    pb = PB.Patiencebar(valmax=n_calc, barsize=50, title="Test bar")
    for i in range(n_calc):
        dostuff()
        pb.update()

More usage details, see `example.py
<https://github.com/ceyzeriat/patiencebar/blob/master/example.py>`_)


Documentation
-------------

All the options are documented in the docstrings for the ``Patiencebar`` and
``Patiencebarmulti`` classes. These can be viewed in a Python shell using:

::

    import patiencebar as PB
    print(PB.Patiencebar.__doc__)
    print(PB.Patiencebarmulti.__doc__)

or, in IPython using:

::

    import patiencebar as PB
    PB.Patiencebar?
    PB.Patiencebarmulti?



License
-------

Copyright 2016 Guillaume Schworer

patiencebar is free software made available under the GNU General
Public License v3 or later (GPLv3+) license (see ``LICENSE``).
