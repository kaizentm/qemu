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
rm -rf $RPM_BUILD_ROOT 
make install


%files
%defattr(-,root,root,-)
/usr/local/bin/*qemu*
/usr/local/libexec/*qemu*
/usr/local/share/qemu/
/usr/local/share/doc/qemu
/usr/local/share/applications
/usr/local/share/icons
/usr/local/libexec
/usr/local/share/man
%doc

%changelog
