use test; 
CREATE TABLE company (
  com_no int NOT NULL AUTO_INCREMENT,
  name varchar(45) NOT NULL COMMENT '회사명',
  sector varchar(45) NOT NULL COMMENT '회사업종',
  size varchar(45) NOT NULL COMMENT '회사규모',
  established varchar(45) DEFAULT NULL COMMENT '설립날짜',
  annual_sales varchar(45) DEFAULT NULL COMMENT '연매출액',
  homepage varchar(100) DEFAULT NULL COMMENT '홈페이지주소',
  workercnt int DEFAULT NULL COMMENT '근로자수',
  PRIMARY KEY (com_no),
  UNIQUE KEY name_UNIQUE (name)
) ENGINE=InnoDB AUTO_INCREMENT=2974;

CREATE TABLE paytype (
  ptype_no int NOT NULL,
  type varchar(45) NOT NULL COMMENT '시급 | 일급 | 월급 | 연봉',
  PRIMARY KEY (ptype_no),
  UNIQUE KEY type_UNIQUE (type)
) ENGINE=InnoDB;

CREATE TABLE sido (
  sido_no int NOT NULL,
  name varchar(45) NOT NULL COMMENT '지역명',
  momid int DEFAULT NULL,
  PRIMARY KEY (sido_no),
  UNIQUE KEY name_UNIQUE (name)
) ENGINE=InnoDB;

CREATE TABLE worktype (
  wtype_no int NOT NULL,
  name varchar(100) NOT NULL COMMENT '직종명',
  PRIMARY KEY (wtype_no)
) ENGINE=InnoDB;

CREATE TABLE Announce (
  ann_no int NOT NULL AUTO_INCREMENT,
  title varchar(100) DEFAULT NULL COMMENT '공고제목',
  career varchar(45) DEFAULT NULL COMMENT '경력',
  education varchar(45) DEFAULT NULL COMMENT '학력',
  emp_p varchar(45) DEFAULT NULL COMMENT '고용형태',
  emp_t varchar(45) DEFAULT NULL COMMENT '근무형태',
  url varchar(200) NOT NULL COMMENT '워크넷 원본 주소',
  company_no int NOT NULL COMMENT '공고올린 회사의 번호',
  worktype_no int NOT NULL COMMENT '직종의 번호',
  paytype_no int NOT NULL COMMENT '돈지급방식의 번호',
  paymoney int DEFAULT NULL COMMENT '돈',
  sido_no int NOT NULL,
  detail_add varchar(100) DEFAULT NULL,
  x decimal(20,15) DEFAULT NULL,
  y decimal(20,15) DEFAULT NULL,
  PRIMARY KEY (ann_no),
  KEY fk_Announce_company_idx (company_no),
  KEY fk_Announce_worktype1_idx (worktype_no),
  KEY fk_Announce_payType1_idx (paytype_no),
  KEY fk_Announce_sido1_idx (sido_no),
  CONSTRAINT fk_Announce_company FOREIGN KEY (company_no) REFERENCES company (com_no),
  CONSTRAINT fk_Announce_payType1 FOREIGN KEY (paytype_no) REFERENCES paytype (ptype_no),
  CONSTRAINT fk_Announce_sido1 FOREIGN KEY (sido_no) REFERENCES sido (sido_no),
  CONSTRAINT fk_Announce_worktype1 FOREIGN KEY (worktype_no) REFERENCES worktype (wtype_no)
) ENGINE=InnoDB AUTO_INCREMENT=7075;



