import time
import submit
import resolve_config


def write_log(log_file, flag, submit_status):
    localtime = time.asctime(time.localtime(time.time()))
    with open(log_file, "w+") as fp:
        fp.write(localtime + "\t" + flag + "\t" + submit_status + "\n")


def main():
    con = resolve_config.main()
    flag_list = open(con.flag_list_file, "r").read().splitlines()
    for flag in flag_list:
        result = submit.main(con.submit, {'flag': flag})
        write_log(con.log_file, flag, result["submit_status"])
        time.sleep(con.submit_wait)


if __name__ == "__main__":
    main()
