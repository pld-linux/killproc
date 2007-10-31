Summary:	killproc and assorted tools for boot scripts
Name:		killproc
Version:	2.12
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	3e7b29c10a504364579ddd11fca73ab2
Patch0:		%{name}-suse.patch
BuildRequires:	rpmbuild(macros) >= 1.402
BuildRequires:	showconsole-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_exec_prefix	/

%description
Some useful programs for a replacment of the shell functions daemon
and killproc found in the Linux System V init suite. killproc(8) for
signaling or terminating, checkproc(8) for checking and startproc(8)
for starting processes. Each program has its own manual page.

%prep
%setup -q
%patch0 -p0

%build
%{__make} \
	CC="%{__cc}" \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/fsync
%attr(755,root,root) %{_bindir}/usleep
%attr(755,root,root) %{_sbindir}/checkproc
%attr(755,root,root) %{_sbindir}/pidofproc
%attr(755,root,root) %{_sbindir}/start_daemon
%attr(755,root,root) %{_sbindir}/killproc
%attr(755,root,root) %{_sbindir}/startproc
%{_mandir}/man1/fsync.1*
%{_mandir}/man1/usleep.1*
%{_mandir}/man8/checkproc.8*
%{_mandir}/man8/killproc.8*
%{_mandir}/man8/start_daemon.8
%{_mandir}/man8/pidofproc.8
%{_mandir}/man8/startproc.8*
