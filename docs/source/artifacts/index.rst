.. _artifacts:

Artifacts
=========

Figure 5 below illustrates a complete map of the resource, profile and extension FHIR artifacts used to support the eMERGE report
defined by this specification. It starts at the center with #1 the GenomicsReport profile in purple from the FHIR CG Genomics Reporting IG.
At the top are the red artifacts representing the patient and specimen concepts. The light green
artifacts in the upper right hand side represent the order (Service-Request) and the ordered assay (PlanDefinition) along with the ordering and performing practitioners and their facility.
The yellow artifacts on the left-hand side represent the top-level interpretation, comments and recommended actions, if applicable.
The bottom half of the mapping diagram divides the diagnostic disease gene panel findings and results in pink on the left from the
pharmacogenomic gene panel findings and results in green on the right. Both results and findings share common artifacts in orange at the
bottom of the diagram to represent the variants and genotypes associated with the findings and results.

The additional sub-diagrams at the bottom of Figure 5 contain the complete set of extensions utilized in this specification. These
extensions were used from other sources when available as indicated or created as custom extensions if no reasonable alternative was
available. These extensions primarily are used to extend the Patient (X1 thru X4) and GenomicsReport (X6 thru X8) concepts, but one
extension was needed for capturing summary interpretation text (X5) on both the GenomicsReport and/or any Observation.

.. figure:: ../_images/artifact-overview.png
   :align: left

   **Figure 5: Artifact Catalogue Map**
   A map of the associations between the major schema artifacts (resources, profiles and extensions).

.. _catalogue:

**Catalogue**

The following catalogue provides a tabular view corresponding to the numbers in Figure 5 as well as the figures shown elsewhere in this specification.
The links will open the specific artifact's page in this specification.

.. list-table::
   :class: my-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   * - No.
     - Artifact
     - FHIR Resource
     - Description
   * - 1
     - :ref:`Genomics-Report <genomics_report>`
     - DiagnosticReport
     - The genomics report profile ...
   * - 2
     - :ref:`Patient <patient>`
     - Patient
     - The patient ...
   * - 3
     - :ref:`Specimen <specimen>`
     - Specimen
     - The specimen ...
   * - 4
     - :ref:`Service-Request <service_request>`
     - ServiceRequest
     - The service request profile ...
   * - 5
     - :ref:`(Assay) PlanDefinition <plan_definition>`
     - PlanDefinition
     - The plan definition resources is used to represent the eMERGE lab developed test (LDT).
   * - 6
     - :ref:`PractitionerRole <practitioner_role>`
     - PractitionerRole
     - The practitioner role is used to represent the health care personnel in the context of their role and organization (e.g. geneticists, clinicians, etc..).
   * - 6a
     - :ref:`Practitioner <practitioner>`
     - Practitioner
     - The patient ...
   * - 7
     - :ref:`Organization <organization>`
     - Organization
     - The organization ...
   * - 8
     - :ref:`Recommended-Followup <recommended_followup>`
     - Task
     - The recommended followup profile is a proposed task resource for structuring the return of recommendations for the report.
   * - 9
     - :ref:`Report Comment <report_comment>`
     - Observation
     - The report comment ...
   * - 10
     - :ref:`Overall-Interpretation <overall_interpretation>`
     - Observation
     - The overall interpretation ...
   * - 11
     - :ref:`Dx Grouper <grouper_dx>`
     - Observation
     - The grouper profile for diagnostic gene panel grouped results ...
   * - 12
     - :ref:`Inherited-Disease-Pathogenicity <inh_dis_path>`
     - Observation
     - The inherited disease pathogenicity profile ...
   * - 13
     - :ref:`PGx Grouper <grouper_pgx>`
     - Observation
     - The grouper profile for PGx gene panel results ...
   * - 14
     - :ref:`Medication-Implication <medication_implication>`
     - Observation
     - The organization ...
   * - 15
     - :ref:`Variant <variant>`
     - Observation
     - The variant profile supports the return of structured short sequence variants along with their zygosity for observed findings typically to support interpretations related to their clinical significance or in the context of the assay.
   * - 16
     - :ref:`Genotype <genotype>`
     - Observation
     - The genotype profile supports the return of structured genotypes derived from individual variant alleles. This is used primarily to structure PGx diplotypes.
   * - X#
     - :ref:`Extensions <extensions>`
     - Extension
     - The list of all extensions used throughout this specification with special emphasis on the few custom extensions developed by eMERGE to support the project's requirements.


.. toctree::
   :hidden:

   genomics_report
   patient
   specimen
   service_request
   plan_definition
   practitioner_role
   practitioner
   organization
   recommended_followup
   report_comment
   overall_interpretation
   grouper_profile
   inherited_disease_pathogenicity
   med_implication
   variant
   genotype
   extensions
