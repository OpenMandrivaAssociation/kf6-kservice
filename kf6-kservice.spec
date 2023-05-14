%define libname %mklibname KF6Service
%define devname %mklibname KF6Service -d
%define git 20230513

Name: kf6-kservice
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kservice/-/archive/master/kservice-master.tar.bz2#/kservice-%{git}.tar.bz2
Summary: KService allows to query information about installed applications and their associated file types
URL: https://invent.kde.org/frameworks/kservice
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6DocTools)
Requires: %{libname} = %{EVRD}

%description
KService allows to query information about installed applications and their associated file types

%package -n %{libname}
Summary: KService allows to query information about installed applications and their associated file types
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KService allows to query information about installed applications and their associated file types

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

KService allows to query information about installed applications and their associated file types

%prep
%autosetup -p1 -n kservice-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

# Some translations still use old filenames...
for i in %{buildroot}%{_mandir}/*/kbuildsycoca5* %{buildroot}%{_mandir}/*/*/kbuildsycoca5*; do
	mv $i ${i/sycoca5/sycoca6}
done

%find_lang %{name} --all-name --with-qt --with-html --with-man

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kservice.*
%{_sysconfdir}/xdg/menus/applications.menu
%{_bindir}/kbuildsycoca6
%{_mandir}/man8/kbuildsycoca6.8*

%files -n %{devname}
%{_includedir}/KF6/KService
%{_libdir}/cmake/KF6Service
%{_qtdir}/mkspecs/modules/qt_KService.pri
%{_qtdir}/doc/KF6Service.*

%files -n %{libname}
%{_libdir}/libKF6Service.so*
