.. _artifacts:

Artifacts
=========

FHIR provides a DiagnosticReport Resource which is the root resource for representing the contents of returned lab results.

The following diagram illustrates the core Resource hierarchy starting with the DiagnosticReport at the far left and
branching through the various sub-resources dedicated to sharing various portions of the lab results. There is a table
below that describes each numbered resource to provide additional context.

.. todo:: <rewrite based on selection of artifacts from CG IG perspective>

.. figure:: ../_images/schema-overview.png
   :align: left

   **Figure 4: Schema Overview**
   An illustration of the associations between the major schema components.

Each major component is described in detail in the corresponding sub-sections.

Catalogue
!!!!!!!!!!!!!!!!!!!!!!!!!!

**Artifact Catalogue**

.. list-table::
   :class: my-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   * - No.
     - Resource (Section)
     - Description
   * - 1
     - :ref:`Diagnostic Report <diagnostic-report>`
     - The diagnostic report ...
   * - 2
     - :ref:`Patient <patient>`
     - The patient ...
   * - ?
     - ToDo
     - The ...


.. toctree::
   :hidden:

   diagnostic_report
   patient
   specimen
   service_request/index
   performer_and_results_interpreter
   diagnostic_gene_panel/index
   overall_interpretation
   gene_coverage
   recommendation
   variant_and_genotype
   pgx_gene_panel/index
