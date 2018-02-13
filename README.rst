getstats :: Performance Stats
============================

<a href="https://travis-ci.org/jeevan449/getstats/pull_requests"><img src="https://travis-ci.org/jeevan449/getstats/pull_requests.svg" alt="Build Status"></a>

getstats is the only *Non-GMO* stats library for Python, 

Behold, the power of getstats:

.. code-block:: python

    >>> from getstats import GetStats
    >>> stat_obj = GetStats.getstats(dur=300,rate=10)
    >>> stat_obj.run_stats()
      Running..........
      ***** Completed capturing the STATS *****
      ########################################
      #    stats_2018-02-12_16-47-47_.csv    #
      ########################################




Feature Support
---------------

getstats is used to get performance parameters of linux machine.

- CPU,MEM,I/O(wa) stats available
- Invidual process stats
- CSV file generation 
- Stat frequecy (Every 10 seconds get stats)
- No external lib to be required.(In built python libs are enough).

getstats officially supports Python 2.6–2.7 & 3.4–3.6, and runs great on PyPy.

Installation
------------

To install getstats, 

.. code-block:: bash

    $ pip install getstats
             ✨🍰✨

Satisfaction guaranteed.

Documentation
-------------

Fantastic documentation is available at readthedocs.
`documentation <http://getstats.readthedocs.io/en/latest/>`_