
Name:           zmrepo       
Version:        22
Release:        2%{?dist}
Summary:        Zoneminder and its dependencies for Fedora 22

Group:          System Environment/Daemons 
License:        GPLv2+ and LGPLv2+ and MIT

URL:            http://www.zoneminder.com/
Source0:        RPM-GPG-KEY-rpmfusion-free-fedora-22-zmrepo
Source1:        RPM-GPG-KEY-zmrepo	
Source2:        GPL
Source3:	zmrepo-fedora.repo	

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
Requires:      fedora-release = %{version} 

%description
This package contains the ZoneMinder (zmrepo) repository
GPG keys as well as configuration for yum and up2date.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .
install -pm 644 %{SOURCE2} .
install -pm 644 %{SOURCE3} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-rpmfusion-free-fedora-22-zmrepo
install -Dpm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-zmrepo

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE3}  \
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
* Mon Jul 6 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 22-2
- Update gpg key to Fedora 22

* Tue May 26 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 22-1
- Initial Package

