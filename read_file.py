import time
import submit
import resolve_config


def main():
    con = resolve_config.main()
    flag_list = open(con.ip_list_file, "r").read().splitlines()
    for flag in flag_list:
        submit.main(con.submit, {'flag': flag})
        time.sleep(con.submit_wait)


if __name__ == "__main__":
    main()
