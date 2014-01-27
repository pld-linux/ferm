Summary:	For Easy Rule Making
Name:		ferm
Version:	2.2
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://ferm.foo-projects.org/download/2.2/%{name}-%{version}.tar.gz
# Source0-md5:	f2d6e6950d90c768ef9e1f055a01fba2
URL:		http://ferm.foo-projects.org/
BuildRequires:	rpmbuild(macros) >= 1.671
BuildRequires:	systemd-devel
Requires:	systemd-units >= 38
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ferm is a tool to maintain complex firewalls, without having the
trouble to rewrite the complex rules over and over again. Ferm allows
the entire firewall rule set to be stored in a separate file, and to
be loaded with one command. The firewall configuration resembles
structured programming-like language, which can contain levels and
lists.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	SERVICEDIR=$RPM_BUILD_ROOT%{systemdunitdir}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README TODO NEWS examples/
%attr(755,root,root) %{_sbindir}/import-ferm
%attr(755,root,root) %{_sbindir}/ferm
%{_mandir}/man1/ferm.1*
%{_mandir}/man1/import-ferm.1*
%{systemdunitdir}/%{name}.service
