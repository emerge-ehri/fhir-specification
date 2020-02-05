Artifacts
=========

<rewrite based on selection of artifacts from CG IG perspective>
The eMERGE results FHIR is based on the Diagnostic Report Resource profile and guidance from the
[HL7 CG WG Implementation Guide on General Genomic Reporting](http://build.fhir.org/ig/HL7/genomics-reporting/general.html).

This specification aims to harmonize and leverage the draft work of the HL7 CG WG to both validate and inform its development.
In cases where there are gaps or requirements that are unclear or unmet, they are raised with the HL7 CG WG and
custom extensions or profiles are developed to fill the missing needs with the expectation that these issues
will ultimately be reconcilable as the standard matures.

.. figure:: ../_images/schema-overview.png
   :align: left

   **Figure 5: Schema Overview**
   An illustration of the associations between the major schema components.

Each major component is described in detail in the corresponding sub-sections.

FHIR Report Resource Model
!!!!!!!!!!!!!!!!!!!!!!!!!!

FHIR provides a DiagnosticReport Resource which is the root resource for representing the contents of returned lab results.

The following diagram illustrates the core Resource hierarchy starting with the DiagnosticReport at the far left and branching through the various sub-resources dedicated to sharing various portions of the lab results. There is a table below that describes each numbered resource to provide additional context.

.. figure:: ../_images/schema-overview.png
   :align: left

**Figure 2:** eMERGE Report FHIR Resource Map

**Resource Mapping Table**

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
   :caption: Schema Components
   :maxdepth: 2

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
