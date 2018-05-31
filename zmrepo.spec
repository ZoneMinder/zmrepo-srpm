# Unified zmrepo specfile for all supported distros

%if 0%{?fedora}
    %global zmrepo_mjr_ver %{fedora}
    %global distro fedora
    %global rpmfusion_gpg_key RPM-GPG-KEY-rpmfusion-free-%{distro}-%{zmrepo_mjr_ver}-zmrepo
%else
    %global zmrepo_mjr_ver %{rhel}
    %global distro rhel
    %global rpmfusion_gpg_key RPM-GPG-KEY-rpmfusion-free-el-%{zmrepo_mjr_ver}-zmrepo
%endif

Name:           zmrepo       
Version:        %{zmrepo_mjr_ver}
Release:        1%{?dist}
Summary:        Zoneminder and its dependencies for %{distro} %{zmrepo_mjr_ver}

Group:          System Environment/Daemons 
License:        GPLv2

URL:            https://github.com/ZoneMinder/zmrepo-srpm
Source0:        https://github.com/ZoneMinder/zmrepo-srpm/archive/master.tar.gz#/zmrepo.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils

Requires:      %{distro}-release = %{zmrepo_mjr_ver}
%{?rhel:Requires: epel-release >= %{zmrepo_mjr_ver}} 

%description
This package contains the ZoneMinder (zmrepo) repository
GPG keys as well as configuration for yum/dnf.

%prep
%autosetup -n zmrepo-master

%build
# Nothing to build

%install
# Create folders in buildroot
%{__mkdir} -p %{buildroot}%{_sysconfdir}/pki/rpm-gpg
%{__mkdir} -p %{buildroot}%{_sysconfdir}/yum.repos.d

# Install the repo config files
install -pm 0644 repo/zmrepo-%{distro}.repo %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 0644 repo/zmrepo-%{distro}-testing.repo %{buildroot}%{_sysconfdir}/yum.repos.d

# Insall the GPG Keys
install -pm 0644 gpg/%{rpmfusion_gpg_key} %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -pm 0644 gpg/RPM-GPG-KEY-zmrepo %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%files
%license LICENSE
%config(noreplace) /etc/yum.repos.d/zmrepo-%{distro}.repo
%config(noreplace) /etc/yum.repos.d/zmrepo-%{distro}-testing.repo
%{_sysconfdir}/pki/rpm-gpg/%{rpmfusion_gpg_key}
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-zmrepo

%changelog
* Thu May 31 2018 Andrew Bauer <zonexpertconsulting@outlook.com> - %{version}-1
- Add support for Fedora %{version}

* Fri Mar 31 2017  Andrew Bauer <zonexpertconsulting@outlook.com> - 27-1
- Redesign for easier management

