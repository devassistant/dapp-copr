%if 0%{?fedora}
%global         with_python3    1
%endif #fedora

%global shortname dapp

Name:           python-%{shortname}
Version:        0.3.0
Release:        2%{?dist}
Summary:        Implementation of the DevAssistant PingPong library in Python

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

%if 0%{?with_python3}
BuildRequires:  python3-pytest
BuildRequires:  python3-devel
BuildRequires:  python3-jinja2
BuildRequires:  python3-six
BuildRequires:  python3-PyYAML
%endif #fedora

Requires:       python-argparse
Requires:       python-jinja2
Requires:       python-six
Requires:       PyYAML

%description
This is the Python 2 implementation of the DevAssistant PingPong protocol.

%if 0%{?with_python3}
%package -n python3-%{shortname}
Summary:        This is the Python 3 implementation of the DevAssistant PingPong protocol.
Requires:       python3-jinja2
Requires:       python3-six
Requires:       python3-PyYAML

%description -n python3-%{shortname}
This is the Python 3 implementation of the DevAssistant PingPong protocol.
%endif #fedora

%prep
%setup -q -n %{shortname}-%{version}
rm -rf %{name}.egg-info

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
pushd %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
popd
%endif # with_python3

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --root %{buildroot}
popd
%endif # with_python3

%check
%{__python} setup.py test -t py.test

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py test -t py.test
popd
%endif # with_python3

%files
%doc README.rst LICENSE
%{python_sitelib}/%{shortname}
%{python_sitelib}/%{shortname}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{shortname}
%doc README.rst LICENSE
%{python3_sitelib}/%{shortname}
%{python3_sitelib}/%{shortname}-%{version}-py?.?.egg-info

%endif # with_python3
%changelog
* Tue Dec 02 2014 Tomas Radej <tradej@redhat.com> - 0.4.0-2
- Added Python 3 subpackage

* Thu Nov 20 2014 Tomas Radej <tradej@redhat.com> - 0.4.0-1
- Version 0.4.0

