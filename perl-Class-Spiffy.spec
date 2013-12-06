%define	upstream_name	 Class-Spiffy
%define	upstream_version 0.15

Summary:	Spiffy Perl Interface Framework For You
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	9
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/I/IN/INGY/%{upstream_name}-%{upstream_version}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel

%description
"Class::Spiffy" is a framework and methodology for doing object oriented (OO)
programming in Perl. Class::Spiffy combines the best parts of Exporter.pm,
base.pm, mixin.pm and SUPER.pm into one magic foundation class. It attempts to
fix all the nits and warts of traditional Perl OO, in a clean, straightforward
and (perhaps someday) standard way.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make 

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Class/Spiffy.pm
%{perl_vendorlib}/Class/Spiffy/*
%{_mandir}/man3/*

