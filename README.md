tds_fdw
=======

CentOS/RH/Amazon RPMs for tds_fdw  <https://github.com/GeoffMontee/tds_fdw> and postgresql 9.3.4 or later

Tested on CentOS 6.4/7.1 x86_64 and Amazon Linux 2014.03

tds_fdw is a PostgreSQL foreign data wrapper that can connect to databases that use the Tabular Data Stream (TDS) protocol, such as Sybase databases and Microsoft SQL server.

It does not yet support write operations, as added in PostgreSQL 9.3.

Requirements
------------

Use postgresql93\* packages for PostgreSQL 9.3 (>= 9.3.4) or posgresql94\* packages for PostgreSQL 9.4 (>= 9.4.1)

To build: 

* freetds-devel
* postgresql93-devel or postgresql94-devel
* automake
* gcc-c++
* Git
* rpmbuild

To install the RPM for PostgreSQL

* postgresql93 >= 9.3.4 or postgresql94 >= 9.4.1
* postgresql93-server >= 9.3.4 or postgresql94-server >= 9.4.1
* postgresql93-libs >= 9.3.4 or postgresql94-libs >= 9.4.1
* freetds >= 0.91

Building fresh RPMs
-------------------

Clone the repo: 

    git@github.com:juliogonzalez/tds_fdw-rpm.git
    cd tds_fdw-rpm


Build the tds_fdw RPM
---------------------

Build the RPMs:

    ./tds-fdw_rpm -p 9.3 for PostgreSQL 9.3

    or

    ./tds-fdw_rpm -p 9.4 for PostgreSQL 9.4

And install:

    rpm -Uvh RPMS/$HOSTTYPE/postgresql-93-tds_fdw-1.0.3-1.*.$HOSTTYPE.rpm for PostgreSQL 9.3

    or

    rpm -Uvh RPMS/$HOSTTYPE/postgresql-94-tds_fdw-1.0.3-1.*.$HOSTTYPE.rpm for PostgreSQL 9.4
