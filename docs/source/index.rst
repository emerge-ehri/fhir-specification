.. _home:

*********************************
eMERGE Results FHIR Specification
*********************************

.. sidebar:: Contents

    * :ref:`intro`
    * :ref:`howtoread`
    * :ref:`cgig`
    * :ref:`emerge3`
    * :ref:`emerge-pilot`
    * :ref:`spec-aims`

.. _intro:

Introduction
============
Simple description (what is this doc)



.. _howtoread:

How to read this Guide
======================
This Guide is divided into several pages which are listed at the top of each page in the menu bar.

* :ref:`Home<home>`: The home page provides the introduction and background for the eMERGE Results FHIR Specification.

* Design: These pages provide insights into the design process used to generate the specification.

    * Report Structure: , mapping, fhir hierarchy)

* Artifacts: ... (catalogue of artifacts & detailed pages)

     * Catalogue (classified as core, ig, custom)  (table of resources)

     * (Detailed Artifact Pages)

* Discussion: ... (identified issues and use cases)

* Supplemental Material: ... (presentation, paper, github, definitions spreadsheet, examples, etc...)

.. Examples (example data, json, nice to have)

.. _cgig:

FHIR Genomics Reporting IG
==========================
This specification in built on top of the |fhir-gr-ig| which is under active
development by the |hl7-cg-wg|. During the development of this specification the
|fhir-gr-ig| progressed from Draft to Standard for Trial Use version 1.

.. _emerge3:

eMERGE Phase III Results
========================
The eMERGE Results HL7 FHIR Specification is a product of the
|emerge-network| and was initiated by the |ehri-workgroup| during phase
III of the study. It focuses on providing an HL7 FHIR electronic message standard
for returning the lab results for the |emerge-seq| panel
assays performed by the two eMERGE Sequencing Centers (SC) for
the `individual eMERGE sites <https://emerge-network.org/emerge-sites/>`__.
During the fulfillment of the eMERGESeq Platform of phase III an XML schema was
specified and all results were generated, delivered and stored using this format.
This specification is an evolution of the phase III eMERGE XML structure Schema.

.. _emerge-pilot:

eMERGE Pilot Implementation
===========================
eMERGE is piloting and implementation of this specification
in conjunction with its development and release which includes a subset of the
eMERGEseq Platform's panel results returned from the SCs.

.. _spec-aims:

Specification Aim
==================
The aim of the eMERGE test results return specification and implementation is to
inform the efforts of the HL7 CG workgroup so as to accelerate the process towards
a normative standard for general practice in clinical genetic test reporting.

.. toctree::
   :hidden:

   report_structure
   artifacts/index
   discussion
   supplemental_materials
