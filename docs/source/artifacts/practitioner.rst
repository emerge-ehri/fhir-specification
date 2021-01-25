.. _practitioner:

Practitioner
============

A person who is directly or indirectly involved in the provisioning of healthcare.

Scope
^^^^^
Practitioner covers all individuals who are engaged in the healthcare process and healthcare-related services as part of their formal responsibilities and this Resource is used for attribution of activities and responsibilities to these individuals. The two Practitioners for eMERGE are the ordering provider in the role of requester ordering the test and geneticist in the role of resultsInterpreter responsible for the interpretations and conclusions of the test. See PractitionerRole and Organization artifacts for additional detail.

The two Practitioner resources are referenced in :ref:`practitioner_role`.

Content
^^^^^^^
eMERGE uses the |practitioner-res| resource with the following constraints.

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :transforms: ../_files/transformation-mappings.json
   :sheet: Practitioner
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G10

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

.. note:: Results Interpreter
   For details see multi-use artifact: :ref:`practitioner_role`

Referenced By: :ref:`genomics_report`
