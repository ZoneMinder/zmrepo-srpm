# Unified zmrepo specfile for all supported distros

%if 0%{fedora}
    %global zmrepo_mjr_ver %{fedora}
    %global distro fedora
    %global rpmfusion_gpg_key RPM-GPG-KEY-rpmfusion-free-%{distro}-%{zmrepo_mjr_ver}-zmrepo
%else
    %global zmrepo_mjr_ver %{rhel}
    %global distro rhel
    %global rpmfusion_gpg_key RPM-GPG-KEY-rpmfusion-free-el-%{zmrepo_mjr_ver}-zmrepo
%endif

Name:           zmrepo       
Version:        %{zmrepo_mjr_ver}.0
Release:        1%{?dist}
Summary:        Zoneminder and its dependencies for %{distro} %{zmrepo_mjr_ver}

Group:          System Environment/Daemons 
License:        GPLv2

URL:            https://github.com/knnniggett/zmrepo
Source0:        https://github.com/knnniggett/zmrepo/archive/master.tar.gz#/zmrepo-%{version}.tar.gz

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
install -pm 0644 SOURCES/zmrepo-%{distro}.repo %{buildroot}%{_sysconfdir}/yum.repos.d
install -pm 0644 SOURCES/zmrepo-%{distro}-testing.repo %{buildroot}%{_sysconfdir}/yum.repos.d

# Insall the GPG Keys
install -pm 0644 SOURCES/%{rpmfusion_gpg_key} %{buildroot}%{_sysconfdir}/pki/rpm-gpg
install -pm 0644 SOURCES/RPM-GPG-KEY-zmrepo %{buildroot}%{_sysconfdir}/pki/rpm-gpg

%post

%postun 

%files
%license GPL
%config(noreplace) /etc/yum.repos.d/zmrepo-%{distro}.repo
%config(noreplace) /etc/yum.repos.d/zmrepo-%{distro}-testing.repo
%{_sysconfdir}/pki/rpm-gpg/%{rpmfusion_gpg_key}
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-zmrepo

#
# Most recent changelog entry should use the version macro
# Older changelog entries should use the zmrepo_mjr_ver macro
#
%changelog
* Fri Mar 31 2017  Andrew Bauer <zonexpertconsulting@outlook.com> - %{version}
- Redesign for easier management

