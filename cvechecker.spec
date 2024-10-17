Summary:	CVE reporting tool
Name: 		cvechecker
Version: 	3.1
Release: 	2
Group: 		System/Servers
License: 	GPL
URL:		https://cvechecker.sourceforge.net/
Source0: 	%{name}-%{version}.tar.gz
BuildRequires:	libconfig-devel
BuildRequires:	mysql-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel
Requires:	wget
Requires:	xsltproc
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
cvechecker reports about possible vulnerabilities on your system by scanning
the installed software and matching the results with the CVE database. This is
not a bullet-proof method and you will most likely have many false positives,
but it is still better than nothing, especially if you are running a
distribution with little security coverage.

%prep

%setup -q

%build
%configure2_5x \
    --localstatedir=/var/lib \
    --enable-sqlite3 \
    --enable-mysql
%make

%install
rm -rf %{buildroot}

%makeinstall_std

rm -rf %{buildroot}%{_docdir}/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog docs/userguide.xml
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/cvechecker.conf
%{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*
%{_datadir}/cvechecker
%dir /var/lib/cvechecker
%dir /var/lib/cvechecker/local
%dir /var/lib/cvechecker/cache



%changelog
* Thu Apr 14 2011 Oden Eriksson <oeriksson@mandriva.com> 3.1-1mdv2011.0
+ Revision: 652911
- import cvechecker


* Thu Apr 14 2011 Oden Eriksson <oeriksson@mandriva.com> 3.1-1mdv2010.2
- 3.1

* Wed Apr 13 2011 Oden Eriksson <oeriksson@mandriva.com> 3.0-1mdv2010.2
- initial Mandriva package
