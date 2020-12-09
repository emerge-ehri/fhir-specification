.. _design:

Design
=======

.. Warning::
    This document is a work in progress and is not ready for production use.

.. sidebar:: Contents

    * :ref:`rept-examples`
    * :ref:`rept-struct`
    * :ref:`fhir-rept-resources`

The creation of a HL7 FHIR based specification for eMERGE III electronic return of structured results is motivated by several key design principles:

1. **Structured content - **
   All content from the narrative PDF eMERGE reports and all eMERGE standard reporting use cases should be captured in structured format and as meaningful data elements without losing content and context.
2. **Alignment with HL7 FHIR Core and GR IG - **
   All eMERGE concepts and associated elements shall be aligned with GR IG and FHIR Core Standards and extended as required.
3. **Computationally reliable representation of results - **
   An optimal computational form for each data element shall be determined, prioritizing eMERGE pilot objectives for EHR integration and CDS. All specimen types and genetic data elements related to the resulting observations must be based on reference sequences, coordinates and structures that consistently and accurately reflect the lab methods used to align the raw data, determine coverage and call the variants.
4. **Codify concepts when reasonable - **
   Concepts should be codified using FHIR Core and GR IG guidance. eMERGE concepts that extend beyond the FHIR and CG guidance should be codified if possible and within reason.


.. _rept-examples:

Example Reports
-----------------

The eMERGE reporting process is supported by two separate clinical workflows at the
corresponding sequencing centers (SCs); The HGSC Lab at Baylor College of Medicine and
The LMM Lab at Partners Healthcare (in conjunction with Broad Institute).

Below are two example (deidentified) positive reports one from each of the two SCs.

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

This section introduces the process used to convert and map these two similar reports into a common HL7 FHIR structure.

.. _rept-struct:

Report Layout & Structure
--------------------------

The subsections below show figures containing a general report model alongside an
example report with all of the detailed elements mapped using coloring and numbered call outs.
Each subsection represents one of the two SC report designs shown in the preceding section.
This structuring and mapping exercise was thoroughly reviewed and vetted by users at
each of the two SCs.

HGSC Report Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^

TODO <add a brief description of the common vs different elements from that of LMM>

The HGSC general report layout and detailed mapping to their example report...


.. figure:: _images/hgsc-report-layout.png
   :alt: HGSC eMERGE Report Layout
   :class: sidebyside

.. figure:: _images/hgsc-report-mapped.png
   :alt: HGSC eMERGE Example Report Detailed Mapping
   :height:  600 px
   :class: sidebyside

.. rst-class:: clearsidebyside

**Figure 2:** HGSC general report layout and detailed mapping (click to enlarge)


LMM Report Structure
^^^^^^^^^^^^^^^^^^^^^^^^^

TODO <add a brief description of the common vs different elements from that of HGSC>

The LMM general report layout and detailed mapping to their example report...

.. figure:: _images/lmm-report-layout.png
   :alt: LMM eMERGE Report Layout
   :class: sidebyside

.. figure:: _images/lmm-report-mapped.png
   :alt: LMM eMERGE Example Report Detailed Mapping
   :height:  600 px
   :class: sidebyside

.. rst-class:: clearsidebyside

**Figure 3:** LMM general report layout and detailed mapping (click to enlarge)

FHIR Mapping
----------------

The principle outcomes of the eMERGE FHIR Specification development were to 

1. Identify the complete set of report concepts and elements used throughout all eMERGE reporting use case;
2. Create a FHIR based schema using the GR IG that was implementable by eMERGE;
3. Provide a public document of the eMERGE FHIR specification; 
4. Collaborate with the HL7 CG Workgroup to harmonize useful feedback into the GR IG and FHIR Specification in general.

.. _fhir-rept-resources:

FHIR Report Schema & Resources
------------------------------

.. figure:: _images/schema-overview.png
   :align: left

   **Figure 4: FHIR Diagnostic Report Schema Alignment**
   An illustration of the associations between the major report components and FHIR Diagnostic Report Schema.

FHIR Mapping
----------------

The principle outcomes of the eMERGE FHIR Specification development were to 

1. identify the complete set of report concepts and elements used throughout all eMERGE reporting use case;
2. Create a FHIR based schema using the GR IG that was implementable by eMERGE;
3. Provide a public document of the eMERGE FHIR specification; 
4. Collaborate with the HL7 CG Workgroup to harmonize useful feedback into the GR IG and FHIR Specification in general.

The development of the eMERGE FHIR Specification consisted of the following steps - 

- Identify data elements using existing results from a comprehensive set of eMERGE reporting use cases. Here, the scope of this effort was confined to the Standard Reporting use cases and result delivery, while including provisions for future expansion. 
- Map eMERGE report elements and structures both semantically and structurally to GR IG resources and profiles; perform an analysis, identify issues that required further resolution, and propose resolutions.
- Harmonize and document finalized decisions informed by 
	- Harmonizing changes with GR IG
	- Documenting resolutions requiring custom profiles & extensions
	- Feedback from BCM-HGSC lab pilot development.

With the emergence of FHIR as an interoperable healthcare standard and the work of the HL7 Clinical Genomics (CG) Workgroup towards the creation of a FHIR Genomics Reporting Implementation Guide (GR IG){Updating}, the Network decided to develop and evaluate the GR IG in an effort to contribute to and validate the nascent GR IG.


TODO <discuss the process for mapping CG IG profiles and FHIR resources to elements.>
          <and mention the decision to follow the Genomics Reporting IG vs starting from scratch>


Genomics Reporting Guidance from IG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The eMERGE results FHIR is based on the Genomics Reporting profile and guidance from the |fhir-gr-ig|.

This specification aims to harmonize and leverage the draft work of the HL7 CG WG to both validate and inform its development.
In cases where there are gaps or requirements that are unclear or unmet, they are raised with the HL7 CG WG and
custom extensions or profiles are developed to fill the missing needs with the expectation that these issues
will ultimately be reconcilable as the standard matures.

The table below lists the eMERGE report components and their preferred alignment
based on the HL7 CG Genomics Reporting IG specification. For components that do not
align cleanly alternative solutions are provided including but not limited to the
introduction of custom extensions. The following section on Artifacts has a comprehensive
catalogue of every resource, profile and extension used by this eMERGE specification.

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
