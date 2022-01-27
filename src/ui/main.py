#!/usr/bin/env python3

"""A UI for a program to summarize text, I guess."""

import sys
import gi
#from summarizer.ui.widgets import Window, MenuButton   # for build
from widgets import Window, MenuButton                  # for development
from gi.repository import Gtk

gi.require_version("Gtk", "4.0")  # GTK 4 ftw


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
        self.headerbar.pack_end(save_btn)

        load_btn = Gtk.Button()
        load_btn.set_label("Load from File")
        load_btn.set_tooltip_text("Load from File")
        load_btn.set_has_frame(False)
        load_btn.set_icon_name("document-open-symbolic")
        self.headerbar.pack_end(load_btn)

        # Create actions to handle menu actions
        self.create_action('clear', self.menu_handler)
        self.create_action('preferences', self.menu_handler)
        self.create_action('shortcuts', self.menu_handler)
        self.create_action('about', self.menu_handler)

        apply_btn = Gtk.Button()
        apply_btn.set_label("Summarize")
        apply_btn.set_halign(Gtk.Align.END)
        self.headerbar.pack_start(apply_btn)

        main = self.setup_main_page()
        self.set_child(main)

    def setup_main_page(self):
        """Main Page"""
        main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        scroll_view = Gtk.ScrolledWindow()
        text = Gtk.TextView.new()
        text.set_vexpand(True)
        text.set_hexpand(True)
        text.set_wrap_mode(Gtk.WrapMode.WORD)
        txt = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.' \
            'Donec tempus leo at interdum iaculis. ' \
            'Cras a dolor ut augue blandit varius. Aliquam ac fermentum turpis. ' \
            'Duis nisl ante, faucibus eget magna eget, interdum pretium orci. ' \
            'Curabitur efficitur ipsum vitae justo pharetra, eu sodales erat aliquet. ' \
            'Sed commodo dui nunc, a rutrum ligula ornare nec. ' \
            'Morbi lacinia porta pretium. ' \
            'Nullam nunc libero, aliquet id arcu in, tincidunt molestie magna. ' \
            'Maecenas porttitor, justo eget maximus consequat, ' \
            'velit nisl dictum mauris, et tristique ante justo eget mauris. '
        text.get_buffer().set_text(txt)
        scroll_view.set_child(text)
        main.append(scroll_view)
        return main

    def show_shortcuts(self):
        builder = Gtk.Builder.new_from_file('src/ui/shortcuts.ui')
        shortcuts = builder.get_object('shortcuts')
        shortcuts.present()

    def show_preferences(self):
        # TODO
        pass

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
            # TODO
            pass
        elif name == 'preferences':
            self.show_preferences()
        elif name == 'about':
            self.show_about()

    def on_button_clicked(self, widget):
        """ callback for buttom clicked """
        pass


class Application(Gtk.Application):
    """ Main Aplication class """

    def __init__(self):
        super().__init__(application_id='de.haigruppe.summarizer')

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
