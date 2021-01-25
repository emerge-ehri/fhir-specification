.. _genotype:

Genotype
=========
The genotype profile is used to represent a diplotypes tested and/or identified. It is a profile that can identify and link the underlying :ref:`variant` findings that define the genotype or diplotype concept tested or found.

.. sidebar:: Discussions

   | :ref:`issue-variant-data-types`
   | :ref:`variant-representation`
   | :ref:`pgx-results`

Scope
^^^^^
The genotype profile is a higher order profile that can use other variant profile records to define the variant components of the genotype. The eMERGE report uses the Genotype profile primarily for the pharmacogenomic gene panel diplotype findings. These diplotype findings are the basis for the :ref:`medication_implication` interpretations that are the aim of the PGx gene panel assay.

eMERGE specified the need to include variants found for the specific PGx genes tested. The PGx genes were derived from both sequence and genotype testing. The eMERGE PGx methodology used one or more predefined locations with the various PGx genes to assert the haplotypes and diplotypes for those PGx genes. The CPIC star allele nomenclature was the display format for the final PGx diplotype calls.

This resource is referenced in :ref:`medication_implication` and :ref:`grouper_pgx` observations.

Content
^^^^^^^
eMERGE uses the |genotype-prof| profile which is derived from  the |genomics-base-prof| profile and the |observation-res| in turn.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: Genotype
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 100, 45, 125, 355]
   :selection: A1:G33
