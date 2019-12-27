# Unified zmrepo specfile for all supported distros

%if 0%{?fedora}
    %global zmrepo_mjr_ver %{fedora}
    %global distro fedora
%else
    %global zmrepo_mjr_ver %{rhel}
    %global distro rhel
%endif

Name:           zmrepo       
Version:        %{zmrepo_mjr_ver}
Release:        3%{?dist}
Summary:        Zoneminder and its dependencies for %{distro} %{zmrepo_mjr_ver}

Group:          System Environment/Daemons 
License:        GPLv2

URL:            https://github.com/ZoneMinder/zmrepo-srpm
Source0:        https://github.com/ZoneMinder/zmrepo-srpm/archive/master.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils

Requires:      rpmfusion-free-release = %{zmrepo_mjr_ver}
%{?rhel:Requires: epel-release >= %{zmrepo_mjr_ver}} 

%description
This package contains the ZoneMinder (zmrepo) repository
GPG keys as well as configuration for yum/dnf.

%prep
%autosetup -n zmrepo-srpm-master

# $releasever does not expand as expected on rhel, so replace it
%if 0%{?rhel}
sed -i 's!$releasever!%{rhel}!' repo/zmrepo-rhel.repo
%endif

%build
# Nothing to build

%install
# Create folders in buildroot
%{__mkdir} -p %{buildroot}%{_sysconfdir}/pki/rpm-gpg
%{__mkdir} -p %{buildroot}%{_sysconfdir}/yum.repos.d

# Install the repo config file
install -pm 0644 repo/zmrepo-%{distro}.repo %{buildroot}%{_sysconfdir}/yum.repos.d

# Insall the GPG Key
install -pm 0644 gpg/RPM-GPG-KEY-zmrepo %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%license LICENSE
%config(noreplace) /etc/yum.repos.d/zmrepo-%{distro}.repo
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-zmrepo

%changelog
* Fri Dec 27 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - %{version}-3
- Removed requirement for distro-release package, as it was problematic
- Added requirement for rpmfusion-free-release

* Fri Dec 27 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - %{version}-2
- Fix source0 & autosetup
- Don't use $releasever, it's not expanding as expected on RHEL.

* Wed Dec 25 2019 Andrew Bauer <zonexpertconsulting@outlook.com> - %{version}-1
- zmrepo yum/dnf repo config

