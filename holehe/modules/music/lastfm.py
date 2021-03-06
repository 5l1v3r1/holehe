from holehe.core import *
from holehe.localuseragent import *



def lastfm(email):
    req = requests.get("https://www.last.fm/join")
    try:
        token = req.cookies["csrftoken"]
    except:
        return({"rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})

    data = {"csrfmiddlewaretoken": token, "userName": "", "email": email}
    headers = {
        "Accept": "*/*",
        "Referer": "https://www.last.fm/join",
        "X-Requested-With": "XMLHttpRequest",
        "Cookie": "csrftoken="+str(token),
    }
    check = requests.post(
        "https://www.last.fm/join/partial/validate",
        headers=headers,
        data=data).json()
    if check["email"]["valid"]:
        return({"rateLimit": False, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
    else:
        return({"rateLimit": False, "exists": True, "emailrecovery": None, "phoneNumber": None, "others": None})
