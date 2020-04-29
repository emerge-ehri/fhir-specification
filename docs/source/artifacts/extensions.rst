.. _extensions:

Extensions
==========

The eMERGE Results FHIR Reports use several FHIR extensions to supplement the resources and profiles specified by the the |fhir-gr-ig-short|. When an extension was warranted the process was to find an available extension amongst those defined as part of the |fhir-gr-ig-short|, then to look at other registered extensions available in the FHIR specification and finally to define our own custom extensions. All custom extensions were discussed with the HL7 Clinical Genomics WG as proposed additions to the |fhir-gr-ig-short|.

The list of extensions below are used throughout this specification are marked with their source or "emerge" if they were custom defined for this specification only. Additionally, each extension references the artifact that it is used by to provide context.

.. list-table::
   :class: my-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   * - No.
     - Extension
     - Source
     - Used In...
     - Description
   * - X1
     - BirthSex
     - US-Core
     - Patient
     - The birth sex extension is used to provide a specific biological sex for the patient being tested.
   * - X2
     - Ethnicity
     - US-Core
     - Patient
     - The ethnicity extension is used to provide a specific set of ethnicities for the patient being tested.
   * - X3
     - Race
     - US-Core
     - Patient
     - The race extension is used to provide a specific set of races for the patient being tested.
   * - X4
     - Age
     - eMERGE
     - Patient
     - The age extension is used to provide a specific age in years of the patient at the time of testing.
   * - X5
     - SummaryInterpretationText
     - eMERGE
     - DiagRept,Obs
     - The summary interpretation text extension is used to provide short narrative summary interpretations at the report level and any observation level as needed.
   * - X6
     - Test Disclaimer
     - eMERGE
     - GenomicsReport
     - The test disclaimer extension is used to return the performing lab's test disclaimer at the report level.
   * - X7
     - RelatedArtifact
     - hl7-cg-wg
     - GenomicsReport
     - The related artifact extension is used to allow emerge to return the Gene Coverage file (BED format) as an attachment.
   * - X8
     - RecommendedAction
     - eMERGE
     - GenomicsReport
     - The recommended action extension is used to return a top-level proposed recommendation from the lab to the ordering provider.