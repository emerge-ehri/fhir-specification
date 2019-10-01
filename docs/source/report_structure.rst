Report Structure
================

The eMERGE reporting process is supported by two separate clinical workflows at the corresponding sequencing centers (SCs); The HGSC Lab at Baylor College of Medicine and The LMM Lab at Partners Healthcare (in conjunction with Broad Institute).

Below are two example (deidentified) positive reports one from each of the two SCs.

.. figure:: _images/hgsc-report-plain.png
   :alt: HGSC eMERGE Report
   :height:  600 px
   :class: sidebyside

.. figure:: _images/lmm-report-plain.png
   :alt: LMM eMERGE Report
   :height:  600 px
   :class: sidebyside

.. rst-class:: clearsidebyside

**Figure 1:** HGSC & LMM eMERGE Report Examples (click to enlarge)

This section introduces the process used to convert and map these two similar reports into a common HL7 FHIR structure.

FHIR Report Resource Model
!!!!!!!!!!!!!!!!!!!!!!!!!!

FHIR provides a DiagnosticReport Resource which is the root resource for representing the contents of returned lab results.

The following diagram illustrates the core Resource hierarchy starting with the DiagnosticReport at the far left and branching through the various sub-resources dedicated to sharing various portions of the lab results. There is a table below that describes each numbered resource to provide additional context.

.. figure:: _images/schema-overview.png
   :align: left

**Figure 2:** eMERGE Report FHIR Resource Map

.. .. imagesvg:: _images/schema-overview.svg
..    :tagtype: object
..    :width: 100%
..    :align: center

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
     - :ref:`3.1 Diagnostic Report <diagnostic-report>`
     - The diagnostic report ...
   * - 2
     - :ref:`3.2 Patient <patient>`
     - The patient ...
   * - ?
     - ToDo
     - The ...


Mapping Report to Resources
!!!!!!!!!!!!!!!!!!!!!!!!!!!

Below we show two sets of figures to represent the layouts of each of the SCs example reports at the top of this section and how they map to the FHIR resource model above.

First the HGSC example report layout and mapping...

.. figure:: _images/hgsc-report-layout.png
   :alt: HGSC eMERGE Report Layout
   :class: sidebyside

.. figure:: _images/hgsc-report-mapped.png
   :alt: HGSC eMERGE Example Report Detailed Mapping
   :height:  600 px
   :class: sidebyside

.. rst-class:: clearsidebyside

**Figure 3:** HGSC Example Report layout and detailed mapping (click to enlarge)


And here's the LMM example report layout and mapping...

.. figure:: _images/lmm-report-layout.png
   :alt: LMM eMERGE Report Layout
   :class: sidebyside

.. figure:: _images/lmm-report-mapped.png
   :alt: LMM eMERGE Example Report Detailed Mapping
   :height:  600 px
   :class: sidebyside

.. rst-class:: clearsidebyside

**Figure 4:** LMM Example Report layout and detailed mapping (click to enlarge)


.. Some more text
..
.. .. imagesvg:: _images/emerge.svg
..    :tagtype: object
..    :width: 500px
..
.. And still more



.. .. thumbnail:: _images/hgsc-report-plain.png
..    :width: 200px
..    :title: **Figure:** HGSC eMERGE Report
..    :show_caption: true
..
.. .. thumbnail:: _images/lmm-report-plain.png
..    :width: 200px
..    :title: **Figure:** LMM eMERGE Report
..    :show_caption: true
