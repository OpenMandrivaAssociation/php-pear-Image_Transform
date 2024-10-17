%define		_class		Image
%define		_subclass	Transform
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.9.1
Release:	10
Summary:	Standard interface to manipulate images using different libraries
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Image_Transform/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Patch0:		Image_Transform-IMAGETYPE_fix.diff
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

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

%prep
%setup -q -c
%patch0 -p0
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-8mdv2012.0
+ Revision: 742026
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-7
+ Revision: 679379
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-6mdv2011.0
+ Revision: 613696
- the mass rebuild of 2010.1 packages

* Fri Dec 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.9.1-5mdv2010.1
+ Revision: 473550
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.9.1-4mdv2010.0
+ Revision: 441218
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-3mdv2009.1
+ Revision: 322257
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-2mdv2009.0
+ Revision: 236903
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-1mdv2008.0
+ Revision: 15770
- rediffed P0
- 0.9.1


* Sat Mar 10 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-2mdv2007.1
+ Revision: 140441
- also add the patch
- fix deps

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-1mdv2007.1
+ Revision: 81984
- Import php-pear-Image_Transform

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.0-1mdk
- 0.9.0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.8-1mdk
- initial Mandriva package (PLD import)

