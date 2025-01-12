import streamlit as st
import atcoder as ac
import problems as pb

question=""
url=""
display_url=""
students=[]
select="手動入力"

color_dict={"AC":"green","WA":"red","TLE":"orange","MLE":"orange","RE":"orange","CE":"orange","OLE":"orange","IE":"orange"}

def message():
    st.title("コードのリアルタイム表示")
    st.write("AtCoderの問題の進捗をリアルタイムで確認することができます。")

def input_contents():
    global question, url, display_url, select
    select=st.selectbox(label="選択してください",options=("手動入力","A-四則演算", "A-条件分岐","B-文字列", "B-forループ", "C-リスト", "C-1次予選過去問","S1-whileループ","S1-多重ループ","S1-多次元リスト","S2-組み込み関数","S2-組み込み関数(上級)","S2-ソート関数","S2-ソート関数(上級)","S3-関数の定義","S3-再帰関数","S3-再帰関数(上級)"))
    if select=="手動入力":
        url=st.text_input("問題ページのURLを入力してください")
        if len(url.split("/"))==7:
            question=ac.url_to_problem_name(url)
        else:
            st.write("ERROR: URLが正しくありません")
            question=""
        display_url=""
    else:
        if select=="A-四則演算":
            titles=[]
            for i in pb.A_calc:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.A_calc[titles.index(qustion)]
        elif select=="A-条件分岐":
            titles=[]
            for i in pb.A_if:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.A_if[titles.index(qustion)]
        elif select=="B-文字列":
            titles=[]
            for i in pb.B_string:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.B_string[titles.index(qustion)]
        elif select=="B-forループ":
            titles=[]
            for i in pb.B_for:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.B_for[titles.index(qustion)]
        elif select=="C-リスト":
            titles=[]
            for i in pb.C_list:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.C_list[titles.index(qustion)]
        elif select=="C-1次予選過去問":
            titles=[]
            for i in pb.C_kakomon:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.C_kakomon[titles.index(qustion)]
        elif select=="S1-whileループ":
            titles=[]
            for i in pb.S1_while:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.S1_while[titles.index(qustion)]
        elif select=="S1-多重ループ":
            titles=[]
            for i in pb.S1_multi:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.S1_multi[titles.index(qustion)]
        elif select=="S1-多次元リスト":
            titles=[]
            for i in pb.S1_multi_list:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.S1_multi_list[titles.index(qustion)]
        elif select=="S2-組み込み関数":
            titles=[]
            for i in pb.S2_Built_in_functions:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.S2_Built_in_functions[titles.index(qustion)]
        elif select=="S2-組み込み関数(上級)":
            titles=[]
            for i in pb.S2_Built_in_functions_Advance:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.S2_Built_in_functions_Advance[titles.index(qustion)]
        elif select=="S2-ソート関数":
            titles=[]
            for i in pb.S2_sort:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.S2_sort[titles.index(qustion)]
        elif select=="S2-ソート関数(上級)":
            titles=[]
            for i in pb.S2_sort_Advance:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.S2_sort_Advance[titles.index(qustion)]
        elif select=="S3-関数の定義":
            titles=[]
            for i in pb.S3_function:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.S3_function[titles.index(qustion)]
        elif select=="S3-再帰関数":
            titles=[]
            for i in pb.S3_recursive:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.S3_recursive[titles.index(qustion)]
        elif select=="S3-再帰関数(上級)":
            titles=[]
            for i in pb.S3_recursive_Advance:
                titles.append(ac.url_to_problem_name(i))
            qustion=st.selectbox(label="問題を選択してください",options=titles)
            url=pb.S3_recursive_Advance[titles.index(qustion)]
        display_url=url

def input_students():
    global students
    student1=st.text_input("AtCoder IDを入力してください(1人目)")
    if student1!="":
        students.append(student1)
    student2=st.text_input("AtCoder IDを入力してください(2人目)")
    if student2!="":
        students.append(student2)
    student3=st.text_input("AtCoder IDを入力してください(3人目)")
    if student3!="":
        students.append(student3)
    student4=st.text_input("AtCoder IDを入力してください(4人目)")
    if student4!="":
        students.append(student4)

def display_codes():
    temp_message="(この表示は間違いの可能性があります)"
    global url, students
    for student in students:
        if student!="":
            session=ac.login_to_atcoder()
            while True:
                if type(session)!=str:
                    #エラー防止のための初期値
                    contest_name="abc001"
                    if url!="":
                        contest_name=url.split("/")[4]
                    submission_urls=ac.request_submission_list(session,contest_name,student)
                    temp={}
                    for submission_url in submission_urls:
                        problem_name=ac.get_problem_name(submission_url)
                        if problem_name not in temp and problem_name!="":
                            temp[problem_name]=submission_url
                    submission_urls=temp
                    st.write("")
                    if submission_urls=={}:
                        st.write(f'<center><span style="font-size:20px;">{student}: </span> <span style="font-size:20px;">提出がありません{temp_message}</span></center>',unsafe_allow_html=True)
                    else:
                        problem_name=url.split("/")[-1]
                        if problem_name in submission_urls:
                            submission_code,language,result=ac.get_submission(submission_urls[problem_name])
                            result_html=f'<center><span style="font-size:20px;">{student}: </span> <span style="color:{color_dict[result]};font-size:20px;"><b>{result}</b></span></center>'
                            st.write(result_html,unsafe_allow_html=True)
                            st.code(submission_code,language=ac.lang_to_lang[language])
                        else:
                            st.write(f'<center><span style="font-size:20px;">{student}: </span> <span style="font-size:20px;">提出がありません{temp_message}</span></center>',unsafe_allow_html=True)
                    break
    return

def main():
    message()
    input_students()
    input_contents()
    if display_url!="":
        st.write("URL：",display_url)
    if st.button("進捗を確認する"):
        while True:
            try:
                display_codes()
            except:
                st.write("ERROR: 再試行してください。")
            else:
                break

if __name__=="__main__":
    main()