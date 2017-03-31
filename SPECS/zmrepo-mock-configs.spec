# Version tracks the most recent supported version of Fedora

Name:           zmrepo-mock-configs      
Version:        25
Release:        1%{?dist}
Summary:        Zmrepo mock config files

Group:          System Environment/Daemons 
License:        GPLv2

URL:            https://github.com/knnniggett/zmrepo
Source0:        https://github.com/knnniggett/zmrepo/archive/master.tar.gz#/zmrepo-mock-configs.tar.gz

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
install -pm 0644 SOURCES/zmrepo-*.cfg %{buildroot}%{_sysconfdir}/mock

# Install build script into bin
install -pm 755 SOURCES/buildzm.sh %{buildroot}%{_bindir}/

# Install GPG keys into mock keys folder
install -pm 0644 SOURCES/RPM-GPG-KEY* %{buildroot}%{_sysconfdir}/pki/mock

%post

%postun 

%files
%license GPL
%config(noreplace) %{_sysconfdir}/mock/zmrepo-*.cfg
%config(noreplace) %{_sysconfdir}/pki/mock/RPM-GPG-KEY*
%{_bindir}/buildzm.sh

%changelog
* Fri Mar 31 2017 Andrew Bauer <zonexpertconsulting@outlook.com> - 25-1
- Redesign for easier management

