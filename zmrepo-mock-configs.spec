# Version tracks the most recent supported version of Fedora

Name:           zmrepo-mock-configs      
Version:        28
Release:        1%{?dist}
Summary:        Zmrepo mock config files

Group:          System Environment/Daemons 
License:        GPLv2

URL:            https://github.com/ZoneMinder/zmrepo-srpm
Source0:        https://github.com/ZoneMinder/zmrepo-srpm/archive/master.tar.gz#/zmrepo-mock-configs.tar.gz

BuildArch:      noarch

Requires:       mock 

BuildRequires:  coreutils

%description
This package contains zmrepo config files for mock builds.

%prep
%autosetup -n zmrepo-master

%build
# Nothing to build

%install
# Create folders in the buildroot
%{__mkdir} -p %{buildroot}%{_sysconfdir}/mock
%{__mkdir} -p %{buildroot}%{_sysconfdir}/pki/mock
%{__mkdir} -p %{buildroot}%{_bindir}

# Install mock config files into mock config folder
install -pm 0644 cfg/zmrepo-*.cfg %{buildroot}%{_sysconfdir}/mock

# Install build script into bin
install -pm 755 bin/buildzm.sh %{buildroot}%{_bindir}/

# Install GPG keys into mock keys folder
install -pm 0644 gpg/RPM-GPG-KEY* %{buildroot}%{_sysconfdir}/pki/mock

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/mock/zmrepo-*.cfg
%config(noreplace) %{_sysconfdir}/pki/mock/RPM-GPG-KEY*
%{_bindir}/buildzm.sh

%changelog
* Thu May 31 2018 Andrew Bauer <zonexpertconsulting@outlook.com> - 28-1
- Add support for Fedora 28

* Tue Jun 13 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 26-1
- Add support for Fedora 26, support for Fedora 27 unfinished

* Fri Mar 31 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 25-1
- Redesign for easier management

