#
# Conditional build:
%bcond_without	ffmpeg			# build with ffmpeg for thumbnails and previews
%bcond_without	freeimage		# build with freeimage to manage thumbnails/previews
%bcond_without	fuse			# build megafuse
%bcond_without	libmediainfo	# build with libmediainfo for media file attributes

Summary:	Command Line Interactive and Scriptable Application to access MEGA
Name:		megacmd
Version:	1.3.0
Release:	1
# https://github.com/meganz/MEGAcmd/commit/b366c77370c277223be123e05e5ef15fafbce185#r31261647
License:	BSD 2-Clause "Simplified" License
Group:		Applications
# Releases: https://github.com/meganz/MEGAcmd/releases
Source0:	https://github.com/meganz/MEGAcmd/archive/%{version}_Linux/%{name}-%{version}.tar.gz
# Source0-md5:	c308194923ff1114ba0d01ff363e30bf
Source1:	https://github.com/meganz/sdk/archive/b2948c7c7/mega-sdk-v3.7.0-18-gb2948c7c7.tar.gz
# Source1-md5:	8668b1089f0dd290959e1059cee3508d
URL:		https://mega.nz/
%{?with_freeimage:BuildRequires:	FreeImage-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	c-ares-devel
BuildRequires:	cryptopp-devel
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel}
%{?with_fuse:BuildRequires:	libfuse-devel}
%{?with_mediainfo:BuildRequires:	libmediainfo-devel}
BuildRequires:	libraw-devel
BuildRequires:	libsodium-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libuv-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-cxx-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	sqlite3-devel
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MEGAcmd provides non UI access to MEGA services. It intends to offer
all the functionality with your MEGA account via commands. It features
synchronization and backup of local folders into your MEGA account.

%package libs
Summary:	Shared libmega library
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description libs
Shared libmega library.

%package devel
Summary:	Header files for %{name} library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki %{name}
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for %{name} library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki %{name}.

%package fuse
Summary:	megafuse
Group:		Libraries

%description fuse
megafuse.

%prep
%setup -q -n MEGAcmd-%{version}_Linux -a1
mv sdk-*/* sdk

%build
autoreconf -vif
%configure \
	%{__with_without ffmpeg} \
	%{__with_without freeimage} \
	%{__with_without fuse} \
	%{__with_without libmediainfo} \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libmega.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
/etc/bash_completion.d/megacmd_completion.sh
%attr(755,root,root) %{_bindir}/mega-attr
%attr(755,root,root) %{_bindir}/mega-backup
%attr(755,root,root) %{_bindir}/mega-cancel
%attr(755,root,root) %{_bindir}/mega-cat
%attr(755,root,root) %{_bindir}/mega-cd
%attr(755,root,root) %{_bindir}/mega-cmd
%attr(755,root,root) %{_bindir}/mega-cmd-server
%attr(755,root,root) %{_bindir}/mega-confirm
%attr(755,root,root) %{_bindir}/mega-confirmcancel
%attr(755,root,root) %{_bindir}/mega-cp
%attr(755,root,root) %{_bindir}/mega-debug
%attr(755,root,root) %{_bindir}/mega-deleteversions
%attr(755,root,root) %{_bindir}/mega-df
%attr(755,root,root) %{_bindir}/mega-du
%attr(755,root,root) %{_bindir}/mega-errorcode
%attr(755,root,root) %{_bindir}/mega-exclude
%attr(755,root,root) %{_bindir}/mega-exec
%attr(755,root,root) %{_bindir}/mega-export
%attr(755,root,root) %{_bindir}/mega-find
%attr(755,root,root) %{_bindir}/mega-ftp
%attr(755,root,root) %{_bindir}/mega-get
%attr(755,root,root) %{_bindir}/mega-graphics
%attr(755,root,root) %{_bindir}/mega-help
%attr(755,root,root) %{_bindir}/mega-https
%attr(755,root,root) %{_bindir}/mega-import
%attr(755,root,root) %{_bindir}/mega-invite
%attr(755,root,root) %{_bindir}/mega-ipc
%attr(755,root,root) %{_bindir}/mega-killsession
%attr(755,root,root) %{_bindir}/mega-lcd
%attr(755,root,root) %{_bindir}/mega-log
%attr(755,root,root) %{_bindir}/mega-login
%attr(755,root,root) %{_bindir}/mega-logout
%attr(755,root,root) %{_bindir}/mega-lpwd
%attr(755,root,root) %{_bindir}/mega-ls
%attr(755,root,root) %{_bindir}/mega-mediainfo
%attr(755,root,root) %{_bindir}/mega-mkdir
%attr(755,root,root) %{_bindir}/mega-mount
%attr(755,root,root) %{_bindir}/mega-mv
%attr(755,root,root) %{_bindir}/mega-passwd
%attr(755,root,root) %{_bindir}/mega-permissions
%attr(755,root,root) %{_bindir}/mega-preview
%attr(755,root,root) %{_bindir}/mega-proxy
%attr(755,root,root) %{_bindir}/mega-put
%attr(755,root,root) %{_bindir}/mega-pwd
%attr(755,root,root) %{_bindir}/mega-quit
%attr(755,root,root) %{_bindir}/mega-reload
%attr(755,root,root) %{_bindir}/mega-rm
%attr(755,root,root) %{_bindir}/mega-session
%attr(755,root,root) %{_bindir}/mega-share
%attr(755,root,root) %{_bindir}/mega-showpcr
%attr(755,root,root) %{_bindir}/mega-signup
%attr(755,root,root) %{_bindir}/mega-speedlimit
%attr(755,root,root) %{_bindir}/mega-sync
%attr(755,root,root) %{_bindir}/mega-thumbnail
%attr(755,root,root) %{_bindir}/mega-transfers
%attr(755,root,root) %{_bindir}/mega-tree
%attr(755,root,root) %{_bindir}/mega-userattr
%attr(755,root,root) %{_bindir}/mega-users
%attr(755,root,root) %{_bindir}/mega-version
%attr(755,root,root) %{_bindir}/mega-webdav
%attr(755,root,root) %{_bindir}/mega-whoami
%attr(755,root,root) %{_bindir}/megacli
%attr(755,root,root) %{_bindir}/megasimplesync

%if %{with fuse}
%files fuse
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/megafuse
%endif

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmega.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmega.so.30700

%files devel
%defattr(644,root,root,755)
%{_includedir}/mega
%{_includedir}/mega.h
%{_includedir}/megaapi.h
%{_includedir}/megaapi_impl.h
%{_libdir}/libmega.so
%{_pkgconfigdir}/libmega.pc
