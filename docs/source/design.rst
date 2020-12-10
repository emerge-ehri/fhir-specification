.. _design:

Design & Development
=====================

.. Warning::
    This document is a work in progress and is not ready for production use.

.. sidebar:: Contents

    * :ref:`rept-examples`
    * :ref:`rept-struct`
    * :ref:`fhir-rept-resources`    

The design of a HL7 FHIR Genomics Reporting IG based specification for eMERGE Phase III electronic return of structured results was motivated by the following guiding principles:

1. **Structured content**
   - All content from the narrative PDF eMERGE reports and all eMERGE standard reporting use cases should be captured in structured format and as meaningful data elements without losing content and context.
2. **Alignment with HL7 FHIR Core and GR IG**
   - All eMERGE concepts and associated elements shall be aligned with GR IG and FHIR Core Standards and extended as required.
3. **Computationally reliable representation of results**
   - An optimal computational form for each data element shall be determined, prioritizing eMERGE pilot objectives for EHR integration and CDS. All specimen types and genetic data elements related to the resulting observations must be based on reference sequences, coordinates and structures that consistently and accurately reflect the lab methods used to align the raw data, determine coverage and call the variants.
4. **Codify concepts when reasonable**
   - Concepts should be codified using FHIR Core and GR IG guidance. eMERGE concepts that extend beyond the FHIR and CG guidance should be codified if possible and within reason.

The principle outcomes of the eMERGE FHIR Specification development were to 

1. Identify the complete set of report concepts and elements used throughout all eMERGE reporting use case;
2. Create a FHIR based schema using the GR IG that was implementable by eMERGE;
3. Provide a public document of the eMERGE FHIR specification; 
4. Collaborate with the HL7 CG Workgroup to harmonize useful feedback into the GR IG and FHIR Specification in general.


The design and development of the eMERGE FHIR Specification consisted of the following steps - 

Identification of eMERGE Report Concepts and Elements
------------------------------------------------------

The first step towards the creation of the eMERGE FHIR Specification was an “As Is” analysis of the existing genetic reports to inventory all eMERGE reporting concepts and elements. To this end, we compiled a set of all-inclusive representative reports from both the CSGs (see Figure 1 for a de-identified example report from each CSG) to ensure use cases requiring unique report concepts and elements were included.


.. figure:: _images/hgsc-report-plain.png
   :alt: HGSC eMERGE Report
   :height:  600 px
   :class: sidebyside

.. figure:: _images/lmm-report-plain.png
   :alt: LMM eMERGE Report
   :height:  600 px
   :class: sidebyside

.. rst-class:: clearsidebyside

**Figure 1:** HGSC & LMM eMERGE Report Examples (click to enlarge)

Using selected reports for these use cases, the structure and composition of the reports was analyzed and a set of data elements was assembled (Figures 2 & 3), resulting in 18 core concepts and around 100 fundamental data elements. This analysis and documentation of the existing eMERGE report content served as the foundation for the design of the eMERGE FHIR Specification. 

.. figure:: _images/hgsc-report-layout.png
   :alt: HGSC eMERGE Report Layout
   :class: sidebyside

.. figure:: _images/hgsc-report-mapped.png
   :alt: HGSC eMERGE Example Report Detailed Mapping
   :height:  600 px
   :class: sidebyside

.. rst-class:: clearsidebyside

**Figure 2:** HGSC general report layout and detailed mapping (click to enlarge)


.. figure:: _images/lmm-report-layout.png
   :alt: LMM eMERGE Report Layout
   :class: sidebyside

.. figure:: _images/lmm-report-mapped.png
   :alt: LMM eMERGE Example Report Detailed Mapping
   :height:  600 px
   :class: sidebyside

.. rst-class:: clearsidebyside

**Figure 3:** LMM general report layout and detailed mapping (click to enlarge)


eMERGE Report to FHIR Genomics Reporting Implementation Guide - Mapping and Analysis
---------------------------------------------------------------------------------------

The next step in the development of the eMERGE FHIR Specification was the mapping of eMERGE report concepts and elements to the Genomics Reporting Implementation Guide (GR IG). Adopting the GR IG's guidance, all major eMERGE report concepts were aligned to the GR IG resources and profiles, followed by a granular mapping of every eMERGE report element to a corresponding FHIR resource element.

The GR IG provided the guidance for driving the mapping of the eMERGE report concepts to its resources, profiles and extensions. Our first attempt at mapping resulted in several key structural and organizational questions, documented at :ref:`Issues & Resolutions<issues-and-resolutions>`.

Addressing and resolving these issues resulted in the mapping and structural design of the  specification, illustrated in Figure 4. As illustrated, the root profile of the specification is the GenomicsReport; this is the key resource that encapsulates the ServiceRequest for the test, the Observations that constitute the results (i.e. findings or implications of the test), the Tasks that include clinical care recommendations, and the Grouper Profile to organize and manage composite resulting (i.e. GenePanel and PGx results). Other major resources attached to the GenomicsReport include the Patient for whom the test is being ordered, the associated Specimen, the Practitioner ordering the test, the Organization (i.e. Diagnostic Laboratory performing the test) and the Practitioner interpreting the results of the test. 

.. figure:: _images/schema-overview.png
   :align: left

   **Figure 4: FHIR Diagnostic Report Schema Alignment**
   An illustration of the associations between the major report components and FHIR Diagnostic Report Schema.

We then mapped every eMERGE report attribute to an equivalent field in the FHIR resources identified in the previous step. This was a laborious process which in addition to requiring precise and careful mapping of the fields themselves, also required determining naming systems and assignment of coding systems, codes and values. The :ref:`artifacts section<artifacts>` includes the complete set of eMERGE FHIR resources and its associated elements, with a summary listed in Table 2. Furthermore, gap analysis at this step revealed the need for additional fields such as summary interpretation text, test disclaimer etc. that were not available in the GR IG. Though we documented these as feature requests in HL7’s Tracking System Jira, to satisfy the immediate needs of the project, we created these fields as FHIR Extensions. 

.. list-table::
   :class: my-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   * - No.
     - Element
     - FHIR Resource
     - IG Profile/Ext
     - Related Properties
   * - 1
     - Report
     - |diagnosticreport-res|
     - |genomics-report-prof|
     - | Test Disclaimer,
       | Gene Coverage
   * - 2
     - Patient
     - |patient-res|
     - none
     -
   * - 3
     - Sample / Specimen
     - |specimen-res|
     - |specimen-prof|
     -
   * - 4
     - Request / Orderer
     - |servicerequest-res|
     - |service-request-prof|
     -
   * - 5
     - Test Performed ...
     - |plandefinition-res|
     - none
     - | ...Name,
       | ...Background,
       | ...Methodology,
       | ...References
   * - 6
     - | Ordering Provider,
       | Results Interpreter
     - |practitionerrole-res|
     - none
     -
   * - 7
     - Performing Lab
     - |organization-res|
     - none
     -
   * - 8
     - Recommendations (Proposed)
     - |task-res|
     - |recommended-followup-prof|
     -
   * - 9
     - Comments (Additional Notes)
     - |observation_res|
     - none
     -
   * - 10
     - Overall Interpretation
     - |observation-res|
     - |overall-interp-prof|
     - Summary Text
   * - 11
     - Diagnostic Gene Panel Results Group
     - |observation-res|
     - |grouper-prof|
     - Summary Text
   * - 12
     - Clinical Interpretation
     - |observation-res|
     - |inh-dis-path-prof|
     -
   * - 13
     - PGx Gene Panel Results Group
     - |observation-res|
     - |grouper-prof|
     -
   * - 14
     - Medication Implication
     - |observation-res|
     - | |metab-impl-prof-abbr|,
       | |transport-impl-prof-abbr|,
       | |efficacy-impl-prof-abbr|
     -
   * - 15
     - Identified Variant Genotype
     - |observation-res|
     - |variant-prof|
     -
   * - 16
     - Identified Variant Diplotype
     - |observation-res|
     - |genotype-prof|
     -
   * - X5
     - Summary Text
     - none
     - custom
     -
   * - X6
     - Test Disclaimer
     - none
     - custom
     -
   * - X7
     - Gene Coverage
     - none
     - |related-artifact-ext|
     -

