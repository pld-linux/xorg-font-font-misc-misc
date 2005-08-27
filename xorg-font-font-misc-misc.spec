Summary:	misc-misc font
Summary(pl):	Font misc-misc
Name:		xorg-font-font-misc-misc
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-misc-misc-%{version}.tar.bz2
# Source0-md5:	40c631945183f130d3f8fd9012c6126e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
misc-misc font.

%description -l pl
Font misc-misc.

%prep
%setup -q -n font-misc-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/misc/*
