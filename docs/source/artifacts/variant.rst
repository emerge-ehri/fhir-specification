.. _variant:

Variant
=========
The variant profile is used to represent a variants tested and/or identified. It specifies whether the variant is present, absent, indeterminate or a no call for the assay performed.

.. sidebar:: Discussions

   | :ref:`issue-variant-data-types`
   | :ref:`variant-representation`

Scope
^^^^^
The variant is a complex profile that can be used to represent numerous forms of variation. The eMERGE report uses the Variant profile primarily for the diagnostic gene panel variant findings with their zygosity. These variant findings are the basis for the :ref:`inh_dis_path` interpretations that are the aim of the diagnostic gene panel assay.

Please refer to the discussion topics for more information on this profile.

This resource is referenced in :ref:`inh_dis_path`, :ref:`genotype`, :ref:`grouper_dx` and :ref:`grouper_pgx` observations.


Content
^^^^^^^
eMERGE uses the |variant-prof| profile which is derived from  the |genomics-base-prof| profile and the |observation-res| in turn.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: Variant
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G151


Notes
^^^^^

The complexity and options available for applying this profile cause it to be confusing to use. There is no other alternative method for defining variants in a universally consistent and computationally reliable way at the current time.

Variant contains a zygosity attribute which enables the implementer to represent short variation (e.g. SNPs, indels, etc.) as genotypes, which can seem confusing with the naming and purpose of the |genotype-prof|.
