
Name:		stress-ng
Summary:	Tool to load and stress a computer
Version:	0.10.17
Release:	1
License:	GPLv2+
URL:		http://kernel.ubuntu.com/~cking/stress-ng/
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
%setup -q

%build
make -C stress-ng %{?_smp_mflags}

%install
cd stress-ng
make install DESTDIR="%{buildroot}"

rm -rf %{buildroot}%{_datadir}/bash-completion

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%license stress-ng/COPYING
%{_bindir}/stress-ng

%files doc
%defattr(-, root, root)
%doc stress-ng/README
%{_mandir}/man1/stress-ng.1*
%{_datadir}/stress-ng/example-jobs
