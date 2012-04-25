Name:		kxstitch
Version:	0.9.0
Release:	1
Summary:	Creation and editing of cross stitch patterns
Source0:	http://downloads.sourceforge.net/project/kxstitch/%{name}/%{version}/%{name}-%{version}-KDE4.tar.gz
Patch0:		kxstitch-0.9.0-mdv-linkage.patch
License:	GPLv2+
Group:		Graphics
URL:		http://kxstitch.sourceforge.net/
BuildRequires:	cmake
BuildRequires:	kdelibs4-devel
BuildRequires:	imagemagick-devel

%description
Kxstitch is a program that lets you create cross stitch patterns and charts.
Patterns can be created from scratch on a user defined size of grid, which can
be enlarged or reduced in size as your pattern progresses.  Alternatively you
can import images from many graphics formats or use an image as a background. 
You can also scan images using any Sane supported scanner.
These imported images can then be modified using the supplied tools to produce
your final design.

%prep
%setup -q -n %{name}-%{version}-KDE4
%patch0 -p1

%build
%cmake
%make

%install
pushd build
%makeinstall_std
popd

%find_lang %{name}

%files -f %{name}.lang
%attr(0755,root,root) %{_bindir}/%{name}
%defattr(0644,root,root,0755)
%{_datadir}/icons/*/*/apps/*.png
%{_datadir}/apps/%{name}
%{_datadir}/doc/HTML/en/*
%{_mandir}/man?/%{name}.?*
%{_kde_applicationsdir}/kxstitch.desktop
%{_datadir}/config.kcfg/kxstitch.kcfg
%{_datadir}/mime/packages/kxstitch.xml
