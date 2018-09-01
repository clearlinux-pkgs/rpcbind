#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rpcbind
Version  : 1.2.5
Release  : 15
URL      : https://sourceforge.net/projects/rpcbind/files/rpcbind/1.2.5/rpcbind-1.2.5.tar.bz2
Source0  : https://sourceforge.net/projects/rpcbind/files/rpcbind/1.2.5/rpcbind-1.2.5.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: rpcbind-bin
Requires: rpcbind-config
Requires: rpcbind-license
Requires: rpcbind-man
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
Requires: rpcbind-config
Requires: rpcbind-license
Requires: rpcbind-man

%description bin
bin components for the rpcbind package.


%package config
Summary: config components for the rpcbind package.
Group: Default

%description config
config components for the rpcbind package.


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


%prep
%setup -q -n rpcbind-1.2.5
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535841947
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static --enable-warmstarts --with-nss-modules="files altfiles"
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1535841947
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/rpcbind
cp COPYING %{buildroot}/usr/share/doc/rpcbind/COPYING
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

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/rpcbind.service
/usr/lib/systemd/system/rpcbind.socket

%files license
%defattr(-,root,root,-)
/usr/share/doc/rpcbind/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man8/rpcbind.8
/usr/share/man/man8/rpcinfo.8
