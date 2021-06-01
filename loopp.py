import time
import attack
import submit
import log
import resolve_config


def main():
    con = resolve_config.main()
    while 1:
        for ip in con.ip_list:
            message = attack.main(ip)
            message = submit.main(con.submit,message)
            log.main(ip,message)
            time.sleep(con.submit_wait)
        time.sleep(con.round_time)


if __name__ == '__main__':
    main()
