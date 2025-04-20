import scratchattach as sa
from scratchattach.utils.exceptions import LoginFailure

class TextEffect:
    BLACK          = '\033[30m'#(文字)黒
    RED            = '\033[31m'#(文字)赤
    GREEN          = '\033[32m'#(文字)緑
    YELLOW         = '\033[33m'#(文字)黄
    BLUE           = '\033[34m'#(文字)青
    MAGENTA        = '\033[35m'#(文字)マゼンタ
    CYAN           = '\033[36m'#(文字)シアン
    WHITE          = '\033[37m'#(文字)白
    COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す
    BOLD           = '\033[1m'#太字
    UNDERLINE      = '\033[4m'#下線
    INVISIBLE      = '\033[08m'#不可視
    REVERCE        = '\033[07m'#文字色と背景色を反転
    BG_BLACK       = '\033[40m'#(背景)黒
    BG_RED         = '\033[41m'#(背景)赤
    BG_GREEN       = '\033[42m'#(背景)緑
    BG_YELLOW      = '\033[43m'#(背景)黄
    BG_BLUE        = '\033[44m'#(背景)青
    BG_MAGENTA     = '\033[45m'#(背景)マゼンタ
    BG_CYAN        = '\033[46m'#(背景)シアン
    BG_WHITE       = '\033[47m'#(背景)白
    BG_DEFAULT     = '\033[49m'#背景色をデフォルトに戻す
    RESET          = '\033[0m'#全てリセット

def login_scratch():
    print("<Login>")
    global session
    username = input("username: ")
    password = input("password: ")
    try:
        session = sa.login(username, password)
        print(f"{TextEffect.CYAN}{TextEffect.BOLD}Login successful{TextEffect.RESET}")
    except LoginFailure:
        print(f"{TextEffect.RED}{TextEffect.BOLD}ERROR: Login failed. Your username or password may be incorrect. Please check. If the problem persists, you may have typed incorrectly too many times, so try accessing scratch from your browser, logging out, and then logging in from your browser.{TextEffect.RESET}")

def cloud_variable():
    project_id = input("project_id: ")
    cloud = session.connect_cloud(project_id)

    variable_name = input("Enter variable name: ")
    value = cloud.get_var(variable_name)
    if value == None:
        print(f"{TextEffect.YELLOW}{TextEffect.BOLD}Result: None or Variable does not exist.{TextEffect.RESET}")
    else:
        print(f"{TextEffect.CYAN}{TextEffect.BOLD}Result: {value}{TextEffect.RESET}")


if __name__ == "__main__":
    print("ctrl+C to quit")
    login_scratch()
    while True:
        print("ctrl+C to quit")
        print("Type 'login' or 'get cloud variable'")
        command = input("enter command: ")
        if command == "login":
            login_scratch()
        elif command == "get cloud variable":
            cloud_variable()
        else:
            print("ERROR: command not found")
