%define	module	Class-Spiffy
%define	name	perl-%{module}
%define	version	0.15
%define	release	%mkrel 1

Version:	%{version}
Name:		%{name}
Release:	%{release}
Summary:	Spiffy Perl Interface Framework For You
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/I/IN/INGY/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
"Class::Spiffy" is a framework and methodology for doing object oriented (OO)
programming in Perl. Class::Spiffy combines the best parts of Exporter.pm,
base.pm, mixin.pm and SUPER.pm into one magic foundation class. It attempts to
fix all the nits and warts of traditional Perl OO, in a clean, straightforward
and (perhaps someday) standard way.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make 

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man*/*
%{perl_vendorlib}/Class/Spiffy.pm
%{perl_vendorlib}/Class/Spiffy/*

