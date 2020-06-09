.. _medication_implication:

Medication Implication
======================

(todo LB)
TODO description
Reference the three subtypes included here (metabolism, efficacy, transporter)

.. sidebar:: Discussions

   | :ref:`issue-interp-summary-text`
   | :ref:`issue-citing-assesed-meds`


Scope
^^^^^
TODO scope

Content
^^^^^^^
eMERGE uses the following three profiles that all derive from the medication implication profile:
        * |metab-impl-prof|
        * |efficacy-impl-prof|
        * |transport-impl-prof|

These three profiles support the specific medication implications related to metabolism, efficacy and transport function, respectively. They all ultimately derive from the |observation-res| resource.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: MedicationImplication
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G45
