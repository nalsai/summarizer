# Running 🦈 Summarizer on Windows

Currently, there is no native package for Windows.
You can run 🦈 Summarizer using msys2 on Windows, like this:

Install msys2 using chocolatey, or  
go to https://www.msys2.org/ and download the x86_64 installer and follow the instructions on the page for setting up the basic environment.

Run `C:\msys64\mingw64.exe` (`C:\tools\msys64\mingw64.exe` for chocolatey) - a terminal window should pop up

Execute the following commands to install all dependencies:

```
pacman -Syu
pacman -S mingw-w64-x86_64-gtk4 mingw-w64-x86_64-libadwaita mingw-w64-x86_64-python3 mingw-w64-x86_64-python-pip mingw-w64-x86_64-python-wheel mingw-w64-x86_64-python-gobject mingw-w64-x86_64-gcc git
python -m pip install nltk
```

Now, you can clone this repository and run the ui.

```
git clone https://github.com/Nalsai/summarizer.git
cd summarizer/
chmod +x src/ui.py 
chmod +x src/main.py 
./src/ui.py
```
