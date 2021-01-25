.. _practitioner_role:

PractitionerRole
=================

A specific set of Roles/Locations/specialties/services that a practitioner may perform at an organization for a period of time.

Scope
^^^^^
PractitionerRole covers the recording of the location and types of services that Practitioners are able to provide for an organization.

The role, specialty, location and healthcare service aspects of the PractitionerRole resource have been used in eMERGE to distinguish  between the role of the ordering provider placing the test order (requester) and the geneticist responsible for the report's interpretations and conclusions (resultsInterpreter) by creating a PractitionerRole resource for each role respectively. Additionally highlighted in this resource are the institutions i.e. Organization resource under which Practitioners assigned to this role perform their respective responsibilities.

See :ref:`practitioner` and :ref:`organization` artifacts for additional detail.

The resultsInterpreter and performer are referenced in :ref:`genomics_report` while the requester is referenced in :ref:`service_request`.

Content
^^^^^^^
eMERGE uses the |practitionerrole-res| resource with the following constraints.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: PractitionerRole
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G11


Notes
^^^^^
**Performer & Results Interpreter**
The performer and results interpreter typically correspond to the testing laboratory
and lab resource that finalizes the report, respectively. These two components are
closely related and exist at the DiagnosticReport level. In eMERGE there will always
be one laboratory as the performer and there is typically one results interpreter.
It is possible to have more than one of either, but that was not in scope for the
eMERGE specification.

Their is no profile or extension for the Performer or the Results Interpreter and
these components use the standard FHIR Resources of |organization-res| and |practitionerrole-res|, respectively.

.. note:: Performer
   For details see multi-use artifact: :ref:`organization`

Referenced By: :ref:`genomics_report`
