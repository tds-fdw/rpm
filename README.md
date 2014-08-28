tds_fdw
=======

CentOS/RH/Amazon RPMs for tds_fdw  <https://github.com/GeoffMontee/tds_fdw> and postgresql 9.3.4 or later

Tested on x64 CentOS 6.4 and Amazon Linux 2014.03

tds_fdw is a PostgreSQL foreign data wrapper that can connect to databases that use the Tabular Data Stream (TDS) protocol, such as Sybase databases and
Microsoft SQL server.

It does not yet support write operations, as added in PostgreSQL 9.3.

Requirements
------------

To build: 

* freetds-devel
* postgresql93-devel 
* automake
* gcc-c++
* Git
* rpmbuild

To install the RPM

* postgresql93 >= 9.3.4
* postgresql93-server >= 9.3.4
* postgresql93-libs >= 9.3.4
* freetds >= 0.91

Building fresh RPMs
-------------------

Clone the repo: 

    git@github.com:juliogonzalez/tds_fdw-rpm.git
    cd tds_fdw-rpm


Build the tds_fdw RPM
---------------------

Build the RPMs:

    ./tds-fdw_rpm

And install:

    rpm -Uvh RPMS/$HOSTTYPE/postgresql-93-tds_fdw-1.0.1-1.*.$HOSTTYPE.rpm
