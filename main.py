import streamlit as st

# Introduction and explanation of the growth mindset
def introduction():
    st.title("Growth Mindset Challenge")
    st.write("""
        A **growth mindset** is the belief that abilities and intelligence can be developed through dedication, 
        hard work, and learning from mistakes. This challenge will help you develop a growth mindset by 
        reflecting on your personal experiences, identifying areas of growth, and learning to embrace challenges.
    """)

# List of challenges (questions)
def get_challenges():
    challenges = [
        "Describe a time when you learned something new and were proud of your progress.",
        "Think about a failure or mistake you've made. What did you learn from it?",
        "What is a skill you want to improve? What steps will you take to improve it?",
        "What challenges do you face that can help you grow?",
        "When you encounter difficulties, how do you usually respond? How can you change this response to embrace challenges?"
    ]
    return challenges

# Reflection and feedback based on answers
def reflect_on_answers(answers):
    feedback = []
    for answer in answers:
        if "fail" in answer or "mistake" in answer:
            feedback.append("Great job reflecting on your failures! Remember, failure is an important part of growth.")
        elif "improve" in answer or "learn" in answer:
            feedback.append("Excellent! A key part of a growth mindset is always striving to improve.")
        elif "challenge" in answer:
            feedback.append("Challenges are opportunities to grow. Keep embracing them!")
        else:
            feedback.append("Keep focusing on learning and growing through every experience.")
    return feedback

# Define the Streamlit app
def main():
    # Introduction to the app
    introduction()

    # Display challenge questions and collect answers
    challenges = get_challenges()
    answers = []

    for i, challenge in enumerate(challenges):
        answer = st.text_area(f"Challenge {i+1}: {challenge}", "")
        answers.append(answer)

    # Submit button to evaluate the answers
    if st.button("Submit Responses"):
        if any(answer == "" for answer in answers):
            st.error("Please answer all the challenges!")
        else:
            st.success("Thank you for completing the Growth Mindset Challenge!")
            feedback = reflect_on_answers(answers)
            st.write("### Feedback on Your Responses:")
            for i, f in enumerate(feedback):
                st.write(f"**Challenge {i+1} Feedback:** {f}")

            st.write("""
                Keep working on developing your growth mindset. The more you reflect on your challenges and 
                focus on learning and improving, the more you'll grow!
            """)

# Run the app
if __name__ == '__main__':
    main()
