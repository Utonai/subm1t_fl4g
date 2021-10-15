import time
import submit
import resolve_config


def main():
    con = resolve_config.main()
    flag_list = open(con.flag_list_file, "r").read().splitlines()
    for flag in flag_list:
        result = submit.main(con.submit, {'flag': flag})
        if "submit success" not in result["submit_status"]:
            print(flag,"-",result["submit_status"])
        time.sleep(con.submit_wait)


if __name__ == "__main__":
    main()
