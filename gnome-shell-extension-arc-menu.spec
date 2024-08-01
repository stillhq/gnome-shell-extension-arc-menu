%global extuuid		arcmenu@arcmenu.com
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		ArcMenu
%global giturl		https://gitlab.com/arcmenu/%{gitname}
%global srcdir		%{_builddir}/%{gitname}-%{version}/src

Name:		gnome-shell-extension-arc-menu
Version:	58
Release:	2%{?dist}
Summary:	GNOME Shell Extension - ArcMenu

License:	GPLv2+
URL:		https://extensions.gnome.org/extension/3628/arcmenu/
Source0:	 %{giturl}/-/archive/v%{version}/ArcMenu-v%{version}.zip
BuildArch:	noarch

Requires:  gnome-menus

BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  glib2

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
%make_build

%install
%make_install

mkdir -p %{_datadir}/glib-2.0/schemas
cp -a %{buildroot}%{extdir}/schemas/org.gnome.shell.extensions.arcmenu.gschema.xml %{buildroot}%{_datadir}/glib-2.0/schemas
cp COPYING %{buildroot}/usr/share/licenses/%{NAME}

%postun
if [ $1 -eq 0 ] ; then
  %{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
  %{_bindir}/glib-compile-schemas %{extdir}/schemas &> /dev/null || :
fi

%posttrans
%{_bindir}/glib-compile-schemas %{gschemadir} &> /dev/null || :
%{_bindir}/glib-compile-schemas %{extdir}/schemas &> /dev/null || :

%files
%license COPYING
%{extdir}
%{_datadir}/glib-2.0/schemas/org.gnome.shell.extensions.arcmenu.gschema.xml

%changelog
* Wed Jul 31 2024 Cameron Knauff
- Switched to using MAKE

* Tue Jul 30 2024 Cameron Knauff
- Extension
