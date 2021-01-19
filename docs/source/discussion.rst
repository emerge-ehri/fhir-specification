.. _discussion:

Discussion
==========

The questions and issues raised and discussed during the development and implementation of this specification varied in scale in both importance as well as complexity.  We have highlighted a few in this section; all our discussion has been captured on the `
eMERGE genomics stream <https://chat.fhir.org/#narrow/stream/189875-genomics-.2F.20eMerge.20Pilot>`_ on Zulip.

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
Community standards are required to define variants in a manner that will allow science and medicine to adopt and develop tools and procedures to track and attach information to variants at the scale demanded by genetic testing. Efforts to describe and identify variants to date include but are not limited to; Human Genome Variation Society (HGVS) nomenclature, International System for Human Cytogenetic Nomenclature (ISCN) nomenclature[cite?], and Variant Call File (VCF) formats[cite?]. Public repositories and registries established by various authorities have evolved over the past decade or more to provide identifiers for variants in these systems (e.g. dbSNP, ClinVar, ClinGen Allele Registry, COSMIC, ...[cite all these?]). Without a common baseline set of data types and standards to support exchanging the breadth of sequence and structural variants in the genome and its derivative molecular products, genetic test results and generalized knowledge about variants will lack interoperability and continue to present barriers in complexity, cost and risk for use in clinical care and and scaling research and discovery.

The notion of a definitional or reference variant does not exist in FHIR or the GR IG. The Observation resource in FHIR is defined to exchange "Measurements and simple assertions made about a patient, device or other subject"[cite].  Without the existence of a single community standard model of data types for representing the breadth of variants required by genetic testing, FHIR and the CG WG are unlikely to include the data types and resources needed to build these referenceable variants. The CG WG's proposed resolution to this complex challenge is to develop FHIR profiles based on the Observation resource. This approach begins to address the concern of separating the variant observation using the Variant or Genotype Profiles from the other assertion profiles, like disease causality or therapeutic implications of metabolism or efficacy, related to one or more of the observed variants. However, it does not provide a pragmatic computational standard for representing the variants referenced within those observed variants and associated assertions. The GR IG Variant profile provides a large list of components that enable the flexibility of exchanging most of the popular nomenclatures, formats and variant identifier systems used in practice today along with a number of other annotations about the observed variant. While this seems to be a reasonable approach to enable innovators to structure data used in practice today, it may not convince early adopters to invest the engineering dollars if there is uncertainty in the clinical reliability, extensibility, complexity and basic capability of the use of this data for the rapidly growing requests for CDS and other downstream use of genetic test results. 

If the data types and resources for defining a variant based on computationally reliable standards existed in FHIR and the GR IG, then reference variants could be built and used not only to help interpret genetic testing results but also be used in exchanging FHIR messages to and from knowledge bases to associate assertions about variants as well as allow registries and tools to interoperate with each other to support comparison and mappings to variants in alternative and emerging reference systems.

The eMERGE XML format that was used in phase III and preceded the creation of the eMERGE FHIR specification separated out the data structures needed for reference variants. The eMERGE XML used those reference variant structures to create the variant finding observations and to create the assertion (or lack thereof) of the variant in the interpretation context  for testing (e.g. germline disease, somatic, pharmacogenomic) as a separate observation. Both case-specific findings and knowledge about variants are treated as statements. These two kinds of variant statements also contain additional qualifiers and context that allow the knowledge to be appropriately applied to the case findings and to allow the case findings to be appropriately used as evidence to further enrich and generate knowledge. These subject variants, whether simple SNPs or complex structural variants, should define the variant to the precision appropriate to the testing methodology (cytogenetic bands for a karyotype versus genomic coordinates for WGS) or essential to the knowledge produced by the domain experts. The data types or building blocks used to represent and exchange these variants should be interoperable to fulfill the growing demand and requirements for use in CDS and downstream use of genetic test results. The improved consistency, quality and simplicity should dramatically reduce the risk for adoption and remove key barriers for innovation.

While developing a standard model for variants and genomic features is a considerable challenge, it is paramount to successfully scaling the clinical use of genetic results. The Genomic Knowledge Standards (GKS) Workstream of the Global Alliance for Genomic Health (GA4GH) is committed to developing and expanding the Variation Representation Specification (VRS) to address the need for standards for computationally sharing variation. Instituting such a model in FHIR will significantly reduce the adoption risks caused by the complexity and unguided extensibility of the current GR IG and FHIR specifications. As such, the growing collaboration between the CG WG and the GA4GH GKS Workstream represents a promising step forward at introducing the concepts, resources and data types needed in the FHIR specification to improve the viability of implementing use cases related to variation in FHIR systems.


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
