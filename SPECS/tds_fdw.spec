Name:           postgresql-93-tds_fdw
Version:        1.0.1
Release:        1%{?dist}
Summary:        TDS foreing data wrapper for PostgreSQL 9.3

License:        None
URL:            https://github.com/GeoffMontee/tds_fdw
Source:         https://github.com/GeoffMontee/tds_fdw/archive/v%{version}.tar.gz

Requires:       postgresql93 >= 9.3.4
Requires:	postgresql93-server >= 9.3.4
Requires:       postgresql93-libs >= 9.3.4
Requires:       freetds >= 0.91

BuildRequires:  freetds-devel, postgresql93-devel 
BuildRequires:	automake, gcc-c++

%description
This is a PostgreSQL foreign data wrapper that can connect to databases that
use the Tabular Data Stream (TDS) protocol, such as Sybase databases and
Microsoft SQL server.
.
It does not yet support write operations, as added in PostgreSQL 9.3.

%global debug_package %{nil}

%prep
%setup -q -n tds_fdw-1.0.1


%build
PATH=/usr/pgsql-9.3/bin:$PATH make USE_PGXS=1

%install
rm -rf %{buildroot}
PATH=/usr/pgsql-9.3/bin:$PATH make USE_PGXS=1 install DESTDIR=%{buildroot}
mkdir %{buildroot}/usr/share/doc/%{name}-%{version}
mv %{buildroot}/usr/share/doc/pgsql/extension/README.tds_fdw.md %{buildroot}/usr/share/doc/%{name}-%{version}/README.md
rm -rf %{buildroot}/usr/share/doc/pgsql/extension/

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root)/usr/pgsql-9.3/lib/tds_fdw.so
%attr(644, root, root)/usr/pgsql-9.3/share/extension/tds_fdw--1.0.1.sql
%attr(644, root, root)/usr/pgsql-9.3/share/extension/tds_fdw.control
%doc /usr/share/doc/%{name}-%{version}/README.md



%changelog

* Thu Aug 28 2014 Julio Gonzalez Gil <git@juliogonzalez.es> - 1.0.1
- Initial build of 1.0.1 from https://github.com/GeoffMontee/tds_fdw
