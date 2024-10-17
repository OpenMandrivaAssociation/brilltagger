%define name    brilltagger
%define version 1.14
%define tag     1_14
%define release 12

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    Rule based tagger
Source:     http://www.cs.jhu.edu/~brill/RBT%{tag}.tar.bz2
Patch0:     %{name}.makefile.patch
Patch1:     %{name}.no-hardcoded-path-check.patch
# this url no longer work, and it seems it disappeared from internet
URL:        https://www.cs.jhu.edu/~brill/
License:    MIT
Group:      Sciences/Computer science
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
The Brill tagger is a transformation-based part-of-speech tagger.

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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.14-11mdv2011.0
+ Revision: 616838
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 1.14-10mdv2010.0
+ Revision: 424689
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.14-9mdv2009.0
+ Revision: 266402
- rebuild early 2009.0 package (before pixel changes)

* Mon May 26 2008 Michael Scherer <misc@mandriva.org> 1.14-8mdv2009.0
+ Revision: 211372
- bunzip patchs
- add a description

* Sat May 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-7mdv2009.0
+ Revision: 210925
- rebuild
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import brilltagger


* Tue Aug 01 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-5mdv2007.0
- %%mkrel
- fix doc files perms

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-4mdk 
- spec cleanup 

* Thu Jul 08 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.14-3mdk 
- rpmbuilupdate aware

* Fri Jan 16 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.14-2mdk
- fix stupid check for other binaries

* Thu Jan 08 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.14-1mdk
- first mdk release
