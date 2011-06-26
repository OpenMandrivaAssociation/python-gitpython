%define upstream_name GitPython
%define name    python-gitpython
%define version 0.3.1
%define beta    beta2
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Python Git library
License:	BSD
Group: 		Development/Python
Url: 		http://gitorious.org/projects/git-python/
Source0: 	http://pypi.python.org/packages/source/G/GitPython/GitPython-%{version}-%{beta}.tar.gz
BuildRequires:  python-distribute
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
GitPython is a python library used to interact with Git repositories.

GitPython provides object model access to your git repository. Once you have
created a repository object, you can traverse it to find parent commit(s),
trees, blobs, etc.

GitPython is a port of the grit library in Ruby created by Tom Preston-Werner
and Chris Wanstrath

%prep
%setup -q -n git-python-mainline

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGES README.rst LICENSE TODO VERSION
%{python_sitelib}/git
%{python_sitelib}/GitPython-%{version}-py%{pyver}.egg-info
