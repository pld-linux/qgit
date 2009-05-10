Summary:	A git GUI viewer built on Qt
Summary(pl.UTF-8):	Graficzna przeglądarka repozytorium git oparta o Qt
Name:		qgit
Version:	2.3
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/qgit/%{name}-%{version}.tar.bz2
# Source0-md5:	1f6cd60cc1b92973718b108d542e3270
Source1:	%{name}.desktop
URL:		http://digilander.libero.it/mcostalba/
BuildRequires:  QtCore-devel
BuildRequires:  QtGui-devel
BuildRequires:  qt4-build >= 4.3.3-3
BuildRequires:  qt4-qmake >= 4.3.3-3
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	git-core >= 1.5.3
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
%setup -q -n %{name}

%build
qmake-qt4 qgit.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}}

install bin/qgit $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
