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
In general, observations resulting from an assay involve the clear and consistent representation of measures made about a sample for a subject in the context of an assay. A measure can be many things, but it must be consistent and unequivocally understood so that those results may be confidently shared and applied to making assertions and diagnosis about a patient's condition in external downstream processes. 

Genetic testing assays use methods to produce variant calls. Variant calls represent varying levels of complex representations about the state of residue sequences as compared to a reference sequence. These variant calls are then analyzed in the context of the subject's case and the assay's design to identify those variants that should be reported in the results. Some of these variants may closely reflect the variant call data as simple single nucleotide variants while others may be contrived from the variant call data to assert a more complex variant concept like pharmacogenomic haplotypes and diplotypes. Additionally, variant calls produced from different genetic testing methods can have varying degrees of specificity from precise molecular sequence variation to structural genomic alterations and sequence copy number gains and losses.

Variants are referenced as first class concepts when geneticists and domain experts begin to identify those forms of variation that have generalizable association to phenotypes. Monogenic disease causality and therapeutic implications on efficacy and metabolism are a few examples of variant- phenotype associations that have knowledge bases being developed by labs and expert communities today. The variants in these knowledge bases like those observed in individual samples assayed during genetic testing must be consistently and unequivocally understood by the community in order to computationally link patient results with expert knowledge in a scalable and clinically reliable manner.

Currently, there is no universally accepted standard for defining and representing variants. ASome attempts have been made to codify common variants using LOINC, but this is clearly not scalable. The Human Variome Project has developed a widely used and valuable nomenclature called HGVS [REF] which has vastly improved the ability for representing many forms of variation for humans and computers and is considered by many to be the best solution available for computationally representing variants. The Variant Call Format (VCF) has emerged as a de facto is arguably the standard for sequence variant calling and has enormous tooling and community adoption for handling large sets of variants efficiently. ISCN is a longstanding and well adopted nomenclature for structural variation. There are also registries and repositories of variation that are becoming more widely used to provide common identifiers for variants, including  like dbSNP, ClinVar, and COSMIC and others.

The GR IG is left to work with extending and profiling the top-level Observation resource in FHIR to represent all observed variant measures for myriad all clinical genetic testing result needs. This is an oversimplified and unreasonable strategy to an area of clinical testing that is growing and complex. The GR IG has been working admirably for years at tackling this complexity by continuing to build out a complex hierarchy of Observation profiles to support the broad array of genetic test observations related to variant results. The eMERGE XML message format that preceded the FHIR specification developed herein provided the ability to represent variants as first class concepts, independent of Observations (the approach used in the GR IG), that could be referenced by both Observations and act as generalized assertions of knowledge about the same or related variants. This iswas not reasonably achievable with the manner in which the GR IG profiles and underlying FHIR resources were designed. 
AThe creation of a separate set of resources to consistently and unequivocally represent the definitional genomic concepts like variants are essential to simplifying the design of the GR IG and ungating the resistance to adoption of FHIR for practical use in clinical genetic testing. This solution while seemingly obvious to some is riddled with challenges. Since no single standard exists for computationally representing the definition of variants it is not reasonable to expect the CG workgroup or FHIR to take that burden on. One promising development is the growing collaboration between the Information Modeling (IM) subgroup of the HL7 CG workgroup and the Genomic Knowledge Standards (GKS) Workstream of the Global Alliance for Genomic Health (GA4GH) to leverage the GKS work around Variation Representation and the Variation Annotation Specification and develop the resources needed in FHIR to incorporate these standards. 

Based on our experience the current GR IG design raises questions on the utility of its approach to sharing variants and variant observations. It is our assertion that in order for the structured variant data related to clinically significant variant observations to rise to the level of clinical computational use downstream that the variant data itself must be consistently and unequivocally represented. This consistent representation must be both used and approved for by the clinical domain experts and authorities to enable their use in clinical decision support and automating discovery of knowledge updates from clinical grade repositories and registries. By separating the concept of the variant definition from the observation in the GR IG now it will lend itself to less radical refactoring and ease the concerns and risks associated with early adoption.
Case level observations versus definitional variants to be used in knowledge and case level data to provide linkage. This is needed to provide reliable computational linkage between variant knowledge and evidence and case level systems.


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

The eMERGE PGx results make calls on the diplotypes, called star alleles,  found in each relevant PGx gene that is covered by the PGx gene panel. These diplotypes are then used as a basis for relating PGx gene-drug knowledge implications.  For eMERGE these PGx implications or PGx phenotype interpretations fell into three classes; metabolism, transporter, and efficacy. The eMERGE assay tested 7 PGx genes that contributed to 6 gene-drug phenotype implications. 

The two key challenges to sharing PGx results are to provide a complete and accurate representation of the identified variants used to make the PGx gene diplotype calls. Efforts like PharmCat[http://pharmcat.org/ or https://www.nature.com/articles/s41525-020-0135-2] are defining named allele matching[https://github.com/PharmGKB/PharmCAT/wiki/NamedAlleleMatcher-101] approaches that may help standardize this area. Regardless, the GR IG or FHIR should provide a straightforward mechanism for defining the precise variants used to call the haplotypes and diplotypes and then provide the use of one or more of these diplotype assertions as subjects of the gene-drug phenotype result that is the intended output of the PGx gene panel service. This separation of concerns and design approach is further evidence supporting the need for variant data types as discussed in Variant Representation.





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
