Summary:	A git GUI viewer built on Qt
Summary(pl.UTF-8):	Graficzna przeglądarka repozytorium git oparta o Qt
Name:		qgit
Version:	1.5.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qgit/%{name}-%{version}.tar.bz2
# Source0-md5:	4b9615c16af04fcb21cf0cd0a5bbb986
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

%description -l pl.UTF-8
QGit to graficzna przeglądarka repozytorium git oparta na Qt/C++. Przy
jej użyciu można przeglądać historię zmian, oglądać zawartość łat i
zmienione pliki, graficznie przechodząc po różnych gałęziach rozwoju.

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
