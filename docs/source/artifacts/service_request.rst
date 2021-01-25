.. _service_request:

Service Request
===============

.. sidebar:: Discussions

   | :ref:`issue-test-information`

The service request is the order information describing the specific assay requested and/or fulfilled, the patient and specimen and the ordering provider that authorized the request.

Scope
^^^^^
The eMERGE project had prescribed assays from the two sequencing centers that fulfilled the
genetic testing services. As such, the service request was used to represent the fulfilled
assay. In a generic clinical genetic testing system, order management would require
additional uses of the service request not included here.

The ordering provider or requester is typically a practitioner and their provider organization,
but a provider organization alone may be used if appropriate.

This resource is referenced in :ref:`genomics_report` and all observations in the eMERGE report.

Content
^^^^^^^
eMERGE uses the |service-request-prof| here which is derived from the |servicerequest-res| resource.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: ServiceRequest
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G45

Notes
^^^^^
The ordered and performed test (or assay) is also provided in the service request via the
*instiantiatesCanonical* association to the |plandefinition-res| Please refer to the
PlanDefinition page for the rationale and approach to scope and structure of the Assay.
