Summary:	A git GUI viewer built on Qt
Summary(pl):	Graficzna przegl±darka repozytorium git oparta o Qt
Name:		qgit
Version:	1.5.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qgit/%{name}-%{version}.tar.bz2
# Source0-md5:	c1420385dc18716f0ab538756e7e2476
Source1:	%{name}.desktop
URL:		http://digilander.libero.it/mcostalba/
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	git-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QGit is a git GUI viewer built on Qt/C++. With qgit you will be able
to browse revisions history, view patch content and changed files,
graphically following different development branches.

%description -l pl
QGit to graficzna przegl±darka repozytorium git oparta na Qt/C++. Przy
jej u¿yciu mo¿na przegl±daæ historiê zmian, ogl±daæ zawarto¶æ ³at i
zmienione pliki, graficznie przechodz±c po ró¿nych ga³êziach rozwoju.

%prep
%setup -q

%build
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--with-qt-includes=%{_includedir}/qt \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
