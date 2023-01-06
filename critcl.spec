%{!?directory:%define directory /usr}

Name:           critcl
Version:        3.2
Summary:        Compiled Runtime In Tcl
Release:        0
License:        TCL
Group:          Development/Libraries/Tcl
Url:            https://github.com/andreas-kupries/critcl
BuildRequires:  tcl >= 8.6
BuildRequires:  tcllib
BuildRequires:  gcc
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
CriTcl is a system to build C extension packages for Tcl on the fly,
from C code embedded within Tcl scripts, for all who wish to make their
code go faster.

%package devel
Summary:        Development package for Critcl
Group:          Development/Libraries/Tcl
Requires:       %{name} = %version

%description devel
CriTcl is a system to build C extension packages for Tcl on the fly,
from C code embedded within Tcl scripts, for all who wish to make their
code go faster.
 
This package contains the files needed to compile programs.

%prep
%setup -q

%build

%install
export TCLLIBPATH=" %{buildroot}/usr/lib64/tcl/critcl-app3.2 %{buildroot}/usr/lib64/tcl/critcl3.2"
tclsh ./build.tcl install --dest-dir %{buildroot}  --lib-dir /usr/lib64/tcl

%files
%defattr(-,root,root)
%doc license.terms README.md
%_bindir/*

%files devel
%defattr(-,root,root)
%_libdir/tcl/*
%{directory}/include/critcl_callback
%{directory}/include/critcl_callback/callback.h
%{directory}/include/critcl_callback/critcl_callback.decls
%{directory}/include/critcl_callback/critcl_callbackDecls.h
%{directory}/include/critcl_callback/critcl_callbackStubLib.h

%changelog

