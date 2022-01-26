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
./src/ui/main.py
```


# Dependencies:

Python3  
Gtk4  
PyGObject  
meson (only for building)

## Installing PyGObject

https://pygobject.readthedocs.io/en/latest/getting_started.html        


# Ressources

- Gtk4 Docs: https://docs.gtk.org/gtk4/
- Python Gtk4 Example: https://github.com/timlau/gtk4-python
- Cambalache (UI Designer): https://gitlab.gnome.org/jpu/cambalache
