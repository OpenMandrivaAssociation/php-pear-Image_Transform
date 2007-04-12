%define		_class		Image
%define		_subclass	Transform
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - standard interface to manipulate images using different libraries
Name:		php-pear-%{_pearname}
Version:	0.9.0
Release:	%mkrel 2
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Image_Transform/
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
Patch0:		Image_Transform-0.9.0-IMAGETYPE_fix.diff
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package was written to provide a simpler and cross-library
interface to doing image transformations and manipulations.

It provides :
 - support for GD, ImageMagick, Imagick and NetPBM,
 - files related functions,
 - addText,
 - Scale (by length, percentage, maximum X/Y),
 - Resize,
 - Rotate (custom angle),
 - Add border (soon),
 - Add shadow (soon).

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c
%patch0 -p0

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Driver/Imagick

install %{_pearname}-%{version}/%{_subclass}.php %{buildroot}%{_datadir}/pear/%{_class}/
install %{_pearname}-%{version}/Driver/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Driver
install %{_pearname}-%{version}/Driver/Imagick/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Driver/Imagick

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%dir %{_datadir}/pear/%{_class}/%{_subclass}
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Driver
%dir %{_datadir}/pear/%{_class}/%{_subclass}/Driver/Imagick
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/Driver/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/Driver/Imagick/*.php
%{_datadir}/pear/packages/%{_pearname}.xml


