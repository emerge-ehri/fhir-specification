.. _organization:

Organization
=============

A formally or informally recognized grouping of people or organizations formed for the purpose of achieving some form of collective action. Includes the institutions requesting a genetic test and the diagnostic service responsible for delivering on the test.

Scope
^^^^^
This resource is used in eMERGE to identify the Organization that the PractitionerRoles i.e. the requester of the test and resultsInterpreter for the test belong to. This resource is also used to identify the performer of the test i.e. the diagnostic lab providing the service. See PractitionerRole and Practitioner for additional detail.

The performer is referenced in the GenomicsReport and ServiceRequest profiles while the Organization is referenced in the the PractitionerRole resources.

Content
^^^^^^^
eMERGE uses the |organization-res| resource here.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: Organization
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G12
