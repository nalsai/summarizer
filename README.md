# 🦈 Summarizer

Prog1 WS 2021/22: Automatic Text Summary — prog1-ws21-summarizer6

## Usage Examples

```bash
./src/main.py -h  # print help

./src/main.py -i ./test/test-en.txt  # summarize ./test/test-en.txt

./src/main.py -i ./test/test-en.txt -o ./tmp/out.txt -n 3  # summarize to 3 sentences and save the summary

echo -e "first line.\nsecond line" | ./src/main.py -i -  # you can also summarize using pipes

./src/ui.py  # Start UI
```

## Dependencies

Python3  
Gtk4  
PyGObject  
libadwaita  
nltk  
flatpak-builder or meson (for building)
cx_Freeze (for building win32)

## Running on Windows

see [docs/windows.md](docs/windows.md)

## Running on Linux

You can install the Flatpak, which includes everything you need, like this:

```bash
flatpak install https://flatpak.nils.moe/de.haigruppe.summarizer.flatpakref
```

If you've never installed a Flatpak, follow the [setup guide](https://flatpak.org/setup/) first.

## Building

You can build and run from GNOME Builder.
Alternatively, use the following commands to build with meson or with flatpak-builder.

### meson

Make sure you have all dependencies installed, then you can run the following:

```bash
meson configure build
cd build
meson compile
meson install
```

### Flatpak

```bash
flatpak-builder --install-deps-from=flathub --force-clean build-dir de.haigruppe.summarizer.json
flatpak-builder --user --install --force-clean build-dir de.haigruppe.summarizer.json
```

## Resources

- Gtk4 Docs: <https://docs.gtk.org/gtk4/>
- libadwaita Docs: <https://gnome.pages.gitlab.gnome.org/libadwaita/doc/1-latest/>
- Python Gtk4 Tutorial: <https://github.com/Taiko2k/GTK4PythonTutorial>
- Python Gtk4 Example: <https://github.com/timlau/gtk4-python>
- Cambalache (UI Designer): <https://gitlab.gnome.org/jpu/cambalache>
