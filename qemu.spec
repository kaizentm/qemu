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

############################################################
# Core runtime (system binary + generic modules)
############################################################
%package -n qemu-kvm-core
Summary: QEMU system emulator (KVM accelerated) core
Requires: glibc
# Provide a generic 'qemu-kvm' style alias if you like:
Provides: qemu-kvm = %{epoch}:%{version}-%{release}

%description -n qemu-kvm-core
Core KVM-enabled QEMU system binary and common device modules for KubeVirt.
Other device/display/USB modules are split into separate subpackages.

############################################################
# qemu-img tool
############################################################
%package -n qemu-img
Summary: QEMU disk image manager
Requires: qemu-kvm-core = %{epoch}:%{version}-%{release}

%description -n qemu-img
Standalone qemu-img utility for manipulating virtual disk images.

############################################################
# USB host passthrough
############################################################
%package -n qemu-kvm-device-usb-host
Summary: QEMU USB host passthrough device modules
Requires: qemu-kvm-core = %{epoch}:%{version}-%{release}

%description -n qemu-kvm-device-usb-host
Modules enabling host USB device passthrough.

############################################################
# USB redirection (SPICE / usbredir)
############################################################
%package -n qemu-kvm-device-usb-redirect
Summary: QEMU USB redirection device modules
Requires: qemu-kvm-core = %{epoch}:%{version}-%{release}

%description -n qemu-kvm-device-usb-redirect
Modules enabling USB redirection via usbredir components.

############################################################
# Virtio-GPU (base)
############################################################
%package -n qemu-kvm-device-display-virtio-gpu
Summary: QEMU virtio-gpu display device modules
Requires: qemu-kvm-core = %{epoch}:%{version}-%{release}

%description -n qemu-kvm-device-display-virtio-gpu
Virtio-GPU 2D/3D display modules (non-VGA, non-PCI alias variants).

############################################################
# Virtio-VGA (legacy VGA w/ virtio path)
############################################################
%package -n qemu-kvm-device-display-virtio-vga
Summary: QEMU virtio-vga display device modules
Requires: qemu-kvm-core = %{epoch}:%{version}-%{release}

%description -n qemu-kvm-device-display-virtio-vga
Virtio-VGA display modules (VGA compatibility with virtio GPU backend).

############################################################
# Virtio-GPU PCI specialization
############################################################
%package -n qemu-kvm-device-display-virtio-gpu-pci
Summary: QEMU virtio-gpu PCI variant display modules
Requires: qemu-kvm-core = %{epoch}:%{version}-%{release}

%description -n qemu-kvm-device-display-virtio-gpu-pci
PCI-specific variant modules for virtio-gpu devices.

############################################################
# (Optional) s390x CCW variant (only if you build for s390x)
############################################################
%ifarch s390x
%package -n qemu-kvm-device-display-virtio-gpu-ccw
Summary: QEMU virtio-gpu CCW display modules (s390x)
Requires: qemu-kvm-core = %{epoch}:%{version}-%{release}

%description -n qemu-kvm-device-display-virtio-gpu-ccw
CCW transport variant of virtio-gpu display modules for s390x.
%endif


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

%files
%defattr(-,root,root,-)
/usr/local/bin/
/usr/local/libexec/
/usr/local/share
/usr/local/include

%doc

%changelog
