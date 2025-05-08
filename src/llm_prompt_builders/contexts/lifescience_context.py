# -*- coding: utf-8 -*-
"""
Provides contextual information snippets about the life sciences / pharmaceutical industry environment.

These functions return strings intended to be used as part of a system prompt
to ground LLM responses within the typical constraints, processes, and objectives
of pharmaceutical companies, based on common knowledge implicitly referenced in
standard pharma roles.

The context provided here focuses on the 'what' and 'why' of the environment,
complementing the 'who' and 'how' defined in the 'roles' subpackage.
"""

def get_drug_development_overview() -> str:
    """
    Returns context on the typical drug development lifecycle in pharma.

    Based on concepts like phases, milestones, TPP across roles
    (e.g., Asset Team Lead, Clinical Development Lead).
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

    Based on concepts like regulatory bodies, submissions (NDA), and the need for
    compliance and strategic interaction (e.g., Regulatory Manager, Asset Team Lead).
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
    underpinning clinical trials, manufacturing, and regulatory submissions.
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
    and launch mentioned in relevant roles (Marketing, Market Access, HEOR, Asset Lead).
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

    Based on the various internal and external groups across
    multiple persona descriptions (e.g., interactions with regulators, payers, HCPs,
    KOLs, internal teams).
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


def get_cross_functional_collaboration_model() -> str:
    """
    Returns context on the necessity and nature of cross-functional teams in pharma.

    Based on the pervasive need for integration across functions highlighted in roles
    like Asset Team Lead and the interactions described for most other roles.
    """
    return (
        "CONTEXT: CROSS-FUNCTIONAL COLLABORATION MODEL\n"
        "Pharmaceutical asset development and commercialization inherently require intensive cross-functional collaboration.\n"
        "Rationale: No single function possesses all the expertise (scientific, clinical, regulatory, manufacturing, market access, commercial) needed. Integrating these perspectives is vital for coherent strategy and execution.\n"
        "Operating Model: Typically involves core teams (e.g., Asset Development Team, Launch Team) with representatives from key functions, often led by an integrator role (like Asset Team Lead).\n"
        "Key Challenges: Aligning functional priorities, managing interdependencies, ensuring timely information flow, resolving conflicts between functional viewpoints (e.g., clinical desires vs. manufacturing constraints vs. commercial needs).\n"
        "Objective: To create and execute a unified asset strategy that balances scientific rigor, regulatory requirements, manufacturing feasibility, patient needs, and commercial viability.\n"
        "Constraint: Siloed operations or poor cross-functional alignment leads to strategic gaps, delays, suboptimal decisions, and potential failure to maximize asset value."
    )

def get_evidence_generation_strategy() -> str:
    """
    Returns context on the different types of evidence needed in pharma and their purpose.

    Based on the activities described for roles focused on generating specific data
    (Clinical Dev Lead - clinical trials; HEOR Lead - economic/outcomes data) and roles
    that consume this data (Market Access, Marketing, Regulatory).
    """
    return (
        "CONTEXT: EVIDENCE GENERATION STRATEGY\n"
        "Pharmaceutical success hinges on generating diverse types of credible evidence to meet the needs of various stakeholders.\n"
        "Key Evidence Types:\n"
        "- Clinical Trial Data (RCTs): Primary evidence for regulatory approval, demonstrating safety and efficacy in controlled settings. Essential for HCP confidence.\n"
        "- Health Economics & Outcomes Research (HEOR): Evidence on cost-effectiveness, budget impact, and comparative effectiveness relative to alternatives. Crucial for payers and reimbursement decisions.\n"
        "- Real-World Evidence (RWE): Data gathered outside clinical trials (e.g., registries, claims data) showing effectiveness, safety, and usage patterns in routine clinical practice. Increasingly important for regulators, payers, and HCPs.\n"
        "- Patient-Reported Outcomes (PROs): Evidence on treatment impact from the patient's perspective (e.g., quality of life, symptom burden). Supports value demonstration to patients, HCPs, and payers.\n"
        "Strategic Planning: Evidence generation must be planned early and integrated into the overall development strategy to ensure the right data is available at the right time for key decisions (regulatory submission, pricing/reimbursement negotiations, clinical guideline inclusion).\n"
        "Constraint: Relying solely on traditional clinical trial data is often insufficient for market access and commercial success. A comprehensive evidence package addressing multiple stakeholder perspectives is required."
    )

def get_product_lifecycle_management_context() -> str:
    """
    Returns context on managing a pharmaceutical product after its initial approval.

    Based on the Asset Team Lead's responsibility for 'lifecycle value' and the implied
    need to manage products beyond launch.
    """
    return (
        "CONTEXT: PRODUCT LIFECYCLE MANAGEMENT (LCM)\n"
        "Managing a pharmaceutical product extends well beyond its initial launch and approval.\n"
        "Objective: To maximize the value of the asset over its entire lifespan, adapting to changing market dynamics, competitive pressures, and evolving scientific understanding.\n"
        "Key LCM Activities:\n"
        "- Indication Expansion: Seeking regulatory approval for use in new patient populations or diseases.\n"
        "- Formulation Development: Creating improved versions (e.g., easier dosing, extended release).\n"
        "- Geographic Expansion: Launching the product in new countries/regions.\n"
        "- Post-Marketing Studies: Fulfilling regulatory commitments, further exploring safety/efficacy, generating RWE.\n"
        "- Intellectual Property Management: Defending patents and managing the transition during loss of exclusivity (LoE).\n"
        "- Competitive Response: Adapting strategy based on new entrants or competitor data.\n"
        "Strategic Importance: Effective LCM can significantly extend a product's commercial life and return on investment.\n"
        "Constraint: LCM requires ongoing investment and strategic foresight. Failure to proactively manage the lifecycle can lead to premature decline in market share and revenue."
    )

def get_competitive_intelligence_context() -> str:
    """
    Returns context on the role of competitive intelligence in pharma strategy.

    Based on the need for roles like Marketing Lead and Asset Team Lead to understand
    the market and position their asset effectively.
    """
    return (
        "CONTEXT: COMPETITIVE INTELLIGENCE (CI) IN PHARMA\n"
        "The pharmaceutical market is highly competitive, making CI a critical input for strategic decision-making.\n"
        "Purpose: To systematically gather, analyze, and disseminate information about the external environment, particularly competitors, to inform development and commercial strategies.\n"
        "Focus Areas:\n"
        "- Competitor Pipelines: Monitoring drugs in development (mechanisms, targets, clinical trial progress, timelines).\n"
        "- Competitor Data: Analyzing published/presented clinical trial results, RWE, and regulatory interactions.\n"
        "- Competitor Strategy: Understanding their commercial positioning, pricing, market access approaches, and lifecycle plans.\n"
        "- Market Dynamics: Tracking therapeutic area trends, evolving standards of care, and unmet needs.\n"
        "Application: CI informs Target Product Profile definition, clinical trial design (e.g., comparator choice), forecasting, positioning, messaging, and overall asset strategy.\n"
        "Constraint: Operating without robust CI leads to reactive strategies, potential mispositioning, and failure to anticipate market shifts or competitive threats. Ethical and legal boundaries must be strictly observed in gathering CI."
    )

def get_medical_affairs_function_context() -> str:
    """
    Returns context on the distinct role and purpose of the Medical Affairs function.

    Based on mentions of Medical Affairs as a key collaborator for HEOR, Marketing,
    and other functions, highlighting its bridging role.
    """
    return (
        "CONTEXT: MEDICAL AFFAIRS FUNCTION\n"
        "Medical Affairs is a distinct function within pharmaceutical companies, bridging clinical development and commercial operations.\n"
        "Core Purpose: To communicate complex scientific and clinical information accurately and non-promotionally to the medical community, gather insights, and support appropriate product use.\n"
        "Key Activities:\n"
        "- KOL Engagement: Building relationships with Key Opinion Leaders for scientific exchange and insights.\n"
        "- Scientific Communication: Presenting data at medical congresses, publishing manuscripts, developing medical information resources.\n"
        "- Medical Education: Supporting independent medical education initiatives.\n"
        "- Evidence Generation Support: Supporting investigator-initiated studies (IIS) and contributing to RWE generation plans.\n"
        "- Internal Expertise: Providing medical/scientific expertise to internal teams (e.g., Commercial, Market Access).\n"
        "Distinction from Commercial: Medical Affairs operates with scientific objectivity and avoids direct product promotion. Its interactions are focused on scientific exchange, not sales.\n"
        "Constraint: Must operate within strict compliance guidelines (e.g., separating scientific exchange from promotional activities) to maintain credibility with the medical community and regulators."
    )


def get_portfolio_strategy_context() -> str:
    """Returns the system prompt for a Portfolio Strategy context."""
    return (
        "Context: An executive therapeutic‑area portfolio review where leaders assess pipeline assets, allocate capital and set strategic priorities.\n"
        "Inputs: Long‑range forecasts, risk‑adjusted Net Present Values (NPVs), competitive assessments, resource capacity analyses.\n"
        "Focus: Decide whether to accelerate, partner, pause or terminate assets; balance scientific risk, unmet need and commercial return; document rationale for governance.\n"
        "Participants: TA Head, Strategy & Ops Lead, Finance, R&D, Business Development & Licensing (BD&L), Medical.\n"
        "Tone: Data‑driven, scenario‑based, investment‑oriented, transparent."
    )


def get_competitive_landscape_context() -> str:
    """Returns the system prompt for a Competitive Landscape context."""
    return (
        "Context: A cross‑functional workshop preparing the competitive landscape section of a board or Executive Leadership Team (ELT) update.\n"
        "Inputs: Live competitor pipeline tracker, trial read‑outs, deal news, launch timelines, share/messaging analyses.\n"
        "Focus: Identify competitor moves that threaten or enable our strategy, model potential impact on forecasts, craft positioning/mitigation options.\n"
        "Participants: Competitive Intelligence (CI) Director, Forecasting Lead, Brand Strategy, Medical Affairs, Business Development & Licensing (BD&L).\n"
        "Tone: Vigilant, evidence‑based, scenario‑testing, ethically sourced."
    )


def get_market_insight_context() -> str:
    """Returns the system prompt for a Market Insight context."""
    return (
        "Context: An insight‑generation session following new primary/secondary market research read‑outs.\n"
        "Inputs: Quantitative market sizing, qualitative patient/HCP interviews, segmentation, patient‑flow models.\n"
        "Focus: Translate findings into unmet‑need priorities, opportunity sizing, and implications for asset positioning and lifecycle strategy.\n"
        "Participants: Market Research Lead, Strategy & Ops, Brand, Medical, Access.\n"
        "Tone: Curious, customer‑centric, hypothesis‑driven, actionable."
    )


def get_forecast_planning_context() -> str:
    """Returns the system prompt for a Forecast Planning context."""
    return (
        "Context: The annual forecast refresh cycle where consensus short‑, mid‑ and long‑range forecasts are built.\n"
        "Inputs: Epidemiology updates, pricing & reimbursement assumptions, demand drivers, supply constraints, competitive scenarios.\n"
        "Focus: Produce baseline and scenario forecasts, document key assumptions, pressure‑test with stakeholders, lock numbers for budgeting and governance.\n"
        "Participants: Forecasting & Analytics Lead, Finance, Market Research, Supply Chain, Access, Strategy.\n"
        "Tone: Analytical, assumption‑transparent, collaborative, version‑controlled."
    )


def get_launch_readiness_context() -> str:
    """Returns the system prompt for a Launch Readiness context."""
    return (
        "Context: A T‑12‑month launch readiness review assessing preparedness across functions.\n"
        "Inputs: Integrated launch playbook, milestone tracker, risk dashboard, launch Key Performance Indicators (KPIs).\n"
        "Focus: Confirm critical‑path achievement, surface and mitigate launch risks, align resources, update Go/No‑Go status.\n"
        "Participants: Launch Excellence Lead, Brand Team, Medical, Access, Supply, Regulatory, Finance.\n"
        "Tone: Milestone‑oriented, risk‑aware, solution‑seeking, cross‑functional."
    )


def get_evidence_generation_context() -> str:
    """Returns the system prompt for an Evidence Generation context."""
    return (
        "Context: An integrated evidence planning meeting to align clinical, Health Economics & Outcomes Research (HEOR) and Real‑World Evidence (RWE) activities with value story and market access needs.\n"
        "Inputs: Target product profile (TPP), evidence gap analysis, planned interventional and observational studies, publication roadmap.\n"
        "Focus: Prioritise evidence packages, sequence studies, assign owners, ensure alignment with payer and guideline requirements.\n"
        "Participants: HEOR & RWE Strategy Director, Medical Affairs, Clinical Development, Access, Publications.\n"
        "Tone: Strategic, methodologically rigorous, payer‑focused, cross‑disciplinary."
    )


def get_risk_governance_context() -> str:
    """Returns the system prompt for a Risk Governance context."""
    return (
        "Context: A quarterly risk review board applying the enterprise risk management framework to the therapeutic‑area portfolio and operations.\n"
        "Inputs: Updated risk register, heat map, mitigation/contingency status, new emerging risks.\n"
        "Focus: Validate risk ratings, approve mitigation plans, escalate critical risks, embed lessons learned, update risk appetite statements.\n"
        "Participants: Portfolio Governance Manager, Risk Management Lead, TA Leadership, Compliance, Finance.\n"
        "Tone: Proactive, structured, ownership‑driven, continuous‑improvement."
    )
