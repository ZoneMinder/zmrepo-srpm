Name:           zmrepo-mock-configs      
Version:        1.0
Release:        2%{?dist}
Summary:        Zmrepo mock config files

Group:          System Environment/Daemons 
License:        GPLv2

URL:            https://github.com/knnniggett/zmrepo
Source0:        GPL
SOURCE1:        zmrepo-el6-i386.cfg
Source2:        zmrepo-el6-x86_64.cfg
Source3:	zmrepo-el7-x86_64.cfg
Source4:	zmrepo-f20-i386.cfg
Source5:	zmrepo-f20-x86_64.cfg
Source6:	zmrepo-f21-i386.cfg
Source7:	zmrepo-f21-x86_64.cfg
Source8:	zmrepo-f21-armhfp.cfg
Source9:	zmrepo-f22-i386.cfg
SOURCE10:	zmrepo-f22-x86_64.cfg
SOURCE11:	zmrepo-f22-armhfp.cfg
SOURCE12:	buildzm.sh
SOURCE13:	RPM-GPG-KEY-EPEL-6-zmrepo
SOURCE14:	RPM-GPG-KEY-EPEL-7-zmrepo
SOURCE15:	RPM-GPG-KEY-rpmfusion-free-el-6-zmrepo
SOURCE16:	RPM-GPG-KEY-rpmfusion-free-fedora-20-zmrepo
SOURCE17:	RPM-GPG-KEY-rpmfusion-free-fedora-21-zmrepo
SOURCE18:	RPM-GPG-KEY-rpmfusion-free-fedora-22-zmrepo
SOURCE19:	RPM-GPG-KEY-zmrepo

BuildArch:     noarch
Requires:      mock 

%description
This package contains zmrepo config files for mock.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .
install -pm 644 %{SOURCE2} .
install -pm 644 %{SOURCE3} .
install -pm 644 %{SOURCE4} .
install -pm 644 %{SOURCE5} .
install -pm 644 %{SOURCE6} .
install -pm 644 %{SOURCE7} .
install -pm 644 %{SOURCE8} .
install -pm 644 %{SOURCE9} .
install -pm 644 %{SOURCE10} .
install -pm 644 %{SOURCE11} .
install -pm 644 %{SOURCE12} .
install -pm 644 %{SOURCE13} .
install -pm 644 %{SOURCE14} .
install -pm 644 %{SOURCE15} .
install -pm 644 %{SOURCE16} .
install -pm 644 %{SOURCE17} .
install -pm 644 %{SOURCE18} .
install -pm 644 %{SOURCE19} .

%build

%install
# Create folders in the buildroot
mkdir -p %{buildroot}%{_sysconfdir}/mock
mkdir -p %{buildroot}%{_sysconfdir}/pki/mock
mkdir -p %{buildroot}%{_bindir}

# Install mock config files into mock config folder
install -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE8} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE9} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE10} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE11} %{buildroot}%{_sysconfdir}/mock/

# Install GPG keys into mock keys folder
install -pm 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE14} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE15} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE16} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE17} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE18} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE19} %{buildroot}%{_sysconfdir}/pki/mock/

# Install build script into bin
install -pm 755 %{SOURCE12} %{buildroot}%{_bindir}/

%post

%postun 

%files
%defattr(-,root,root,-)
%doc GPL

%config(noreplace) %{_sysconfdir}/mock/*.cfg
%config(noreplace) %{_sysconfdir}/pki/mock/*
%{_bindir}/buildzm.sh

%changelog
* Tue May 26 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 1-2
- Add support for Fedora 22

* Thu May 14 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 1-1
- Initial Package
