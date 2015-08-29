%define upstream_rel 7.0

Name:           zmrepo       
Version:        7
Release:        5%{?dist}
Summary:        Zoneminder and its dependencies for CentOS 7

Group:          System Environment/Daemons 
License:        GPLv2+ and LGPLv2+ and MIT

URL:            http://www.zoneminder.com/
# RPMFusion does not yet have rpms for el7
#Source0:        RPM-GPG-KEY-rpmfusion-free-el-7-zmrepo
Source1:	RPM-GPG-KEY-EPEL-7-zmrepo
Source2:        RPM-GPG-KEY-zmrepo	
Source3:        GPL
Source4:	zmrepo-centos.repo
Source5:	zmrepo-centos-testing.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:	noarch
Requires:	redhat-release >= %{upstream_rel}
Conflicts:	fedora-release

%description
This package contains the ZoneMinder (zmrepo) repository
GPG keys as well as configuration for yum and up2date.

%prep
%setup -q  -c -T
#install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .
install -pm 644 %{SOURCE2} .
install -pm 644 %{SOURCE3} .
install -pm 644 %{SOURCE4} .
install -pm 644 %{SOURCE5} .

# Comment out reference to rpmfusion gpg key for el7
/usr/bin/sed -i 's/.*RPM-GPG-KEY-rpmfusion-free.*/#&/' %{SOURCE4}

%build

%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
#install -Dpm 644 %{SOURCE0} \
#    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-el-7-zmrepo
install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7-zmrepo
install -Dpm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-zmrepo

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE4}  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE5}  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%post
# Not needed for el6 as sources has been removed
#echo "# epel repo -- added by epel-release " \
#    >> %{_sysconfdir}/sysconfig/rhn/sources
#echo "yum epel http://download.fedora.redhat.com/pub/epel/%{version}/\$ARCH" \
#    >> %{_sysconfdir}/sysconfig/rhn/sources

%postun 
#sed -i '/^yum\ epel/d' %{_sysconfdir}/sysconfig/rhn/sources
#sed -i '/^\#\ epel\ repo\ /d' %{_sysconfdir}/sysconfig/rhn/sources


%files
%defattr(-,root,root,-)
%doc GPL
%config /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%changelog
* Sat Aug 29 2015  Andrew Bauer <knnniggett@users.sourceforge.net> - 7-5
- Added testing and SRPM repos

* Thu Apr 2 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 7-4
- Fixed an issue checking the redhat-release version

* Thu Feb 12 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 7-3
- Add EPEL 7 key and rename it.

* Wed Feb 11 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 7-2
- Upstream added upstream_rel varaiable.  Modify accordingly.

* Mon Feb 9 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 7-1
- Initial Package

* Fri Sep 5 2014 Andrew Bauer <knnniggett@users.sourceforge.net> - 20-3
- Rename third party gpgkey filenames to prevent rpm conflicts

* Thu Sep 4 2014 Andrew Bauer <knnniggett@users.sourceforge.net> - 20-2
- Fix error in requires/conflicts statement

* Wed Sep 3 2014 Andrew Bauer <knnniggett@users.sourceforge.net> - 20-1
- Initial Package
