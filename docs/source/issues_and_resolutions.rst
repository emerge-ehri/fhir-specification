.. _issues-and-resolutions:

Issues & Resolutions
====================

.. Warning::
    This document is a work in progress and is not ready for production use.

This section includes a review of the issues that required resolution. These issues and topics range in effort and complexity which are qualified as major or minor.

The section below pertains to the work performed by the BCM and Broad Institute teams to create the eMERGE FHIR Specification based on the |fhir-gr-ig-short| during 2019. It should be noted that with the Clinical Genomics WG continuing to work on upgraded versions of the IG (i.e. STU2, ...), there will be changes and variations between the STU1 version discussed here compared to any subsequent versions released or currently in development by the Clinical Genomics WG.

During the course of implementing the eMERGE Results using the |fhir-gr-ig-short| a number of issues were uncovered, discussed and resolved. Noteworthy issues are summarized below along with their outcome. Also included is extended documentation related to the collaboration and tracking of these items with the associated HL7 FHIR Working Groups.

.. _issue-composite-reporting:

#1 Composite reporting
----------------------
**HL7 WG:** Clinical Genomics | **Category:** Major

**Description:** Group multiple sections and associated results in one composite report.

The eMERGE clinical genetic report includes both gene panel and PGx results in one report. Though still bundled together, we planned to separate the gene panel and PGx results; the result will be a composite report that includes separate interpretations and results for the gene panel and PGx respectively.  This approach of organizing multiple results in the same report, in addition to allowing diagnostic labs to bundle multiple result panels together will also enable consuming EHR systems to efficiently retrieve the results required for computation, storage or CDS.

**Resolution:**
Use the |grouper-prof| Profile to group all related gene panel & PGx result resources, respectively. This will enable consuming EHR systems to utilize the panel & PGx results as disparate components.

**Reference(s):** `Jira #19828  <https://jira.hl7.org/browse/FHIR-19828?filter=-2>`_ | `Zulip CG: FHIR representation of a genetics test with multiple test... <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/FHIR.20representation.20of.20a.20genetics.20test.20with.20multiple.20test.2E.2E.2E>`_

.. _issue-test-information:

#2 Test Information
-------------------
**HL7 WG:** Orders and Observations | **Category:** Major

**Description:** Inclusion of Test Information, Methodology and References

Lab developed tests (LDTs) are standard practice in clinical genetic testing. As such it is useful and needed (for eMERGE) to share the assay title, code, description, methodology and references (citations) that appear in the report.

**Resolution:**
The recommendation to use the |plandefinition-res| resource to represent the eMERGE test info and associated elements was satisfactory for the eMERGE use case. More investigation for broader application across the domain could be useful.

**Reference(s):** `Jira #19827 <https://jira.hl7.org/browse/FHIR-19827?filter=-2>`_ | `Zulip CG: Report sections <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Report.20Sections>`_

.. _issue-report-comments:

#3 Inclusion of Report Comments
-------------------------------
**HL7 WG:** Orders and Observations | **Category:** Major

**Description:**
eMERGE and other clinical genetic test results have a comments or additional notes section with case specific information (see Example). These comments are not really recommendations, conclusions or observations. They are additional information that the reporting lab wants to provide the ordering physician and patient related to the overall outcomes or to a grouped set of results.

*Example:*
Analysis of exonic deletions and duplications is pending and were not assessed at this time. The report will be updated if pathogenic or likely pathogenic deletions or duplications are detected in this patient's sample.

**Resolution:**
As these comments are about the report itself and not a particular Observation, based on recommendations by the Orders and Observations WG, the resolution was to use an Observation result associated to the DiagnosticReport to include the comments. This Observation is assigned the LOINC “Report Comment” 86467-8 code and with the comments being mapped to the value field. Though sufficing for the short term, a more robust long term approach might be to evaluate the addition of a comments element to the Diagnostic Report Resource.

**Reference(s):** `Jira #22830 <https://jira.hl7.org/browse/FHIR-22830?filter=-2>`_ | `Zulip CG: Report Comments  <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Report.20Comments>`_ | `Zulip OO: Notes on Observations <https://chat.fhir.org/#narrow/stream/179256-Orders-and.20Observation.20WG/topic/Notes.20on.20Observations.20and.20DR/near/173777260>`_

.. _issue-recommendations:

#4 Inclusion of Recommendations
-------------------------------
**HL7 WG:** Orders and Observations | **Category:** Major

**Description:**
eMERGE reports include a proposed recommendation section (see Example).  We need to represent this accurately not only to enable actionability for the consuming EHR system but also to ensure that this is a requested proposed recommendation and not a resulting order.

*Example:* It is recommended that correlation of these findings with the clinical phenotype be performed. Genetic counseling for the patient and at-risk family members is recommended.

**Resolution:**
Use the RecommendedTask extension in DiagnosticReport to reference a Task. The Task resource itself, with a status of requested and intent of proposal, fulfills eMERGE requirements for including proposed recommendations.

**Reference(s):** `Jira #22830 <https://jira.hl7.org/browse/FHIR-22830?filter=-2>`_ | `Zulip CG: Report Comments <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Report.20Comments>`_

.. _issue-nested-results:

#5 Nested & Indirect Results
----------------------------
**HL7 WG:** Orders and Observations | **Category:** Major

**Description:**
The eMERGE Diagnostic Report utilizes the Grouper resource to aggregate primary Observations (results) which in turn references other Observation results using either hasMember or derivedFrom. Without the reference to all Observations (results) directly in the Diagnostic Report, two related concerns are:

1. Will consuming systems be impacted without a direct linkage of all results in the Diagnostic Report?
2. Can the derivedFrom be used to reference a related value that is not directly a result for this Diagnostic Report?

**Resolution:**
With the usage of the Grouper, hasMember and derivedFrom clearly documented, it was agreed that using nested Observation references streamlines the Diagnostic Report bundle. It was also agreed that derivedFrom could reference a related reference that is not a direct result for this Diagnostic Report.

**Reference(s):** `Zulip CG: Indirect Results <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Indirect.20Results>`_

.. _issue-confirmation-testing:

#6 Representation of Confirmation Testing
-----------------------------------------
**HL7 WG:** Orders and Observations | **Category:** Major

**Description:**
The eMERGE report includes information about confirmatory testing for both SNVs and CNVs.

**Resolution:**
Though this request was deliberated and discussed by the Clinical Genomics WG, a resolution was not reached at the time of the creation of the eMERGE FHIR Specification. As a temporary solution, confirmation information has been added to the note element of the Inherited Disease Pathogenicity profile for the eMERGE FHIR Specification.

**Reference(s):** `Jira #19829 <https://jira.hl7.org/browse/FHIR-19829?filter=-2>`_ | `Zulip CG: Sanger confirmation testing <https://chat.fhir.org/#narrow/stream/179197-genomics/topic/Sanger.20confirmation.2Ftesting>`_

.. _issue-interp-summary-text:

#7  Interpretation Summary Text
-------------------------------
**HL7 WG:** Clinical Genomics & Orders and Observations | **Category:** Major

**Description:**
Textual findings/interpretations are currently included in the eMERGE genetic report both at the report level and at the individual result (Observation) level. Without a  option to include this kind of interpretative or summary text in the GenomicsReport or an Observation currently, a `InterpretationSummaryText custom extension <https://simplifier.net/emergefhirextensionresources/interpretationsummarytext>`_ was created to house this information.

**Resolution:**
Pending. Request in discussion by both Clinical Genomics and Orders and Observations WGs.

**Reference(s):** `Jira #20978 <https://jira.hl7.org/browse/FHIR-20978?filter=-2>`_ | `Zulip CG ? <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/search/summary>`_

.. _issue-region-coverage:

#8  Gene/Region Coverage
------------------------
**HL7 WG:** Clinical Genomics | **Category:** Major

**Description:**
For every test subject, information about coverage information on the regions studied as part of the eMERGE test panel is attached as part of the results. Generally information provided includes chromosome, gene, transcript, CDS, start position, end position and coverage. Though the Region Studied resource does seem like a possible candidate to represent this information, if we have to create a separate region studied resource for each of the regions that are in this test, that might run into 100s or 1000s of region studied resources and might not be a scalable solution. Ideally, it might be helpful to have a resource which we can use to include all the regions covered as part of the test.

**Resolution:**
In the interim, for the current version of the eMERGE specification, we are attaching the coverage file to the GenomicsReport as a RelatedArtifact.

**Reference(s):** `Jira (Bob Dolin) #16258 <https://jira.hl7.org/browse/FHIR-16258?jql=text%20~%20%22gene%20coverage%22>`_ | `Zulip CG: Guidance re region studied <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Guidance.20re.20region.20studied>`_

.. _issue-secondary-findings:

#9  Secondary Findings
----------------------
**HL7 WG:** Clinical Genomics | **Category:** Major

**Description:**
The |fhir-gr-ig-short| defines an abstract observation profile, |genomics-base-prof|, that is the basis for all of their observations. GenomicsBase contains a |2nd-finding-ext| extension which is used to indicate when a given observation is a secondary finding (SF). The eMERGE use case considered the need for easily identifying and segregating observations that are primary from secondary. Additionally, there are a number of different types of observations that are used in the eMERGE defined assay. Only |inh-dis-path-prof| observations may potentially be SFs since they represent the specific variant-disease findings that meet a given SF policy and is different than the primary indication for testing. The IG directs that the extension should only be used when the observation is a SF and the specific SF policy should be specified within the extension on each observation. eMERGE initially considered creating a simple custom boolean extension on the |inh-dis-path-prof| to indicate whether the interpretation was a SF or not and associating the SF policy with the assay methodology in the |plandefinition-res|.

**Resolution:**
Use the CG IGs |2nd-finding-ext| extension on the |inh-dis-path-prof| profile. The choice was made to use the CodeableConcept's text field to indicate whether the inherited disease pathogenicity observation was a secondary finding or not.

**Reference(s):**  `Zulip CG: Representation of secondary findings <https://chat.fhir.org/#narrow/stream/179197-genomics/topic/Representation.20of.20secondary.20findings>`_

.. _issue-variant-types:

#10 Creation of definitional Variant Data Types
-----------------------------------------------
**HL7 WG:** Clinical Genomics | **Category:** Major

**Description:**
The current flexibility in exchanging variant level information may be helpful in allowing adoption. However, implementers should be cautioned about the perils of using these forms of representation for clinical decision support (CDS). Clinical grade precision will require more rigor and guidance. Definitional data types and/or resources would help isolate the concern and advance progress towards that aim.



**Resolution:**
For more information on Variant Representation see :ref:`variant-representation` Discussion.

**Reference(s):**  `Zulip CG: Variant Data Type Proposal <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Variant.20Data.20Type.20Proposal>`_

.. _issue-computation-test-structure:

#11 Need for computational test structure
-----------------------------------------

**HL7 WG:** Clinical Genomics | **Category:** Major

**Description:**
TODO Larry

**Resolution:**
Pending

**Reference(s):**  Zulip discussion

.. _issue-patient-identifier-type:

#12 Patient Internal Identifier Type Code
-----------------------------------------

**HL7 WG:** Modeling & Methodology | **Category:** Minor

**Description/Resolution:** eMERGE uses an internal patient identifier to identify a patient. An internal patient identifier is not a defined available `identifier type <https://hl7.org/fhir/R4/valueset-identifier-type.html>`_ for the Patient resource. However Patient internal identifier (code: PI) is available in the `HL7 Version 2 Table 0203 <http://hl7.org/fhir/v2/0203/>`_ but usage of the code PI from Table 0203 resulted in a validation warning during implementation. Based on the response (posted below) to the Jira ticket posted for this issue, it was decided to use Table 0203 and the code PI for the Patient internal identifier.

*Jira ticket response:* "The binding for this attribute is extensible so you are allowed to specify alternate codes if the value set does not cover your required concept. The warning that you are receiving is correct and can be ignored if you have specified a proper code for your purposes."

**Reference(s):** `Jira #24637  <https://jira.hl7.org/browse/FHIR-24637?filter=-2>`_

.. _issue-interp-with-multiple-phenotypes:

#13 Pathogenicity phenotype cardinality change
----------------------------------------------

**HL7 WG:** Clinical Genomics | **Category:** Minor

**Description/Resolution:**
The cardinality of the associated-phenotype element in the |inh-dis-path-prof| profile was updated from 0..1 to 0..* per eMERGE request to accommodate the inclusion of possibly multiple phenotypes associated with a pathogenic/Likely Pathogenic variant.

**Reference(s):** `Jira #20552  <https://jira.hl7.org/browse/FHIR-20552?filter=-2>`_

.. _issue-14:

#14 InhDisPath value (CC) made extensible
-----------------------------------------

**HL7 WG:** Clinical Genomics | **Category:** Minor

**Description/Resolution:**
Updated ValueSet bindings to extensible for the valueCodeableConcept element in the InheritedDiseasePathogenicity profile to accommodate additional entries from the Clinvar Clinical Significance list. Furthermore, the Clinical Genomics WG also updated `other ValueSet bindings <https://docs.google.com/document/d/1E-nal_OPhJ8SSaIN_f9XqiLI5lyuGyhTIbUae8MWLMU/edit>`_ to be extensible.

**Reference(s):** `Jira #20549  <https://jira.hl7.org/browse/FHIR-20549?filter=-2>`_

.. _issue-15:

#15 Genomics Report category cardinality changed to 0..*
--------------------------------------------------------

**HL7 WG:** Clinical Genomics | **Category:** Minor

**Description/Resolution:**
The cardinality of the category element in the |genotype-prof| was updated from 0..1 to 0..* per eMERGE request to accommodate the inclusion of multiple test categories (LAB, GE) if required.

**Reference(s):** `Jira #20538  <https://jira.hl7.org/browse/FHIR-20538?filter=-2>`_

.. _issue-citing-assesed-meds:

#16 Citing specific assessed medication implications
----------------------------------------------------

**HL7 WG:** Clinical Genomics | **Category:** Minor

**Description/Resolution:**
DISCUSS, IT DOES NOT LOOK LIKE THIS IS COMPLETED

**Reference(s):** `Zulip CG: relatedArtifact extension request  <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/relatedArtifact.20extension.20change.20request>`_

.. _issue-report-sign-out-v-sent-dates:

#17 Report Sign-Out v Report Sent Date
---------------------------------------

**HL7 WG:** Orders and Observations | **Category:** Minor

**Description/Resolution:**
eMERGE tracks both the report sign-out date and report issued date. However, as the Diagnostic Report only records the report issued date, per OO recommendation, it was decided to include the report issued date in the Genomics Report Profile and to track the report sign-out date internally.

**Reference(s):** `Zulip OO: date reported vs sign-off date  <https://chat.fhir.org/#narrow/stream/179256-Orders-and.20Observation.20WG/topic/date.20reported.20vs.20sign-off.20date>`_

.. _issue-recommendation-with-multi-reasons:

#18 RecommendedAction Task with Multiple Reasons
------------------------------------------------

**HL7 WG:** FHIR Infrastructure | **Category:** Minor

**Description/Resolution:**
The cardinality for reasonCode and reasonReference elements in the |task-res| resource was updated 0..* per eMERGE request. This request is accommodate use cases where we might need to indicate that multiple Observations resulted in a particular Task Recommendation.

**Reference(s):** `Jira #25255 <https://jira.hl7.org/browse/FHIR-25255?filter=-2>`_ | `Zulip CG: task recommendations <https://chat.fhir.org/#narrow/stream/179197-genomics/topic/task.20recommendations>`_

.. _issue-patient-age:

#19  Add Age to US-Core Patient Profile
---------------------------------------

**HL7 WG:** FHIR Mgmt | **Category:** Unknown

**Description:**
The Patient resource currently only includes Date of Birth but not Age. As DOB is considered PHI, for de-identifying purposes we collect Age instead of (or in addition to) DOB as part of a test order to comply with CLIA regulations. As the Jira ticket to the Patient Administration and FHIR Mgmt WGs on this standard extension request is still pending, we created a `Patient.Age custom extension <https://simplifier.net/eMERGEFHIRExtensionResources/PatientAge/~overview>`_ to handle this requirement.

**Resolution:**
Pending. The Patient Administration Workgroup does not believe that a standard extension for Age for the Patient resource should be created.

**Reference(s):** `Jira #24652 <https://jira.hl7.org/browse/FHIR-24652>`_

.. _issue-research-flag:

#20  Clinical v Research Flag
-----------------------------

**HL7 WG:** Clinical Genomics | **Category:** Unknown

**Description:**
The BCM HGSC Clinical Lab produces both clinical and research genetic reports and we generally tag and label the reports as research or clinical. Typically, research reports are do not go through Sanger or similar confirmation process. It would be helpful to have a flag in the DiagnosticReport indicating if a report is clinical or research.

**Resolution:**
Pending.  This is an optional feature request and does not impact the current design of the eMERGE FHIR Specification.

**Reference(s):** `Jira #22782 <https://jira.hl7.org/browse/FHIR-22782?filter=-2>`_

.. _issue-fixed-report-code:

#21 Why is the Report code fixed to LOINC:81247-9?
--------------------------------------------------

**HL7 WG:** Clinical Genomics | **Category:** Unknown

**Description:**
What is the purpose of the LOINC code 81247-9 as a code value for the code field in the Genomics Report resource? How does this code distinguish between different genetics tests e.g. Whole Exome Sequencing, Whole Genome Sequencing, Exome Panels etc.? T

**Resolution:**
Pending. This code is currently added to the eMERGE FHIR Specification to meet the requirement of the Genomics Reporting IG.

*Clinical Genomics WG feedback:* Current guidance is to require this code be present on all genetic reports. Note that you can supply a more granular code in another system as an additional coding on the same CodeableConcept to cater to more specific use cases.

**Reference(s):** `Jira #19831 <https://jira.hl7.org/browse/FHIR-19831?filter=-2>`_

.. _issue-recommendation-codes:

#22 RecommendedAction "code" should be extensible
-------------------------------------------------

**HL7 WG:** Clinical Genomics | **Category:** Unknown

**Description:**
The change request is to make the "code" binding extensible versus the current state of required. Currently, there are 3 codes available for recommendations and it seems highly unlikely these will be robust enough to serve the implementations yet to occur. This is an enhancement requirement for the future and does not impact the current eMERGE FHIR Specification implementation.

**Resolution:**
Pending

**Reference(s):** `Jira #25187 <https://jira.hl7.org/browse/FHIR-25187?filter=-2&jql=reporter%20%3D%20lbabb%20%20order%20by%20created%20DESC>`_ | `Zulip CG: task recommendation follow up <https://chat.fhir.org/#narrow/stream/179197-genomics/topic/task.20recommendation.20follow.20up>`_

.. _issue-disclaimers:

#23 Inclusion of Disclaimers
----------------------------

**HL7 WG:** Orders and Observations | **Category:** Unknown

**Description:**
Test disclaimers are a standard inclusion in every eMERGE report.  The disclaimer is not case specific. Without a  option to include the disclaimer in the GenomicsReport or an Observation currently, a `TestDisclaimer custom extension <https://simplifier.net/emergefhirextensionresources/testdisclaimer>`_ was created to house the disclaimer and the disclaimer was added to the GenomicsReport Profile.

**Resolution:**
Pending

**Reference(s):** `Zulip CG: Report Comments <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Report.20Comments>`_
