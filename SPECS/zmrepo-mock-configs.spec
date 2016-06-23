Name:           zmrepo-mock-configs      
Version:        1.0
Release:        3%{?dist}
Summary:        Zmrepo mock config files

Group:          System Environment/Daemons 
License:        GPLv2

URL:            https://github.com/knnniggett/zmrepo
Source0:        GPL

Source1:        zmrepo-el6-i386.cfg
Source2:        zmrepo-el6-x86_64.cfg
Source3:	zmrepo-el7-x86_64.cfg
Source4:	zmrepo-f20-i386.cfg
Source5:	zmrepo-f20-x86_64.cfg
Source6:	zmrepo-f21-i386.cfg
Source7:	zmrepo-f21-x86_64.cfg
Source8:	zmrepo-f21-armhfp.cfg
Source9:	zmrepo-f22-i386.cfg
Source10:	zmrepo-f22-x86_64.cfg
Source11:	zmrepo-f22-armhfp.cfg
Source12:	zmrepo-f23-i386.cfg
Source13:	zmrepo-f23-x86_64.cfg
Source14:	zmrepo-f23-armhfp.cfg

Source15:	buildzm.sh

Source16:	RPM-GPG-KEY-EPEL-6-zmrepo
Source17:	RPM-GPG-KEY-EPEL-7-zmrepo
Source18:	RPM-GPG-KEY-rpmfusion-free-el-6-zmrepo
Source19:	RPM-GPG-KEY-rpmfusion-free-fedora-20-zmrepo
Source20:	RPM-GPG-KEY-rpmfusion-free-fedora-21-zmrepo
Source21:	RPM-GPG-KEY-rpmfusion-free-fedora-22-zmrepo
Source22:	RPM-GPG-KEY-rpmfusion-free-fedora-23-zmrepo
Source23:	RPM-GPG-KEY-zmrepo

Source24:	zmrepo-f24-i386.cfg
Source25:	zmrepo-f24-x86_64.cfg
Source26:	zmrepo-f24-armhfp.cfg
Source27:	RPM-GPG-KEY-rpmfusion-free-fedora-24-zmrepo

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
install -pm 644 %{SOURCE20} .
install -pm 644 %{SOURCE21} .
install -pm 644 %{SOURCE22} .
install -pm 644 %{SOURCE23} .
install -pm 644 %{SOURCE24} .
install -pm 644 %{SOURCE25} .
install -pm 644 %{SOURCE26} .
install -pm 644 %{SOURCE27} .

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
install -pm 644 %{SOURCE12} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE14} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE24} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE25} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE26} %{buildroot}%{_sysconfdir}/mock/

# Install build script into bin
install -pm 755 %{SOURCE15} %{buildroot}%{_bindir}/

# Install GPG keys into mock keys folder
install -pm 644 %{SOURCE16} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE17} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE18} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE19} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE20} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE21} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE22} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE23} %{buildroot}%{_sysconfdir}/pki/mock/
install -pm 644 %{SOURCE27} %{buildroot}%{_sysconfdir}/pki/mock/

%post

%postun 

%files
%defattr(-,root,root,-)
%doc GPL

%config(noreplace) %{_sysconfdir}/mock/*.cfg
%config(noreplace) %{_sysconfdir}/pki/mock/*
%{_bindir}/buildzm.sh

%changelog
* Wed Jun 22 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 1-4
- Add support for Fedora 24

* Mon Nov 16 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 1-3
- Add support for Fedora 23

* Tue May 26 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 1-2
- Add support for Fedora 22

* Thu May 14 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 1-1
- Initial Package
