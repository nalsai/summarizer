#!/usr/bin/env python3

"""A UI for a program to summarize text, I guess."""

import sys
import os
import gi
try:
    from summarizer.widgets import Window, MenuButton
    import summarizer.text_summarize
except ImportError:
    from widgets import Window, MenuButton
    import text_summarize

gi.require_version("Gtk", "4.0")  # GTK 4 ftw
gi.require_version("Adw", version="1")

from gi.repository import Gtk, Gio, Adw


# Gtk.Builder xml for the application menu
APP_MENU = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
<requires lib="gtk" version="4.0"/>
<requires lib="libadwaita" version="1.0"/>
<menu id='app-menu'>
  <section>
    <item>
      <attribute name='label' translatable='yes'>_Clear Text</attribute>
      <attribute name='action'>win.clear</attribute>
    </item>
    <item>
      <attribute name='label' translatable='yes'>_Preferences</attribute>
      <attribute name='action'>win.preferences</attribute>
    </item>
    <item>
      <attribute name='label' translatable='yes'>_Keyboard Shortcuts</attribute>
      <attribute name='action'>win.shortcuts</attribute>
    </item>
    <item>
      <attribute name='label' translatable='yes'>_About Summarizer</attribute>
      <attribute name='action'>win.about</attribute>
    </item>
  </section>
</menu>
</interface>
"""


class MyWindow(Window):

    def __init__(self, title, width, height, **kwargs):
        super().__init__(title, width, height, **kwargs)
        self.revealer = None

        menu = MenuButton(APP_MENU, 'app-menu')
        menu.set_tooltip_text("Main Menu")
        menu.set_has_frame(False)
        self.headerbar.pack_end(menu)

        save_btn = Gtk.Button()
        save_btn.set_label("Save to File")
        save_btn.set_tooltip_text("Save to File")
        save_btn.set_has_frame(False)
        save_btn.set_icon_name("document-save-symbolic")
        save_btn.connect('clicked', self.on_save_btn)
        self.headerbar.pack_end(save_btn)

        load_btn = Gtk.Button()
        load_btn.set_label("Load from File")
        load_btn.set_tooltip_text("Load from File")
        load_btn.set_has_frame(False)
        load_btn.set_icon_name("document-open-symbolic")
        load_btn.connect('clicked', self.on_load_btn)
        self.headerbar.pack_end(load_btn)

        # Create actions to handle menu actions
        self.create_action('clear', self.menu_handler)
        self.create_action('preferences', self.menu_handler)
        self.create_action('shortcuts', self.menu_handler)
        self.create_action('about', self.menu_handler)

        apply_btn = Gtk.Button()
        apply_btn.set_label("Summarize")
        apply_btn.set_halign(Gtk.Align.END)
        apply_btn.set_css_classes(["suggested-action"])
        apply_btn.connect('clicked', self.on_summarize_btn)
        self.headerbar.pack_start(apply_btn)

        main = self.setup_main_page()
        self.set_child(main)

    def setup_main_page(self):
        """Main Page"""
        main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        scrolledwindow = Gtk.ScrolledWindow()
        self.textview = Gtk.TextView.new()
        self.textview.set_left_margin(8)
        self.textview.set_top_margin(8)
        self.textview.set_right_margin(8)
        self.textview.set_bottom_margin(8)
        self.textview.set_vexpand(True)
        self.textview.set_hexpand(True)
        self.textview.set_wrap_mode(Gtk.WrapMode.WORD)
        self.textbuffer = self.textview.get_buffer()
        self.textbuffer.set_text(
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' \
            'Donec tempus leo at interdum iaculis. ' \
            'Cras a dolor ut augue blandit varius. Aliquam ac fermentum turpis. ' \
            'Duis nisl ante, faucibus eget magna eget, interdum pretium orci. ' \
            'Curabitur efficitur ipsum vitae justo pharetra, eu sodales erat aliquet. ' \
            'Sed commodo dui nunc, a rutrum ligula ornare nec. ' \
            'Morbi lacinia porta pretium. ' \
            'Nullam nunc libero, aliquet id arcu in, tincidunt molestie magna. ' \
            'Maecenas porttitor, justo eget maximus consequat, ' \
            'velit nisl dictum mauris, et tristique ante justo eget mauris. '
        )
        scrolledwindow.set_child(self.textview)
        main.append(scrolledwindow)
        return main

    def show_shortcuts(self):
        if(os.path.exists("data/resources/ui/shortcuts.ui")):
            builder = Gtk.Builder.new_from_file("data/resources/ui/shortcuts.ui")
        else:
            builder = Gtk.Builder.new_from_resource("/de/haigruppe/summarizer/ui/shortcuts.ui")
        shortcuts = builder.get_object("shortcuts")
        shortcuts.present()

    def show_preferences(self):
        # TODO
        print("まだ")

    def show_about(self):
        about = Gtk.AboutDialog()
        about.set_logo_icon_name("media-view-subtitles-symbolic")
        about.set_program_name("🦈 Summarizer")
        about.set_version("0.1.0")
        about.set_comments("A program to summarize text, I guess.")
        about.set_website(
            "https://gitlab.cl.uni-heidelberg.de/prog1-ws21/prog1-ws21-summarizer6/")
        about.set_license_type(Gtk.License.GPL_3_0)
        about.set_authors(["Nils Fürniß https://git.nalsai.de/",
                          "Spyridon Link https://github.com/Astrothewhiteshadow/"])
        about.present()

    # ---------------------- Handlers --------------------------

    def menu_handler(self, action, state):
        """ Callback for  menu actions"""
        name = action.get_name()
        #print(f'active : {name}')
        if name == 'shortcuts':
            self.show_shortcuts()
        elif name == 'clear':
            self.textview.get_buffer().set_text("")
        elif name == 'preferences':
            self.show_preferences()
        elif name == 'about':
            self.show_about()

    def on_load_btn(self, widget):
        """ callback for load buttom clicked """
        dialog = Gtk.FileChooserDialog()
        f = Gtk.FileFilter()
        f.set_name("Text files")
        f.add_mime_type("text/plain")
        dialog.add_filter(f)
        dialog.set_action(Gtk.FileChooserAction.OPEN)
        dialog.set_title("Load from File")
        dialog.add_button("_Select", Gtk.ResponseType.ACCEPT)
        dialog.add_button("_Cancel", Gtk.ResponseType.CANCEL)
        dialog.set_transient_for(self)
        dialog.set_modal(self)
        dialog.connect('response', self.on_save_response)
        dialog.present()

    def on_load_response(self, dialog, response):
        """ callback for load response from FileChooserDialog """
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
            input_text = self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), False)
            with open(file.get_path(), "w") as file:
                text_input = file.write(input_text)
        dialog.destroy()

    def on_save_btn(self, widget):
        """ callback for save buttom clicked """
        dialog = Gtk.FileChooserDialog()
        f = Gtk.FileFilter()
        f.set_name("Text file")
        f.add_mime_type("text/plain")
        dialog.add_filter(f)
        dialog.set_action(Gtk.FileChooserAction.SAVE)
        dialog.set_title("Save to File")
        dialog.add_button("_Save", Gtk.ResponseType.ACCEPT)
        dialog.add_button("_Cancel", Gtk.ResponseType.CANCEL)
        dialog.set_transient_for(self)
        dialog.set_modal(self)
        dialog.connect('response', self.on_load_response)
        dialog.present()

    def on_save_response(self, dialog, response):
        """ callback for save response from FileChooserDialog """
        if response == Gtk.ResponseType.ACCEPT:
            file = dialog.get_file()
            with open(file.get_path(), "r") as file:
                text_input = file.read()
                self.textbuffer.set_text(text_input)
        dialog.destroy()

    def on_summarize_btn(self, widget):
        """ callback for summarize buttom clicked """
        input_text = self.textbuffer.get_text(self.textbuffer.get_start_iter(), self.textbuffer.get_end_iter(), False)
        self.textbuffer.set_text(text_summarize.do_stuff(input_text))


class Application(Adw.Application):
    """ Main Aplication class """

    def __init__(self):
        super().__init__(application_id='de.haigruppe.summarizer', flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_startup(self):
        Adw.Application.do_startup(self)
        style_manager = Adw.StyleManager.get_default()
        style_manager.props.color_scheme = Adw.ColorScheme.PREFER_DARK  # Use dark appearance unless the system prefers prefers light colors.
                                                                        # should probably be removed with Gnome 42 Runtime

    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MyWindow("🦈 Summarizer", 700, 500, application=self)
        win.present()


def main():
    """ Run the main application"""
    app = Application()
    return app.run(sys.argv)


if __name__ == '__main__':
    main()
