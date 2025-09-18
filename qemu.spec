Name:           qemu
Version:        10.1.50.mshv.v4
Release:        1%{?dist}
Summary:        QEMU the FAST! processor emulator

License:        GPLv2+
URL:            https://www.qemu.org
Source0:        qemu-%{version}.tar.xz

BuildRequires:  gtk2-devel
BuildArch:      x86_64

%description
Packaging the latest (at time of writing) version of qemu that is not available from Red Hat repository

%prep
%setup -q -n %{name}-%{version}

%global __strip /usr/bin/true




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

%files
%defattr(-,root,root,-)
/usr/local/bin/
/usr/local/libexec/
/usr/local/share
/usr/local/include



%doc

%changelog
