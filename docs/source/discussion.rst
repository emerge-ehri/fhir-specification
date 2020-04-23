.. _discussion:

Discussion
==========

.. Warning::
    This document is a work in progress and is not ready for production use.

This section includes a review of the issues that required resolution as well as topics and questions raised and discussed during the development and implementation of this specification.
These issues and topics range in effort and complexity which are qualified as major or minor.

Issues & Resolutions
During the course of implementing the eMERGE Results using the |fhir-gr-ig-short| a number of issues were uncovered, discussed and resolved. The noteworthy issues are summarized below along with their outcome.

#1 Group composite sections and associated results in one report
Links: Jira(https://jira.hl7.org/browse/FHIR-19828?filter=-2)  Zulip (https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/FHIR.20representation.20of.20a.20genetics.20test.20with.20multiple.20test.2E.2E.2E)
Group: Clinical Genomics Workgroup
Category: Major
Description: The eMERGE report includes both gene panel and PGx results in one report. Though still bundled together, we plan to separate the gene panel and PGx results. The result will be a composite report that includes separate interpretations and results for the gene panel and PGx respectively.
Resolution: Use the Grouper Profile to group all related gene panel & PGx result resources, respectively. This will enable consuming EHR systems to utilize the panel & PGx results as disparate components.

#2 Inclusion of Test Info, Methodology, References
Links: Jira(https://jira.hl7.org/browse/FHIR-19827?filter=-2)  Zulip (https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Report.20Sections)
Group: Clinical Genomics Workgroup
Category: Major
Description: Lab developed tests (LDTs) are standard practice in clinical genetic testing. As such it is useful and needed (for eMERGE) to share the assay title, code, description, methodology and references (citations) that appear in the report.
Resolution: The recommendation to use the PlanDefinition resource to represent the eMERGE test info and associated elements was satisfactory for the eMERGE use case. More investigation for broader application across the domain could be useful.

#3 Inclusion of Report Comments
Links: Jira(https://jira.hl7.org/browse/FHIR-22830?filter=-2)  Zulip (https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Report.20Comments)
Group: Clinical Genomics Workgroup
Category: Major
Description: eMERGE and other clinical genetic test results have a comments or additional notes section with case specific information. These comments are not really recommendations, conclusions or observations. They are additional information that the reporting lab wants to provide the ordering physician and patient related to the overall outcomes or to some grouped set of results.
Example: Example: Analysis of exonic deletions and duplications is pending and were not assessed at this time. The report will be updated if pathogenic or likely pathogenic deletions or duplications are detected in this patient's sample.
Resolution: Use an Observation result associated to the DiagnosticReport to house comments. This Observation is assigned the LOINC “Report Comment” code and the comments is mapped to the value field.

#4 Inclusion of Recommendations
Links: Jira(https://jira.hl7.org/browse/FHIR-22830?filter=-2)  Zulip (https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Report.20Comments)
Group: Clinical Genomics Workgroup
Category: Major
Description: eMERGE reports include a proposed recommendation section.  We want to represent this to enable actionability for the consuming EHR system but also ensure that this is a requested proposed recommendation and not a resulting order.
Resolution: Use the RecommendedTask extension in DiagnosticReportt to reference a Task. The Task resource itself, with a status of requested and intent of proposal, fulfilled our requirements.

#5. Nested & Indirect Result Referencing - hasMembers & derivedFrom?
Links: Zulip (https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Indirect.20Results)
Group: Clinical Genomics Workgroup
Category: Major
Description: eMERGE reports include a proposed recommendation section.  We want to represent this to enable actionability for the consuming EHR system but also ensure that this is a requested proposed recommendation and not a resulting order.
Resolution: Use the RecommendedTask extension in DiagnosticReportt to reference a Task. The Task resource itself, with a status of requested and intent of proposal, fulfilled our requirements.


6. New Identifier Type Code(s)
7. InhDisPath phenotype cardinality change
8. InhDisPath value (CC) made extensible
9. DR category cardinality changed to 0..*
10. RelatedArtifact extension in Observation Components - Assessed Meds Citations (CG)
11. Distinction between Report Sign-Out/Off Date and Report Sent Date - (Sign Out = Issue) (OO)

12. RecommendedAction Task reasonRef cardinality to 0..* (OO)
Group: CG | us-core | O&O | ?
Description


13. Add Age to US-Core Patient Profile (PatAdm)
14. Clinical vs Research Flag (Core)
15. Why is DR.code fixed to LOINC 81247-9? (CG)
16. RecommendedAction profile "code" should be extensible (CG)
17. Inclusion of disclaimers to Observation and DR  (minor)
18. Representation of Validation/Confirmation Testing  (minor)
19. Inclusion of Interpretation Summary Text to Observation & DR  (major)



Topics & Questions
""""""""""""""""""
Adoption and Direction *  (Mullai) - one pager

    We are making recommendations to eMERGE - so we'd like more evidence to inform our decisions.
    Groups/Labs/EHRs adopting or planning to adopt CG IG STU1 spec?
    EPIC usage of HL7 V2 for their Genomics module
    How can the spec be readily used?
    Are there plans to create targeted IGs that can simplify adoption?


Open Questions  (one page for each major topic)

    Management of Secondary Findings  (major)  - incidental findings v secondary findings  (clinically significant observations not directly resulting from primary indication)
    Definitional Variant Data Types  (major)  - Larry
    Representation of Gene Coverage  (major)  - Mullai
    Need for computational representation of tests (major)








.. COMMENTING OUT BELOW UNTIL WE DECIDE WETHER IT BELONGS AND TO WHAT LEVEL OF DEPTH
..
.. Test Result Scope
.. ^^^^^^^^^^^^^^^^^
.. TODO Consider adding this to the discussion spec at a high level. No need for a detailed writeups.
..
.. -- Talk about scope but keep it minimal - revisit how to discuss this.
..
..
.. Below are the various use cases that this eMERGE specification supports.
..
.. Included in eMERGE III Results
.. """""""""""""""""""""""""""""""
.. * Postive Gene Panel results
..     * SNP finding positive  (note about CNV finding challenges)
..     * Positive for secondary findings only
..     * Positive for both primary indication and secondary findings
.. * Negative Gene Panel results
.. * Nested PGx results reporting
.. * Custom gene and SNP list for clinical site (covered by plan definition approach)
..
.. Potential Future Use Cases
.. """"""""""""""""""""""""""""
.. * PRS results (discussed but not supported)
.. * Research only reports (discussed but not supported)
