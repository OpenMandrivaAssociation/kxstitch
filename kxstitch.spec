Name:		kxstitch
Version:	0.9.0
Release:	2
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


%changelog
* Wed Apr 25 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.9.0-1
+ Revision: 793374
- imported package kxstitch



* Thu Aug 31 2006 Couriousous <couriousous@mandriva.org> 0.8-1mdv2007.0
- 0.8

* Thu Aug 17 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.7-7mdv2007.0
- Rebuild against new dbus

* Thu Jul 06 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.7-6mdv2007.0
- Rebuild for new menu && extension

* Fri Mar 17 2006 Couriousous <couriousous@mandriva.org> 0.7-5mdk
- Rebuild

* Sat Jan 14 2006 Couriousous <couriousous@mandriva.org> 0.7-4mdk
- Rebuild

* Wed Aug 24 2005 Oden Eriksson <oeriksson@mandriva.com> 0.7-3mdk
- rebuilt against new Magick libs

* Sun Jul 31 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.7-2mdk
- Fix BuildRequires

* Fri Jul 15 2005 Couriousous <couriousous@mandriva.org> 0.7-1mdk
- 0.7

* Fri Mar 25 2005 Couriousous <couriousous@mandrake.org> 0.6-2mdk
- Rebuild

* Sun Jan 2 2005 Couriousous <couriousous@mandrake.org> 0.6-1mdk
- First Mandrakelinux package
