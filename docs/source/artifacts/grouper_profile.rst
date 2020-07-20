Grouper Profile(s)
==================

Organizes information within a genetic report.

.. sidebar:: Discussions

   | :ref:`issue-nested-results`
   | :ref:`issue-interp-summary-text`
   | :ref:`issue-secondary-findings`

Scope
^^^^^
Results for both the eMERGE gene panel and PGx sites are assembled together as a single report. Though bundled together, these results are discrete components requiring composite representation. Utilizing the Grouper profile, Observation results for both gene panel and PGx were added as members of the Diagnostic Gene Panel Grouper and PGx Grouper respectively, with these two Grouper resources referenced as results of the GenomicsReport Profile thereby resulting in the aggregation of a composite report.

See below for addtional scope and content details on both the Diagnostic Gene Panel and PGx Grouper profile artifacts.

.. _grouper_dx:

Diagnostic Gene Panel Grouper
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The primary design of the eMERGE Seq assay is to perform a diagnostic assessment of the variation in a pre-defined panel of genes. The Diagnostic Gene Panel Grouper is an organizing Observation profile that aggregates the primary and secondary findings of any clinically significant variants identified, their assessments, as well as a reference to the overall interpretation for the final report of which the diagnostic panel is the basis.

Content
-------
eMERGE uses the |grouper-prof| profile here which is derived from the |observation_res| resource.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: GrouperDx
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 100, 45, 125, 355]
   :selection: A1:G29


Notes
-----
Primary and Secondary findings may optionally be segregated into separate "groupers" if it useful to the lab or clinic process. For eMERGE both primary and secondary findings were reported together in a single Diagnostic Gene Panel Grouper.

See :ref:`issue-secondary-findings` for more details on the issues related to representing secondary findings and their derived interpretations.


.. _grouper_pgx:

PGx Gene Panel Grouper
^^^^^^^^^^^^^^^^^^^^^^

In addition to the Diagnostic Gene Panel findings and interpretations, the eMERGE Seq Panel was designed to include the medication implications of several pharmacogenomic genes. The Pharmacogenomic Gene Panel Grouper an organizing Observation profile that aggregates all of the observed states of the pharmacogenomic genes and their medication implications. The pharmacogenomic gene results have no bearing on the overall interpretation for the report, unlike the diagnostic gene panel results.

Content
-------
eMERGE uses the |grouper-prof| profile here which is derived from the |observation_res| resource.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: GrouperPgx
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 100, 45, 125, 355]
   :selection: A1:G28

Notes
-----
In practice the PGx results could be reported independently (as was the case in the BI/LMM reporting workflow). However, with genetic tests that are based on larger panels, exomes or genomes, there may be several categories of assessment that have useful clinical value based on the original wet lab finding (sequencing and/or genotyping). Genetic test reports for these larger assays often combine these distinct but grouped assessments in a single physical report. The Grouper profile provided an acceptable solution for eMERGE that did not otherwise exist.
