import re
import sys
import json
from constants import *
from utils import Utils
from reload import reloadFiles
from time import sleep
from PIL import Image

try:
    WALLPAPER_PATH = sys.argv[1]
    DARK_THEME = sys.argv[2]
except:
    print(f"usage: {sys.argv[0]} [Wallpaper path] [bool:isDark]")
    sys.exit(1)

wclient = Utils()


def setWallpaper():
    swww_command = f'{SWWW} img "{WALLPAPER_PATH}" --transition-bezier .43,1.19,1,.4 --transition-type "grow" --transition-duration 0.7 --transition-fps 60 --invert-y --transition-pos "$( hyprctl cursorpos )"'
    wclient.run_command(swww_command)


def qtToggle(dark: bool):
    config_path = f"{CONFIG_DIR}/qt6ct/qt6ct.conf"
    config_file = wclient.read_file(f"{config_path}")
    if dark:
        config_file = re.sub(
            r"color_scheme_path=.+",
            f"color_scheme_path={QT6_COLOR_SCHEMES_DARK}",
            config_file,
        )
    else:
        config_file = re.sub(
            r"color_scheme_path=.+",
            f"color_scheme_path={QT6_COLOR_SCHEMES_LIGHT}",
            config_file,
        )

    wclient.write_file(config_path, config_file)


def generateColorScheme():
    wal_path = WALLPAPER_PATH

    if WALLPAPER_PATH.split(".")[-1] == "gif":
        with Image.open(WALLPAPER_PATH) as img:
            img.save("/tmp/gifwal.png")
            wal_path = "/tmp/gifwal.png"

    if wclient.isDark(DARK_THEME):
        generate = f"wal -s -n -t -e -i {wal_path}"
        # wclient.run_command("gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita-dark'")
        wclient.run_command(
            "gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'"
        )
        qtToggle(True)
    else:
        generate = f"wal --saturate 0.9 -l -s -n -t -e -i {wal_path}"
        # wclient.run_command("gsettings set org.gnome.desktop.interface gtk-theme 'Adwaita'")
        wclient.run_command(
            "gsettings set org.gnome.desktop.interface color-scheme 'prefer-light'"
        )

        qtToggle(False)

    wclient.run_command(generate)
    print("Schemes generated...")


def discordColorScheme():
    final_file = ""

    def is_black(hex_color):
        import colorsys

        hex_color = hex_color.lstrip("#")
        rgb = tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

        # Limiar para determinar se a cor é escura o suficiente para ser considerada preta
        threshold = 90

        # Verifica se a soma dos componentes RGB está abaixo do limiar
        # E se a saturação é baixa (por exemplo, menor que 10%)
        return (
            sum(rgb) < threshold
            and colorsys.rgb_to_hls(*[c / 255.0 for c in rgb])[2] < 0.1
        )

    content = json.loads(wclient.read_file(f"{CACHE_DIR}/wal/colors.json"))
    theme_file = wclient.read_file(f"{DISCORD_THEMES_FOLDER}/{DISCORD_THEME_NAME}")

    accent_color = wclient.hex_to_hsl(content["special"]["background"])
    accent_color = f"{accent_color[0]}"

    if is_black(content["special"]["background"]) and DARK_THEME:
        final_file = re.sub(
            r"--accent-saturation:.+", f"--accent-saturation: 0%;", theme_file
        )
    else:
        final_file = re.sub(
            r"--accent-saturation:.+", f"--accent-saturation: 71%;", theme_file
        )

    final_file = re.sub(
        r"--accent-hue:.+", f"--accent-hue: {accent_color};", final_file
    )
    wclient.write_file(f"{DISCORD_THEMES_FOLDER}/{DISCORD_THEME_NAME}", final_file)


def copyFiles():
    wclient.copy(WAL_KITTY_TERMINAL, APP_KITTY_TERMINAL)
    wclient.copy(WAL_HYPERLAND_COLORS, APP_HYPERLAND_COLORS)
    discordColorScheme()


def start():
    generateColorScheme()
    copyFiles()
    reloadFiles()


if __name__ == "__main__":
    setWallpaper()
    start()
