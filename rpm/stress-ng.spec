
Name:		stress-ng
Summary:	Tool to load and stress a computer
Version:	0.04.15
Release:	1
License:	GPLv2
Group:		Development/Tools
URL:		http://kernel.ubuntu.com/~cking/stress-ng/
Source0:	%{name}-%{version}.tar.gz
Patch0:		0001-Remove-stress-key-test-because-we-don-t-have-keyutil.patch

BuildRequires:	libattr-devel

%description
stress-ng can stress various subsystems of a computer.  It can stress load
CPU, cache, disk, memory, socket and pipe I/O, scheduling and much more.
stress-ng is a re-write of the original stress tool by Amos Waterland but
has many additional features such as specifying the number of bogo operations
to run, execution metrics, a stress verification on memory and compute
operations and considerably more stress mechanisms.

%prep
%setup -q
%patch0 -p1 -d stress-ng

%build
make -C stress-ng %{?jobs:-j%jobs}

%install
cd stress-ng
make install DESTDIR="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc stress-ng/README stress-ng/COPYING
%doc %{_mandir}/man1/stress-ng.1*
%{_bindir}/stress-ng
