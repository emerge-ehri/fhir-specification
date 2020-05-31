.. _genomics_report:

Genomics Report
===============

The final findings and interpretation of the eMERGEseq Platform genetic test performed
on patients and specimens derived from these.

.. sidebar:: Discussions

   :ref:`discussion-1`


Scope
^^^^^
The eMERGEseq platform project only focuses on the delivery of final reports from
the lab to the provider. These unsolicited results are returned to the providers
within this specified DiagnosticReport resource. The report includes textual and
coded interpretations, variant findings and their diagnostic pathogenicity assessment,
and pharmacogenomic implications, requesting and provider information, assay description
and methodology and formatted representation of the final report.

Content
^^^^^^^

eMERGE uses the |genomics-report-prof| profile here which is derived from the |diagnosticreport-res| resource.

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
