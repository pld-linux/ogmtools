Summary:	Programs to handle audio and video in ogg stream
Summary(pl):	Programy do obs³ugi audio i video w strumieniu ogg
Name:		ogmtools
Version:	0.950
Release:	1
License:	GPL
Group:		Applications
Source0:	http://www.bunkus.org/videotools/%{name}/%{name}-%{version}.tar.bz2
URL:		http://www.bunkus.org/videotools/ogmtools/
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libdvdread-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OGM (Ogg Media) is a video format created on Windows. It is Ogg stream with
with video stream like those usually found in AVI file (like DivX3, DivX4,
XviD etc) and several audio (usually Vorbis) and subtitle streams. ogmtools
allow creation and extraction, as well as provide information about such
files.

%description -l pl
OGM (Ogg Media) to format video stworzony pod systemem Windows. Jest to
zwyk³y strumieñ Ogg w którym enkapsulowane s± strumienie video identyczne z
tymi w plikach AVI (DivX3, DivX4, XviD etc) oraz kilka strumieni audio
(zwykle Vorbis) i tekstowych, zawieraj±cych napisy do filmu. ogmtools
pozwala na tworzenie, rozbieranie i uzyskiwanie informacji o plikach OGM.

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
%attr(644,root,root) %{_mandir}/man1/*
