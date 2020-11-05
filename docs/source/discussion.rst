.. _discussion:

Discussion
==========

.. Warning::
    This document is a work in progress and is not ready for production use.

This section includes topics and questions raised and discussed during the development and implementation of this specification.

.. _adoption-and-direction:

Adoption and Direction
----------------------
The principal goal of the eMERGE network for this project was to explore the feasibility of using FHIR in general and the Genomics Reporting IG in particular for representing clinical genomic results and for EHR Integration with Clinical Decision Support. Part of this feasibility analysis was also to explore the potential of using FHIR as the interoperability standard for the upcoming eMERGE Phase IV. To this end, the Baylor College of Medicine and Broad Institute team were tasked with putting together direction and adoptions recommendations for the eMERGE Network to evaluate going forward.   As the roadmap and plans of the HL7 Clinical Genomics Workgroup  regarding  the Genomics Reporting IG would have somewhat of a direct bearing both on the goals of this project as well as a projected plan for future eMEREGE phases, the Baylor College of Medicine and Broad Institute team wanted to ensure that appropriate discussion with the Clinical Genomics Workgroup was used to inform their decisions and recommendations.

With this in mind, the  team highlighted the topic of Adoption Readiness and Direction  during a presentation of eMERGE FHIR work to  the  HL7 Clinical Genomics Workgroup in December 2019 with questions ranging across two categories.  The first category, about the Genomics Reporting IG itself, included the following questions:

- What is the adoption readiness of the IG itself?
- Are there any plans to create targeted IGs to simplify adoption?

The second category, about the interest and keenness of the EHR vendors and Diagnostic Labs  in this space, included the following questions:

- How  are  the major EHR vendors  and Diagnostic Labs positioned with respect to considering the use of FHIR and in particular the Genomics Reporting IG as an interoperable standard for clinical genomic reporting?
- Are there any EHR vendors, Diagnostic Labs or Institutions working on or planning on adopt the Genomics Reporting IG STU1 for a pilot or for full scale production?

Subsequent related discussions with the HL7 Clinical Genomics Workgroup helped the team identify a few production pilots, in addition to the eMERGE pilot,  that capitalized on the Genomics Reporting IG STU1 - 1. Creation of a HLA Reporting IG based on the Genomics Reporting IG STU led by Bob Milius at the NMDP; 2. A pilot project that utilizes the Genomics Reporting IG STU1 led by Kevin Power at Cerner, in collaboration with a Diagnostic Laboratory; 3. Representation of a VCF using FHIR led by Bob Dolin at Elimu Informatics; 4. An oncology FHIR implementation led by Patrick Werner at MOLIT Institur gGMbH.

On the subject of adoption readiness, the HL7 Clinical Genomics Workgroup recognizing the somewhat steep learning curve associated with using the Genomics Reporting IG, is currently eliciting input from Subject Matter Experts for STU2 themes, documented and discussed at https://chat.fhir.org/#narrow/stream/179197-genomics/topic/Themes.20for.20STU2

The team, in light of the collaborations and discussions with the HL7 Clinical Genomics Workgroup, experiences with the creation of eMERGE FHIR specification and the subsequent pilot, study of the ecosystem and landscape around this space,
Additionally, the BCM/Broad team based on its work on creating the specification, implementing the pilot and collaborations/discussions with the CG WG, puts forth the following recommendations:

1. The Genomics Reporting IG STU1 specification can be utilized successfully, as proven by the eMERGE specification and the pilot, but cannot be readily and easily used by non-SMEs;
2. The STU1 of the IG needs more maturity for full scale production implementations particularly in areas such definitional vs observations resources,  management of secondary findings, interpretation summary text representation, knowledge bases of clearly findings/recommendations etc.;
3. The current IG is broad and tries to cover multiple use cases and edge cases, targeting minimal viable products or headlining real-world usage scenarios might be helpful for widespread adoption;
4. Considering the diversity and heterogeneity of the eMERGE Network, participation in STU2 themes and collaboration with HL7 Clinical Genomics Workgroup during the upcoming eMERGE Phase iV will help inform the roadmap of the specification going forward.

.. _variant-representation:

Variant Representation
----------------------
Observational variants or case-centric variants are precise representations of variants observed in a genetic assay. For clinical use, these must meet a high degree of accuracy and reliability over time as they will be the basis for the variants in EHRs. There is currently no clinical requirement for the content and form of an observational variant in an EHR. Many efforts are underway to store computational variants in EHRs in order to enable greater utility of genomic test results in both clinical decision support (CDS) and in clinical research. HL7 Clinical Genomics (HL7/CG) & Global Alliance for Genomic Health (GA4GH) amongst others are working to identify ways to share a broad spectrum of variation in a computationally sound manner which could open the door for clinical use of this data in EHRs. Observational variation should be comparable between heterogeneous reporting sources and as such should reflect the first form of the variant call made by a given testing technology used to identify the variant in a subject. This means that DNA assays should represent genomic variant forms, likewise, RNA and protein sequencing assays should produce RNA and protein observational variants, respectively. Universally accessible and immutable reference sequences should used as a basis for all variation, making it possible to align and transform the findings between different versions of sequences. Results that contain only derived representations of the observational variants (e.g. transcript or protein variant derived from a DNA assay) add unnecessary risk to the accuracy of the clinically observed variant call and should be assessed by the proper authorities as to whether they should be used in CDS algorithms, even though they might still be useful for clinical research purposes.

Definitional variants or knowledge-centric variants are used to aggregate evidence and assertions about variation to build knowledge that can be used not only within a single lab to generate higher quality variant assessments, but instead to build clinical-grade public knowledge repositories to support physicians and enable CDS in EHRs. Variant knowledge bases like ClinVar and CIViC capture evidence and knowledge around specific variants regardless of which version of the human genome reference build a given variant is aligned. The definitional variants that are the cornerstone of these knowledge bases contain all of the observational forms of the variant that the knowledge base determines to be "the same for the purposes of aggregating related evidence". These definitional forms of the variant are then used to build higher-order assertions of knowledge.

.. Definitional variants are higher order concepts of a variant that transcends a single observational form. As an example,
..
..
.. a genetic test that aligns its genomic sequencing reads against build 37 of the human reference genome and then make positional variant calls based on that,

The eMERGE genetic test contains results that are based on variant calls made from observations on genomic DNA sequencing and genotyping assays for targeted regions of the genome. Diagnostic interpretation results are then generated by assessing these variant calls to determine their clinical significance in the context of both the primary indication for testing and the ACMG56 secondary findings. An additional component of the test focuses on assessing the variant diplotype findings for several pharmacogenomic genes in the context of their pharmacogenomic drug implications (i.e. metabolism, efficacy, etc..). The essential elements of these genetics results are the variants, genes, diseases, drugs, and phenotypes which both the variant findings and their context-specific interpretations rely. Of these essential elements variants are the most fundamental unit.

Computationally precise and accurate representation of variants is paramount to enabling meaningful use of genetic test results in EHRs. Storing, comparing, searching and associating data related to computationally represented variants reliably can only be done with standards that are verifiable and enforceable across healthcare systems. There are many challenges for sharing clinically reliable variant data. Two big challenges are 1) the diversity of testing technologies used to identify variants and 2) the harmonization (consistency & specificity) of variant calls across reporting laboratories and EHRs. Sequencing and genotyping technologies were used to study the prescribed regions or points in the genomic DNA to support the eMERGE testing objectives. The combined output of these two technologies produce the final set of variant findings that are then assessed to determine whether they have diagnostic clinical significance and to associate the most relevant pharmacogenomic implication knowledge for each case.

(It is a bit confusing to include the point regarding the testing technologies since it is outside our scope. consider removing the issue of diversity of testing)

.. The assessments, association and interpretation of variant findings require

Current/historical practices for representing variation (short list hgvs, iscn, vcf, etc...) - an example of where the errors occur.

CG IG variant observation enables flexibility (has potential) - mix of annotations and observation.

Collaborations with Experts to Define a Standard --

HL7 CG WG scope of responsibilities
HL7 FHIR is an exchange standard for enabling the sharing of healthcare data. Currently, the burden of defining variant exchange standards has fallen on the shoulders of the HL7 Clinical Genomics (CG) workgroup. While this may seem logical it is not realistic as the HL7 CG WG is not a standards making group but instead a group that works to enlist the best practices of the CG domain to allow them to begin sharing structured genetic test results. The HL7 CG WG is not equipped with the resources and expertise to delve into the depths of the vast and rapidly changing world of variant representation.


.. _gene-region coverage:

Gene / Region Coverage
----------------------
Clinical genetic testing methodologies can vary greatly. As such, one important aspect that should be computationally shared with the results of the test is the gene and region coverage or simply region coverage. This Provides a quantitative representation of the precise molecular sequenced regions covered and the quality of coverage for each region. Perhaps more importantly, this  clearly identifies what was not covered. 

Clinical genetic tests are often designed to target specific regions of the genome. Even when whole genome or exome sequencing is performed there may be a predisposition for the assay to only analyze certain regions or genes related to the indication for testing. There's also the chance that the outcome of running an assay on an individual sample may produce different actual coverage results than is expected or designed by the test. All of these factors play a role in raising the importance of being able to computationally represent the coverage regions with the results of a given assay. With both the clinically significant findings and the coverage region, receiving systems would be equipped to accurately determine whether a patient may need retesting or not, even though it may appear that they have been tested in the past for a given region of interest. Additionally, this information will be essential for clinical research and discovery at understanding patterns that are comparable across cohorts and studies.

.. _interpretation-summary text:

Interpretation Summary Text
---------------------------
While structured and coded results are of great importance to the computational utility of results, text will always play a significant role in conveying information between humans. There are a number of text attributes available throughout the GR IG profiled observation resources and their associated substructures. The genetics community and eMERGE require the ability to associate an interpretation summary with each reported clinically significant variant assessment. Additionally, there is a need to be able to provide interpretation text that summarizes the grouped observations. Using the grouper profile to organize subsections of results creates the need for an interpretation summary text attribute for these grouped results. 
It is our recommendation that the CG workgroup consider all of the important kinds of text fields needed to support clinical genetic test results and assure that there is a mechanism to do so, starting with an interpretation summary text field.

.. _pgx-results representation:

PGx Results Representation
--------------------------

..Commenting out for now, can decide if we want to include later
..Potential Future Use Cases
..* PRS results (discussed but not supported) - TODO
..
..* Research only reports (discussed but not supported) - TODO




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
