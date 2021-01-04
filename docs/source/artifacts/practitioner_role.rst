.. _practitioner_role:

PractitionerRole
=================

A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.

Scope
^^^^^
PractitionerRole covers the recording of the location and types of services that Practitioners are able to provide for an organization.

The role, specialty, location and healthcare service aspects of the PractitionerRole resource have been used in eMERGE to distinguish  between the role of the ordering provider placing the test order (requester) and the geneticist responsible for the report's interpretations and conclusions (resultsInterpreter) by creating a PractitionerRole resource for each role respectively. Additionally highlighted in this resource are the institutions i.e. Organization resource under which Practitioners assigned to this role perform their respective responsibilities. Also to be considered in this context and distinct from the resultsInterpreter is the performer i.e the Organization resource executing the test and delivering the results. While the resultsInterpreter is responsible for the conclusions in the report, the Performer is the Organization responsible for delivering on the desired diagnostic service i.e. the genetic test itself with the resultsInterpreter typically being a member of this Organization. See Practitioner and Organization artifacts for additional detail.

The resultsInterpreter and performer are referenced in the GenomicsReport profile while the requestor and the performer are referenced in the ServiceRequest profile.

Content
^^^^^^^
eMERGE uses the |practitionerrole-res| resource here.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: PractitionerRole
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G11
