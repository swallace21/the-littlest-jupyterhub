.. _contributing/plugins:

============
TLJH Plugins
============

TLJH plugins are the official way to make customized 'spins' or 'stacks' 
with TLJH as the base. For example, the earth sciences community can make
a plugin that installs commonly used packages, set up authentication
and pre-download useful datasets. The mybinder.org community can
make a plugin that gives you a single-node, single-repository mybinder.org.
Plugins are very powerful, so the possibilities are endless.

Design
======

`pluggy <https://github.com/pytest-dev/pluggy>`_ is used to implement
plugin functionality. TLJH exposes specific **hooks** that your plugin
can provide implementations for. This allows us to have specific hook
points in the application that can be explicitly extended by plugins,
balancing the need to change TLJH internals in the future with the
stability required for a good plugin ecosystem. 

Writing a simple plugins
========================

We shall try to write a simple plugin that installs a few libraries,
and use it to explain how the plugin mechanism works. We shall call
this plugin ``tljh-simple``.

Plugin directory layout
-----------------------

We recommend creating a new git repo for your plugin. Plugins are
normal python packages - however, since they are usually simpler,
we recommend they live in one file.

For ``tljh-simple``, the repository's structure should look like:

.. code-block:: none
   
   tljh_simple:
    - tljh_simple.py
    - setup.py
    - README.md
    - LICENSE

The ``README.md`` (or ``README.rst`` file) contains human readable
information about what your plugin does for your users. ``LICENSE``
specifies the license used by your plugin - we recommend the 
3-Clause BSD License, since that is what is used by TLJH itself.

``setup.py`` - metadata & registration
--------------------------------------

``setup.py`` marks this as a python package, and contains metadata
about the package itself. It should look something like:

.. code-block:: python

    from setuptools import setup

    setup(
        name="tljh-simple",
        author="YuviPanda",
        version="0.1",
        license="3-clause BSD",
        url='https://github.com/yuvipanda/tljh-simple',
        entry_points={"tljh": ["simple = tljh_simple"]},
        py_modules=["tljh_simple"],
    )


This is a mostly standard ``setup.py`` file. ``entry_points={"tljh": ["simple = tljh_simple]}``
'registers' the module ``tljh_simple`` (in file ``tljh_simple.py``) with TLJH as a plugin.

``tljh_simple.py`` - implementation
-----------------------------------

In ``tljh_simple.py``, you provide implementations for whichever hooks
you want to extend. 

A hook implementation is a function that has the following characteristics:

#. Has same name as the hook
#. Accepts some or all of the parameters defined for the hook
#. Is decorated with the ``hookimpl`` decorator function, imported from
   ``tljh.hooks``.

The current list of available hooks and when they are called can be
seen in ```tljh/hooks.py`` <https://github.com/jupyterhub/the-littlest-jupyterhub/blob/master/tljh/hooks.py>`_
in the source repository.


This example provides an implementation for the ``tljh_extra_user_conda_packages``
hook, which can return a list of conda packages that'll be installed in users' 
environment from conda-forge.

.. code-block:: python

    from tljh.hooks import hookimpl

    @hookimpl
    def tljh_extra_user_conda_packages():
        return [
            'xarray',
            'iris',
            'dask',
        ]


Publishing plugins
==================

Plugins are python packages and should be published on PyPI. Users
can also install them directly from GitHub - although this is
not good long term practice. 

The python package should be named ``tljh-<pluginname>``.