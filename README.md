tds_fdw
=======

CentOS/RH/Amazon RPMs for tds_fdw  <https://github.com/tds-fdw/tds_fdw> and postgresql 9.3.4 or later

Tested on Rocky Linux 8 x86_64 and openSUSE Leap 15.6. Should work for pretty much any RPM base distributions. Feel free to report problems on the issues, so we can have a look.

tds_fdw is a PostgreSQL foreign data wrapper that can connect to databases that use the Tabular Data Stream (TDS) protocol, such as Sybase databases and Microsoft SQL server.

It does not yet support write operations, as added in PostgreSQL 9.3.

PostgreSQL versions that the SPEC can support
---------------------------------------------
* 9.3 >= 9.3.4 (EoL and not maintained by tds_fdw upstream anymore, but it should still work)
* 9.4 >= 9.4.1 (EoL and not maintained by tds_fdw upstream anymore, but it should still work)
* 9.5 >= 9.5.1 (EoL and not maintained by tds_fdw upstream anymore, but it should still work)
* 9.6 >= 9.6.1 (EoL and not maintained by tds_fdw upstream anymore, but it should still work)
* 10 >= 10.0 (EoL and not maintained by tds_fdw upstream anymore, but it should still work)
* 11 >= 11.0 (EoL and not maintained by tds_fdw upstream anymore, but it should still work)
* 12 >= 12.0 (EoL and not maintained by tds_fdw upstream anymore, but it should still work)
* 13 >= 13.0
* 14 >= 14.0
* 15 >= 15.0
* 16 >= 16.0
* 17 >= 17.0
* 18 >= 17.0

Requirements
------------

To build: 

* freetds-devel
* gcc
* Git
* make
* rpmbuild

And:

* postgresql[version]-devel

Being **[version]** one of: 93, 94, 95, 96, 10, 11, 12, 13, 14, 15, 16, 17, 18

To install the RPM for PostgreSQL

* freetds >= 0.91

And:
* postgresql[version]
* postgresql[version]-server
* postgresql[version]-libs

Being **[version]** one of: 93, 94, 95, 96, 10, 11, 12, 13, 14, 15, 16, 17, 18

Building fresh RPMs
-------------------

Clone the repo: 

    git@github.com:juliogonzalez/tds_fdw-rpm.git
    cd tds_fdw-rpm


Build the tds_fdw RPM
---------------------

Build the RPMs for with:

    ./tds-fdw_rpm -p [version]

Where `[version]` is one of: 9.3, 9.4, 9.5, 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18

And install with

    rpm -Uvh RPMS/$HOSTTYPE/postgresql-[version]-tds_fdw-*.*.$HOSTTYPE.rpm

Where `[version]` is one of: 9.3, 9.4, 9.5, 9.6, 10, 11, 12, 13, 14, 15, 16, 17, 18
