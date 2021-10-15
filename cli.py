import time
import submit
import resolve_config


def main():
    con = resolve_config.main()
    while 1:
        flag_list = []
        for line in iter(input, ''):
            flag_list.append(line)
        for flag in flag_list:
            result = submit.main(con.submit, {'flag': flag})
            if "submit failed" in result["submit_status"]:
                print(f"invalid flag:{flag}")
            time.sleep(con.submit_wait)


if __name__ == "__main__":
    main()
