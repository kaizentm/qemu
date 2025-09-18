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

# --- Subpackages (minimal with Summaries) ---

%package -n qemu-kvm-core
Summary: QEMU KVM system core
%description -n qemu-kvm-core
Core KVM-enabled QEMU system binary and common modules.

%package -n qemu-img
Summary: QEMU disk image utility
%description -n qemu-img
qemu-img utility for creating and converting disk images.

%package -n qemu-kvm-device-usb-host
Summary: QEMU USB host device modules
%description -n qemu-kvm-device-usb-host
Modules enabling host USB passthrough.

%package -n qemu-kvm-device-usb-redirect
Summary: QEMU USB redirection modules
%description -n qemu-kvm-device-usb-redirect
Modules enabling USB redirection (usbredir).

%package -n qemu-kvm-device-display-virtio-gpu
Summary: QEMU virtio-gpu display modules
%description -n qemu-kvm-device-display-virtio-gpu
Virtio-GPU display device backend modules.

%package -n qemu-kvm-device-display-virtio-vga
Summary: QEMU virtio-vga display modules
%description -n qemu-kvm-device-display-virtio-vga
Virtio-VGA display device modules.

%package -n qemu-kvm-device-display-virtio-gpu-pci
Summary: QEMU virtio-gpu PCI variant modules
%description -n qemu-kvm-device-display-virtio-gpu-pci
PCI variant modules for virtio-gpu display devices.

%ifarch s390x
%package -n qemu-kvm-device-display-virtio-gpu-ccw
Summary: QEMU virtio-gpu CCW modules (s390x)
%description -n qemu-kvm-device-display-virtio-gpu-ccw
CCW transport virtio-gpu display modules for s390x.
%endif

%package -n qemu-pr-helper
Summary: QEMU persistent reservation helper
%description -n qemu-pr-helper
Helper for SCSI persistent reservations (qemu-pr-helper).




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
