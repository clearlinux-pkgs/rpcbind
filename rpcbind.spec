#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rpcbind
Version  : 1.2.6
Release  : 21
URL      : https://sourceforge.net/projects/rpcbind/files/rpcbind/1.2.6/rpcbind-1.2.6.tar.bz2
Source0  : https://sourceforge.net/projects/rpcbind/files/rpcbind/1.2.6/rpcbind-1.2.6.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: rpcbind-bin = %{version}-%{release}
Requires: rpcbind-license = %{version}-%{release}
Requires: rpcbind-man = %{version}-%{release}
Requires: rpcbind-services = %{version}-%{release}
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libtirpc)
Patch1: 0002-rpcbind-service-file.patch
Patch2: 0003-rpcbind-socket-file.patch

%description
This release was a native source release from Sun.
It has been ported from FreeBSD 5.2.1 to GNU/Linux in 2004.

%package bin
Summary: bin components for the rpcbind package.
Group: Binaries
Requires: rpcbind-license = %{version}-%{release}
Requires: rpcbind-services = %{version}-%{release}

%description bin
bin components for the rpcbind package.


%package license
Summary: license components for the rpcbind package.
Group: Default

%description license
license components for the rpcbind package.


%package man
Summary: man components for the rpcbind package.
Group: Default

%description man
man components for the rpcbind package.


%package services
Summary: services components for the rpcbind package.
Group: Systemd services

%description services
services components for the rpcbind package.


%prep
%setup -q -n rpcbind-1.2.6
cd %{_builddir}/rpcbind-1.2.6
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664911703
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --enable-warmstarts \
--with-nss-modules="files altfiles"
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1664911703
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/rpcbind
cp %{_builddir}/rpcbind-%{version}/COPYING %{buildroot}/usr/share/package-licenses/rpcbind/b104b8d9872e8a1270808da08aa5af553b080ce1 || :
%make_install
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/sockets.target.wants
install -m644 rpcbind.service %{buildroot}/usr/lib/systemd/system/
install -m644 rpcbind.socket %{buildroot}/usr/lib/systemd/system/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rpcbind
/usr/bin/rpcinfo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/rpcbind/b104b8d9872e8a1270808da08aa5af553b080ce1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/rpcbind.8
/usr/share/man/man8/rpcinfo.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/rpcbind.service
/usr/lib/systemd/system/rpcbind.socket
