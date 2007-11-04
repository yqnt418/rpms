# $Id$
# Authority: dag
# Upstream: ☺唐鳳☻ <cpan$audreyt,org>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Unicode-EastAsianWidth

Summary: Perl module that implements East Asian Width properties
Name: perl-Unicode-EastAsianWidth
Version: 1.02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Unicode-EastAsianWidth/

Source: http://www.cpan.org/modules/by-module/Unicode/Unicode-EastAsianWidth-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
perl-Unicode-EastAsianWidth is a Perl module that implements
East Asian Width properties.

This package contains the following Perl module:

    Unicode::EastAsianWidth

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST META.yml README SIGNATURE
%doc %{_mandir}/man3/Unicode::EastAsianWidth.3pm*
%dir %{perl_vendorlib}/Unicode/
#%{perl_vendorlib}/Unicode/EastAsianWidth/
%{perl_vendorlib}/Unicode/EastAsianWidth.pm

%changelog
* Sun Nov 04 2007 Dag Wieers <dag@wieers.com> - 1.02-1
- Initial package. (using DAR)
