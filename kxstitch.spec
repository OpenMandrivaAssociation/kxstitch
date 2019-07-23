Name:		kxstitch
Summary:	Program to create cross stitch patterns
Version:	2.2.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
URL:		https://www.kde.org/applications/graphics/kxstitch/
Source0:	https://download.kde.org/stable/kxstitch/%{version}/%{name}-%{version}.tar.xz
BuildRequires:	doxygen
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5TextWidgets)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5X11Extras)
BuildRequires:	pkgconfig(MagickCore)
BuildRequires:	pkgconfig(shared-mime-info)
BuildRequires:	pkgconfig(x11)
Recommends:	%{name}-handbook

%description
KXStitch is a program that lets you create cross stitch patterns and charts.

%files -f %{name}.lang
%{_kde5_bindir}/%{name}
%{_kde5_applicationsdir}/org.kde.%{name}.desktop
%{_kde5_datadir}/metainfo/org.kde.%{name}.appdata.xml
%{_kde5_datadir}/%{name}/
%{_kde5_iconsdir}/*/*/apps/%{name}.png
%{_kde5_iconsdir}/*/*/actions/%{name}*.png
%{_kde5_iconsdir}/hicolor/scalable/apps/%{name}.svgz
%{_kde5_mandir}/man?/%{name}.*
%{_kde5_datadir}/kxmlgui5/%{name}/
%{_kde5_datadir}/config.kcfg/%{name}.kcfg

#------------------------------------------------------------------------------

%package handbook
Summary:	KXStitch handbook
Group:		Documentation
BuildArch:	noarch
Requires:	%{name} >= %{version}-%{release}

%description handbook
This package provides the KXStitch handbook.

%files handbook
%doc %{_kde5_docdir}/HTML/*/%{name}/

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

%find_lang %{name} --with-man

