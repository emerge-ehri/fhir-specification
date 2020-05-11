.. _service_request:

Service Request
===============

.. sidebar:: Artifact

    * Type: Profile
    * Spec: |service-request-prof|

The service request contains the information about the requested and performed services.

Scope
^^^^^
The service request contains the vital elements of the *order* in addition to updates made
by the performing organization (or fulfiller). It is common for the original order or
requisition to be modified or updated by the fulfiller in coordination with ordering provider.

The requester or order placer is typically a practitioner and his/her provider organization,
but a provider organization alone may be used if appropriate.

The ordered and performed test (or assay) is also provided in the service request.

A common genetic testing panel and plan was coordinated across both emerge sequencing centers.
However, as is often the case with genetic testing, the individual sequencing centers
often use different procedures and technologies to achieve similar aims. These differences
in methodologies for both sequencing and resulting are essential in reporting results.

For cases where a global or shared test registry can be defined with sufficient and
accurate test information, the computational reporting of test information could possibly
be simplified to passing an identifier to such a resource. In the case of emerge
the sequencing assays performed for various providers and across sequencing centers
deviates to a large enough degree that it is critical to include these details about
the testing methodology, description and references in the structured electronic results.
Since this information is not case specific it is not considered to be an observable
result but instead a definition of the test itself. It will be consistent across all
cases that share the same testing methodology for a given SC.

Content
^^^^^^^
TODO content


.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: ServiceRequest
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G45
