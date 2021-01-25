.. _inh_dis_path:

Inherited Disease Pathogenicity
===============================

The inherited disease pathogenicity observation is the interpretation that the results interpreter associates with a genotype finding within the diagnostic gene panel.


.. sidebar:: Discussions

   | :ref:`issue-confirmation-testing`
   | :ref:`issue-interp-summary`
   | :ref:`issue-secondary-findings`
   | :ref:`issue-variant-data-types`
   | :ref:`issue-path-phenotypes`
   | :ref:`issue-path-values`

Scope
^^^^^
The eMERGE assay is designed to sequence, identify, confirm and report the clinically significant variants in relation to the indication for testing. The inherited disease pathogenicity interpretation is the result that specifies which disease or condition the associated variant finding is pathogenic or likely pathogenic and thus considered clinically significant.

The inherited disease pathogenicity interpretation may also be used to identify secondary findings if it is not associated with the primary indication for testing but still within the secondary finding list of conditions. Secondary finding interpretations are indicated by using the *observation-secondaryFinding* attribute of the inherited disease pathogenicity association.

This resource is referenced in :ref:`overall_interpretation` and :ref:`grouper_dx` observations of the eMERGE report.

Content
^^^^^^^
eMERGE uses the |inh-dis-path-prof| profile which is derived from the |genomics-base-prof| profile and the |observation-res| in turn.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: InheritedDiseasePathogenicity
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 100, 45, 125, 355]
   :selection: A1:G47
