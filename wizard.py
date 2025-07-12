# wizard.py
import streamlit as st
import time

wizard_steps = [
    "Project Start and Basic Info",
    "Agenda 2030 Goal",
    "Target Group",
    "Work Packages",
    "Organisation & Competence",
    "Risk Analysis & Reporting Methods",
    "Communication Plan & Dissemination",
    "Internal Policies",
    "Final Submission",
]


def generate_dummy_ai(step_name, user_input=None):
    detail = f"**Your input:** {user_input}\n\n" if user_input else ""

    # Add table content for specific sections
    if step_name == "Work Packages":
        table_content = """
| WP No. | Work Package Name | Leader | Start Month | End Month | Deliverables |
|--------|-------------------|--------|-------------|-----------|--------------|
| 1      | Needs Analysis   | Partner A | 1          | 6         | Report on current state |
| 2      | Pilot Development| Partner B | 4          | 12        | Prototype system |
| 3      | Implementation   | Partner C | 10         | 18        | Deployed solution |
| 4      | Evaluation      | Partner A | 16         | 24        | Final evaluation report |
"""
        return (
            detail + f"**AI-generated draft for {step_name}:**\n\n"
            "Here's a proposed work package structure for your project:\n\n"
            + table_content
            + "\n\n"
            "The work packages are designed to ensure a logical flow from analysis to implementation."
        )

    elif step_name == "Organisation & Competence":
        table_content = """
| Role | Organization | Key Personnel | Responsibilities |
|------|--------------|---------------|------------------|
| Project Lead | University X | Prof. Smith | Overall coordination |
| Technical Lead | Company Y | Dr. Johnson | Technical oversight |
| Admin Lead | NGO Z | Ms. Williams | Financial reporting |
"""
        return (
            detail + f"**AI-generated draft for {step_name}:**\n\n"
            "Suggested organization structure with key roles:\n\n"
            + table_content
            + "\n\n"
            "This structure ensures all critical functions are covered."
        )

    elif step_name == "Risk Analysis & Reporting Methods":
        table_content = """
| Risk | Probability | Impact | Mitigation Strategy | Responsible |
|------|-------------|--------|---------------------|-------------|
| Delays in partner deliverables | Medium | High | Regular checkpoints | Project Lead |
| Budget overruns | Low | High | Monthly financial reviews | Admin Lead |
| Technology not meeting needs | Medium | Medium | Alternative solutions identified | Technical Lead |
"""
        return (
            detail + f"**AI-generated draft for {step_name}:**\n\n"
            "Risk analysis table with mitigation strategies:\n\n"
            + table_content
            + "\n\n"
            "Regular monitoring will be implemented for all identified risks."
        )

    elif step_name == "Communication Plan & Dissemination":
        table_content = """
| Audience | Channel | Frequency | Message | Owner |
|----------|---------|-----------|---------|-------|
| SMEs | Webinars | Quarterly | New opportunities | Partner A |
| Policy makers | Reports | Biannual | Project outcomes | Partner B |
| General public | Social media | Monthly | Project updates | Partner C |
"""
        return (
            detail + f"**AI-generated draft for {step_name}:**\n\n"
            "Proposed communication plan:\n\n" + table_content + "\n\n"
            "This plan ensures all stakeholders receive timely information."
        )

    # Default content for other sections
    return (
        detail + f"**AI-generated draft for {step_name}:**\n\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eu augue at sapien placerat venenatis.\n"
        "Sed posuere sapien id tellus bibendum, vel tincidunt lorem sollicitudin.\n"
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus eu augue at sapien placerat venenatis.\n"
        "Sed posuere sapien id tellus bibendum, vel tincidunt lorem sollicitudin.\n"
    )




def wizard_ui():
    email = st.session_state.get("user", "guest@example.com")
    username = email.split("@")[0]

    st.markdown(
        f"""
        <div style="background-color: #f5f5f5; padding: 1rem; border-radius: 8px; margin-bottom: 1.5rem;">
            <b>🧙‍♂️ ERDF Application Wizard</b> | 👤 <span style="color:gray">Logged in as: <strong>{username}</strong></span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "step" not in st.session_state:
        st.session_state.step = 0
        st.session_state.edited_sections = {}

    step = st.session_state.step
    step_label = wizard_steps[step]
    step_input_key = f"step_{step}_input"
    step_output_key = f"step_{step}_generated"

    st.subheader(f"Step {step+1}/{len(wizard_steps)}: {step_label}")
    st.divider()

    # Input UI per step with detailed requirements
    user_input = ""
    if step == 0:  # Project Start and Basic Info
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Project name (text field)", key="project_name")
        with col2:
            st.selectbox(
                "Financier/Region (dropdown)",
                ["Region North", "Region South"],
                key="region",
            )

        st.selectbox(
            "Programme area (ERDF)",
            ["Smart Growth", "Green Transition"],
            key="programme",
        )

        user_input = st.text_area(
            "Short project idea (max 1,000 characters)",
            key="project_idea",
            max_chars=1000,
        )

        if st.button("Generate Project Info Suggestions"):
            with st.spinner("Generating suggestions..."):
                time.sleep(1)
                st.session_state[step_output_key] = generate_dummy_ai(
                    step_label, user_input
                )
                st.rerun()

    elif step == 1:  # Agenda 2030 Goal
        st.selectbox(
            "Select Agenda 2030 Goal",
            [
                "Goal 7: Sustainable Energy",
                "Goal 9: Innovation",
                "Goal 11: Sustainable Cities",
            ],
            key="agenda_goal",
        )

        if st.button("Generate Justification"):
            with st.spinner("Generating justification..."):
                time.sleep(1)
                st.session_state[step_output_key] = generate_dummy_ai(
                    step_label, st.session_state.get("agenda_goal", "")
                )
                st.rerun()

    elif step == 2:  # Target Group
        user_input = st.text_area(
            "Describe your target group in one concise description", key="target_group"
        )

        if st.button("Generate Target Group Details"):
            with st.spinner("Generating target group details..."):
                time.sleep(1)
                st.session_state[step_output_key] = generate_dummy_ai(
                    step_label, user_input
                )
                st.rerun()

    elif step == 3:  # Work Packages
        if "work_packages" not in st.session_state:
            st.session_state.work_packages = []

        if st.button("Generate Work Packages"):
            with st.spinner("Generating work packages..."):
                time.sleep(1)
                st.session_state[step_output_key] = generate_dummy_ai(step_label, "")
                st.rerun()

        # Work package carousel simulation
        if step_output_key in st.session_state:
            st.markdown("### Work Package Templates")
            cols = st.columns(3)
            templates = ["Digital Needs Analysis", "Pilot Lab", "SME Coaching"]
            for i, (col, template) in enumerate(zip(cols, templates)):
                with col:
                    if st.button(f"Add {template}"):
                        st.session_state.work_packages.append(
                            {
                                "name": template,
                                "description": f"AI-generated description for {template}",
                            }
                        )

    elif step == 4:  # Organisation & Competence
        user_input = st.text_input(
            "Enter keywords for roles and competencies", key="org_roles"
        )

        if st.button("Generate Organisation Text"):
            with st.spinner("Generating organisation structure..."):
                time.sleep(1)
                st.session_state[step_output_key] = generate_dummy_ai(
                    step_label, user_input
                )
                st.rerun()

    elif step == 5:  # Risk Analysis
        selected_risks = st.multiselect(
            "Select 3-4 generic risks",
            ["Low participation", "Budget overrun", "Tech delays", "Staff turnover"],
            key="risks",
        )

        if st.button("Generate Risk Analysis"):
            with st.spinner("Generating risk analysis..."):
                time.sleep(1)
                st.session_state[step_output_key] = generate_dummy_ai(
                    step_label, ", ".join(selected_risks)
                )
                st.rerun()

    elif step == 6:  # Communication Plan
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Audiences (e.g., businesses, youth)", key="audience")
        with col2:
            st.text_input("Channels (e.g., LinkedIn, website)", key="channels")

        user_input = st.text_area("Messages (e.g., sustainability)", key="messages")

        if st.button("Generate Communication Plan"):
            with st.spinner("Generating communication plan..."):
                time.sleep(1)
                st.session_state[step_output_key] = generate_dummy_ai(
                    step_label, user_input
                )
                st.rerun()

    elif step == 7:  # Internal Policies
        st.file_uploader(
            "Upload policy documents (optional)", type=["pdf", "docx"], key="policies"
        )

        if st.button("Generate Policy Compliance Text"):
            with st.spinner("Generating policy text..."):
                time.sleep(1)
                st.session_state[step_output_key] = generate_dummy_ai(
                    step_label, "Policy documents uploaded"
                )
                st.rerun()

    elif step == 8:  # Final Submission
        st.success("🎉 All steps complete!")
        st.markdown(
            "Click below to go to your Dashboard where you can review and edit all sections."
        )
        if st.button("👉 Go to Dashboard"):
            st.session_state["wizard_complete"] = True
            st.rerun()

    st.session_state[step_input_key] = user_input

    # Show Draft with edit capability
    if step_output_key in st.session_state:
        with st.expander("✏️ AI-Generated Draft (Editable)", expanded=True):
            edited = st.text_area(
                "Edit the draft below:",
                value=st.session_state[step_output_key],
                height=300,
                key=f"edit_{step}",
                label_visibility="collapsed",
            )
            # Save edited version
            if edited != st.session_state[step_output_key]:
                st.session_state.edited_sections[step_label] = edited
                st.session_state[step_output_key] = edited

            st.markdown(
                "ℹ️ Remember to click the Generate button again if you make changes to your inputs."
            )

    st.divider()

    # Navigation buttons
    col1, col2, col3 = st.columns([1, 3, 1])
    with col1:
        if step > 0 and st.button("◀ Previous"):
            st.session_state.step -= 1
            st.rerun()
    with col3:
        if step < len(wizard_steps) - 1 and st.button("Next ▶"):
            st.session_state.step += 1
            st.rerun()
