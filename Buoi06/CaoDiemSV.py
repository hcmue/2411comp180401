API_HOST = "https://onlineapi.hcmue.edu.vn/api"
API_KEY = "hcmuepscRBF0zT2Mqo6vMw69YMOH43IrB2RtXBS0EHit2kzvL2auxaFJBvw=="
API_CLIENTID = "hcmue"

import requests
import json

def login():
    url = f"{API_HOST}/authenticate/authpsc"
    myheaders = {
        "Apikey": API_KEY, "Clientid": API_CLIENTID
    }
    result = requests.post(
        url,
        json={"username":"9111","password":"9111"},
        headers=myheaders
    )
    if result.status_code == 200:
        print("Login success")
        print(result.json())
        global TOKEN
        TOKEN = result.json()["Token"]

def lay_diem_theo_Sv(masv):
    url = f"{API_HOST}/professor/GetAllMarkStudentByProgramID"
    myheaders = {
        "Apikey": API_KEY, "Clientid": API_CLIENTID,
        "Authorization": f"Bearer {TOKEN}"
    }
    result = requests.post(
        url,
        json={"p1":masv,"p2":"K497480201","p3":"ALL","p4":"ALL"},
        headers=myheaders
    )
    if result.status_code == 200:
        print("Get success")
        print(result.json())


def lay_dssv_theo_lop(malop):
    url = f"{API_HOST}/professor/GetStudentInClassCVHT"
    myheaders = {
        "Apikey": API_KEY, "Clientid": API_CLIENTID,
        "Authorization": f"Bearer {TOKEN}"
    }
    result = requests.post(
        url,
        json={"YearStudy":"2024-2025","TermId":"HK01","Id":malop},
        headers=myheaders
    )
    if result.status_code == 200:
        print("Get success")
        print(json.dumps(result.json(), indent=4))
#Call
login()
print("Token", TOKEN)
# lay_diem_theo_Sv("49.01.104.104")
lay_dssv_theo_lop("48.01.CNTT.A")

'''
1/ Lấy thống tin lớp CVHT
POST: {{API_HOST}}/professor/GetClassStudentCVHT
Body: {"YearStudy":"2024-2025","TermId":"HK01"}

2/ Lấy danh sách SV theo lớp CVHT
POST: {{API_HOST}}/professor/GetStudentInClassCVHT
Body: {"YearStudy":"2024-2025","TermId":"HK01","Id":"47.01.CNTT.C"}
'''

