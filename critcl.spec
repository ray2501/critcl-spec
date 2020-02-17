Name:           critcl
Version:        3.1.18
Summary:        Compiled Runtime In Tcl
Release:        0
License:        TCL
Group:          Development/Libraries/Tcl
Url:            https://github.com/andreas-kupries/critcl
BuildRequires:  tcl >= 8.5
BuildRequires:  tcllib
BuildRequires:  gcc
Source:         %{name}-%{version}.tar.gz
Patch0:         build.patch
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
%patch0

%build

%install
export TCLLIBPATH=" %{buildroot}/usr/lib64/tcl/critcl-app3.1.18 %{buildroot}/usr/lib64/tcl/critcl3.1.18 \
%{buildroot}/usr/lib64/tcl/dict841 %{buildroot}/usr/lib64/tcl/lassign841.0.1 \
%{buildroot}/usr/lib64/tcl/lmap841"
tclsh ./build.tcl install %{buildroot}/usr/lib64/tcl

%files
%defattr(-,root,root)
%doc license.terms README.md
%_bindir/*

%files devel
%defattr(-,root,root)
%_libdir/tcl/*
/usr/include/critcl_callback/*

%changelog

