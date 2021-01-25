.. _medication_implication:

Medication Implication
======================

The result interpreter's assessed implication of medication(s) associated with specific variant and/or genotype/diplotype findings for pharmacogenomic genes.


.. sidebar:: Discussions

   | :ref:`issue-interp-summary`
   | :ref:`issue-variant-data-types`
   | :ref:`issue-assesed-med-citations`
   | :ref:`pgx-results`

Scope
^^^^^
There are three subtypes of the medication implication profile: metabolism, efficacy, and transporter.

eMERGE uses the following three profiles that all derive from the medication implication profile:

        1. |metab-impl-prof|
        2. |efficacy-impl-prof|
        3. |transport-impl-prof|

These three profiles support the specific medication implications related to metabolism, efficacy and transport function, respectively. They all ultimately derive from the |observation-res| resource.

This resource is referenced in :ref:`grouper_pgx` observations of the eMERGE report.

Content
^^^^^^^
The descriptions & constraints column in the attribute table below will indicate the specific numbered subtypes impact on the attribute, if applicable.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: MedicationImplication
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G45
