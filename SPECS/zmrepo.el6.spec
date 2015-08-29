Name:           zmrepo       
Version:        6
Release:        5%{?dist}
Summary:        Zoneminder and its dependencies for Enterprise Linux 6

Group:          System Environment/Daemons 
License:        GPLv2+ and LGPLv2+ and MIT

URL:            http://www.zoneminder.com/
Source0:        RPM-GPG-KEY-EPEL-6-zmrepo
Source1:        RPM-GPG-KEY-rpmfusion-free-el-6-zmrepo
Source2:        RPM-GPG-KEY-zmrepo	
Source3:        GPL
Source4:	zmrepo-centos.repo
Source5:	zmrepo-centos-testing.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
Requires:      redhat-release =  %{version} 
Conflicts:     fedora-release

%description
This package contains the ZoneMinder (zmrepo) repository
GPG keys as well as configuration for yum and up2date.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .
install -pm 644 %{SOURCE2} .
install -pm 644 %{SOURCE3} .
install -pm 644 %{SOURCE4} .
install -pm 644 %{SOURCE5} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-EPEL-6-zmrepo
install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-el-6-zmrepo
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
* Sat Aug 29 2015  Andrew Bauer <knnniggett@users.sourceforge.net> - 6-5
- Added testing and SRPM repos

* Fri Sep 5 2014 Andrew Bauer <knnniggett@users.sourceforge.net> - 6-4
- Fix typo

* Fri Sep 5 2014 Andrew Bauer <knnniggett@users.sourceforge.net> - 6-3
- Rename third party gpg key filenames to prevent rpm conflicts

* Wed Sep 3 2014 Andrew Bauer <knnniggett@users.sourceforge.net> - 6-2
- Added connortechnology as an additional site to pull from

* Mon Sep 1 2014 Andrew Bauer <knnniggett@users.sourceforge.net> - 6-1
- Initial Package
