import streamlit as st
import random

st.set_page_config(page_title="Jansan's Web Quiz", layout="centered")

questions = [
    {
        "question": "Python किस तरह की भाषा है?",
        "options": ["कंप्यूटर", "प्रोग्रामिंग", "मोबाइल", "गेम"],
        "answer": "प्रोग्रामिंग"
    },
    {
        "question": "Python को किसने बनाया?",
        "options": ["Elon Musk", "Guido van Rossum", "Sundar Pichai", "Bill Gates"],
        "answer": "Guido van Rossum"
    },
    {
        "question": "Python में कौन से लूप होते हैं?",
        "options": ["for", "while", "दोनों", "कोई नहीं"],
        "answer": "दोनों"
    }
]

st.title("🧠 Jansan's Python Quiz")

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.q_index = 0
    st.session_state.quiz_over = False
    random.shuffle(questions)

name = st.text_input("अपना नाम दर्ज करें:")

if name and not st.session_state.quiz_over:
    q = questions[st.session_state.q_index]
    st.subheader(f"Q{st.session_state.q_index + 1}: {q['question']}")
    choice = st.radio("विकल्प:", q["options"], key=st.session_state.q_index)

    if st.button("जमा करें"):
        if choice == q["answer"]:
            st.success("✅ सही जवाब!")
            st.session_state.score += 1
        else:
            st.error(f"❌ गलत! सही जवाब था: {q['answer']}")

        st.session_state.q_index += 1

        if st.session_state.q_index >= len(questions):
            st.session_state.quiz_over = True

    st.write(f"स्कोर: {st.session_state.score}/{len(questions)}")

elif st.session_state.quiz_over:
    st.success(f"🎉 {name}, आपने {st.session_state.score}/{len(questions)} सही किए!")

    if st.button("🔁 फिर से खेलें"):
        st.session_state.score = 0
        st.session_state.q_index = 0
        st.session_state.quiz_over = False
        random.shuffle(questions)
