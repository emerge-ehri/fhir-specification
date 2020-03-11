.. _genomics_report:

Genomics Report
===============

.. sidebar:: Contents

    Type: Profile
    Source: |fhir-gr-ig-short|
    Specification: |genomics-report-prof|

The final findings and interpretation of the eMERGEseq Platform genetic test performed
on patients and specimens derived from these. The report includes textual and
coded interpretations, variant findings and their diagnostic pathogenicity assessment,
and pharmacogenomic implications, requesting and provider information, assay description
and methodology and formatted representation of the final report.

Scope
^^^^^
The eMERGEseq platform project only focuses on the delivery of final reports from
the lab to the provider. These unsolicited results are returned to the providers
within this specified DiagnosticReport resource.


Content
^^^^^^^
This structure is derived from the CG Genomics Reporting IG artifact `Genomics Report <http://build.fhir.org/ig/HL7/genomics-reporting/genomics-report.html>`__.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :sheet: GenomicsReport
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G59

References
^^^^^^^^^^
links to
