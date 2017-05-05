#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rpcbind
Version  : 0.2.4
Release  : 10
URL      : http://downloads.sourceforge.net/project/rpcbind/rpcbind/0.2.4/rpcbind-0.2.4.tar.bz2
Source0  : http://downloads.sourceforge.net/project/rpcbind/rpcbind/0.2.4/rpcbind-0.2.4.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: rpcbind-bin
Requires: rpcbind-config
Requires: rpcbind-doc
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libtirpc)
Patch1: 0002-rpcbind-service-file.patch
Patch2: 0003-rpcbind-socket-file.patch
Patch3: cve-2017-8779.patch

%description
This release was a native source release from Sun.
It has been ported from FreeBSD 5.2.1 to GNU/Linux in 2004.

%package bin
Summary: bin components for the rpcbind package.
Group: Binaries
Requires: rpcbind-config

%description bin
bin components for the rpcbind package.


%package config
Summary: config components for the rpcbind package.
Group: Default

%description config
config components for the rpcbind package.


%package doc
Summary: doc components for the rpcbind package.
Group: Documentation

%description doc
doc components for the rpcbind package.


%prep
%setup -q -n rpcbind-0.2.4
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494002579
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
%configure --disable-static --enable-warmstarts --with-nss-modules="files altfiles"
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1494002579
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/sockets.target.wants
install -m644 rpcbind.service %{buildroot}/usr/lib/systemd/system/
install -m644 rpcbind.socket %{buildroot}/usr/lib/systemd/system/
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/rpcbind
/usr/bin/rpcinfo

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/rpcbind.service
/usr/lib/systemd/system/rpcbind.socket

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*
