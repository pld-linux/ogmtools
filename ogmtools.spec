Summary:	Programs to handle audio and video in ogg stream
Summary(pl):	Programy do obs³ugi audio i video w strumieniu ogg
Name:		ogmtools
Version:	0.8
Release:	0
License:	GPL
Group:		Applications
Source0:	http://www.bunkus.org/videotools/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.bunkus.org/videotools/ogmtools/
BuildRequires:	transcode-avilib
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q

%build

./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
