.. _issues-and-resolutions:

Issues & Resolutions
====================

This section includes a review of the issues that were identified and raised with the |hl7-cg-wg|.

The section below pertains to the work performed by the eMERGE specification and pilot development teams to create this specification based on the |fhir-gr-ig-short| during 2019. When this project started the |hl7-cg-wg| was working on the STU1 release of the |fhir-gr-ig-short|. As such some issues were able to be addressed quickly (e.g. Composite reporting). At the time of finalizing the specification the |hl7-cg-wg| is continuing to address and improve changes, which this work has informed.

While the eMERGE specification design and pilot development teams worked independently to apply the |fhir-gr-ig-short|, significant gaps or insufficiencies were documented as issues.

**Difficulty**
A rating of *Major* or *Minor* is assigned to each issue to represent the level of difficulty to design a solution and gain consensus for its adoption by the developers of the HL7 GR IG or FHIR specification if needed.

**Resolution Status**
The HL7 CG WG members helped address eMERGE issues by clarifying existing options, adopting changes in GR IG STU1 or submitting issue to the HL7 Jira board for consideration of changes to future GR IG or FHIR specification releases. Most of the issues required immediate resolutions to complete the eMERGE FHIR specification and pilot projects. Several issues were complex and not resolved. These were deferred by eMERGE but were documented and raised as they were determined to be important for inclusion in a GR IG and FHIR specification to provide more accurate utility of genetic test results.

The following resolution statuses are used to help summarize the impact of this project had on the |fhir-gr-ig-short| development.

- **Clarification** - a solution in the current |fhir-gr-ig-short| existed and needed clarification.
- **GR IG Change** - changes were applied to address the issue in STU1's final release.
- **Workaround** - a general or custom extension was added for eMERGE only.
- **Deferred** - the issue was deferred and not resolved, CG IG was informed of the issue.

**HL7 Jira Tickets**
Twenty one (21) HL7 Jira tickets of varying scopes and sizes were submitted based on this work. Some of the issues reference those Jira tickets below, but some may not be listed. There statuses at the time this was published are: 10 Triaged, 5 Published, 3 Applied, 2 Resolved/NoChange, 1 Resolved/Changed.

.. _issue-composite-reporting:

#1 Composite Reporting
----------------------
**Difficulty:** Major | **Resolution Status:** GR IG Change

**Description:** Group multiple sections and associated results in one composite report.

Diagnostic labs frequently include several types of results in genetic test reports which then appear in separate sections within an overarching report. eMERGE genetic reports are examples of this model and include both gene panel interpretation as well as PGx results. This style of reporting is analogous to the notion of composite reporting whereby while individual sections of the report can be treated independently they are still combined together as they rely on shared findings from an upstream wet lab assay such as Whole Exome Sequencing or Gene Panels. We evaluated two options to represent composite reporting:  1. Nested Diagnostic Report Resources or 2. The Observation Grouper Profile. Based on analysis and collaborative discussions with the |fhir-gr-ig-short|, we decided on the |grouper-prof| Profile.

**Resolution:**
Use the |grouper-prof| Profile added to STU1 to group all related gene panel & PGx result resources, respectively.

**HL7 CG WG & FHIR Suggestions:**
The resolution to use the Observation based |grouper-prof| Profile allows consuming EHR systems to utilize the Gene Panel & PGx results as separate components. Furthermore, while the usage of |grouper-prof| Profile is well-defined by the GR IG, the concept of nested Diagnostic Reports was still under investigation and not ready for adoption. The benefit of this approach also lends itself to including additional sections such as Polygenic Risk Scores to genetic reports and potentially other related report results that future composite reporting use cases may require. The Jira issue referenced below suggests that the HL7 FHIR designers consider how these more robust composite reporting use cases be handled.

**Reference(s):** `Jira #19828  <https://jira.hl7.org/browse/FHIR-19828?filter=-2>`_ | `Zulip CG: FHIR representation of a genetics test with multiple test... <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/FHIR.20representation.20of.20a.20genetics.20test.20with.20multiple.20test.2E.2E.2E>`_

.. _issue-nested-results:

#2 Nested Results
-----------------
**Difficulty:** Major | **Resolution Status:** Clarification

**Description:**
The eMERGE Diagnostic Report utilizes the Grouper resource to aggregate primary Observations (results) which in turn references other Observation results using either hasMember or derivedFrom. Without the reference to all Observations (results) directly in the Diagnostic Report, two related concerns are:

1. Will consuming systems be impacted without a direct linkage of all results in the Diagnostic Report?
2. Can the derivedFrom be used to reference a related value that is not directly a result for this Diagnostic Report?

**Resolution:**
With the usage of the Grouper, hasMember and derivedFrom clearly documented, it was agreed that using nested Observation references streamlines the Diagnostic Report bundle. It was also agreed that derivedFrom could reference a related reference that is not a direct result for this Diagnostic Report.

**Reference(s):** `Zulip CG: Indirect Results <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Indirect.20Results>`_

.. _issue-test-information:

#3 Test Information
-------------------
**Difficulty:** Major | **Resolution Status:** Clarification

**Description:** Inclusion of Test Information, Methodology and References

Lab developed tests (LDTs) are standard practice in clinical genetic testing. As such it is useful and needed (for eMERGE) to share the assay title, code, description, methodology and references (citations) that appear in the report.

**Resolution:**
The recommendation to use the |plandefinition-res| resource to represent the eMERGE test info and associated elements was satisfactory for the eMERGE use case.

**HL7 O&O WG & FHIR Suggestion:**
More investigation for broader application across the domain could be useful. The assay definition, covered regions, methodology, etc... should be structured such that the elements can be reliably exchanged, accessed and used in relaying documentation, order guidance and computational queries for reporting and decision support.

**Reference(s):** `Jira #19827 <https://jira.hl7.org/browse/FHIR-19827?filter=-2>`_ | `Zulip CG: Report sections <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Report.20Sections>`_

.. _issue-interp-summary:

#4  Interpretation Summary
--------------------------
**Difficulty:** Major | **Resolution Status:** Workaround

**Description:**
Textual findings/interpretations are currently included in the eMERGE genetic report both at the report level and at the individual result (Observation) level.

**Resolution:**
Without a  option to include this kind of interpretative or summary text in the GenomicsReport or an Observation currently, a `InterpretationSummaryText custom extension <https://simplifier.net/emergefhirextensionresources/interpretationsummarytext>`_ was created to house this information.

**HL7 CG WG & FHIR Suggestions:**
Jira ticket request submitted and for consideration by both Clinical Genomics and Orders and Observations WGs. This is of fairly significant importance to the genetic testing community.

**Reference(s):** `Jira #20978 <https://jira.hl7.org/browse/FHIR-20978?filter=-2>`_ | `Zulip CG ? <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/search/summary>`_

.. _issue-region-coverage:

#5  Gene/Region Coverage
------------------------
**Difficulty:** Major | **Resolution Status:** Workaround

**Description:**
For every test subject, information about coverage information on the regions studied as part of the eMERGE test panel is attached as part of the results. Generally information provided includes chromosome, gene, transcript, CDS, start position, end position and coverage. Though the Region Studied resource does seem like a possible candidate to represent this information, if we have to create a separate region studied resource for each of the regions that are in this test, that might run into 100s or 1000s of region studied resources and might not be a scalable solution. Ideally, it might be helpful to have a resource which we can use to include all the regions covered as part of the test.

**Resolution:**
In the interim, for the current version of the eMERGE specification, we are attaching the coverage file (BED format) to the GenomicsReport as a RelatedArtifact.

**HL7 CG WG & FHIR Suggestions:**
The current published solution associated with the Jira ticket #16258 does not seem to be a reasonable solution for large gene panels and a better solution should be considered.

**Reference(s):** `Jira (Bob Dolin) #16258 <https://jira.hl7.org/browse/FHIR-16258?jql=text%20~%20%22gene%20coverage%22>`_ | `Zulip CG: Guidance re region studied <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Guidance.20re.20region.20studied>`_

.. _issue-recommendations:

#6 Recommendations
------------------
**Difficulty:** Major | **Resolution Status:** Clarification

**Description:**
eMERGE reports include a proposed recommendation section (see Example).  We need to represent this accurately not only to enable actionability for the consuming EHR system but also to ensure that this is a requested proposed recommendation and not a resulting order.

*Example:* It is recommended that correlation of these findings with the clinical phenotype be performed. Genetic counseling for the patient and at-risk family members is recommended.

**Resolution:**
Use the RecommendedTask extension in DiagnosticReport to reference a Task. The Task resource itself, with a status of requested and intent of proposal, fulfills eMERGE requirements for including proposed recommendations.

.. _issue-secondary-findings:

#7 Secondary Findings
----------------------
***Difficulty:** Major | **Resolution Status:** Clarification

**Description:**
The |fhir-gr-ig-short| defines an abstract observation profile, |genomics-base-prof|, that is the basis for all of their observations. GenomicsBase contains a |2nd-finding-ext| extension which is used to indicate when a given observation is a secondary finding (SF). The eMERGE use case considered the need for easily identifying and segregating observations that are primary from secondary. Additionally, there are a number of different types of observations that are used in the eMERGE defined assay. Only |inh-dis-path-prof| observations may potentially be SFs since they represent the specific variant-disease findings that meet a given SF policy and is different than the primary indication for testing. The IG directs that the extension should only be used when the observation is a SF and the specific SF policy should be specified within the extension on each observation. eMERGE initially considered creating a simple custom boolean extension on the |inh-dis-path-prof| to indicate whether the interpretation was a SF or not and associating the SF policy with the assay methodology in the |plandefinition-res|.

**Resolution:**
Use the CG IGs |2nd-finding-ext| extension on the |inh-dis-path-prof| profile. The choice was made to use the CodeableConcept's text field to indicate whether the inherited disease pathogenicity observation was a secondary finding or not.

**Reference(s):**  `Zulip CG: Representation of secondary findings <https://chat.fhir.org/#narrow/stream/179197-genomics/topic/Representation.20of.20secondary.20findings>`_

.. _issue-variant-data-types:

#8 Variant Data Types
----------------------
**Difficulty:** Major | **Resolution Status:** Deferred

**Description:**
The current flexibility in exchanging variant level information may be helpful in allowing adoption. However, implementers should be cautioned about the perils of using these forms of representation for clinical decision support (CDS). Clinical grade precision will require more rigor and guidance. Definitional variant data types and/or resources would help isolate the concern and advance progress towards that aim.

**Resolution:**
For more information on Variant Representation see :ref:`variant-representation` Discussion.

**Reference(s):**  `Zulip CG: Variant Data Type Proposal <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Variant.20Data.20Type.20Proposal>`_

.. _issue-report-comments:

#9 Report Comments
------------------
**Difficulty:** Minor | **Resolution Status** Clarification

**Description:**
eMERGE and other clinical genetic test results have a comments or additional notes section with case specific information (see Example). These comments are not really recommendations, conclusions or observations. They are additional information that the reporting lab wants to provide the ordering physician and patient related to the overall outcomes or to a grouped set of results.

*Example:*
Analysis of exonic deletions and duplications is pending and were not assessed at this time. The report will be updated if pathogenic or likely pathogenic deletions or duplications are detected in this patient's sample.

**Resolution:**
These comments are about the report itself or a section of the report and not a particular Observation. The O&O WG recommended using a dedicated Observation result associated to the DiagnosticReport to include the comments. This Observation is assigned the LOINC “Report Comment” 86467-8 code and with the comments being mapped to the value field.

**HL7 O&O WG & FHIR Suggestions:**
Though sufficing for the short term, a more robust long term approach might be to evaluate the addition of a comments element to the Diagnostic Report Resource.

**Reference(s):** `Jira #22830 <https://jira.hl7.org/browse/FHIR-22830?filter=-2>`_ | `Zulip CG: Report Comments  <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Report.20Comments>`_ | `Zulip OO: Notes on Observations <https://chat.fhir.org/#narrow/stream/179256-Orders-and.20Observation.20WG/topic/Notes.20on.20Observations.20and.20DR/near/173777260>`_

.. _issue-confirmation-testing:

#10 Confirmation Testing
------------------------
**Difficulty:** Major | **Resolution Status:** Workaround

**Description:**
The eMERGE report includes information about confirmatory testing for both SNVs and CNVs.

**Resolution:**
Though this request was deliberated and discussed by the Clinical Genomics WG, a resolution was not reached at the time of the creation of the eMERGE FHIR Specification. As a temporary solution, confirmation information has been added to the note element of the Inherited Disease Pathogenicity profile for the eMERGE FHIR Specification.

**HL7 CG WG & FHIR Suggestions:**
The Jira ticket below is triaged and considered for future use. The idea of adding a confirmationMethod attribute to the Variant Profile to indicate when specific findings have been confirmed by an orthogonal method may be sufficient. This may also be something that could be added to the testing methodology or possibly as a separate report level observation that covers all findings in the report.

**Reference(s):** `Jira #19829 <https://jira.hl7.org/browse/FHIR-19829?filter=-2>`_ | `Zulip CG: Sanger confirmation testing <https://chat.fhir.org/#narrow/stream/179197-genomics/topic/Sanger.20confirmation.2Ftesting>`_

.. _issue-path-phenotypes:

#11 Pathogenicity Phenotypes
----------------------------
**Difficulty:** Minor | **Resolution Status:** GR IG Change

**Description:**
Inherited disease pathogenicity interpretations can sometimes require a condition componenent that is defined by multiple phenotypes.

**Resolution:**
The cardinality of the associated-phenotype element in the |inh-dis-path-prof| profile was updated from 0..1 to 0..* per eMERGE request to accommodate the inclusion of possibly multiple phenotypes associated with a pathogenic/Likely Pathogenic variant.

**Reference(s):** `Jira #20552  <https://jira.hl7.org/browse/FHIR-20552?filter=-2>`_

.. _issue-path-values:

#12 Pathogenicity Values
------------------------
**Difficulty:** Minor | **Resolution Status:** GR IG Change

**Description:**
Terms such as risk factor or risk allele are being considered by the ACMG. Constraining the valueset binding for pathogenicity to not be extensible is not reasonable.

**Resolution:**
Updated ValueSet bindings to extensible for the valueCodeableConcept element in the InheritedDiseasePathogenicity profile to accommodate additional entries from the Clinvar Clinical Significance list. Terms such as risk factor or risk allele are being considered by the ACMG

Note: the Clinical Genomics WG also updated `other ValueSet bindings <https://docs.google.com/document/d/1E-nal_OPhJ8SSaIN_f9XqiLI5lyuGyhTIbUae8MWLMU/edit>`_ to be extensible.

**Reference(s):** `Jira #20549  <https://jira.hl7.org/browse/FHIR-20549?filter=-2>`_

.. _issue-rept-category:

#13 Report Category
-------------------
**Difficulty:** Minor | **Resolution Status:** GR IG Change

**Description:**
Multiple report categories are needed to specify when a lab produces genetic test results report.

**Resolution:**
The cardinality of the category element in the |genotype-prof| was updated from 0..1 to 0..* per eMERGE request to accommodate the inclusion of multiple test categories (LAB, GE) if required.

**Reference(s):** `Jira #20538  <https://jira.hl7.org/browse/FHIR-20538?filter=-2>`_

.. _issue-assesed-med-citations:

#14 Assessed Med Citations
--------------------------
**Difficulty:** Major | **Resolution Status:** Workaround

**Description:**
In the eMERGE PGx results the individual interpretations for each PGx diplotype found in the panel had one or more associated medications or assessed medications from the GR IG profile. Each assessed medication may also have one or more citations from the CPIC guidelines.

**Resolution:**
The CG WG members suggested the use of the relatedArtifact at the top-level observation, however, some implications had different guidelines for each medication within the same observed medication implication. The eMERGE team determined the association of the CPIC guidelines was most appropriately associated within the assessed medication component. So a custom extension was added to the medication implication's assessed medication component to add a 0..* related artifact whereby the guidelines associated to a given medication could be linked.

**Reference(s):** `Zulip CG: relatedArtifact extension request  <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/relatedArtifact.20extension.20change.20request>`_

.. _issue-sign-out-v-sent-dates:

#15 Sign-Out v Sent Date
------------------------
**Difficulty:** Minor | **Resolution Status:** Workaround

**Description:**
eMERGE tracks both the report sign-out date and report sent date, which can differ. However, as the Diagnostic Report only records the report issued date, per Orders & Observations WG recommendations.

**Resolution:**
eMERGE decided to use the report issued date in the Genomics Report Profile to include the sign-out date and to defer sending the report sent date, which represented the date the report was sent out to the ordering provider.

**Reference(s):** `Zulip OO: date reported vs sign-off date  <https://chat.fhir.org/#narrow/stream/179256-Orders-and.20Observation.20WG/topic/date.20reported.20vs.20sign-off.20date>`_

.. _issue-recommendation-reasons:

#16 Recommended Followup Reasons
--------------------------------
**Difficulty:** Minor | **Resolution Status:** Workaround

**Description:**
The cardinality for reasonReference element in the |task-res| resource is 0..1 and should be modified to support multiple reasons if needed. This request will accommodate use cases where implementers might need to indicate that multiple Observations resulted in a particular Task Recommendation.

**Resolution:**
Unresolved. Did not impact eMERGE's use case.

**HL7 CG WG & FHIR Suggestions:**
Only 1 code was needed for the eMERGE study. The Recommended followup profile has yet to be corrected to support multiple reason references post STU1.

**Reference(s):** `Jira #25255 <https://jira.hl7.org/browse/FHIR-25255?filter=-2>`_ | `Zulip CG: task recommendations <https://chat.fhir.org/#narrow/stream/179197-genomics/topic/task.20recommendations>`_

.. _issue-recommended-followup-codes:

#17 Recommended Followup Codes
------------------------------
**Difficulty:** Minor | **Resolution Status:** GR IG Change

**Description:**
The change request is to make the "code" binding extensible versus the current state of required. Currently, there are 3 codes available for recommended followup codes and it seems highly unlikely these will be robust enough to serve the implementations yet to occur. This is an enhancement requirement for the future and does not impact the current eMERGE FHIR Specification implementation.

**Resolution:**
Only 1 code was needed for the eMERGE study. The Recommended followup profile appears to be corrected to support multiple codes post STU1.

**Reference(s):** `Jira #25187 <https://jira.hl7.org/browse/FHIR-25187?filter=-2&jql=reporter%20%3D%20lbabb%20%20order%20by%20created%20DESC>`_ | `Zulip CG: task recommendation follow up <https://chat.fhir.org/#narrow/stream/179197-genomics/topic/task.20recommendation.20follow.20up>`_

.. _issue-disclaimers:

#18 Disclaimers
---------------
**Difficulty:** Major | **Resolution Status:** Workaround

**Description:**
Test disclaimers are a standard inclusion in every eMERGE report.  The disclaimer is not case specific. There is no option to associate a Test Disclaimer on a Diagnostic Report or Genomic Report profile.

**Resolution:**
Without an option to include the disclaimer in the GenomicsReport or an Observation currently, a `TestDisclaimer custom extension <https://simplifier.net/emergefhirextensionresources/testdisclaimer>`_ was created to house the disclaimer and the disclaimer was added to the GenomicsReport Profile.

**Reference(s):** `Zulip CG: performing lab disclaimers <https://chat.fhir.org/#narrow/stream/179197-genomics/topic/performing.20lab.20disclaimers>`_

.. _issue-patient-internal-id:

#19 Patient Internal ID
-----------------------
**Difficulty:** Minor | **Resolution Status:** Clarification

**Description/Resolution:**
eMERGE uses an internal patient identifier to identify a patient. An internal patient identifier is not a defined available `identifier type <https://hl7.org/fhir/R4/valueset-identifier-type.html>`_ for the Patient resource. However Patient internal identifier (code: PI) is available in the `HL7 Version 2 Table 0203 <http://hl7.org/fhir/v2/0203/>`_ but usage of the code PI from Table 0203 resulted in a validation warning during implementation.

**Resolution:**
Based on the response (posted below) to the Jira ticket posted for this issue, it was decided to use Table 0203 and the code PI for the Patient internal identifier.

*Jira ticket response:* "The binding for this attribute is extensible so you are allowed to specify alternate codes if the value set does not cover your required concept. The warning that you are receiving is correct and can be ignored if you have specified a proper code for your purposes."

**Reference(s):** `Jira #24637  <https://jira.hl7.org/browse/FHIR-24637?filter=-2>`_

.. _issue-patient-age:

#20 Patient Age
---------------
**Difficulty:** Major | **Resolution Status:** Workaround

**Description:**
The Patient resource currently only includes Date of Birth but not Age. As DOB is considered PHI, for de-identifying purposes we collect Age instead of (or in addition to) DOB as part of a test order to comply with CLIA regulations.

**Resolution:**
eMERGE created a `Patient.Age custom extension <https://simplifier.net/eMERGEFHIRExtensionResources/PatientAge/~overview>`_ to handle this requirement.

**HL7 PA WG & FHIR Suggestions:**
The Patient Administration Workgroup does not believe that a standard extension for Age for the Patient resource should be created.

**Reference(s):** `Jira #24652 <https://jira.hl7.org/browse/FHIR-24652>`_

.. _issue-research-flag:

#21 Research Flag
-----------------
**Difficulty:** Minor | **Resolution Status:** Deferred

**Description:**
The BCM HGSC Clinical Lab produces both clinical and research genetic reports and we generally tag and label the reports as research or clinical. Typically, research reports are do not go through Sanger or similar confirmation process. It would be helpful to have a flag in the DiagnosticReport indicating if a report is clinical or research.

**Resolution:**
Pending.  This is an optional feature request and does not impact the current design of the eMERGE FHIR Specification. It is believed to be a useful addition to the FHIR DiagnosticReport to distinguish clinical from research study results.

**Reference(s):** `Jira #22782 <https://jira.hl7.org/browse/FHIR-22782?filter=-2>`_
