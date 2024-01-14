
Name:		stress-ng
Summary:	Tool to load and stress a computer
Version:	0.17.03
Release:	1
License:	GPLv2+
URL:		https://github.com/mer-qa/stress-ng
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	libattr-devel

%description
stress-ng can stress various subsystems of a computer.  It can stress load
CPU, cache, disk, memory, socket and pipe I/O, scheduling and much more.
stress-ng is a re-write of the original stress tool by Amos Waterland but
has many additional features such as specifying the number of bogo operations
to run, execution metrics, a stress verification on memory and compute
operations and considerably more stress mechanisms.

%package doc
Summary:        Documentation and examples for stress-ng
Requires:       %{name} = %{version}

%description doc
This package contains the documentation and examples for stress-ng

%prep
%autosetup -n %{name}-%{version}/%{name}

%build
%make_build

%install
%make_install

rm -rf %{buildroot}%{_datadir}/bash-completion

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/stress-ng

%files doc
%defattr(-, root, root)
%doc README.md
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/example-jobs
