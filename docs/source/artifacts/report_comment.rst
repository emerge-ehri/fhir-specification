.. _report_comment:

Report Comment
==============

Observation resource that includes assertions made about the patient.

.. sidebar:: Discussions

   | :ref:`issue-report-comments`

Scope
^^^^^
eMERGE reports typically include have a comments or additional notes section with case specific information. These comments are not really recommendations, conclusions or observations. This is additional information that the reporting lab wants to provide the ordering provider and patient related to the overall outcomes. The  Observation resource is used to include this information by limiting the scope of this resource to a standard LOINC Report Comment code (86467-8) and an associated value that houses the comment or additional notes text. See #3 in Discussion -> Issues & Resolutions for further detail.

This resource is referenced in GenomicsReport as a result.

Content
^^^^^^^
eMERGE uses the |observation_res| resource here.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: ReportComment
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G23
