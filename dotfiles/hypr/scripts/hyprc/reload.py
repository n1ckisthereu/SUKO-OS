from utils import Utils 
from constants import HYPRCTL, PYWALFOX

APPS_RELOAD = [
    {"app": "kitty", "sig": "USR1"},
    {"app": "hypr", "sig": f"{HYPRCTL} reload"},
    {"app": "firefox", "sig": f"{PYWALFOX} update"}
]

def reloadFiles():
    wclient = Utils()

    for x in APPS_RELOAD:
        APP = x["app"]

        if APP == "hypr":
            wclient.run_command(x["sig"]);print("Hyper restarted successfully!")
            continue
        elif APP == "firefox":
            wclient.run_command(x["sig"]);print("Firefox restarted successfully!")
            continue

        if wclient.reload_app(APP, x["sig"]):
            print(f"{APP} restarted successfully")
        else:
            print(f"Failed to restart {APP}.")
