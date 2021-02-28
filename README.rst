cookiecutter-tiddlywiki-plugin
==============================

A `Cookiecutter`_ template for creating `TiddlyWiki`_ plugins.

This template creates the basic plugin structure as well as a documentation wiki.
Run ``make`` inside the plugin directory to build the documentation wiki.

Requirements
------------

* Python 3.6+
* `Cookiecutter`_
* `Yarn <https://yarnpkg.com/>`_

Variables
---------

``name``
   The name of the plugin without the publisher namespace, e.g., ``$:/plugins/publisher/{{ name }}``.

``project_slug``
   The name of plugin source directory, also used to construct the repository name.

``publisher``
   The publisher namespace, e.g., ``$:/plugins/{{ publisher }}/name``.

``type``
   One of ``plugin``, ``theme``, or ``language``.

``version``
   The plugin version.

``url``
   The plugin homepage. Defaults to a GitHub repository URL.

``author``
   Your full name.

``email``
   Your email address.

``description``
   A short description of the plugin. Also used as the site subtitle in the documentation wiki.

``license``
   Choose from one of several common open source licenses.

``include_github_fork_ribbon``
   Install the official `github-fork-ribbon plugin <https://github.com/Jermolene/TiddlyWiki5/tree/v5.1.23/plugins/tiddlywiki/github-fork-ribbon>`_ plugin.
   This adds a "Fork me on GitHub" ribbon to the top right corner of the documentation wiki.

.. _Cookiecutter: https://cookiecutter.readthedocs.io/
.. _TiddlyWiki: https://tiddlywiki.com/
