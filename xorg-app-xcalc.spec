Summary:	xcalc application - scientific calculator for X
Summary(pl.UTF-8):	Aplikacja xcalc - kalkulator naukowy dla X
Name:		xorg-app-xcalc
Version:	1.1.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xcalc-%{version}.tar.xz
# Source0-md5:	c70f47ddd3dc661950e17b9ab36d8a87
Source1:	xcalc.desktop
Source2:	xcalc.png
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-proto-xproto-devel >= 7.0.17
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xcalc is a scientific calculator desktop accessory that can emulate a
TI-30 or an HP-10C.

%description -l pl.UTF-8
xcalc to naukowy kalkulator dostępny na pulpicie, potrafiący emulować
TI-30 lub HP-10C.

%prep
%setup -q -n xcalc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/xcalc.desktop
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/xcalc.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xcalc
%{_datadir}/X11/app-defaults/XCalc
%{_datadir}/X11/app-defaults/XCalc-color
%{_desktopdir}/xcalc.desktop
%{_pixmapsdir}/xcalc.png
%{_mandir}/man1/xcalc.1*
