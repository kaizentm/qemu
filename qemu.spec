Name:           qemu
Version:        10.1.50.mshv.v4
Release:        1%{?dist}
Summary:        QEMU the FAST! processor emulator

License:        GPLv2+
URL:            https://www.qemu.org
Source0:        qemu-%{version}.tar.xz


BuildRequires: gcc 
BuildRequires: make 
BuildRequires: meson 
BuildRequires: ninja-build 
BuildRequires: glib2-devel 
BuildRequires: pixman-devel 
BuildRequires: zlib-devel 
BuildRequires: libfdt-devel 
BuildRequires: libaio-devel 
BuildRequires: libiscsi-devel 
BuildRequires: liburing-devel 
BuildRequires: libseccomp-devel 
BuildRequires: libcap-ng-devel 
BuildRequires: nettle-devel 
BuildRequires: gnutls-devel 
BuildRequires: libgcrypt-devel 
BuildRequires: numactl-devel 
BuildRequires: libxml2-devel 
BuildRequires: usbredir-devel 
BuildRequires: libusb1-devel 
BuildRequires: libepoxy-devel 
BuildRequires: libattr-devel 
BuildRequires: python3 
BuildRequires: python3-setuptools 
BuildRequires: python3-tomli 
BuildRequires: pkgconfig 
BuildRequires: bzip2 
BuildRequires: xz 
BuildRequires: findutils


BuildArch:      x86_64

%description
Packaging the latest (at time of writing) version of qemu that is not available from Red Hat repository

%prep
%setup -q -n %{name}-%{version}

%global __strip /usr/bin/true




%build
./configure \
  --prefix=/usr \
  --libdir=%{_libdir} \
  --target-list=x86_64-softmmu \
  --enable-mshv \
  --disable-gtk \
  --disable-xen \
  --disable-vnc-jpeg \
  --enable-libiscsi
make -j%{?_smp_build_ncpus}

%install
export DESTDIR=$RPM_BUILD_ROOT
make install

%clean
rm -rf $RPM_BUILD_ROOT

# --- Files sections ---

%files
%license COPYING COPYING.LIB
%doc README.rst
%{_bindir}/qemu-system-x86_64
%{_bindir}/qemu-img
%{_bindir}/qemu-nbd
%{_bindir}/qemu-pr-helper
%{_bindir}/qemu-storage-daemon
%{_bindir}/qemu-io
%{_bindir}/qemu-ga
%{_bindir}/qemu-edid
%{_bindir}/qemu-keymap
%{_bindir}/qemu-vmsr-helper
%{_libexecdir}/qemu-bridge-helper
%{_datadir}/qemu
%{_mandir}/man1/qemu*.1*
%{_mandir}/man7/qemu*.7*
%{_mandir}/man8/qemu*.8*



%doc

%changelog
