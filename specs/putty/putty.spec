# $Id$
# Authority: dag
# Upstream: <putty$projects,tartarus,org>

%{?dist: %{expand: %%define %dist 1}}

%{?rh7:%define _without_freedesktop 1}
%{?el2:%define _without_freedesktop 1}
%{?rh6:%define _without_freedesktop 1}

Summary: Graphical SSH, Telnet and Rlogin client
Name: putty
Version: 0.55
Release: 1
License: MIT
Group: Applications/Internet
URL: http://www.chiark.greenend.org.uk/~sgtatham/putty/

Packager: Dag Wieers <dag@wieers.com>
Vendor: Dag Apt Repository, http://dag.wieers.com/apt/

Source0: http://the.earth.li/~sgtatham/putty/latest/putty-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gtk+-devel, ImageMagick, desktop-file-utils

%description
Putty is a SSH, Telnet & Rlogin client for Linux.

%prep
%setup

%{__cat} <<EOF >putty.desktop
[Desktop Entry]
Name=Putty Terminal Client
Comment=Log on to remote systems using SSH, Telnet or Rlogin
Exec=putty
Icon=putty.png
Terminal=false
Type=Application
StartupNotify=false
Categories=GNOME;Application;Network;
EOF

./mkfiles.pl

%{__perl} -pi.orig -e 's|-O2 -Wall -Werror -g|%{optflags}|g' unix/Makefile.gtk

%build
%{__make} %{?_smp_mflags} -C unix -f Makefile.gtk \
	prefix="%{_prefix}"
%{__make} -C doc

%install
%{__rm} -rf %{buildroot}
%{__install} -d -m0755 %{buildroot}%{_bindir} \
			%{buildroot}%{_mandir}/man1/ \
%makeinstall -C unix -f Makefile.gtk

%if %{?_without_freedesktop:1}0
	%{__install} -D -m0644 putty.desktop %{buildroot}%{_datadir}/gnome/apps/Network/putty.desktop
%else
	%{__install} -d -m0755 %{buildroot}%{_datadir}/applications/
	desktop-file-install --vendor gnome                \
		--add-category X-Red-Hat-Base              \
		--dir %{buildroot}%{_datadir}/applications \
		putty.desktop
%endif

convert putty.ico putty.png
%{__install} -D -m644 putty.png.0 %{buildroot}%{_datadir}/pixmaps/putty.png

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc CHECKLST.txt LICENCE MODULE README* doc/*.html doc/*.txt
%doc %{_mandir}/man1/p*.1*
%{_bindir}/p*
%{_datadir}/pixmaps/putty.png
%{!?_without_freedesktop:%{_datadir}/applications/gnome-putty.desktop}
%{?_without_freedesktop:%{_datadir}/gnome/apps/Network/putty.desktop}

%changelog
* Wed Aug 04 2004 Dag Wieers <dag@wieers.com> - 0.55-1
- Updated to release 0.55.

* Sun Apr 04 2004 Dag Wieers <dag@wieers.com> - 0.54-1
- Disabled StartupNotify in desktop-file. (Gavin Henry)

* Mon Feb 16 2004 Dag Wieers <dag@wieers.com> - 0.54-0
- Updated to release 0.54.

* Mon Nov 24 2003 Dag Wieers <dag@wieers.com> - 0.53-0.20030821
- Initial package. (using DAR)
