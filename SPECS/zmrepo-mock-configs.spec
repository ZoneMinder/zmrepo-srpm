Name:           zmrepo-mock-configs      
Version:        1.0
Release:        1%{?dist}
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

%build

%install
install -dpm 755 %{buildroot}%{_sysconfdir}/mock
install -pm 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE6} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE7} %{buildroot}%{_sysconfdir}/mock/
install -pm 644 %{SOURCE8} %{buildroot}%{_sysconfdir}/mock/

%post

%postun 

%files
%defattr(-,root,root,-)
%doc GPL

%{_sysconfdir}/mock/*.cfg

%changelog
* Thu May 14 2015 Andrew Bauer <knnniggett@users.sourceforge.net> - 1-1
- Initial Package
