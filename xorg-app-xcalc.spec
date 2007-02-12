Summary:	xcalc application
Summary(pl.UTF-8):   Aplikacja xcalc
Name:		xorg-app-xcalc
Version:	1.0.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xcalc-%{version}.tar.bz2
# Source0-md5:	07b948cf671fde88df1a59bfb0cab3b8
Source1:	xcalc.desktop
Source2:	xcalc.png
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-util-util-macros >= 0.99.2
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xcalc application.

%description -l pl.UTF-8
Aplikacja xcalc.

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_bindir}/xcalc
%{_datadir}/X11/app-defaults/XCalc*
%{_desktopdir}/xcalc.desktop
%{_pixmapsdir}/xcalc.png
%{_mandir}/man1/xcalc.1x*