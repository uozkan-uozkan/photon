Summary:        ALSA Utilities
Name:           alsa-utils
Version:        1.2.3
Release:        1%{?dist}
License:        LGPLv2+
URL:            http://alsa-project.org
Group:          Applications/Internet
Vendor:         VMware, Inc.
Distribution:   Photon
Source0:        ftp://ftp.alsa-project.org/pub/utils/%{name}-%{version}.tar.bz2
%define sha1    alsa-utils=4114e54169de9550e69c00575573ddf75c5a54ba
Patch0:         ens1371.patch
BuildRequires:  alsa-lib-devel ncurses-devel
Requires:       linux-drivers-sound alsa-lib ncurses
%description
The ALSA Utilities package contains various utilities which are useful for controlling your sound card.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-alsaconf --disable-xmlto
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
install -d -m 755 $RPM_BUILD_ROOT/var/lib/alsa

%post
alsactl init
alsactl -L store

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
/lib/*
%{_sbindir}/*
%{_datadir}/*
%{_localstatedir}/*

%changelog
* Wed Jul 08 2020 Gerrit Photon <photon-checkins@vmware.com> 1.2.3-1
- Automatic Version Bump
* Mon Dec 10 2018 Alexey Makhalov <amakhalov@vmware.com> 1.1.7-1
- initial version, moved from Vivace
