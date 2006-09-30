Summary:	A git GUI viewer built on Qt
Name:		qgit
Version:	1.5.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qgit/%{name}-%{version}.tar.bz2
# Source0-md5:	251568da2d93b0e621ea7a2cb7de611d
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
