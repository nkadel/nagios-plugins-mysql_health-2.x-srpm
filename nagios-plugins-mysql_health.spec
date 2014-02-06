#
# spec file for package nagios-plugins-mysql_health
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# Added for RHEL
%global nagios_plugindir %{_libdir}/nagios/plugins


Name:           nagios-plugins-mysql_health
Version:        2.1.8.2
Release:        6.3
License:        GPL-2.0+
Summary:        Check various parameters of a MySQL database
Url:            http://labs.consol.de/lang/en/nagios/check_mysql_health/
Group:          System/Monitoring
Source0:        check_mysql_health-%{version}.tar.gz
#BuildRequires:  nagios-rpm-macros
Requires:       mysql-client
#Recommends:     perl(DBD::mysql)
#Recommends:     perl(DBI)
Requires:       perl(DBD::mysql)
Requires:       perl(DBI)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
When using a database that are business critical it can be a good idea to
monitor the internals.

This Nagios plugin allows you to monitor the internal details of your
MySQL database.

%prep
%setup -q -n check_mysql_health-%{version}

%build
%configure \
	--libdir=%{nagios_plugindir} \
	--with-mymodules-dyn-dir=%{nagios_plugindir} \
 	--with-mymodules-dir=%{nagios_plugindir} \
	--prefix=%{nagios_plugindir}

%install
mkdir -p %{buildroot}/%{nagios_plugindir}
%make_install
mv %{buildroot}%{_libexecdir}/check_mysql_health %{buildroot}/%{nagios_plugindir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README TODO NEWS ChangeLog AUTHORS COPYING contrib
# avoid build dependecy of nagios - own the dirs
#%dir %{nagios_libdir}
%{nagios_plugindir}/*

%changelog
* Fri Jan 25 2013 lars@linux-schulserver.de
- add COPYING to doc
* Wed Jan 23 2013 lars@linux-schulserver.de
- update to 2.1.8.2:
  + bugfix in querycache-hitrate (div by 0 after db restart)
  + fix warnings for newest perl versions
  + new parameters –mycnf and –mycnfgroup
* Thu Jul 12 2012 lars@linux-schulserver.de
- update to 2.1.7
  + innodb modes now detect problems with the innodb engine
  + fix a bug with statefilesdir and capital letters
  + add –labelformat so that groundwork no longer complains
    (max label length is 19 characters)
  + bugfix in mode sql (numerical vs. regexp output)
* Fri Jul 29 2011 lars@linux-schulserver.de
- initial version 2.1.5.1
