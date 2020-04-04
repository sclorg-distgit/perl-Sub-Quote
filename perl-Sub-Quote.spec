%{?scl:%scl_package perl-Sub-Quote}

Name:           %{?scl_prefix}perl-Sub-Quote
Version:        2.006006
Release:        2%{?dist}
Summary:        Efficient generation of subroutines via string eval
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Sub-Quote
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Sub-Quote-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl-interpreter
BuildRequires:  %{?scl_prefix}perl(:VERSION) >= 5.6.0
BuildRequires:  %{?scl_prefix}perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  %{?scl_prefix}perl(strict)
BuildRequires:  %{?scl_prefix}perl(warnings)
# Run-time
BuildRequires:  %{?scl_prefix}perl(B)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(Scalar::Util)
# Tests
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(constant)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(File::Spec)
BuildRequires:  %{?scl_prefix}perl(lib)
BuildRequires:  %{?scl_prefix}perl(List::Util)
BuildRequires:  %{?scl_prefix}perl(overload)
BuildRequires:  %{?scl_prefix}perl(POSIX)
BuildRequires:  %{?scl_prefix}perl(Test::Builder)
BuildRequires:  %{?scl_prefix}perl(Test::Fatal) >= 0.003
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.94
BuildRequires:  %{?scl_prefix}perl(threads)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Conflicts:      %{?scl_prefix}perl-Moo < 2.003000

%description
This package provides performant ways to generate subroutines from strings.

%prep
%setup -q -n Sub-Quote-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 && %{make_build}%{?scl:'}

%install
%{?scl:scl enable %{scl} '}%{make_install}%{?scl:'}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%files
%doc LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Jan 06 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.006006-2
- SCL

* Wed Oct 02 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.006006-1
- 2.006006 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.006003-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.006003-2
- Perl 5.30 rebuild

* Mon Mar 11 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.006003-1
- 2.006003 bump

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.005001-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.005001-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.005001-2
- Perl 5.28 rebuild

* Fri Apr 20 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.005001-1
- 2.005001 bump

* Wed Feb 07 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.005000-1
- 2.005000 bump

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.004000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.004000-1
- 2.004000 bump

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.003001-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.003001-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 12 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.003001-1
- Initial release
