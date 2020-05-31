.. _patient:

Patient
=======

.. sidebar:: Artifact

    * Type: Resource
    * Spec: |patient-res|

The patient resource contains demographic information for the individual receiving the genetic test.

Scope
^^^^^

The data in the Resource covers the "who" information about the patient: its attributes are focused on the demographic information necessary to support the result interpretation, logistic, administrative, compliance and regulatory procedures. A Patient record is generally created and maintained by each organization providing care for a patient. A patient or animal receiving care at multiple organizations may therefore have its information present in multiple Patient Resources.

Not all concepts required for eMERGE were included within the base resource, such as race, ethnicity, birthsex and age.  Race, ethnicity and birthsex were included from the `US Core Profile as extensions <http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient>`_. Age, an optional element to be included in lieu of birthsex for de-identifying purposes was created as a `custom extension <https://simplifier.net/eMERGEFHIRExtensionResources/PatientAge/~overview>`_ for eMERGE. See #19 i Discussion -> Issues & Resolutions for further detail.

Content
^^^^^^^

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: Patient
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G44
