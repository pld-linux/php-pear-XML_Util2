# $Revision: 1.31 $, $Date: 2011/04/10 20:45:35 $
%define		status		alpha
%define		pearname	XML_Util2
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - XML utility class
Name:		php-pear-XML_Util2
Version:	0.2.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	911743de3076f2a077fa2617e22d5f1d
URL:		http://pear.php.net/package/XML_Util2/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(pcre)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Selection of methods that are often needed when working with XML
documents. Functionality includes creating of attribute lists from
arrays, creation of tags, validation of XML names and more.

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

mv docs/XML_Util2/examples .

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/XML/Util2.php
%{php_pear_dir}/XML/Util2
%{_examplesdir}/%{name}-%{version}
