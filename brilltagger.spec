%define name    brilltagger
%define version 1.14
%define tag     1_14
%define release %mkrel 5

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Rule based tagger
Source:     http://www.cs.jhu.edu/~brill/RBT%{tag}.tar.bz2
Patch0:     %{name}.makefile.patch.bz2
Patch1:     %{name}.no-hardcoded-path-check.patch.bz2
URL:        http://www.cs.jhu.edu/~brill/
License:    MIT
Group:      Sciences/Computer science

%description
This packages needs a description.

%prep
%setup -q -n RULE_BASED_TAGGER_V%{version}
%patch0
%patch1
mkdir Bin
chmod 644 Docs/*

%build
%make RPM_OPT_FLAGS="%{optflags}"

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -m 755 Bin/* %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 644 Bin_and_Data/* %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Docs README COPYRIGHT
%{_bindir}/*
%{_datadir}/%{name}

