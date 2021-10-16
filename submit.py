import os
import requests
import subprocess
import sys


def requests_submit(submit_address, submit_token, success_request, failed_request, message):
    try:
        flag = message['flag']

        formdata = {
                    "token": submit_token, 
                    "flag": flag, 
                    }
        headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
                    }
        cookies = {
                    "cookie_name": "cookie_value", 
                    }
        response = requests.post(submit_address, data=formdata, headers=headers, cookies=cookies, verify=False, timeout=3)
        # print(response.text)

        if success_request in response.text:
            message['submit_status'] = "submit success"
        elif failed_request in response.text:
            message['submit_status'] = "submit failed"
        else:
            message['submit_status'] = "submit other reasons: " + response.text
        return message
    except Exception as e:
        message['submit_status'] = "submit failed:" + str(e)
        return message


def curl_submit(submit_address, submit_token, success_request, failed_request, message):
    try:
        flag = message['flag']

        # curl -s slient -k no vertify -X POST -d data
        curl_order = f"curl -s -k -X POST {submit_address} -d 'token={submit_token}&flag={flag}'"
        response = subprocess.check_output(curl_order, shell=True).decode()

        if success_request in response:
            message['submit_status'] = "submit success"
        elif failed_request in response:
            message['submit_status'] = "submit failed"
        else:
            message['submit_status'] = "submit other reasons: " + response
        return message
    except Exception as e:
        message['submit_status'] = "submit failed:" + str(e)
        return message


def main(submit, message):
    if submit.submit_method == "requests":
        return requests_submit(submit.submit_address, submit.submit_token, submit.success_request, submit.failed_request, message)

    elif submit.submit_method == "curl":
        return curl_submit(submit.submit_address, submit.submit_token, submit.success_request, submit.failed_request, message)


if __name__ == '__main__':
    import resolve_config
    con = resolve_config.main()
    flag = sys.argv[1]
    message = {'flag': flag}
    print(main(con.submit, message))
