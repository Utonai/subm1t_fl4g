import configparser


class submits:
    def __init__(self, name):
        self.name = __name__


class configs:
    def __init__(self, name):
        self.name = __name__
        self.submit = submits("")


def main():
    con = configs("config")
    config = configparser.ConfigParser()
    config.read("./config.conf")

    ip_list_file = config.get("config", "ip_list_file")
    con.ip_list = open(ip_list_file, "r").read().splitlines()

    con.submit.submit_method = config.get("config", "submit_method")
    con.submit.submit_address = config.get("config", "submit_address")
    con.submit.submit_token = config.get("config", "submit_token")

    con.submit.success_request = config.get("config", "success_request")
    con.submit.failed_request = config.get("config", "failed_request")

    con.round_time = int(config.get("config", "round_time"))
    con.rounds = int(config.get("config", "rounds"))
    con.submit_wait = int(config.get("config", "submit_wait"))

    return con


if __name__ == '__main__':
    main()
