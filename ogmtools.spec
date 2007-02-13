Summary:	Programs to handle audio and video in Ogg stream
Summary(pl.UTF-8):	Programy do obsługi audio i video w strumieniu Ogg
Name:		ogmtools
Version:	1.5
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.bunkus.org/videotools/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	02d356e3d21d53b1d9715bab223d8996
URL:		http://www.bunkus.org/videotools/ogmtools/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdvdread-devel
BuildRequires:	libogg-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OGM (Ogg Media) is a video format created on Windows. It is Ogg stream
with with video stream like those usually found in AVI file (like
DivX3, DivX4, XviD etc) and several audio (usually Vorbis) and
subtitle streams. ogmtools allow creation and extraction, as well as
provide information about such files.

%description -l pl.UTF-8
OGM (Ogg Media) to format video stworzony pod systemem Windows. Jest
to zwykły strumień Ogg w którym enkapsulowane są strumienie video
identyczne z tymi w plikach AVI (DivX3, DivX4, XviD etc) oraz kilka
strumieni audio (zwykle Vorbis) i tekstowych, zawierających napisy do
filmu. ogmtools pozwala na tworzenie, rozbieranie i uzyskiwanie
informacji o plikach OGM.

%prep
%setup -q

%build
rm -rf autom4te.cache
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
%{_mandir}/man1/*
