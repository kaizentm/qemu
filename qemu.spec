Name:           qemu
Version:        10.1.50.mshv.v4
Release:        1%{?dist}
Summary:        QEMU the FAST! processor emulator

License:        GPLv2+
URL:            https://www.qemu.org
Source0:        qemu-%{version}.tar.xz


%description
Packaging the latest (at time of writing) version of qemu that is not available from Red Hat repository

%prep
%setup -q -n %{name}-%{version}

%global __strip /usr/bin/true

# --- Subpackages (minimal) ---

%package -n qemu-kvm-core
%description -n qemu-kvm-core
Core KVM-enabled QEMU system binary and common modules.

%package -n qemu-img
%description -n qemu-img
qemu-img utility.

%package -n qemu-kvm-device-usb-host
%description -n qemu-kvm-device-usb-host
USB host passthrough modules.

%package -n qemu-kvm-device-usb-redirect
%description -n qemu-kvm-device-usb-redirect
USB redirection modules.

%package -n qemu-kvm-device-display-virtio-gpu
%description -n qemu-kvm-device-display-virtio-gpu
Virtio-GPU display modules.

%package -n qemu-kvm-device-display-virtio-vga
%description -n qemu-kvm-device-display-virtio-vga
Virtio-VGA display modules.

%package -n qemu-kvm-device-display-virtio-gpu-pci
%description -n qemu-kvm-device-display-virtio-gpu-pci
Virtio-GPU PCI variant modules.

%ifarch s390x
%package -n qemu-kvm-device-display-virtio-gpu-ccw
%description -n qemu-kvm-device-display-virtio-gpu-ccw
Virtio-GPU CCW display modules (s390x).
%endif

# Optional (only if you build it):
%package -n qemu-pr-helper
%description -n qemu-pr-helper
Persistent reservation helper.



%build
./configure \
    --target-list=x86_64-softmmu \
    --disable-xen \
    --disable-vnc-jpeg \
    --enable-mshv \
    --disable-gtk
cd build
make -j

%install
export DESTDIR=$RPM_BUILD_ROOT
make install

%clean
rm -rf $RPM_BUILD_ROOT

# --- Files sections ---

%global qemu_moddir %{_libdir}/qemu

%files -n qemu-kvm-core
%license COPYING
%doc README* LICENSE*  # Adjust if present
%{_bindir}/qemu-system-x86_64
%dir %{qemu_moddir}
%{qemu_moddir}/*.so
%exclude %{qemu_moddir}/*usb*host*.so
%exclude %{qemu_moddir}/*usb*redir*.so
%exclude %{qemu_moddir}/*virtio-gpu*pci*.so
%exclude %{qemu_moddir}/*virtio-gpu-ccw*.so
%exclude %{qemu_moddir}/*virtio-gpu*.so
%exclude %{qemu_moddir}/*virtio-vga*.so

%files -n qemu-img
%{_bindir}/qemu-img

%files -n qemu-kvm-device-usb-host
%{qemu_moddir}/*usb*host*.so

%files -n qemu-kvm-device-usb-redirect
%{qemu_moddir}/*usb*redir*.so

%files -n qemu-kvm-device-display-virtio-gpu
%exclude %{qemu_moddir}/*virtio-gpu*pci*.so
%exclude %{qemu_moddir}/*virtio-gpu-ccw*.so
%{qemu_moddir}/*virtio-gpu*.so

%files -n qemu-kvm-device-display-virtio-vga
%{qemu_moddir}/*virtio-vga*.so

%files -n qemu-kvm-device-display-virtio-gpu-pci
%{qemu_moddir}/*virtio-gpu*pci*.so

%ifarch s390x
%files -n qemu-kvm-device-display-virtio-gpu-ccw
%{qemu_moddir}/*virtio-gpu-ccw*.so
%endif

%files -n qemu-pr-helper
%{_bindir}/qemu-pr-helper


%doc

%changelog
