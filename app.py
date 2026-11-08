import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Study Time Explorer", page_icon="📚", layout="wide")
st.caption("PSET5 · INTERACTIVE STREAMLIT APP")
st.title("📚 Study Time Explorer")
st.write("Turn your weekly study plan into a visualization. Change any input to update the dashboard instantly.")
with st.sidebar:
    st.header("Your study plan")
    name = st.text_input("Your name", "Student", max_chars=60)
    chart_type = st.selectbox("Chart type", ["Bar chart", "Pie chart", "Line chart"])
    goal = st.slider("Weekly study goal (hours)", 1, 60, 20)
    subjects = ["Mathematics", "Data Science", "English", "Economics", "Other"]
    hours = [st.number_input(f"{subject} hours", min_value=0.0, max_value=40.0, value=default, step=0.5) for subject, default in zip(subjects, [4.0, 6.0, 3.0, 4.0, 2.0])]
df = pd.DataFrame({"Subject": subjects, "Hours": hours})
total = float(df["Hours"].sum())
st.subheader(f"{name.strip() or 'Student'}’s weekly overview")
a, b, c = st.columns(3)
a.metric("Planned study time", f"{total:g} hours")
b.metric("Weekly goal", f"{goal} hours")
c.metric("Goal completion", f"{total / goal:.0%}")
st.progress(min(total / goal, 1.0))
if total >= goal:
    st.success("Your plan meets your weekly goal!")
else:
    st.info(f"Add {goal - total:g} more hours to meet your weekly goal.")
if total == 0:
    st.warning("Enter study hours for at least one subject to display a chart.")
else:
    if chart_type == "Bar chart":
        fig = px.bar(df, x="Subject", y="Hours", color="Subject", text="Hours", title="Study hours by subject")
        fig.update_layout(showlegend=False)
    elif chart_type == "Pie chart":
        fig = px.pie(df[df.Hours > 0], names="Subject", values="Hours", hole=0.45, title="Share of weekly study time")
        fig.update_traces(textinfo="label+percent")
    else:
        fig = px.line(df, x="Subject", y="Hours", markers=True, title="Study hours across subjects")
        st.caption("Subjects are categories; the connecting line is a comparison, not a time trend.")
    fig.update_layout(template="plotly_white", height=440, margin=dict(l=20, r=20, t=60, b=20))
    st.plotly_chart(fig, use_container_width=True)
with st.expander("View your data"):
    st.dataframe(df, hide_index=True, use_container_width=True)
st.download_button("Download study plan (CSV)", df.to_csv(index=False), file_name="study_plan.csv", mime="text/csv")
st.caption("Your inputs are used only for this session. This app does not save your study plan.")
