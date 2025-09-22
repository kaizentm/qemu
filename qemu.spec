Name:           qemu
Version:        10.1.50.mshv.v4
Release:        1%{?dist}
Summary:        Custom QEMU with MSHV support
License:        GPLv2 and LGPLv2+
Source0:        qemu-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  glib2-devel
BuildRequires:  pixman-devel
BuildRequires:  zlib-devel
BuildRequires:  libfdt-devel
BuildRequires:  libaio-devel
BuildRequires:  libiscsi-devel
BuildRequires:  liburing-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  nettle-devel
BuildRequires:  gnutls-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  numactl-devel
BuildRequires:  libxml2-devel
BuildRequires:  usbredir-devel
BuildRequires:  libusb1-devel
BuildRequires:  libepoxy-devel
BuildRequires:  libattr-devel
BuildRequires:  python3
BuildRequires:  python3-setuptools
BuildRequires:  python3-tomli
BuildRequires:  pkgconfig
BuildRequires:  bzip2
BuildRequires:  xz
BuildRequires:  findutils

%description
Custom QEMU build with MSHV support.

%prep
%autosetup -p1

%build
meson setup build --prefix=%{_prefix} --libdir=%{_libdir} -Dlibiscsi=enabled
ninja -C build

%install
DESTDIR=%{buildroot} ninja -C build install


%files
%license COPYING COPYING.LIB
%doc README.rst
%{_bindir}/qemu-system-x86_64
%{_bindir}/qemu-img
%{_bindir}/qemu-nbd
%{_libexecdir}/qemu-bridge-helper
%{_datadir}/qemu/*