import requests
from bs4 import BeautifulSoup
# import dotenv
import os
import streamlit as st

entry_url = "https://atcoder.jp"

lang_to_lang={
    "c_cpp":"cpp",
    "python":"python",
}

def url_to_problem_name(url):
    #urlから問題名を取得する
    if url=="":
        return ""
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    #問題名のタイトルが4から始まる場合はエラーなのでその旨を表示
    for tag in soup.select("title"):
        while True:
            if tag.text[0] != "4":
                return tag.text

def get_a_token(session):
    login_page = session.get(entry_url+"/login")
    soup = BeautifulSoup(login_page.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'}).get('value')
    return csrf_token

def login_to_atcoder():
    # ローカルの場合
    # dotenv.load_dotenv()
    # USER = os.getenv("USER")
    # PASS = os.getenv("PASS")
    # オンラインの場合
    USER = st.secrets["USER"]
    PASS = st.secrets["PASS"]
    session = requests.session()
    csrf_token = get_a_token(session)
    login_info = {
        "username": USER,
        "password": PASS,
        "csrf_token": csrf_token
    }
    url_login = entry_url + "/login"
    res = session.post(url_login, data=login_info)
    if res.status_code == 200:
        return session
    else:
        return "Login failed"

def request_submission_list(session, contest_name, user_id):
    #提出一覧を取得する
    submission_urls = []
    url = entry_url + "/contests/" + contest_name + "/submissions?f.User=" + user_id
    html = session.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    submission_list = soup.find_all('td', class_='text-center')
    for submission in submission_list:
        a_tag = submission.find('a')
        if a_tag and a_tag.get('href'):
            submission_urls.append(entry_url + a_tag.get('href'))
    return submission_urls

def get_problem_name(url):
    #urlから問題名を取得する
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    submission_info = soup.find_all('td', class_='text-center')
    for info in submission_info:
        if info.find('a'):
            a_tag = info.find('a')
            a_url = a_tag.get('href')
            if a_tag and a_url:
                if "tasks" in a_url:
                    return a_url.split("/")[-1]
    return ""

def get_submission(submission_url):
    #提出のコードを取得する
    html = requests.get(submission_url)
    soup = BeautifulSoup(html.content, "html.parser")
    submission = soup.find('pre', id='submission-code').text
    language = soup.find('pre', id='submission-code')['data-ace-mode']
    result = soup.find('td', id='judge-status').text
    return submission, language, result