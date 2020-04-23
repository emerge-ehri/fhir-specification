.. _practitioner:

Practitioner
============

.. sidebar:: Artifact

    * Type: Resource
    * Spec: |practitioner-res|

TODO reference practitionerRole and Organization and discussion on the three types of roles (performer, requester, interpreter).

Scope
^^^^^
TODO scope

Content
^^^^^^^
TODO content

.. excel-table::
   :file: ../_files/emerge-fhir-resources-definitions.xlsx
   :sheet: Practitioner
   :overflow: false
   :row_header: false
   :col_header: false
   :colwidths: [20, 20, 20, 70, 50, 130, 375]
   :selection: A1:G10


TODO move next section to a logical place to be referenced by Practitioner, PractitionerRole and Organization.

Performer & Results Interpreter
-------------------------------

The performer and results interpreter typically correspond to the testing laboratory
and lab resource that finalizes the report, respectively. These two components are
closely related and exist at the DiagnosticReport level. In eMERGE there will always
be one laboratory as the performer and there is typically one results interpreter.
It is possible to have more than one of either, but that was not in scope for the
eMERGE specification.

Their is no profile or extension for the Performer or the Results Interpreter and
these components use the standard FHIR Resources of Organization and PractionerRole, respectively.

.. note:: Performer
   For details see multi-use artifact: Organization

.. note:: Results Interpreter
   For details see multi-use artifact: PractitionerRole

Referenced By: :ref:`genomics_report`
