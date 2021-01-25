.. _organization:

Organization
=============
The institution(s) requesting a genetic test and the diagnostic laboratory responsible for performing and/or interpreting the results.

Scope
^^^^^
This resource is used in eMERGE to identify the Organization that the PractitionerRoles i.e. the requester of the test and resultsInterpreter for the test belong to. This resource is also used to identify the performer of the test i.e. the diagnostic lab providing the service.

The performer (performing organization) is referenced in :ref:`genomics_report` and :ref:`service_request` while the requester and result interpreter organization is referenced via the :ref:`practitioner_role`.

Content
^^^^^^^
eMERGE uses the |organization-res| resource with the following constraints.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: Organization
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G12

Notes
^^^^^
**Performer & Results Interpreter**
The performer and results interpreter typically correspond to the testing laboratory
and lab resource that finalizes the report, respectively. These two components are
closely related and exist at the DiagnosticReport level. In eMERGE there will always
be one laboratory as the performer and there is typically one results interpreter.
It is possible to have more than one of either, but that was not in scope for the
eMERGE specification.

There are no profiles or extensions for the Performer or the Results Interpreter and
these components use the standard FHIR Resources of |organization-res| and |practitionerrole-res|, respectively.

.. note:: Results Interpreter & Requester
   For details see multi-use artifact: :ref:`practitioner_role`
