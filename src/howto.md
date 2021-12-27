How To - Project Documentation
======================================================================

Get Started
----------------------------------------------------------------------

Documentation can be written as rst or md files in the `codershq/docs/src`.


To build and serve docs, use the commands:
    ::

        docker-compose -f local.yml up docs


Changes to files in `docs/src` will be picked up and reloaded automatically.

`MdBook <https://rust-lang.github.io/mdBook/>`_ is the tool used to build documentation.
