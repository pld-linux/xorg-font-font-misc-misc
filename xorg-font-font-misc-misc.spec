Summary:	misc-misc fonts
Summary(pl):	Fonty misc-misc
Name:		xorg-font-font-misc-misc
Version:	1.0.0
Release:	0.2
License:	Public Domain
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/font/font-misc-misc-%{version}.tar.bz2
# Source0-md5:	2a57f6188c41d4bc1b88ca3d08ad011d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 0.99.2
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
misc-misc fonts.

%description -l pl
Fonty misc-misc.

%package base
Summary:	Base fonts (fixed)
Summary(pl):	Podstawowe fonty (fixed)
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires(triggerpostun):	fontpostinst
Requires:	fontpostinst
Provides:	XFree86-fonts-base = %{version}-%{release}
Obsoletes:	XFree86-fonts-base

%description base
Base fonts (fixed) needed to start X server.

%description base -l pl
Podstawowe fonty (fixed) niezbêdne do uruchomienia X serwera.

%package ISO8859-1
Summary:	ISO-8859-1 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-1
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-1 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-1

%description ISO8859-1
ISO-8859-1 basic raster fonts.

%description ISO8859-1 -l pl
Podstawowe fonty rastrowe ISO-8859-1.

%package ISO8859-2
Summary:	ISO-8859-2 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-2
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-2 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-2

%description ISO8859-2
ISO-8859-2 basic raster fonts.

%description ISO8859-2 -l pl
Podstawowe fonty rastrowe ISO-8859-2.

%package ISO8859-3
Summary:	ISO-8859-3 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-3
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-3 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-3

%description ISO8859-3
ISO-8859-3 basic raster fonts.

%description ISO8859-3 -l pl
Podstawowe fonty rastrowe ISO-8859-3.

%package ISO8859-4
Summary:	ISO-8859-4 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-4
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-4 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-4

%description ISO8859-4
ISO-8859-4 basic raster fonts.

%description ISO8859-4 -l pl
Podstawowe fonty rastrowe ISO-8859-4.

%package ISO8859-5
Summary:	ISO-8859-5 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-5
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-5 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-5

%description ISO8859-5
Basic ISO-8859-5 raster fonts.

%description ISO8859-5 -l pl
Podstawowe fonty rastrowe ISO-8859-5.

%package ISO8859-6
Summary:	ISO-8859-6 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-6
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-6 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-6

%description ISO8859-6
ISO-8859-6 basic raster fonts.

%description ISO8859-6 -l pl
Podstawowe fonty rastrowe ISO-8859-6.

%package ISO8859-7
Summary:	ISO-8859-7 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-7
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-7 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-7

%description ISO8859-7
ISO-8859-7 basic raster fonts.

%description ISO8859-7 -l pl
Podstawowe fonty rastrowe ISO-8859-7.

%package ISO8859-8
Summary:	ISO-8859-8 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-8
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-8 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-8

%description ISO8859-8
ISO-8859-8 basic raster fonts.

%description ISO8859-8 -l pl
Podstawowe fonty rastrowe ISO-8859-8.

%package ISO8859-9
Summary:	ISO-8859-9 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-9
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-9 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-9

%description ISO8859-9
ISO-8859-9 basic raster fonts.

%description ISO8859-9 -l pl
Podstawowe fonty rastrowe ISO-8859-9.

%package ISO8859-10
Summary:	ISO-8859-10 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-10
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-10 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-10

%description ISO8859-10
ISO-8859-10 basic raster fonts.

%description ISO8859-10 -l pl
Podstawowe fonty rastrowe ISO-8859-10.

%package ISO8859-11
Summary:	ISO-8859-11 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-11
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-11 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-11

%description ISO8859-11
ISO-8859-11 basic raster fonts.

%description ISO8859-11 -l pl
Podstawowe fonty rastrowe ISO-8859-11.

%package ISO8859-12
Summary:	ISO-8859-12 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-12
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-12 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-12

%description ISO8859-12
ISO-8859-12 basic raster fonts.

%description ISO8859-12 -l pl
Podstawowe fonty rastrowe ISO-8859-12.

%package ISO8859-13
Summary:	ISO-8859-13 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-13
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-13 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-13

%description ISO8859-13
ISO-8859-13 basic raster fonts.

%description ISO8859-13 -l pl
Podstawowe fonty rastrowe ISO-8859-13.

%package ISO8859-14
Summary:	ISO-8859-14 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-14
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-14 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-14

%description ISO8859-14
ISO-8859-14 basic raster fonts.

%description ISO8859-14 -l pl
Podstawowe fonty rastrowe ISO-8859-14.

%package ISO8859-15
Summary:	ISO-8859-15 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-15
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-15 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-15

%description ISO8859-15
ISO-8859-15 basic raster fonts.

%description ISO8859-15 -l pl
Podstawowe fonty rastrowe ISO-8859-15.

%package ISO8859-16
Summary:	ISO-8859-16 basic raster fonts
Summary(pl):	Podstawowe fonty rastrowe ISO-8859-16
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	fontpostinst
Requires:	%{_fontsdir}/misc
Provides:	XFree86-fonts-ISO8859-16 = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-16

%description ISO8859-16
ISO-8859-16 basic raster fonts.

%description ISO8859-16 -l pl
Podstawowe fonty rastrowe ISO-8859-16.

%prep
%setup -q -n font-misc-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-fontdir=%{_fontsdir}/misc

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%post base
fontpostinst misc

%postun base
fontpostinst misc

%post ISO8859-1
fontpostinst misc

%postun ISO8859-1
fontpostinst misc

%post ISO8859-2
fontpostinst misc

%postun ISO8859-2
fontpostinst misc

%post ISO8859-3
fontpostinst misc

%postun ISO8859-3
fontpostinst misc

%post ISO8859-4
fontpostinst misc

%postun ISO8859-4
fontpostinst misc

%post ISO8859-5
fontpostinst misc

%postun ISO8859-5
fontpostinst misc

%post ISO8859-6
fontpostinst misc

%postun ISO8859-6
fontpostinst misc

%post ISO8859-7
fontpostinst misc

%postun ISO8859-7
fontpostinst misc

%post ISO8859-8
fontpostinst misc

%postun ISO8859-8
fontpostinst misc

%post ISO8859-9
fontpostinst misc

%postun ISO8859-9
fontpostinst misc

%post ISO8859-10
fontpostinst misc

%postun ISO8859-10
fontpostinst misc

%post ISO8859-11
fontpostinst misc

%postun ISO8859-11
fontpostinst misc

%post ISO8859-12
fontpostinst misc

%postun ISO8859-12
fontpostinst misc

%post ISO8859-13
fontpostinst misc

%postun ISO8859-13
fontpostinst misc

%post ISO8859-14
fontpostinst misc

%postun ISO8859-14
fontpostinst misc

%post ISO8859-15
fontpostinst misc

%postun ISO8859-15
fontpostinst misc

%post ISO8859-16
fontpostinst misc

%postun ISO8859-16
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_fontsdir}/misc/*.pcf.gz
%exclude %{_fontsdir}/misc/*-ISO8859-*.pcf.gz

%files base
%defattr(644,root,root,755)
%{_fontsdir}/misc/6x13-ISO8859-1.pcf.gz
%ghost %{_fontsdir}/misc/fonts.dir

%files ISO8859-1
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-1.pcf.gz
%exclude %{_fontsdir}/misc/6x13-ISO8859-1.pcf.gz

%files ISO8859-2
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-2.pcf.gz
#%{_fontsdir}/misc/fonts.alias.%{name}-ISO8859-2

%files ISO8859-3
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-3.pcf.gz

%files ISO8859-4
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-4.pcf.gz

%files ISO8859-5
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-5.pcf.gz

#%files ISO8859-6
#%defattr(644,root,root,755)
#%%{_fontsdir}/misc/*ISO8859-6.pcf.gz

%files ISO8859-7
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-7.pcf.gz

%files ISO8859-8
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-8.pcf.gz

%files ISO8859-9
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-9.pcf.gz

%files ISO8859-10
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-10.pcf.gz

%files ISO8859-11
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-11.pcf.gz

#%files ISO8859-12
#%defattr(644,root,root,755)
#%%{_fontsdir}/misc/*ISO8859-12.pcf.gz

%files ISO8859-13
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-13.pcf.gz

%files ISO8859-14
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-14.pcf.gz

%files ISO8859-15
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-15.pcf.gz

%files ISO8859-16
%defattr(644,root,root,755)
%{_fontsdir}/misc/*ISO8859-16.pcf.gz
