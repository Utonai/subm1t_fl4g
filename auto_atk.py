import time
from typing_extensions import runtime
import attack
import submit
import log
import resolve_config


def main():
    con = resolve_config.main()
    while 1:
        start_time = time.time()
        for ip in con.ip_list:
            message = attack.main(ip)
            message = submit.main(con.submit, message)
            log.main(ip, message)
            time.sleep(con.submit_wait)
        end_time = time.time()
        run_time = start_time - end_time
        if con.round_time > run_time:
            time.sleep(con.round_time-run_time)


if __name__ == '__main__':
    main()
