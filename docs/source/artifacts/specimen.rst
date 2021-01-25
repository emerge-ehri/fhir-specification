.. _specimen:

Specimen
========

The characteristics defining the patient's extracted sample to be used for testing and analysis.

Scope
^^^^^
A material sample taken from a biological entity, living or dead. The specimen covers substance used for diagnostic testing. The focus of the specimen resource is the process of gathering the specimen as well as where the specimen originated. An eMERGE specific business identifier assigned to this resource.

This resource is referenced in :ref:`genomics_report`, :ref:`service_request`, and all observations in the eMERGE report.

Content
^^^^^^^
eMERGE uses the |specimen-prof| here which is derived from the |specimen-res| resource.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: Specimen
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G30

Notes
^^^^^
Though the Genomics Reporting IG's specimen profile was used for eMERGE considering that there is a 1:1 overlap between specimen profile and the specimen resource, preference should be given to the core specimen resource.
