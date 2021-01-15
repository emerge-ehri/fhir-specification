.. _genomics_report:

Genomics Report
===============

The final findings and interpretation of the eMERGEseq Platform genetic test performed
on blood specimens derived from patients.

.. sidebar:: Discussions

   | :ref:`issue-composite-reporting`
   | :ref:`issue-report-comments`
   | :ref:`issue-recommendations`
   | :ref:`issue-interp-summary`
   | :ref:`issue-region-coverage`
   | :ref:`issue-rept-category`
   | :ref:`issue-sign-out-v-sent-dates`
   | :ref:`issue-research-flag`
   | :ref:`issue-disclaimers`

Scope
^^^^^
The eMERGE project includes sequencing, interpretation, generation and delivery of clinical genetic reports from  diagnostic labs (eMERGE Clinical Sequencing and Genotyping Facilities) to the ordering providers (eMERGE Study Sites). The GenomicsReport profile derived from the DiagnosticReport resource was adopted to represent the eMERGE report specification and includes textual and coded interpretations, variant findings and their diagnostic pathogenicity assessment, and pharmacogenomic implications, requesting and provider information, assay description and methodology as referenced resources and resulting observations attached to the GenomicsReport profile.

Content
^^^^^^^

eMERGE uses the |genomics-report-prof| profile which is derived from the |diagnosticreport-res| resource.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: GenomicsReport
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 100, 45, 125, 355]
   :selection: A1:G59

Notes
^^^^^
