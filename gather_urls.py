import requests
from bs4 import BeautifulSoup
import sqlite3


url = "https://cleanerlewisham.lovecleanstreets.com/reports"

payload = "__RequestVerificationToken=KDALdzId6Mn3XlFM3Vn__t5qaC6maKmKtRI53GEbNuoW6P_1nOpa1zr0Msn2nB-vp7NIFxBzlBH5TUJPjn61PoYW_nW-N2I1g6JGn2unEAw1&Take=20&AuthorityId=241&=WardId%3D&=Completed%3D&=Tag%3D&CategoryId=16092&ReportedStartDate=24%2F03%2F2024&X-Requested-With=XMLHttpRequest"
headers = {
    "Accept": "*/*",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,fr;q=0.7",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "__utmz=26422690.1708430502.14.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ASP.NET_SessionId=xoispbhimrn14qk5s4l3s5la; __RequestVerificationToken=xCVeX_T6dPOmNh1rxboCSaP4F8zqXUVU8wB9pmpKm2bMD-oxe_IcOcT4qe3sPT-ea6S9_-f8qwSdbJxKkHBzkFWhxOM_syIVmTkLI9PP70k1; ARRAffinity=086bf48ddc3c26dda01fbbc4ee503e6d27d1566a6d5c29aeb1898c831b75baeb; ARRAffinitySameSite=086bf48ddc3c26dda01fbbc4ee503e6d27d1566a6d5c29aeb1898c831b75baeb; __utma=26422690.563911593.1706891970.1708447454.1711404457.17; __utmc=26422690; __utmb=26422690.4.10.1711404457",
    "Origin": "https://cleanerlewisham.lovecleanstreets.com",
    "Referer": "https://cleanerlewisham.lovecleanstreets.com/reports",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest, XMLHttpRequest",
    "sec-ch-ua-mobile": "?0",
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)