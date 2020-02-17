#!/usr/bin/tclsh

set arch "x86_64"
set base "critcl-3.1.18"
set fileurl "https://github.com/andreas-kupries/critcl/archive/3.1.18.tar.gz"

set var [list wget $fileurl -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES
file copy -force build.patch build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb critcl.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete $base.tar.gz
