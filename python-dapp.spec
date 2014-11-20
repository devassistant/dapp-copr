%global shortname dapp

Name:           python-%{shortname}
Version:        0.3.0
Release:        1%{?dist}
Summary:        DevAssistant - Making life easier for developers

License:        GPLv3+ and CC-BY-SA
URL:            https://github.com/devassistant/%{shortname}
Source0:        https://pypi.python.org/packages/source/d/%{shortname}/%{shortname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  pytest
BuildRequires:  python2-devel
BuildRequires:  python-argparse
BuildRequires:  python-jinja2
BuildRequires:  python-six
BuildRequires:  PyYAML

Requires:       python-argparse
Requires:       python-jinja2
Requires:       python-six
Requires:       PyYAML

%description
This is the implementation of the DevAssistant PingPong protocol.

%prep
%setup -q -n %{shortname}-%{version}
rm -rf %{name}.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%check
%{__python} setup.py test -t py.test

%files
%doc README LICENSE
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-%{version}-py?.?.egg-info

%changelog
* Thu Nov 20 2014 Tomas Radej <tradej@redhat.com> - 0.4.0
- Version 0.4.0

