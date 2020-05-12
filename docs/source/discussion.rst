.. _discussion:

Discussion
==========

.. Warning::
    This document is a work in progress and is not ready for production use.

This section includes a review of the issues that required resolution as well as topics and questions raised and discussed during the development and implementation of this specification. The specification was created using STU1 of the Genomics Reporting IG and the section below pertains to the work done by the BCM and Broad Institute team towards the creation of the eMERGE FHIR Specification using STU1 of Genomics Reporting IG during the year 2019. It should be noted that with the Clinical Genomics WG continuing to work on the draft of the STU2 version of the IG, there might be changes and variations between the STU1 version discussed here to the draft version currently being developed by the Clinical Genomics WG.
These issues and topics range in effort and complexity which are qualified as major or minor.

Issues & Resolutions
During the course of implementing the eMERGE Results using the |fhir-gr-ig-short| a number of issues were uncovered, discussed and resolved. Noteworthy issues are summarized below along with their outcome. Also included is extended documentation related to the collaboration and tracking of these items with the associated HL7 FHIR Working Groups.

**#1 Group multiple sections and associated results in one composite report**

**HL7 Workgroup:** Clinical Genomics 

**Category:** Major 

**Description:** The eMERGE clinical genetic report includes both gene panel and PGx results in one report. Though still bundled together, we planned to separate the gene panel and PGx results; the result will be a composite report that includes separate interpretations and results for the gene panel and PGx respectively.  This approach of organizing multiple results in the same report, in addition to allowing diagnostic labs to bundle multiple result panels together will also enable consuming EHR systems to efficiently retrieve the results required for computation, storage or CDS.

**Resolution:** Use the `Grouper <http://hl7.org/fhir/uv/genomics-reporting/grouper.html>`_ Profile to group all related gene panel & PGx result resources, respectively. This will enable consuming EHR systems to utilize the panel & PGx results as disparate components.

**Extended Documentation:** `Jira ticket  <https://jira.hl7.org/browse/FHIR-19828?filter=-2>`_ | `Discussion on Zulip with Clinical Genomics WG  <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/FHIR.20representation.20of.20a.20genetics.20test.20with.20multiple.20test.2E.2E.2E>`_

-----

**#2 Inclusion of Test Information, Methodology and References**

**HL7 Workgroup:** Orders and Observation

**Category:** Major 

**Description:** Lab developed tests (LDTs) are standard practice in clinical genetic testing. As such it is useful and needed (for eMERGE) to share the assay title, code, description, methodology and references (citations) that appear in the report. Resolution: The recommendation to use the PlanDefinition resource to represent the eMERGE test info and associated elements was satisfactory for the eMERGE use case. More investigation for broader application across the domain could be useful.

**Resolution:** The recommendation to use the PlanDefinition(https://www.hl7.org/fhir/plandefinition.html) resource to represent the eMERGE test info and associated elements was satisfactory for the eMERGE use case. More investigation for broader application across the domain could be useful.

**Extended Documentation:** `Jira ticket <https://jira.hl7.org/browse/FHIR-19827?filter=-2>`_ | `Discussion on Zulip with Clinical Genomics WG  <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Report.20Sections>`_

-----

**#3 Inclusion of Report Comments**

**HL7 Workgroup:** Orders and Observation 

**Category:** Major 

**Description:** eMERGE and other clinical genetic test results have a comments or additional notes section with case specific information (see Example). These comments are not really recommendations, conclusions or observations. They are additional information that the reporting lab wants to provide the ordering physician and patient related to the overall outcomes or to a grouped set of results.
Example: Analysis of exonic deletions and duplications is pending and were not assessed at this time. The report will be updated if pathogenic or likely pathogenic deletions or duplications are detected in this patient's sample.

**Resolution:** As these comments are about the report itself and not a particular Observation, based on recommendations by the Orders and Observations WG, the resolution was to use an Observation result associated to the DiagnosticReport to include the comments. This Observation is assigned the LOINC “Report Comment” 86467-8 code and with the comments being mapped to the value field. Though sufficing for the short term, a more robust long term approach might be to evaluate the addition of a comments element to the Diagnostic Report Resource. 

**Extended Documentation:** `Jira ticket <https://jira.hl7.org/browse/FHIR-22830?filter=-2>`_
| `Discussion on Zulip with Clinical Genomics WG  <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Report.20Comments>`_ | `Discussion on Zulip with Orders and Observation WG <https://chat.fhir.org/#narrow/stream/179256-Orders-and.20Observation.20WG/topic/Notes.20on.20Observations.20and.20DR/near/173777260>`_

-----
**#4 Inclusion of Recommendations**

**HL7 Workgroup:** Orders and Observation 

**Category:** Major 

**Description:** eMERGE reports include a proposed recommendation section (see Example).  We need to represent this accurately not only to enable actionability for the consuming EHR system but also to ensure that this is a requested proposed recommendation and not a resulting order.
Example: It is recommended that correlation of these findings with the clinical phenotype be performed. Genetic counseling for the patient and at-risk family members is recommended.

**Resolution:** Use the RecommendedTask extension in DiagnosticReportt to reference a Task. The Task resource itself, with a status of requested and intent of proposal, fulfills eMERGE requirements for including proposed recommendations.

**Extended Documentation:** `Jira ticket <https://jira.hl7.org/browse/FHIR-22830?filter=-2>`_
| `Discussion on Zulip with Clinical Genomics WG  <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot/topic/Report.20Comments>`_ 
 
-----

#5. Nested & Indirect Result Referencing - hasMembers & derivedFrom? - **What is this one, I don't recall?**
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

The principal goal of the eMERGE network for this project was to explore the feasibility of using FHIR in general and the Genomics Reporting IG in particular for representing clinical genomic results and for EHR Integration with Clinical Decision Support. Part of this feasibility analysis was also to explore the potential of using FHIR as the interoperability standard for the upcoming eMERGE Phase IV. To this end, the Baylor College of Medicine and Broad Institute team were tasked with putting together direction and adoptions recommendations for the eMERGE Network to evaluate going forward.   As the roadmap and plans of the HL7 Clinical Genomics Workgroup  regarding  the Genomics Reporting IG would have somewhat of a direct bearing both on the goals of this project as well as a projected plan for future eMEREGE phases, the Baylor College of Medicine and Broad Institute team wanted to ensure that appropriate discussion with the Clinical Genomics Workgroup was used to inform their decisions and recommendations. 

With this in mind, the  team highlighted the topic of Adoption Readiness and Direction  during a presentation of eMERGE FHIR work to  the  HL7 Clinical Genomics Workgroup in December 2019 with questions ranging across two categories.  The first category, about the Genomics Reporting IG itself, included the following questions:

- What is the adoption readiness of the IG itself?
- Are there any plans to create targeted IGs to simplify adoption?

The second category, about the interest and keenness of the EHR vendors and Diagnostic Labs  in this space, included the following questions:

- How  are  the major EHR vendors  and Diagnostic Labs positioned with respect to considering the use of FHIR and in particular the Genomics Reporting IG as an interoperable standard for clinical genomic reporting?
- Are there any EHR vendors, Diagnostic Labs or Institutions working on or planning on adopt the Genomics Reporting IG STU1 for a pilot or for full scale production?


Subsequent related discussions with the HL7 Clinical Genomics Workgroup helped the team identify at least two production pilots, in addition to the eMERGE pilot,  that capitalized on the Genomics Reporting IG STU1 - the first one led by Bob Milius at the NMDP, regarding the creation of a HLA Reporting IG based on the Genomics Reporting IG STU1 and the second led by Kevin Power at Cerner, regarding a pilot with a Diagnostic Lab using the Genomics Reporting IG STU1. 
On the subject of adoption readiness, the HL7 Clinical Genomics Workgroup recognizing the somewhat steep learning curve associated with using the Genomics Reporting IG, is currently eliciting input from Subject Matter Experts for STU2 themes, documented and discussed at https://chat.fhir.org/#narrow/stream/179197-genomics/topic/Themes.20for.20STU2

The team, in light of the collaborations and discussions with the HL7 Clinical Genomics Workgroup, experiences with the creation of eMERGE FHIR specification and the subsequent pilot, study of the ecosystem and landscape around this space, 
Additionally, the BCM/Broad team based on its work on creating the specification, implementing the pilot and collaborations/discussions with the CG WG, puts forth the following recommendations:

1. The Genomics Reporting IG STU1 specification can be utilized successfully, as proven by the eMERGE specification and the pilot, but cannot be readily and easily used by non-SMEs;
2. The STU1 of the IG needs more maturity for full scale production implementations particularly in areas such definitional vs observations resources,  management of secondary findings, interpretation summary text representation, knowledge bases of clearly findings/recommendations etc.;
3. The current IG is broad and tries to cover multiple use cases and edge cases, targeting minimal viable products or headlining real-world usage scenarios might be helpful for widespread adoption;
4. Considering the diversity and heterogeneity of the eMERGE Network, participation in STU2 themes and collaboration with HL7 Clinical Genomics Workgroup during the upcoming eMERGE Phase iV will help inform the roadmap of the specification going forward.




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
