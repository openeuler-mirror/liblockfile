Name:           liblockfile
Version:        1.17
Release:        1
Summary:        Library providing functions to lock standard mailboxes
License:        GPLv2+ and LGPLv2+
URL:            https://github.com/miquels/liblockfile
Source0:        https://github.com/miquels/liblockfile/archive/v%{version}.tar.gz

BuildRequires:  gcc

%description
This library implements a number of functions found in -lmail on SysV
systems.

%package       devel
Summary:       Liblockfile development files
Requires:      liblockfile = %{version}-%{release}

%description   devel
The liblockfile-devel package contains libraries and header files for
liblockfile development.

%package       help
Summary:       Liblockfile help docs and manual pages
Requires:      liblockfile = %{version}-%{release}

%description   help
The liblockfile-help package contains help docs and manual pages for liblockfile.

%prep
%autosetup -n liblockfile-%{version} -p1

sed -i "s/-g root//" Makefile.in

%build
%configure --enable-shared --prefix=%{buildroot} --bindir=%{buildroot}%{_bindir} --mandir=%{buildroot}%{_mandir} --libdir=%{buildroot}%{_libdir} --includedir=%{buildroot}%{_includedir}
%make_build

%install
%make_install

ldconfig -N -n %{buildroot}/%{_libdir}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%doc COPYRIGHT
%{_bindir}/dotlockfile
%{_libdir}/{liblockfile.so.1.0,liblockfile.so.1}

%files  devel
%{_libdir}/{liblockfile.so,liblockfile.a}
%{_includedir}/{maillock.h,lockfile.h}

%files  help
%doc README Changelog
%{_mandir}/man1/dotlockfile.1*
%{_mandir}/man3/{lockfile_create.3*,maillock.3*}

%changelog
* Fri Jul 29 2022 wenzhiwei <wenzhiwei@kylinos.cn> - 1.17-1
- Update to 1.17

* Tue Apr 14 2020 huanghaitao <huanghaitao@huawei.com> 1.14-3
- Package init
