Summary:	Fixed bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe o stałej szerokości
Name:		xorg-font-font-misc-misc
Version:	1.1.0
Release:	2
License:	Public Domain
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/individual/font/font-misc-misc-%{version}.tar.bz2
# Source0-md5:	878bfd4e9f14c1279cea3a8392e0dbdd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	perl-base
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.1.1
BuildRequires:	xorg-util-util-macros >= 1.3
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
# contains useful aliases for these fonts
Requires:	xorg-font-font-alias >= 1.0.1-1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Fixed bitmap fonts. Main package contains Unicode fonts, Japanese k14
font and nil2 font.

%description -l pl.UTF-8
Fonty bitmapowe o stałej szerokości znaków (fixed). Główny pakiet
zawiera fonty unikodowe, japoński font k14 i font nil2.

%package base
Summary:	Base font (fixed)
Summary(pl.UTF-8):	Podstawowy font (fixed)
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires(triggerpostun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
# contains useful aliases for these fonts
Requires:	xorg-font-font-alias >= 1.0.1-1
Obsoletes:	XFree86-fonts-base <= 1:7.0.0

%description base
Base font (fixed) needed to start X server.

%description base -l pl.UTF-8
Podstawowy font (fixed) niezbędny do uruchomienia serwera X.

%package ISO8859-1
Summary:	ISO-8859-1 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-1
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
# contains useful aliases for these fonts
Requires:	xorg-font-font-alias >= 1.0.1-1
Requires:	%{name}-base = %{version}-%{release}
Obsoletes:	XFree86-fonts-ISO8859-1 < 1:7.0.0

%description ISO8859-1
ISO-8859-1 basic raster fonts.

%description ISO8859-1 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-1.

%package ISO8859-2
Summary:	ISO-8859-2 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-2
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-2 < 1:7.0.0

%description ISO8859-2
ISO-8859-2 basic raster fonts.

%description ISO8859-2 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-2.

%package ISO8859-3
Summary:	ISO-8859-3 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-3
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-3 < 1:7.0.0

%description ISO8859-3
ISO-8859-3 basic raster fonts.

%description ISO8859-3 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-3.

%package ISO8859-4
Summary:	ISO-8859-4 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-4
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-4 < 1:7.0.0

%description ISO8859-4
ISO-8859-4 basic raster fonts.

%description ISO8859-4 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-4.

%package ISO8859-5
Summary:	ISO-8859-5 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-5
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-5 < 1:7.0.0

%description ISO8859-5
Basic ISO-8859-5 raster fonts.

%description ISO8859-5 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-5.

%package ISO8859-7
Summary:	ISO-8859-7 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-7
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-7 < 1:7.0.0

%description ISO8859-7
ISO-8859-7 basic raster fonts.

%description ISO8859-7 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-7.

%package ISO8859-8
Summary:	ISO-8859-8 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-8
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-8 < 1:7.0.0

%description ISO8859-8
ISO-8859-8 basic raster fonts.

%description ISO8859-8 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-8.

%package ISO8859-9
Summary:	ISO-8859-9 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-9
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-9 < 1:7.0.0

%description ISO8859-9
ISO-8859-9 basic raster fonts.

%description ISO8859-9 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-9.

%package ISO8859-10
Summary:	ISO-8859-10 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-10
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-10 < 1:7.0.0

%description ISO8859-10
ISO-8859-10 basic raster fonts.

%description ISO8859-10 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-10.

%package ISO8859-11
Summary:	ISO-8859-11 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-11
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-11 < 1:7.0.0

%description ISO8859-11
ISO-8859-11 basic raster fonts.

%description ISO8859-11 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-11.

%package ISO8859-13
Summary:	ISO-8859-13 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-13
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-13 < 1:7.0.0

%description ISO8859-13
ISO-8859-13 basic raster fonts.

%description ISO8859-13 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-13.

%package ISO8859-14
Summary:	ISO-8859-14 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-14
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-14 < 1:7.0.0

%description ISO8859-14
ISO-8859-14 basic raster fonts.

%description ISO8859-14 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-14.

%package ISO8859-15
Summary:	ISO-8859-15 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-15
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-15 < 1:7.0.0

%description ISO8859-15
ISO-8859-15 basic raster fonts.

%description ISO8859-15 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-15.

%package ISO8859-16
Summary:	ISO-8859-16 basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe ISO-8859-16
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-ISO8859-16 < 1:7.0.0

%description ISO8859-16
ISO-8859-16 basic raster fonts.

%description ISO8859-16 -l pl.UTF-8
Podstawowe fonty rastrowe ISO-8859-16.

%package KOI8-R
Summary:	KOI8-R basic raster fonts
Summary(pl.UTF-8):	Podstawowe fonty rastrowe KOI8-R
Group:		Fonts
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
Requires:	fontpostinst
Obsoletes:	XFree86-fonts-KOI8-R < 1:7.0.0
Conflicts:	xorg-font-font-misc-misc <= 1.1.0-1

%description KOI8-R
KOI8-R basic raster fonts.

%description KOI8-R -l pl.UTF-8
Podstawowe fonty rastrowe KOI8-R.

%prep
%setup -q -n font-misc-misc-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--build=%{_host} \
	--host=%{_host} \
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

%post KOI8-R
fontpostinst misc

%postun KOI8-R
fontpostinst misc

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%{_fontsdir}/misc/4x6.pcf.gz
%{_fontsdir}/misc/5x7.pcf.gz
%{_fontsdir}/misc/5x8.pcf.gz
%{_fontsdir}/misc/6x9.pcf.gz
%{_fontsdir}/misc/6x10.pcf.gz
%{_fontsdir}/misc/6x12.pcf.gz
%{_fontsdir}/misc/6x13.pcf.gz
%{_fontsdir}/misc/6x13[BO].pcf.gz
%{_fontsdir}/misc/7x13.pcf.gz
%{_fontsdir}/misc/7x13[BO].pcf.gz
%{_fontsdir}/misc/7x14.pcf.gz
%{_fontsdir}/misc/7x14-JISX0201.1976-0.pcf.gz
%{_fontsdir}/misc/7x14B.pcf.gz
%{_fontsdir}/misc/8x13.pcf.gz
%{_fontsdir}/misc/8x13[BO].pcf.gz
%{_fontsdir}/misc/9x15.pcf.gz
%{_fontsdir}/misc/9x15B.pcf.gz
%{_fontsdir}/misc/9x18.pcf.gz
%{_fontsdir}/misc/9x18B.pcf.gz
%{_fontsdir}/misc/10x20.pcf.gz
%{_fontsdir}/misc/12x13ja.pcf.gz
%{_fontsdir}/misc/18x18ja.pcf.gz
%{_fontsdir}/misc/18x18ko.pcf.gz
%{_fontsdir}/misc/k14.pcf.gz
%{_fontsdir}/misc/nil2.pcf.gz

%files base
%defattr(644,root,root,755)
%{_fontsdir}/misc/6x13-ISO8859-1.pcf.gz
%ghost %{_fontsdir}/misc/fonts.dir

%files ISO8859-1
%defattr(644,root,root,755)
%{_fontsdir}/misc/[45]x*-ISO8859-1.pcf.gz
%{_fontsdir}/misc/6x9-ISO8859-1.pcf.gz
%{_fontsdir}/misc/6x10-ISO8859-1.pcf.gz
%{_fontsdir}/misc/6x12-ISO8859-1.pcf.gz
%{_fontsdir}/misc/6x13[BO]-ISO8859-1.pcf.gz
%{_fontsdir}/misc/[789]x*-ISO8859-1.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-1.pcf.gz

%files ISO8859-2
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-2.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-2.pcf.gz

%files ISO8859-3
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-3.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-3.pcf.gz

%files ISO8859-4
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-4.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-4.pcf.gz

%files ISO8859-5
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-5.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-5.pcf.gz

%files ISO8859-7
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-7.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-7.pcf.gz

%files ISO8859-8
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-8.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-8.pcf.gz

%files ISO8859-9
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-9.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-9.pcf.gz

%files ISO8859-10
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-10.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-10.pcf.gz

%files ISO8859-11
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-11.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-11.pcf.gz

%files ISO8859-13
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-13.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-13.pcf.gz

%files ISO8859-14
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-14.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-14.pcf.gz

%files ISO8859-15
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-15.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-15.pcf.gz

%files ISO8859-16
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-ISO8859-16.pcf.gz
%{_fontsdir}/misc/10x20-ISO8859-16.pcf.gz

%files KOI8-R
%defattr(644,root,root,755)
%{_fontsdir}/misc/[456789]x*-KOI8-R.pcf.gz
%{_fontsdir}/misc/10x20-KOI8-R.pcf.gz
