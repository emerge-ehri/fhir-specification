.. _home:

*********************************
eMERGE Results FHIR Specification
*********************************

Introduction
============
Simple description (what is this doc)

How to read this Guide
======================
This Guide is divided into several pages which are listed at the top of each page in the menu bar.

* Home: ....

* Design: ...  (reports, mapping, fhir hierarchy)

* Artifacts: ... (catalogue of artifacts & detailed pages)

     * Catalogue (classified as core, ig, custom)  (table of resources)

     * (Detailed Artifact Pages)

* Discussion: ... (identified issues and use cases)

* Supplemental Material: ... (presentation, paper, github, etc...)

.. Examples (example data, json, nice to have)

.. _cgig:

FHIR Genomics Reporting Implementation Guide
============================================
This specification in built on top of the |fhir-gr-ig| which is under active
development by the |hl7-cg-wg|. During the development of this specification the
|fhir-gr-ig| progressed from Draft to Standard for Trial Use version 1.


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

eMERGE is piloting and implementation of this specification
in conjunction with its development and release which includes a subset of the
eMERGEseq Platform's panel results returned from the SCs.

The aim of the eMERGE test results return specification and implementation is to
inform the efforts of the HL7 CG workgroup so as to accelerate the process towards
a normative standard for general practice in clinical genetic test reporting.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   report_structure
   artifacts/index
   discussion
   supplemental_materials
