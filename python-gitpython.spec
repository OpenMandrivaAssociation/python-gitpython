%define module gitpython

Name:		python-gitpython
Version:	3.1.47
Release:	1
Summary:	GitPython is a python library used to interact with Git repositories
License:	BSD
Group:		Development/Python
URL:		https://github.com/gitpython-developers/GitPython
Source0:	%{URL}/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	git-core
BuildRequires:	python%{pyver}dist(gitdb)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
Requires:	git-core
Requires:	python%{pyver}dist(gitdb) >= 4.0.1

%description
GitPython is a python library used to interact with Git repositories.

GitPython provides object model access to your git repository. Once you have
created a repository object, you can traverse it to find parent commit(s),
trees, blobs, etc.

GitPython is a port of the grit library in Ruby created by Tom Preston-Werner
and Chris Wanstrath

%files
%doc AUTHORS README.md
%license LICENSE
%{python_sitelib}/git
%{python_sitelib}/%{module}-%{version}.dist-info
