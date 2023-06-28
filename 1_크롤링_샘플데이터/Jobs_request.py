import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

### 리스트 선언
Job_Announcement = [] # 채용공고명
work_area = [] # 지원자격 >>> 근무지역
Education = [] # 학력
wage = [] # 임금
employment_type = [] # 고용형태
Welfare = [] # 복리후생
Job_Description = [] # 직무내용

def getJobDataFromWorknet(url2):
  
  Job_Announcement.clear()
  work_area.clear()
  Education.clear()
  wage.clear()
  employment_type.clear()
  Welfare.clear()
  Job_Description.clear()
  
  request = requests.get(url2)
  html_source = request.text
  time.sleep(3.0) # 30 
  
  html_soup = BeautifulSoup(html_source, 'lxml') 

  ### JobTitle, Eligibility, Working_conditions, employment_type, Welfare, Job_Description 수집
   
  div = html_soup.select('div.ai-recmd')
  
  for paper in div :
    # JobTitle 수집
      JobTitle_info = paper.find('p', {'class', 'tit'})
      print(JobTitle_info.get_text()) # TEST - 제거해도 됨
      Job_Announcement.append(JobTitle_info.get_text().replace("\n","").replace("\t",""))

    # work_area 수집
      work_area_info = paper.select('div.cont > ul > li > span')
      try:
        print(work_area_info[2].get_text()) # TEST
        work_area.append(work_area_info[2].get_text().strip().replace("\n","").replace("\t",""))
      except:
        work_area.append('-')
        
    # Education 수집
      Education_info = paper.select('div.cont > ul > li > span')
      try:
        print(Education_info[1].get_text())# TEST
        Education.append(Education_info[1].get_text().strip().replace("\n","").replace("\t",""))
      except:
        Education.append('-')
        
    # wage 수집
      wage_info = paper.select('div.cont > ul > li > span')
      try:
        print(wage_info[3].get_text())# TEST
        wage.append(wage_info[3].get_text().strip().replace("\n","").replace("\t",""))
      except:
        wage.append('-')
        
    # employment_type 수집
      employment_type_info = paper.select('div.cont > ul > li > span')
      try:
        print(employment_type_info[4].get_text()) # TEST
        employment_type.append(employment_type_info[4].get_text().strip().replace("\n","").replace("\t",""))
      except:
        employment_type.append('-')
        
    # Welfare 수집
      Welfare_info = paper.select('div.cont > ul > li.full > em')
      try:
        print(Welfare_info[0].get_text()) # TEST
        Welfare.append(Welfare_info[0].get_text().strip().replace("\n","").replace("\t",""))
      except:
        Welfare.append('-')
        
    # Job_Description 수집
      Job_Description_info = paper.select('table > tbody > tr > td')
      try:
        print(Job_Description_info[0].get_text()) # TEST
        Job_Description.append(Job_Description_info[0].get_text().strip().replace("\n","").replace("\t",""))
      except:
        Job_Description.append('-')
        
        
  Job_dic = {"채용공고명":Job_Announcement, "학력":Education, "근무지역":work_area,"임금":wage,
                "고용형태":employment_type, "복리후생":Welfare, "직무내용":Job_Description}

  Job_dic = pd.DataFrame(Job_dic) # 수정 가능

  return Job_dic

