#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Cache
%define	pnam	DB_File
Summary:	Cache::DB_File - memory cache which, when full, swaps to DB_File database
Summary(pl):	Cache::DB_File - bufor pamiêci okre¶lonej wielko¶ci, z wymian± do bazy DB_File
Name:		perl-Cache-DB_File
Version:	0.2
Release:	5
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	48fa9e428e2d28ca90253031d0bf9d93
%if %{with tests}
BuildRequires:	perl-DB_File >= 1
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Cache::DB_File is a cache system that has a optional limit on the
number of elements, and optional time limits on elements. When the
memory cache reaches its limit, it will swap infrequently used
elements to disk.

%description -l pl
Cache::DB_File to system bufora, który ma opcjonalny limit na liczbê
elementów i opcjonalne limity czasowe na elementy. kiedy bufor w
pamiêci osi±gnie limit, rzadko u¿ywane elementy zostan± zrzucone na
dysk.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
