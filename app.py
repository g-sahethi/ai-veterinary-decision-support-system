import streamlit as st
from workflow import run_workflow
from collections import Counter

# ✅ MUST BE FIRST
st.set_page_config(page_title="Vet AI System")

# 🎨 CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #fceabb, #f8b500);
}
</style>
""", unsafe_allow_html=True)

# 🧾 MEMORY
if "pet_history" not in st.session_state:
    st.session_state.pet_history = {}

if "profiles" not in st.session_state:
    st.session_state.profiles = {}

# 🔥 PROFILE SELECTOR
selected_pet = st.selectbox(
    "Select Pet Profile",
    ["New Profile"] + list(st.session_state.profiles.keys())
)

# 🔥 MAIN LAYOUT
left, right = st.columns([1, 2])

# ---------------- LEFT SIDE ----------------

with left:
    st.markdown("### 🐾 Pet Profile")

    # 👉 IMAGE PLACEHOLDER (TOP)
    image_placeholder = st.empty()

    # DEFAULT VALUES
    pet_name = ""
    pet_age = 0
    pet_type = "Dog"
    pet_breed = ""
    pet_gender = "Male"

    # LOAD PROFILE
    if selected_pet != "New Profile":
        data = st.session_state.profiles[selected_pet]
        pet_name = data["name"]
        pet_age = data["age"]
        pet_type = data["type"]
        pet_breed = data["breed"]
        pet_gender = data["gender"]

    # 👉 INPUTS (USER CAN CHANGE)
    pet_name = st.text_input("Pet Name", value=pet_name)
    pet_age = st.number_input("Age", value=pet_age, min_value=0)
    pet_type = st.selectbox(
        "Pet Type",
        ["Dog", "Cat", "Other"],
        index=["Dog", "Cat", "Other"].index(pet_type)
    )
    pet_breed = st.text_input("Breed", value=pet_breed)
    pet_gender = st.selectbox(
        "Gender",
        ["Male", "Female"],
        index=["Male", "Female"].index(pet_gender)
    )

    # 👉 UPDATE IMAGE (ALWAYS ON TOP)
    with image_placeholder:
        if pet_type == "Dog":
            st.image("https://cdn-icons-png.flaticon.com/512/616/616408.png", width=120)
        elif pet_type == "Cat":
            st.image("https://cdn-icons-png.flaticon.com/512/616/616430.png", width=120)
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/616/616494.png", width=120)

    # SAVE PROFILE
    if st.button("💾 Save Profile"):
        if pet_name.strip() == "":
            st.warning("Enter pet name")
        else:
            st.session_state.profiles[pet_name] = {
                "name": pet_name,
                "age": pet_age,
                "type": pet_type,
                "breed": pet_breed,
                "gender": pet_gender
            }
            st.success("Profile Saved!")

    # PROFILE SUMMARY
    if selected_pet != "New Profile":
        st.markdown("### 🐶 Profile Summary")
        st.write(f"Name: {pet_name}")
        st.write(f"Age: {pet_age}")
        st.write(f"Type: {pet_type}")
        st.write(f"Breed: {pet_breed}")
        st.write(f"Gender: {pet_gender}")

        # 🧾 HISTORY
        history = st.session_state.pet_history.get(pet_name, [])

        if history:
            st.markdown("### 🧾 Past Health Issues")

            issue_counter = Counter(history)
            for i, (issue, freq) in enumerate(issue_counter.items(), 1):
                st.write(f"{i}. {issue} → occurred {freq} time(s)")

            most_common_issue, freq = issue_counter.most_common(1)[0]

            st.markdown("### 📊 Most Frequent Issue")
            st.write(f"{most_common_issue} → occurred {freq} time(s)")

# ---------------- RIGHT SIDE ----------------
with right:
    st.title("🐾 AI Veterinary Decision System")

    user_input = st.text_area("Enter pet symptoms:")

    if st.button("Analyze"):

        if user_input.strip() == "":
            st.warning("Please enter symptoms")
        else:
            st.write(f"Analyzing for: {pet_type}")

            clean_input = user_input.lower().strip()

            # STORE HISTORY PER PET
            if pet_name not in st.session_state.pet_history:
                st.session_state.pet_history[pet_name] = []

            st.session_state.pet_history[pet_name].append(clean_input)

            history = st.session_state.pet_history.get(pet_name, [])

            # COUNT
            count = sum(
                1 for issue in history
                if any(word in issue for word in clean_input.split())
            )

            st.subheader("📊 Repeated Issue Analysis")
            st.write(f"This issue occurred {count} time(s)")

            # RUN WORKFLOW
            result = run_workflow(
                user_input,
                history,
                st.session_state.profiles.get(pet_name, {})
            )

            st.subheader("🤖 Agent Decision")
            st.write(result.get("decision_type", "No decision"))

            st.subheader("🧠 Symptom Analysis")
            st.write(result.get("symptoms", "No data"))

            st.subheader("💊 Possible Conditions")
            st.write(result.get("diagnosis", "No data"))

            st.subheader("⚠️ Risk Level")
            st.write(result.get("risk", "No data"))

            st.subheader("🚨 Immediate Precautions")
            st.write(result.get("immediate", "No data"))

            st.subheader("🏥 Vet Visit Urgency")
            st.write(result.get("urgency", "No data"))

            st.subheader("🔮 Simulation")
            st.write(result.get("simulation", "No data"))

            st.subheader("✅ Recommendation")
            st.write(result.get("decision", "No data"))

            # 🛠️ TOOLS (FIXED INDENTATION)
            st.subheader("🛠️ Smart Agent Tools")

            tools = result.get("tools", {})

            if tools.get("priority"):
                st.error(tools["priority"])

            if tools.get("history"):
                st.warning(tools["history"])

            if tools.get("profile"):
                st.info(tools["profile"])
                
            st.subheader("🔍 Agent Workflow (Verbose)")
            
            for step in result.get("verbose", []):
                st.write(step)    

            # HISTORY DISPLAY
            st.subheader("🧾 Health History")

            if history:
                issue_counter = Counter(history)
                for i, (issue, freq) in enumerate(issue_counter.items(), 1):
                    st.write(f"{i}. {issue} → occurred {freq} time(s)")
            else:
                st.write("No history yet")

            # MOST COMMON
            if history:
                most_common_issue, freq = Counter(history).most_common(1)[0]
                st.subheader("📊 Most Frequent Issue")
                st.write(f"{most_common_issue} → occurred {freq} time(s)")

            st.subheader("🧠 AI Plan")
            st.write(result.get("plan", "No plan"))