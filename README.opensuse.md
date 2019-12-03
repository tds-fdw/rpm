For openSUSE we still do not have CI, but at least some quick tests can be performed.

First, start a container for the most recent lean version:
```
docker run -ti --rm opensuse/leap /bin/bash
```

Then see what Leap version the container is:
```
cat /etc/os-release
```

Finally run the following commands, after adapting `PGVER`, `LEAPVER` and `BRANCH`as needed.
```
PGVER=12
LEAPVER=15.1
BRANCH=master
PGSVER=$(echo $PGVER|sed -e 's/\.//g')
zypper ar http://download.opensuse.org/repositories/server:/database:/postgresql/openSUSE_Leap_${LEAPVER}/server:database:postgresql.repo
zypper --gpg-auto-import-keys ref
zypper in -y gcc git curl freetds-devel freetds make rpm-build postgresql${PGSVER} postgresql${PGSVER}-devel postgresql${PGSVER}-server postgresql${PGSVER}-server-devel # server-devel only needed for >= 11
git clone https://github.com/tds-fdw/rpm.git
cd rpm
git checkout ${BRANCH}
./clean
./tds_fdw-rpm -p ${PGVER}
mkdir /var/lib/pgsql/data/
chown -R postgres. /var/lib/pgsql/data/
su - postgres /usr/share/postgresql/postgresql-script start
su - postgres -c "psql -c 'CREATE EXTENSION tds_fdw;'"
su - postgres -c "psql -c '\dx'"
