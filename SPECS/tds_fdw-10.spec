%define PG_VER 10
%define PG_SVER 10

Name:           postgresql-%{PG_SVER}-tds_fdw
Version:        2.0.3
Release:        0%{?dist}
Summary:        TDS foreing data wrapper for PostgreSQL %{PG_VER}
License:        None
URL:            https://github.com/tds-fdw/tds_fdw
Source:         https://github.com/tds-fdw/tds_fdw/archive/v%{version}.tar.gz

Provides:       tds_fdw%{PG_SVER}

Requires:       postgresql%{PG_SVER} >= %{PG_VER}.0
Requires:       postgresql%{PG_SVER}-server >= %{PG_VER}.0
%if ! 0%{?suse_version}
Requires:       postgresql%{PG_SVER}-libs >= %{PG_VER}.0
%endif
Requires:       freetds >= 0.91

BuildRequires:  gcc
BuildRequires:  freetds-devel
BuildRequires:  make
BuildRequires:  postgresql%{PG_SVER}-devel

%if 0%{?suse_version}
  %define PG_BIN %{_prefix}/lib/postgresql%{PG_SVER}/bin
  %define PG_LIB %{_prefix}/lib/postgresql%{PG_SVER}/%{_lib}
  %define PG_DATA %{_datadir}/postgresql%{PG_SVER}
  %define PG_DOC  %{_docdir}/postgresql%{PG_SVER}/extension
  %define MOD_DOC %{_docdir}/%{name}
%else
  %define PG_BIN %{_prefix}/pgsql-%{PG_VER}/bin
  %define PG_LIB %{_prefix}/pgsql-%{PG_VER}/lib
  %define PG_DATA %{_prefix}/pgsql-%{PG_VER}/share
  %define PG_DOC %{_prefix}/pgsql-%{PG_VER}/doc/extension
  %define MOD_DOC  %{_docdir}/%{name}
%endif

%description
This is a PostgreSQL foreign data wrapper that can connect to databases that
use the Tabular Data Stream (TDS) protocol, such as Sybase databases and
Microsoft SQL server.
.
It does not yet support write operations, as added in PostgreSQL %{PG_VER}.

%global debug_package %{nil}

%prep
%setup -q -n tds_fdw-%{version}

%build
PATH=%{PG_BIN}/:$PATH make USE_PGXS=1

%install
PATH=%{PG_BIN}/:$PATH make USE_PGXS=1 install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{MOD_DOC}
mv %{buildroot}%{PG_DOC}/README.tds_fdw.md %{buildroot}%{MOD_DOC}/README.md

%files
%attr(755, root, root)%{PG_LIB}/tds_fdw.so
%dir %attr(755, root, root)%{PG_DATA}
%dir %attr(755, root, root)%{PG_DATA}/extension
%attr(644, root, root)%{PG_DATA}/extension/tds_fdw--%{version}.sql
%attr(644, root, root)%{PG_DATA}/extension/tds_fdw.control
%dir %attr(755, root, root)%{MOD_DOC}
%doc %{MOD_DOC}/README.md

%changelog
* Mon Oct 31 2022 Julio Gonzalez Gil <packages@juliogonzalez.es> 2.0.3-0
- 2.0.3 from https://github.com/tds-fdw/tds_fdw

* Sat Sep 26 2020 Julio Gonzalez Gil <packages@juliogonzalez.es> 2.0.2-0
- 2.0.2 from https://github.com/tds-fdw/tds_fdw

* Tue Dec 03 2019 Julio Gonzalez Gil <packages@juliogonzalez.es> 2.0.1-0
- 2.0.1 from https://github.com/tds-fdw/tds_fdw
- SPEC cleanup to allow easier maintenance
- Compatibility with SUSE/openSUSE

* Sat Jan 19 2019 Julio Gonzalez Gil <packages@juliogonzalez.es> 2.0.0-alpha.3.2
- Allow upgrades from official PostgreSQL packages

* Sat Jan 19 2019 Julio Gonzalez Gil <git@juliogonzalez.es> - 2.0.0-alpha.3.1
- 2.0.0-alpha.3 build from https://github.com/tds-fdw/tds_fdw

* Fri Jan 18 2019 Julio Gonzalez Gil <git@juliogonzalez.es> - 2.0.0-alpha.2.1
- Initial build of 2.0.0-alpha.2 from https://github.com/tds-fdw/tds_fdw

