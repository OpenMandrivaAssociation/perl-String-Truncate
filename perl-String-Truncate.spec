%define upstream_name    String-Truncate
%define upstream_version 1.100602

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A module for when strings are too long to be displayed in
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/String/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Sub::Install)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
A module for when strings are too long to be displayed in.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.100.600-2mdv2011.0
+ Revision: 657468
- rebuild for updated spec-helper

* Wed Mar 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.100.600-1
+ Revision: 649170
- update to new version 1.100600

* Sun Feb 28 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.570-1mdv2011.0
+ Revision: 512600
- update to 1.100570

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.102.0-1mdv2010.1
+ Revision: 461279
- fix summary
- import perl-String-Truncate


* Fri Nov 06 2009 cpan2dist 0.102-1mdv
- initial mdv release, generated with cpan2dist


