import sys
import speedtest


def get_speed_test():
    servers = []
    stest = speedtest.Speedtest(secure=True)
    stest.get_servers(servers)
    stest.get_best_server()
    return stest


def command_line_runner():
    stest = get_speed_test()
    down_result = stest.download()
    up_result = stest.upload()
    print(f"download:{down_result}\nupload:{up_result}")


if __name__ == '__main__':
    command_line_runner()
