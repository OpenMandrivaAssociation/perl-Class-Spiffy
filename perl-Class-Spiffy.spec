%define	upstream_name	 Class-Spiffy
%define	upstream_version 0.15

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Spiffy Perl Interface Framework For You
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/I/IN/INGY/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
"Class::Spiffy" is a framework and methodology for doing object oriented (OO)
programming in Perl. Class::Spiffy combines the best parts of Exporter.pm,
base.pm, mixin.pm and SUPER.pm into one magic foundation class. It attempts to
fix all the nits and warts of traditional Perl OO, in a clean, straightforward
and (perhaps someday) standard way.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make 

%check
%__make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man*/*
%{perl_vendorlib}/Class/Spiffy.pm
%{perl_vendorlib}/Class/Spiffy/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.150.0-4mdv2012.0
+ Revision: 765092
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.150.0-3
+ Revision: 763544
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.150.0-2
+ Revision: 667046
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.150.0-1mdv2010.1
+ Revision: 406879
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.15-4mdv2009.0
+ Revision: 223574
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.15-3mdv2008.1
+ Revision: 180368
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 29 2007 Olivier Thauvin <nanardon@mandriva.org> 0.15-2mdv2008.0
+ Revision: 19109
- rebuild


* Fri Feb 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.15-1mdk
- 0.15

* Tue Jan 24 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.12-1mdk
- First MDV release

