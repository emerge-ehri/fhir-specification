.. _artifacts:

Artifacts
=========

.. Warning::
    This document is a work in progress and is not ready for production use.

FHIR provides a DiagnosticReport Resource which is the root resource for representing the contents of returned lab results.

The following diagram illustrates the core Resource hierarchy starting with the DiagnosticReport at the far left and
branching through the various sub-resources dedicated to sharing various portions of the lab results. There is a table
below that describes each numbered resource to provide additional context.

<rewrite based on selection of artifacts from CG IG perspective>

.. figure:: ../_images/schema-overview.png
   :align: left

   **Figure 4: Schema Overview**
   An illustration of the associations between the major schema components.

The next section offers a top-level catalogue of all the resources, profiles, extensions
implemented in this specification.
The subsequence pages describe each component in detail.

.. toctree::
   :hidden:

   catalogue
   diagnostic_report
   patient
   specimen
   service_request
   test
   ordering_provider
   performer_and_results_interpreter
   diagnostic_gene_panel
   overall_interpretation
   inherited_disease_pathogenicity
   gene_coverage
   recommendation
   variant
   genotype
   pgx_gene_panel
   med_implication
