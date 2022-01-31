# prog1-ws21-summarizer6

Prog1 WS 2021/22: Automatic Text Summary

https://gitlab.cl.uni-heidelberg.de/prog1-ws21/prog1-ws21-summarizer6/


## Usage Examples

```
./src/main.py -h    # print help

./src/main.py -i ./test/test-de.txt # summarize ./test/test-de.txt

./src/main.py -i ./test/test-en.txt -o ./tmp/out.txt -n 3 # summarize ./test/test-en.txt into 3 sentences and save it to ./tmp/out.txt 

echo -e "first line\nsecond line" | ./src/main.py -i - # summarize from piped command

# Start UI:
./src/ui.py
```


# Dependencies:

Python3  
Gtk4  
PyGObject  
libadwaita  
meson

## Installing PyGObject

https://pygobject.readthedocs.io/en/latest/getting_started.html


# Building Flatpak

You can build and run from GNOME Builder. Alternatively, use the following commands to build with flatpak-builder.

### Install SDK and Platform

```bash
flatpak install flathub org.Gnome.Sdk//41
flatpak install flathub org.Gnome.Platform//41
```

### Build and install for user

```bash
flatpak-builder --user --install --force-clean build-dir de.haigruppe.summarizer.json
```

### Build to repo

```bash
flatpak-builder --repo=repo --force-clean build-dir de.haigruppe.summarizer.json
```

### Make single-file bundle from repo

```bash
flatpak build-bundle repo summarizer.json de.haigruppe.summarizer stable --runtime-repo="https://flathub.org/repo/flathub.flatpakrepo"
```

# Ressources

- Gtk4 Docs: https://docs.gtk.org/gtk4/
- libadwaita Docs: https://gnome.pages.gitlab.gnome.org/libadwaita/doc/1-latest/
- Python Gtk4 Tutorial: https://github.com/Taiko2k/GTK4PythonTutorial
- Python Gtk4 Example: https://github.com/timlau/gtk4-python
- Cambalache (UI Designer): https://gitlab.gnome.org/jpu/cambalache
