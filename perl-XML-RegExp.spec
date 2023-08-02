#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-XML-RegExp
Version  : 0.04
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/T/TJ/TJMATHER/XML-RegExp-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TJ/TJMATHER/XML-RegExp-0.04.tar.gz
Summary  : ~
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-XML-RegExp-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Perl module: XML-RegExp
All rights reserved.
This program is free software; you can redistribute it and/or modify it
under the same terms as Perl itself.

%package dev
Summary: dev components for the perl-XML-RegExp package.
Group: Development
Provides: perl-XML-RegExp-devel = %{version}-%{release}
Requires: perl-XML-RegExp = %{version}-%{release}

%description dev
dev components for the perl-XML-RegExp package.


%package perl
Summary: perl components for the perl-XML-RegExp package.
Group: Default
Requires: perl-XML-RegExp = %{version}-%{release}

%description perl
perl components for the perl-XML-RegExp package.


%prep
%setup -q -n XML-RegExp-0.04
cd %{_builddir}/XML-RegExp-0.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/XML::RegExp.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
