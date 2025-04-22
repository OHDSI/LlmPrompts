# -*- coding: utf-8 -*-
"""
Provides contextual information snippets about the life sciences / pharmaceutical industry environment.

These functions return strings intended to be used as part of a system prompt
to ground LLM responses within the typical constraints, processes, and objectives
of pharmaceutical companies, based on common knowledge implicitly referenced in
standard pharma roles.

The context provided here focuses on the 'what' and 'why' of the environment,
complementing the 'who' and 'how' defined in the 'roles' subpackage.
It is derived from information and concepts present in the 'LS Personas - Pharmacompany roles' document.
"""

def get_drug_development_overview() -> str:
    """
    Returns context on the typical drug development lifecycle in pharma.

    Based on concepts like phases, milestones, TPP referenced across roles
    (e.g., Asset Team Lead, Clinical Development Lead) in the source document.
    """
    return (
        "CONTEXT: DRUG DEVELOPMENT LIFECYCLE\n"
        "Pharmaceutical drug development is a lengthy, costly, and high-risk process structured in distinct phases:\n"
        "- Preclinical: Initial research, lab/animal testing to assess basic safety and biological activity.\n"
        "- Clinical Trials (Phase I, II, III): Increasingly large human studies to evaluate safety, dosing, efficacy, and side effects against comparators or placebo. Rigorous protocols and data quality (GCP) are essential.\n"
        "- Submission: Compiling comprehensive data (clinical, manufacturing/CMC, preclinical) into a dossier for regulatory review (e.g., NDA/BLA in US, MAA in EU).\n"
        "- Approval & Post-Market: If approved, ongoing monitoring for safety, potentially further studies (Phase IV), and lifecycle management.\n"
        "Key Characteristics:\n"
        "- Milestone-Driven: Progress is gated by achieving specific results and regulatory clearances (e.g., IND, End-of-Phase II meeting, submission acceptance).\n"
        "- Target Product Profile (TPP): Development is guided by a predefined profile outlining desired drug characteristics (indication, efficacy, safety, dosage).\n"
        "- High Attrition: Many candidates fail during development, particularly in clinical phases.\n"
        "- Cross-Functional: Requires integration of R&D, clinical operations, regulatory affairs, manufacturing (CMC), commercial, medical affairs, and other functions.\n"
        "Constraint: Adherence to the structured process and generation of robust evidence for the TPP are paramount. Skipping steps or inadequate data leads to failure or delays."
    )

def get_regulatory_basics() -> str:
    """
    Returns context on the role and function of regulatory agencies in pharma.

    Based on mentions of regulatory bodies, submissions (NDA), and the need for
    compliance and strategic interaction (e.g., Regulatory Manager, Asset Team Lead)
    in the source document.
    """
    return (
        "CONTEXT: PHARMACEUTICAL REGULATORY ENVIRONMENT\n"
        "Regulatory agencies (e.g., FDA in US, EMA in EU) are government bodies mandated to protect public health.\n"
        "Core Function: They evaluate pharmaceutical products based on submitted scientific evidence to ensure they meet required standards for safety, efficacy, and quality before allowing market access.\n"
        "Key Principles:\n"
        "- Evidence-Based Review: Decisions rely on comprehensive data from preclinical studies, clinical trials (demonstrating benefit > risk), and manufacturing controls (CMC).\n"
        "- Benefit-Risk Assessment: The central task is weighing the demonstrated benefits of a drug against its risks for the intended patient population and indication.\n"
        "- Compliance: Strict adherence to regulations (e.g., GxP) and guidelines is mandatory throughout development and manufacturing. Non-compliance can halt development or lead to product withdrawal.\n"
        "- Labeling: Agencies control the official product information (label/SmPC), defining approved uses, dosage, contraindications, and warnings.\n"
        "Interaction Model: Companies engage with agencies throughout development for guidance (e.g., milestone meetings) and submit formal applications for approval. This involves negotiation and addressing agency queries.\n"
        "Constraint: Agency approval is non-negotiable for marketing a drug. Operations must prioritize generating compliant, convincing data and strategically engaging with regulators."
    )

def get_gxp_context() -> str:
    """
    Returns context on the importance of GxP quality guidelines.

    Based on the implied need for quality, data integrity, and standardized practices
    underpinning clinical trials, manufacturing, and regulatory submissions mentioned
    across various roles (Clinical Dev, Regulatory, Asset Lead) in the source document.
    """
    return (
        "CONTEXT: GXP QUALITY SYSTEMS\n"
        "GxP refers to a set of regulations and quality guidelines ('Good Practice') governing various aspects of pharmaceutical development and production.\n"
        "Core Purpose: To ensure product quality, data integrity/reliability, and patient safety.\n"
        "Key Areas (Examples):\n"
        "- GLP (Good Laboratory Practice): Governs non-clinical (animal) safety studies.\n"
        "- GCP (Good Clinical Practice): Governs the design, conduct, monitoring, recording, analysis, and reporting of clinical trials involving human subjects. Ensures data credibility and protects participant rights/safety.\n"
        "- GMP (Good Manufacturing Practice): Governs the manufacturing, processing, packing, and holding of pharmaceutical products to ensure identity, strength, quality, and purity.\n"
        "Key Principle: Standardization and documentation. Processes must be well-defined, validated, documented, and consistently followed. Deviations must be investigated and documented.\n"
        "Impact: GxP compliance is essential for regulatory submissions and inspections. Data generated or products manufactured under non-compliant conditions may be rejected by regulators.\n"
        "Constraint: All relevant pharmaceutical activities (research data for filings, clinical trials, manufacturing) MUST operate under the applicable GxP framework. There is no flexibility on the core principles of quality and data integrity."
    )

def get_commercialization_concepts() -> str:
    """
    Returns context on pharmaceutical commercialization, market access, and value demonstration.

    Based on concepts like commercial strategy, market access, payers, HEOR, branding,
    and launch mentioned in relevant roles (Marketing, Market Access, HEOR, Asset Lead)
    in the source document.
    """
    return (
        "CONTEXT: PHARMACEUTICAL COMMERCIALIZATION & MARKET ACCESS\n"
        "Commercialization involves bringing an approved drug to patients and achieving market success. It extends beyond just clinical efficacy.\n"
        "Key Elements:\n"
        "- Market Access: Securing reimbursement and formulary placement from payers (governments, insurance companies). This requires demonstrating value beyond clinical data.\n"
        "- Value Demonstration: Articulating the drug's benefits in terms relevant to different stakeholders, including clinical, economic (HEOR - Health Economics and Outcomes Research), and humanistic value (e.g., quality of life). Evidence generation for value (e.g., HEOR studies, real-world evidence) is crucial.\n"
        "- Payer Engagement: Interacting with payers to understand their evidence needs and negotiate pricing/reimbursement.\n"
        "- Commercial Strategy: Defining the target patient segments, positioning, branding, messaging, and sales/marketing tactics.\n"
        "- Launch Excellence: Coordinating cross-functional activities (supply chain, sales training, marketing campaigns) for a successful market introduction.\n"
        "Objective: To ensure that clinically effective drugs are accessible to appropriate patients and achieve commercial viability for the company.\n"
        "Constraint: Regulatory approval does not guarantee commercial success. Favorable pricing, reimbursement, and physician adoption depend heavily on demonstrating compelling value to payers and prescribers in a competitive landscape."
    )

def get_pharma_stakeholder_overview() -> str:
    """
    Returns context on the key stakeholders influencing pharmaceutical development and commercialization.

    Based on the various internal and external groups mentioned or implied across
    multiple persona descriptions (e.g., interactions with regulators, payers, HCPs,
    KOLs, internal teams) in the source document.
    """
    return (
        "CONTEXT: KEY PHARMACEUTICAL STAKEHOLDERS\n"
        "The pharmaceutical ecosystem involves a complex network of stakeholders with distinct needs and influence:\n"
        "- Patients: The ultimate consumers, concerned with treatment effectiveness, safety, quality of life, and access.\n"
        "- Healthcare Professionals (HCPs): Prescribers (physicians, nurses) who make treatment decisions based on clinical evidence, experience, guidelines, and patient needs.\n"
        "- Payers: Organizations (governments, insurers) that finance healthcare. They focus on clinical effectiveness, cost-effectiveness, budget impact, and value compared to alternatives when deciding on reimbursement.\n"
        "- Regulatory Agencies: Government bodies (FDA, EMA) focused on ensuring drug safety, efficacy, and quality before and after approval.\n"
        "- Key Opinion Leaders (KOLs): Influential clinical experts who shape medical practice through research, publications, and guideline development.\n"
        "- Internal Teams: Cross-functional groups within the pharma company (R&D, Clinical, Regulatory, Manufacturing/CMC, Medical Affairs, Commercial, HEOR, Market Access, etc.) responsible for different aspects of the drug lifecycle.\n"
        "Interactions: Successfully developing and commercializing a drug requires understanding and addressing the needs and perspectives of these diverse stakeholders.\n"
        "Constraint: Decisions must often balance competing stakeholder interests (e.g., payer cost concerns vs. patient access needs vs. regulatory safety requirements). Effective communication and evidence tailored to each stakeholder group are critical."
    )

