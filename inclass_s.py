# # import streamlit as st 


# # st.title("Login")

# # st.text_input("username")
# # st.text_input("password")

# # st.button("Login")



# import streamlit as st

# st.title("Login")

# if "count" not in st.session_state:
#     st.session_state.count=0
#     # st.write(st.session_state.count)

# if st.button("incr+1"):
#     st.session_state.count +=1


# if st.button("dec+1"):
#     st.session_state.count -=1

# if st.button("reset"):
#     st.session_state.count=0    



# st.write("Count:", st.session_state.count)



# st.sidebar.title("Workshop-Day2")
# st.sidebar.write("welcome to sidebar")
# for i in [1,2,3,4,5]:
#     st.write(i)
# username = st.text_input("Username")
# password = st.text_input("Password", type="password")

# st.sidebar.selectbox("choose yr role :-- ",["trainer","student","admin"])
# # st.sidebar.checkbox("check any one :-- ",["A","B","Both"])
# st.sidebar.multiselect("Choose options", ["A", "B", "Both"])
# st.text_area("enter something with 200 words length",height=300)

# submit = st.button("Submit")





# st.session_state={
#     "count":0
# }

# ai agent project with python + streamlit + groq 
#  :-- study planner 

import streamlit as st
from groq import Groq

# pip install groq
client=Groq(
    api_key= st.secrets["g_api_key"],
    base_url="https://api.groq.com/openai/v1"
) 

st.title("📚 AI Study Planner Agent")


goal = st.text_input("Enter your goal")
# days = st.number_input("Days", min_value=1, value=30)
days=st.number_input("Days",min_value=1,value=15,step=15)

hours = st.number_input("Hours/day", min_value=1, value=2)


# 🆕 Extra custom input
extra = st.text_area("Any specific requirements? (optional)",
                     placeholder="Example: Focus more on projects, skip theory, include revision...")

def fetch_plan(goal,days,hours,extra):
    prompt = f"""
    Create a {days}-day study plan for: {goal}
    Daily time: {hours} hours

    Additional instructions:
    {extra if extra else "No special requirements"}

    Include:
    - Keep it simple and clear and very basic study plan that i can become very confident
    """


    try:
        response=client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )
        return response
    except Exception as e:
        return f"❌ Error: {str(e)}"    

if st.button("genrate plan"):
    if goal:
        with st.spinner("genrtaing plan wait a moment"):
            plan=fetch_plan(goal,days,hours,extra)
            st.write(plan)


