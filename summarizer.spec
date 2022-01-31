Name:           summarizer
Version:        0.1.0
Release:        1%{?dist}
Summary:        A program to summarize text, I guess.

License:        GPLv3+
URL:            https://github.com/rafaelmardojai/blanket
#Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Requires:       glib2
Requires:       gtk4
Requires:       libappstream-glib
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  glib2-devel
BuildRequires:  gtk4-devel

BuildArch:      noarch

%description
A program to summarize text, I guess.


%prep
%autosetup -p1


%build
%meson
%meson_build



%install
%meson_install

%find_lang %{name}


%files -f %{name}.lang
%license LICENSING
%{_bindir}/src
%{_datadir}/src/
#%{_datadir}/applications/com.rafaelmardojai.Blanket.desktop
#%{_datadir}/glib-2.0/schemas/com.rafaelmardojai.Blanket.gschema.xml
#%{_datadir}/icons/hicolor/scalable/apps/com.rafaelmardojai.Blanket.svg
#%{_datadir}/icons/hicolor/symbolic/apps/com.rafaelmardojai.Blanket-symbolic.svg
#%{_datadir}/metainfo/com.rafaelmardojai.Blanket.metainfo.xml

%changelog

