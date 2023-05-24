Name:           ukui-settings-daemon
Version:        3.1.1.1
Release:        1
License:        GPL-3.0+
Summary:        The daemon of UKUI desktop
Url:            https://github.com/ukui/ukui-settings-daemon
Group:          System/GUI/Other
Source0:        https://github.com/ukui/ukui-settings-daemon/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  fdupes
BuildRequires:  qmake5
BuildRequires:  qt5-linguist
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  cmake(KF5Config)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(libxklavier)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-gobject)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libmatemixer)
BuildRequires:  pkgconfig(mate-desktop-2.0)
BuildRequires:  pkgconfig(libmatekbd)
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(dbus-glib-1)

BuildRequires:  lib64ukui-interface-devel

%description
ukui-settings-daemon is the daemon of UKUI desktop, its function is to set
sessions and manage applications running for UKUI desktop.

%prep
%autosetup -p1

sed -i 's|#include <ukuisdk/kylin-com4cxx.h>|#include <kylin-com4cxx.h>|' common/usd_base_class.h
%build
export CC=gcc
export CXX=g++
%qmake_qt5
%make_build
  
%install
%make_install

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}     
%{_datadir}/dbus-1/services/org.ukui.SettingsDaemon.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_sysconfdir}/xdg/autostart/%{name}.desktop
