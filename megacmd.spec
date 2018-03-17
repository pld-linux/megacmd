Summary:	Command Line Interactive and Scriptable Application to access MEGA
Name:		megacmd
Version:	0.9.8
Release:	0.1
License:	Freeware
Group:		Applications
Source0:	https://github.com/meganz/MEGAcmd/archive/%{version}/%{name}-%{version}.tar.gz
Source1:	https://github.com/meganz/sdk/archive/5d211ac6/mega-sdk-v3.2.8-209-g5d211ac6.tar.gz
URL:		https://mega.nz/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MEGAcmd provides non UI access to MEGA services. It intends to offer
all the functionality with your MEGA account via commands. It features
synchronization and backup of local folders into your MEGA account.

%prep
%setup -q -n MEGAcmd-%{version} -a1
mv sdk-*/* sdk
%patch0 -p1

%build
autoreconf -vif
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CREDITS.md LICENCE.md
%attr(755,root,root) %{_bindir}/%{name}
