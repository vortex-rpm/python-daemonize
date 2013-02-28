%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global srcname daemonize

Name:           python-%{srcname}
Version:        2.1.1
Release:        1.vortex%{?dist}
Summary:        Library to enable your code run as a daemon process on Unix-like systems
Vendor:         Vortex RPM

Group:          Development/Libraries
License:        MIT
URL:            https://github.com/thesharp/daemonize
Source0:        http://pypi.python.org/packages/source/p/pip/%{srcname}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-setuptools

%description
daemonize is a library for writing system daemons in Python. It has some bits
from daemonize.sourceforge.net. It is distributed under MIT license.

%prep
%setup -q -n %{srcname}-%{version}

%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{python_sitelib}/%{name}*

%changelog
* Thu Feb 28 2013 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 2.1.1-1.vortex
- Initial packaging.

