.. _extensions:

Extensions
==========

(todo LB)

The eMERGE Results FHIR Reports use several FHIR extensions to supplement the resources and profiles specified by the the |fhir-gr-ig-short|. When an extension was warranted the process was to find an available extension amongst those defined as part of the |fhir-gr-ig-short|, then to look at other registered extensions available in the FHIR specification and finally to define our own custom extensions. All custom extensions were discussed with the HL7 Clinical Genomics WG as proposed additions to the |fhir-gr-ig-short|.

The list of extensions below are used throughout this specification are marked with their source or "emerge" if they were custom defined for this specification only. Additionally, each extension references the artifact that it is used by to provide context.

.. _birth-sex:

X1. Birth Sex
-------------
| **Name.......:** BirthSex
| **Source.....:** US-Core
| **Used In....:** Patient
| **Description:** The birth sex extension is used to provide a specific biological sex for the patient being tested.

.. _ethnicity:

X2. Ethnicity
-------------
| **Name.......:** Ethnicity
| **Source.....:** US-Core
| **Used In....:** Patient
| **Description:** The ethnicity extension is used to provide a specific set of ethnicities for the patient being tested.

.. _race:

X3. Race
--------
| **Name.......:** Race
| **Source.....:** US-Core
| **Used In....:** Patient
| **Description:** The race extension is used to provide a specific set of races for the patient being tested.

.. _age:

X4. Age
-------
| **Name.......:** Age
| **Source.....:** eMERGE
| **Used In....:** Patient
| **Description:** The age extension is used to provide a specific age in years of the patient at the time of testing.

.. _summary-interpretation-text:

X5. Summary Interpretation Text
-------------------------------
| **Name.......:** SummaryInterpretationText
| **Source.....:** eMERGE
| **Used In....:** DiagnosticReport, Observation
| **Description:** The summary interpretation text extension is used to provide short narrative summary interpretations at the report level and any observation level as needed.

.. _test-disclaimer:

X6. Test Disclaimer
-------------------
| **Name.......:** TestDisclaimer
| **Source.....:** eMERGE
| **Used In....:** GenomicsReport
| **Description:** The test disclaimer extension is used to return the performing lab's test disclaimer at the report level.

.. _related-artifact:

X7. Related Artifact
--------------------
| **Name.......:** RelatedArtifact
| **Source.....:** |hl7-cg-wg|
| **Used In....:** GenomicsReport
| **Description:** The related artifact extension is used to allow emerge to return the Gene Coverage file (BED format) as an attachment.

.. _recommended-action:

X8. Recommended Action
----------------------
| **Name.......:** RecommendedAction
| **Source.....:** |hl7-cg-wg|
| **Used In....:** GenomicsReport
| **Description:** action extension is used to return a top-level proposed recommendation from the lab to the ordering provider.
