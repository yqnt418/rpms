# $Id$
# Authority: matthias
# Upstream: <metakit$equi4,com>

%define _lib32dir %{_prefix}/lib
%define python_version %(python -c 'import sys; print sys.version[:3]')

Summary: Embeddable database
Name: metakit
Version: 2.4.9.3
Release: 2
License: GPL
Group: System Environment/Libraries
URL: http://www.equi4.com/metakit/

Source: http://www.equi4.com/pub/mk/metakit-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++, tcl-devel, python-devel

%description
MetaKit is an embeddable database which runs on Unix, Windows,
Macintosh, and other platforms. It lets you build applications which
store their data efficiently, in a portable way, and which will not
need a complex runtime installation. In terms of the data model,
MetaKit takes the middle ground between RDBMS, OODBMS, and flat-file
databases - yet it is quite different from each of them.


%package devel
Summary: Header files and development documentation for metakit
Group: Development/Libraries
Requires: %{name} = %{version}

%description devel
Header files and development documentation for metakit.


%prep
%setup


%build
pushd unix
    %configure \
	--libdir="%{_lib32dir}" \
	--with-python="%{_includedir}/python%{python_version},%{_libdir}/python%{python_version}" \
	--with-tcl
    %{__make} %{?_smp_mflags}
popd


%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_libdir}/python%{python_version}/site-packages/
%{__make} install -C unix DESTDIR=%{buildroot}


%clean
%{__rm} -rf %{buildroot}


%post
/sbin/ldconfig 2>/dev/null

%postun
/sbin/ldconfig 2>/dev/null


%files
%defattr(-, root, root, 0755)
%doc README
%{_lib32dir}/*.so
#%{_libdir}/python%{python_version}/site-packages/Mk4py.so
#%{_libdir}/python%{python_version}/site-packages/metakit.py
%{_libdir}/python%{python_version}/Mk4py.so
%{_libdir}/python%{python_version}/metakit.py
%{_lib32dir}/tcl*/Mk4tcl/


%files devel
%defattr(-, root, root, 0755)
%doc CHANGES WHATSNEW doc
%{_includedir}/*
%exclude %{_lib32dir}/*.la
%{_lib32dir}/*.a


%changelog
* Mon Jul 18 2004 Dag Wieers <dag@wieers.com> - 2.4.9.3-2
- Added tcl and python libraries.

* Thu May 20 2004 Matthias Saou <http://freshrpms.net/> 2.4.9.3-2
- Rebuild for Fedora Core 2.

* Sun May 16 2004 Matthias Saou <http://freshrpms.net/> 2.4.9.3-1
- Updated to release 2.4.9.3.

* Fri Nov 14 2003 Matthias Saou <http://freshrpms.net/> 2.4.9.2-3
- Rebuild for Fedora Core 1.

* Mon Mar 31 2003 Matthias Saou <http://freshrpms.net/>
- Update to 2.4.9.2.
- Rebuilt for Red Hat Linux 9.
- Exclude .la file.

* Wed Dec  4 2002 Matthias Saou <http://freshrpms.net/>
- Initial RPM release, based on PLD spec file.

