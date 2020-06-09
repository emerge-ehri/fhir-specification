.. _overall_interpretation:

Overall Interpretation
======================

Provides a coarse overall interpretation of the genetic results reported.

.. sidebar:: Discussions

   :ref:`issue-interp-summary-text`

Scope
^^^^^

eMERGE reports generally include an overall interpretation for the report, primarily based on the testing results of the gene panel. This Overall interpretation result is typically displayed as a positive, negative and unknown value (Check with Larry - did LMM use unknown or inconclusive?) with summary interpretative text providing additional information and context.  The OverallInterpretation profile included the concepts necessary to represent the result value and the Observations it was based on and is referenced in the GenomicsReport profile as a front-page result for the patient and in the Grouper profile as part of the aggregation of resulting Observations for the patient. However, an option to include summary interpretation text, a key component of the overall interpretation was not available as part of profile and a custom extension for eMERGE was created to include summary text. See #7 in Discussion -> Issues & Resolutions for further detail.

This resource is referenced in GenomicsReport and Grouper.

Content
^^^^^^^
eMERGE uses the |overall-interp-prof| profile here which is derived from the |observation_res| resource.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: OverallInterpretation
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G29
