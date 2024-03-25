# SukoOS

Hello friends, this is just a small project that went a little
far and that became a dream, but it's over, well my life is very difficult,
unfortunately I don't have more time to donate to this project but here I leave it,
if you like this idea, please contribute.

Well the idea was to develop a distro, I started but skipped some steps,
like the mirrors, I had a lot of difficulty, it's not easy to maintain one,
so with everything ready I started to assemble some dotfiles to use as an
interface, and now after a long time I ran out of time for that, so to
eternalize the project, I'm going to save the dotfiles with the hope of
someday coming back and releasing my distro

An important detail, I don't recommend using this prototype, there are many things
that were done in a lot of haste, so there are many paths defined directly for
my user.

The settings were built to use pywal and later a color scheme itself, when you generate
a color scheme it changes the colors of most applications, I didn't automate for
the gtk theme, but it's very simple, I got a lot of code, ideas and resources
from other repositories since the idea was to release as soon as possible and
improve over time, I still need to develop a lot of things like proprietary
themes support, theme of course that was discontinued due to the way I started
developing and how complex it would become, bluetooth, and when I say support,
it's worth remembering that "SukoOs" would use hyprland, and its base is
made on arch, so the support I'm referring to was for the widgets made in eww

But everything was very easy, we were developing a control panel to facilitate
the configurations that could be made in the system, and we chose the Tauri for
its ease, below I will show you a little of what was already ready

![suko](./suko_os.gif)

### Dependencies

- Install pywalfox extension in your browser

```bash
yay -Syyyu --needed gtkmm3 \
  ripgrep \
  playerctl \
  gradience-git \
  adw-gtk3-git \
  jq \
  eww-tray-wayland-git \
  polkit-gnome \
  swww \
  pamixer \
  grimblast-git \
  thunar \
  thunar-archive-plugin
  file-roller \
  xdg-user-dirs \
  wf-recorder \
  dbus-python \
  python-gobject \
  python-requests \
  python-jinja \
  python-material-color-utilities \
  zenity \
  socat \
  hyprpicker-git \
  nwg-look \
  qt5ct \
  qt6ct \
  rust \
  file \
  openssl \
  appmenu-gtk-module \
  gtk3 \
  libappindicator-gtk3 \
  librsvg \
  libvips \
  webkit2gtk \
  nmcli \
  networkmanager \
  pamixer \
  sassc \
  vesktop \
  kitty \
  swappy \
  libqalculate \
  lazygit \
  neovide \
  python-pywal \
  python-pywalfox
```
