"""Healthcare delivery & payment context prompts.

This module mirrors `lifescience_context.py` but for the healthcare‐delivery world.
Each function returns a multi-paragraph text block starting with
`CONTEXT: <NAME>` that explains **what the context is**, **why it matters**,
core characteristics, and explicit **constraints / boundaries**—derived *solely*
from the reference text shared by the user (no external sources).
"""

# flake8: noqa

__all__ = [
    # System & financial contexts
    "get_integrated_delivery_network_context",
    "get_public_health_agency_context",
    "get_fee_for_service_context",
    "get_capitation_payment_model_context",
    "get_bundled_payment_context",
    "get_private_health_insurance_context",
    "get_public_health_insurance_context",
    "get_healthcare_policy_regulation_context",
    "get_actuarial_analysis_context",
    "get_healthcare_economics_financing_context",
    "get_clinical_research_trials_context",
    "get_health_information_technology_context",
    # Care-delivery facilities & programs
    "get_general_hospital_context",
    "get_specialty_hospital_context",
    "get_academic_medical_center_context",
    "get_primary_care_clinic_context",
    "get_specialty_care_center_context",
    "get_urgent_care_center_context",
    "get_community_health_center_context",
    "get_private_practice_solo_context",
    "get_private_practice_group_context",
    "get_long_term_care_facility_context",
    "get_assisted_living_facility_context",
    "get_home_healthcare_context",
    "get_telehealth_context",
    "get_outpatient_surgery_center_context",
    "get_rehabilitation_center_context",
    # Care-models & service lines
    "get_palliative_care_context",
    "get_hospice_care_context",
    "get_preventive_medicine_program_context",
    "get_disease_management_program_context",
    "get_primary_care_model_context",
    "get_specialty_care_model_context",
    "get_emergency_medicine_context",
    "get_critical_care_context",
]

# ---------------------------------------------------------------------------
# System & financial contexts
# ---------------------------------------------------------------------------

def get_integrated_delivery_network_context() -> str:
    """Context for Integrated Delivery Networks (IDNs)."""
    return (
        "CONTEXT: INTEGRATED DELIVERY NETWORK (IDN)\n"
        "An IDN is a single corporate structure that owns or tightly affiliates hospitals, clinics, post-acute facilities, and physician groups to deliver the full continuum of care.\n"
        "Objective: Coordinate services across settings to improve quality, reduce duplication, and perform well under value-based payment (VBC).\n"
        "Key Characteristics: common governance, shared EHR, centralized contracting, population-health infrastructure, ability to bear financial risk.\n"
        "Constraint: While IDNs streamline integration, internal complexity and siloed cultures can still impede true care coordination—LLM outputs should acknowledge governance but not assume perfect information flow between units." 
    )


def get_public_health_agency_context() -> str:
    """Context for Public Health Agencies."""
    return (
        "CONTEXT: PUBLIC HEALTH AGENCY\n"
        "A governmental body charged with monitoring and improving population health through surveillance, prevention programs, and policy guidance rather than direct reimbursement of individual services.\n"
        "Outputs: epidemiologic reports, vaccination campaigns, policy recommendations.\n"
        "Constraint: Operates largely outside traditional provider payment models; resource limits and political oversight shape priorities." 
    )


def get_fee_for_service_context() -> str:
    """Context for Fee-for-Service payment."""
    return (
        "CONTEXT: FEE-FOR-SERVICE (FFS) PAYMENT MODEL\n"
        "A legacy reimbursement approach that pays providers per discrete service rendered.\n"
        "Incentive: Volume—more billed CPT/HCPCS codes yield more revenue.\n"
        "Cognitive Load on Providers: mastering coding rules, documentation to justify each bill.\n"
        "Constraint: Does not reward coordination or outcomes; often criticized for driving over-utilization." 
    )


def get_capitation_payment_model_context() -> str:
    """Context for Capitation payment."""
    return (
        "CONTEXT: CAPITATION PAYMENT MODEL\n"
        "Providers receive a fixed per-member-per-month (PMPM) amount to cover all necessary care for an enrolled population.\n"
        "Incentive: Cost control and prevention.\n"
        "Key Skills: population-health analytics, risk management.\n"
        "Constraint: Financial risk shifts to the provider; inadequate care management can jeopardize solvency or quality." 
    )


def get_bundled_payment_context() -> str:
    """Context for Bundled / Episode-Based payments."""
    return (
        "CONTEXT: BUNDLED (EPISODE-BASED) PAYMENT\n"
        "A single payment covers all services for a defined clinical episode (e.g., joint replacement) across multiple providers.\n"
        "Objective: Align incentives for coordination and efficiency within the episode window.\n"
        "Constraint: Success depends on clear episode definition and data-sharing; outlier cases can erode savings." 
    )


def get_private_health_insurance_context() -> str:
    return (
        "CONTEXT: PRIVATE HEALTH INSURANCE\n"
        "Market-based insurers that design benefit plans, form provider networks, and blend payment models (FFS, capitation, bundles) to manage cost and risk.\n"
        "Drivers: competition, regulatory compliance, actuarial soundness.\n"
        "Constraint: Profit motives and regulatory variation create heterogeneous coverage rules; LLM answers should not assume uniform benefits across insurers." 
    )


def get_public_health_insurance_context() -> str:
    return (
        "CONTEXT: PUBLIC HEALTH INSURANCE\n"
        "Government-funded programs (e.g., Medicare, Medicaid) that define eligibility and payment rules influencing the wider market.\n"
        "Outputs: fee schedules, quality reporting requirements.\n"
        "Constraint: Budget neutrality and political oversight shape policy; coverage changes ripple through provider finances." 
    )


def get_healthcare_policy_regulation_context() -> str:
    return (
        "CONTEXT: HEALTHCARE POLICY & REGULATION\n"
        "Statutes and regulations establish the legal framework for coverage, payment, safety, and quality (e.g., CMS rules, state licensure).\n"
        "Impact: drives documentation standards, compliance programs, and organizational strategy.\n"
        "Constraint: Highly dynamic and politically influenced; guidance may vary by jurisdiction and time." 
    )


def get_actuarial_analysis_context() -> str:
    return (
        "CONTEXT: ACTUARIAL ANALYSIS & RISK ASSESSMENT\n"
        "Quantification of financial risk in healthcare using probabilistic models—inputs for pricing insurance and value-based contracts.\n"
        "Outputs: risk scores, claim cost projections, reserve calculations.\n"
        "Constraint: Dependent on data quality and assumption transparency; not a substitute for underwriting individual cases." 
    )


def get_healthcare_economics_financing_context() -> str:
    return (
        "CONTEXT: HEALTHCARE ECONOMICS & FINANCING\n"
        "Evaluation of resource allocation and market behavior to inform policy and organizational decisions about cost, access, and value.\n"
        "Tools: cost-effectiveness analysis, budget impact models, market trend studies.\n"
        "Constraint: Economic models simplify reality; results sensitive to perspective and data limitations." 
    )


def get_clinical_research_trials_context() -> str:
    return (
        "CONTEXT: CLINICAL RESEARCH & TRIALS\n"
        "Prospective studies that generate evidence on intervention safety and efficacy, informing coverage decisions.\n"
        "Outputs: study protocols, data tables, regulatory submissions.\n"
        "Constraint: Ethical oversight (IRB), Good Clinical Practice (GCP) compliance, and limited generalizability to real-world populations." 
    )


def get_health_information_technology_context() -> str:
    return (
        "CONTEXT: HEALTH INFORMATION TECHNOLOGY (HIT) & DATA ANALYTICS\n"
        "Systems that capture, store, and analyze health data (EHRs, data warehouses, analytics platforms) enabling evidence-based decision-making and payment innovation.\n"
        "Constraint: Data integrity, interoperability challenges, and user burden (EHR fatigue) must be acknowledged when proposing tech-heavy solutions." 
    )

# ---------------------------------------------------------------------------
# Care-delivery facilities & programs
# ---------------------------------------------------------------------------

def _mk_facility(name: str, purpose: str, constraint: str) -> str:
    return f"CONTEXT: {name.upper()}\n{purpose}\nConstraint: {constraint}."


def get_general_hospital_context() -> str:
    return _mk_facility(
        "General Hospital",
        "Provides acute inpatient and outpatient services for a wide range of conditions and acuities, requiring rapid decisions and complex coordination.",
        "Not all services are equally resourced; tertiary or highly specialized care may need referral"
    )


def get_specialty_hospital_context() -> str:
    return _mk_facility(
        "Specialty Hospital",
        "Focuses on a specific condition or population (e.g., cardiac, orthopedic), offering deep expertise and protocol-driven workflows.",
        "Does not provide the breadth of services of a general hospital; patients with unrelated conditions are transferred"
    )


def get_academic_medical_center_context() -> str:
    return _mk_facility(
        "Academic Medical Center (AMC)",
        "Handles complex referral cases while balancing missions of patient care, research, and education—high complexity and multidisciplinary teams.",
        "Teaching and research imperatives can introduce additional layers of bureaucracy and cost"
    )


def get_primary_care_clinic_context() -> str:
    return _mk_facility(
        "Primary Care Clinic",
        "Ambulatory setting delivering longitudinal preventive and chronic care to a general population under high volume and time pressure.",
        "Lacks on-site advanced diagnostics or specialty procedures; relies on referral networks"
    )


def get_specialty_care_center_context() -> str:
    return _mk_facility(
        "Specialty Care Center",
        "Ambulatory facility offering focused expertise, advanced diagnostics, and treatments for referred conditions.",
        "Care is episodic and problem-focused; does not provide comprehensive primary care"
    )


def get_urgent_care_center_context() -> str:
    return _mk_facility(
        "Urgent Care Center",
        "Provides walk-in episodic care for acute but non-life-threatening issues, emphasizing throughput and convenience.",
        "Not equipped for high-acuity emergencies; severe cases must be diverted to ED"
    )


def get_community_health_center_context() -> str:
    return _mk_facility(
        "Community Health Center (CHC)",
        "Federally qualified health center model delivering comprehensive primary care to underserved populations with integrated social services.",
        "Resource constraints and social determinants may limit specialty access"
    )


def get_private_practice_solo_context() -> str:
    return _mk_facility(
        "Private Practice (Solo)",
        "Physician-owned ambulatory practice with high autonomy and business management responsibility.",
        "Limited economies of scale; coverage during absence requires locum or cross-coverage"
    )


def get_private_practice_group_context() -> str:
    return _mk_facility(
        "Private Practice (Group)",
        "Multi-provider practice sharing resources and administrative functions for efficiency.",
        "Group decision-making can dilute individual autonomy"
    )


def get_long_term_care_facility_context() -> str:
    return _mk_facility(
        "Long-Term Care Facility (LTCF)",
        "Residential setting providing 24/7 skilled nursing for chronic illness and ADL support.",
        "Regulatory focus and reimbursement levels influence staffing ratios and available services"
    )


def get_assisted_living_facility_context() -> str:
    return _mk_facility(
        "Assisted Living Facility",
        "Residential environment offering supportive services and supervision for individuals needing help with ADLs but less medical intensity than LTCF.",
        "Medical services are limited; residents often require external providers for clinical care"
    )


def get_home_healthcare_context() -> str:
    return _mk_facility(
        "Home Healthcare",
        "Provision of skilled nursing and therapy services in patients’ homes—autonomous practice demanding home environment assessment and coordination.",
        "Limited ability to perform advanced diagnostics or immediate escalation without transport"
    )


def get_telehealth_context() -> str:
    return _mk_facility(
        "Telehealth / Virtual Care",
        "Remote delivery of consultations and monitoring via technology, enabling access and convenience.",
        "Physical examination and procedures are constrained; technology access disparities affect equity"
    )


def get_outpatient_surgery_center_context() -> str:
    return _mk_facility(
        "Outpatient Surgery Center (ASC)",
        "Ambulatory facility performing same-day surgical procedures with an efficiency focus.",
        "Limited to low-acuity patients; complications may necessitate hospital transfer"
    )


def get_rehabilitation_center_context() -> str:
    return _mk_facility(
        "Rehabilitation Center",
        "Facility providing intensive therapy (PT/OT/SLP) aimed at functional recovery post-acute illness or injury.",
        "Length of stay and therapy intensity often constrained by payer authorization"
    )

# ---------------------------------------------------------------------------
# Care-models & service lines
# ---------------------------------------------------------------------------

def _mk_model(name: str, purpose: str, constraint: str) -> str:
    return f"CONTEXT: {name.upper()}\n{purpose}\nConstraint: {constraint}."


def get_palliative_care_context() -> str:
    return _mk_model(
        "Palliative Care",
        "Interdisciplinary model focused on relief of suffering and quality of life at any stage of serious illness, alongside curative or life-prolonging treatments.",
        "Distinct from hospice; not limited by prognosis but often under-referred"
    )


def get_hospice_care_context() -> str:
    return _mk_model(
        "Hospice Care",
        "Comprehensive comfort-focused care for terminally ill patients with a life expectancy of roughly six months or less, delivered at home or in hospice facilities.",
        "Curative treatments are foregone; eligibility and payment tied to prognosis certification"
    )


def get_preventive_medicine_program_context() -> str:
    return _mk_model(
        "Preventive Medicine / Wellness Program",
        "Structured initiatives (screenings, immunizations, lifestyle coaching) aimed at disease prevention and early detection across populations.",
        "Effectiveness depends on engagement and access; may not capture high-risk individuals who avoid care"
    )


def get_disease_management_program_context() -> str:
    return _mk_model(
        "Disease-Management Program",
        "Ongoing support, education, and monitoring to control established chronic diseases and prevent complications, often delivered remotely.",
        "Requires sustained patient engagement and data flow; isolated programs risk fragmentation if not integrated with primary care"
    )


def get_primary_care_model_context() -> str:
    return _mk_model(
        "Primary Care (Model)",
        "Whole-person, first-contact, longitudinal care managing common acute issues, chronic diseases, prevention, and coordination across a patient’s life span.",
        "Does not offer the specialty depth or immediate stabilization of emergency medicine"
    )


def get_specialty_care_model_context() -> str:
    return _mk_model(
        "Specialty Care (Model)",
        "Depth-focused care on a specific organ system, disease, or demographic, typically accessed via referral for complex or uncommon conditions.",
        "Not responsible for comprehensive longitudinal management of unrelated conditions"
    )


def get_emergency_medicine_context() -> str:
    return _mk_model(
        "Emergency Medicine",
        "Hospital-based specialty providing rapid assessment, resuscitation, and stabilization of undifferentiated acute illnesses or injuries 24/7.",
        "Care is episodic and time-bounded; longitudinal follow-up transitions to inpatient units or outpatient providers"
    )


def get_critical_care_context() -> str:
    return _mk_model(
        "Critical Care / ICU",
        "Intensive monitoring and organ support for life-threatening conditions requiring sophisticated technology and multidisciplinary expertise.",
        "Resource-intensive; reserved for patients needing continuous invasive support, not stable medical patients"
    )
