Welcome to the eMERGE FHIR Specification Project
=================================================

|docs|

Purpose
-------
This is a ReadTheDocs project that is the source of the eMERGE FHIR specification.

Documentation for the Specification
------------------------------------

You will find complete documentation for the eMERGE FHIR Specification at `the eMERGE Results FHIR Specification site`_.

.. _the eMERGE Results FHIR Specification site: https://emerge-fhir-spec.readthedocs.io/


Development Setup
------------------

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See build the documentation locally. All changes committed to this project will automatically trigger the build of the readthedocs.io project that publishes the `the eMERGE Results FHIR Specification site`_.

Prerequisites
^^^^^^^^^^^^^

python 3.7.4

.. code-block:: 

   # Install Python3... after install
   >pip --version
   pip 19.1.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)

Installing
^^^^^^^^^^^

A step by step series of examples that tell you how to get the project building

Install the sphinx project requirements

.. code-block::

   > cd docs
   docs> pip install -r requirements.txt

Build the documentation from the docs folder

.. code-block::

   docs> make html

View the local documentation build

.. code-block::

   docs> open bulid/html/index.html

Versioning
-----------

We use `SemVer`_ for versioning. For the versions available, see the `tags on this repository`_.

.. _SemVer: http://semver.org/
.. _tags on this repository: https://github.com/emerge-ehri/fhir-specification/tags

Authors
---------

* **Mullai Murugan** - *Initial work* - `BCM-HGSC <https://www.hgsc.bcm.edu/>`_
* **Larry Babb** - *Initial work* - `Broad Institute <https://www.broadinstitute.org/>`_

**TBD** See also the list of `contributors <https://github.com/emerge-ehri/fhir-specification/contributors>`_ who participated in this project.

License
---------

This project is licensed under the MIT License - see the `LICENSE.md <LICENSE.md>`_ file for details

Acknowledgments
-----------------

* HL7 CG Working Group - FHIR CG IG
* etc


.. |docs| image:: https://readthedocs.org/projects/emerge-fhir-spec/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://emerge-fhir-spec.readthedocs.io/en/latest/?badge=latest
