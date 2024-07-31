%global extuuid		arcmenu@arcmenu.com
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		ArcMenu
%global giturl		https://gitlab.com/arcmenu/%{gitname}
%global srcdir		%{_builddir}/%{gitname}-%{version}/src

Name:		gnome-shell-extension-arc-menu
Version:	58
Release:	1%{?dist}
Summary:	GNOME Shell Extension - ArcMenu

License:	GPLv2+
URL:		https://extensions.gnome.org/extension/3628/arcmenu/
Source0:	 %{giturl}/-/archive/v%{version}/ArcMenu-v%{version}.zip
BuildArch:	noarch

Requires:  gnome-menus
BuildRequires:  glib2
BuildRequires:	meson

%description
Application menu for GNOME Shell

Features include: various menu layouts, built in GNOME search, quick access to system shortcuts, and much more!

Common solutions for ERROR message:
 - Restart your GNOME session after updating ArcMenu.

General Help:
 - Visit https://gitlab.com/arcmenu/ArcMenu/-/wikis/home

Please report all bugs or issues at https://gitlab.com/arcmenu/ArcMenu

%prep
%autosetup -n %{gitname}-v%{version}

%build
%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{extuuid}
mkdir -p %{buildroot}/usr/share/licenses/%{NAME}
cp COPYING %{buildroot}/usr/share/licenses/%{NAME}
cp -ar * %{buildroot}%{_datadir}/gnome-shell/extensions/%{extuuid}

%files
%license COPYING
%{extdir}

%changelog
* Tue Jul 30 2024 PizzaLovingNerd
- Extension
