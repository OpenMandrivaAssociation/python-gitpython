%define upstream_name GitPython

Name: 		python-gitpython
Version: 	2.1.11
Release: 	1
Summary: 	Python Git library
License:	BSD
Group: 		Development/Python
Url: 		https://github.com/gitpython-developers/GitPython
Source0: 	https://github.com/gitpython-developers/GitPython/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  python-distribute
BuildArch:      noarch

%description
GitPython is a python library used to interact with Git repositories.

GitPython provides object model access to your git repository. Once you have
created a repository object, you can traverse it to find parent commit(s),
trees, blobs, etc.

GitPython is a port of the grit library in Ruby created by Tom Preston-Werner
and Chris Wanstrath

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES README.rst LICENSE TODO VERSION
%{python_sitelib}/git
%{python_sitelib}/GitPython-%{version}-py%{py_ver}.egg-info
