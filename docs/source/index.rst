.. _home:

*********************************
eMERGE Results FHIR Specification
*********************************

.. Warning::
    This document is a work in progress and is not ready for production use.

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
The Electronic Medical Records and Genomics (eMERGE) Network, funded by the National Human Genome Research Institute (NHGRI), is a consortium of of U.S. medical research institutions that “develops, disseminates, and applies approaches to research that combine biorepositories with electronic medical record systems for genomic discovery and genomic medicine implementation research”. Phase III of this program, as part of the Network’s overarching goal to integrate genomic test results to the EHR for clinical care, sought to create a proof of concept, standards-based representation of clinical genomic test results using the rapidly evolving Health Level Seven (HL7) Fast Healthcare Interoperability Resource (FHIR) standard. The effort to implement a FHIR based specification for the eMERGE genetic test results using the HL7 FHIR Genomics Reporting Implementation Guide was managed by the two Centralized Sequencing and Genotyping Facilities (CSGs): the Broad Institute (BI) and Partners Laboratory for Molecular Medicine (LMM) and Baylor College of Medicine Human Genome Sequencing Center (BCM-HGSC).

Below you can find background information on :ref:`emerge3`, :ref:`emerge-pilot`, and :ref:`spec-aims`.

.. _howtoread:

How to read this Guide
======================
This Guide is divided into several pages which are listed at the top of each page in the menu bar.

* :ref:`Home<home>`: The home page provides the introduction and background for the eMERGE Results FHIR Specification.

* :ref:`design`: These pages provide insights into the process used to generate the specification.

    * :ref:`Example Reports<rept-examples>`: This section provides examples of the 2 different versions of lab reports used during eMERGE III.

    * :ref:`Report Layout & Structure<rept-struct>`: This section describes how the 2 different report versions were generalized and mapped into common components.

    * :ref:`FHIR Report Resources<fhir-rept-resources>`: This section introduces the FHIR Diagnostic Report and associated sub component resources relevant to the eMERGE report model.

* :ref:`Artifacts<artifacts>`: ... (catalogue of artifacts & detailed pages)

     * Catalogue (classified as core, ig, custom)  (table of resources)

     * Custom Extensions (3)

* :ref:`Issues & Resolutions<issues-and-resolutions>`: This section contains a comprehensive listing of issues in mapping and structuring the eMERGE data to the |fhir-gr-ig-short| and their resolutions.

* :ref:`Discussion<discussion>`: This section contains discussions on strategic concerns with adoption, concerns related to representing variation and potential future use cases.

* :ref:`Supplemental Material<supp-materials>`: ... (presentation, paper, github, definitions spreadsheet, examples, etc...)

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

   design
   artifacts/index
   issues_and_resolutions
   discussion
   supplemental_materials
