%define	upstream_name	 Class-Spiffy
%define	upstream_version 0.15

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Spiffy Perl Interface Framework For You
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/I/IN/INGY/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
