import imaplib 

hoster =  {c[0]: (c[1], c[2]) for c in [x.strip().split(":") for x in open('hoster.dat','r').readlines()] if len(c)>=2}

def check_email(em):
    host = hoster[em[0].split("@")[1]]
    
    M = imaplib.IMAP4_SSL(host[0])
    M.login(em[0], em[1])
    M.select()

    try:
        typ, data = M.search(None, '(From "account-update@amazon.com")')
        M.logout()
        if data[0]:
            return False 
        else:
            return True
    except Exception as e:print(e)

if __name__ == "__main__":    
    def core():
        for i in live:
            try:
                test(i.split(":"))
            except: continue

    live =[x.strip() for x in open('live_amz.txt', 'r').readlines()]
