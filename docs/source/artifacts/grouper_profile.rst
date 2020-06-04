Grouper Profile(s)
==================

Organizes information within a genetic report.

.. sidebar:: Artifact

    * Type: Profile
    * Spec: |grouper-prof|

Scope
^^^^^
Results for both the eMERGE gene panel and PGx sites are assembled together as a single report. Though bundled together, these results are discrete components requiring composite representation. Utilizing the Grouper profile, Observation results for both gene panel and PGx were added as members of the Diagnostic Gene Panel Grouper and PGx Grouper respectively, with these two Grouper resources referenced as results of the GenomicsReport Profile thereby resulting in the aggregation of a composite report.

See Diagnostic Gene Panel and PGx Grouper profile artifacts for further detail on identification and organization of related resources to the Grouper profiles.

.. _grouper_dx:

Diagnostic Gene Panel Grouper

.. _grouper_pgx:

PGx Gene Panel Grouper


Content
^^^^^^^
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

.. _grouper_pgx:

PGx Gene Panel Grouper
----------------------

TODO description

Scope
^^^^^
TODO scope

Content
^^^^^^^
TODO content

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: GrouperPgx
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 100, 45, 125, 355]
   :selection: A1:G28
