import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_detail_info(url: str) -> dict:
    res = requests.get(url)
    SOUP = BeautifulSoup(res.text, "lxml")
    border = SOUP.find("div", attrs={"class": "border"})
    left, right = SOUP.find("div", attrs={"class": "border"}).find(
        "div", attrs={"class": "left"}
    ), border.find("div", attrs={"class": "right"})
    f = lambda x: " ".join(x.get_text().strip().split())
    Title = f(left.find("p", attrs={"class": "tit"}))
    # devnull, 경력, 학력, 지역, 임금, 고용형태, 근무형태
    devnull, Career, Education, Work_area, Pay, Employment_type, 근무형태 = map(
        f, left.find_all("span")
    )
    # 기업명 업종 기업규모,설립년도,연매출액,홈페이지,근로자수
    Company_name, Sectors, 기업규모, 설립년도, 연매출액, 홈페이지, 근로자수 = map(
        f, right.find("div", attrs={"class": "info"}).find_all("div")
    )
    return {
        "Title": Title,
        "Career": Career,
        "Education": Education,
        "Work_area": Work_area,
        "Pay": Pay,
        "Employment_type": Employment_type,
        "Company_name": Company_name,
    }


if __name__ == "__main__":
    df = pd.DataFrame(
        index=range(0),
        columns=(
            "Title",
            "Career",
            "Education",
            "Work_area",
            "pay",
            "Employment_type",
            "Company_name",
        ),
    )
    with open("test.txt", "rb") as f1:
        for i in range(4):
            try:
                url = f1.readline()
                data = get_detail_info(url)
                df.loc[i] = data.values()
                print(i)
            except Exception as e:
                print(e)
                continue
print(df)
