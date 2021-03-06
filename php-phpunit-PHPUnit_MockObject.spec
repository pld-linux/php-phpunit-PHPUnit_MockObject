%define		status		stable
%define		pearname	PHPUnit_MockObject
Summary:	%{pearname} - Mock Object library for PHPUnit
Name:		php-phpunit-PHPUnit_MockObject
Version:	1.2.3
Release:	2
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	401bb1092279f75cfb984b5a4be83c0a
URL:		http://pear.phpunit.de/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php(reflection)
Requires:	php(spl)
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
Requires:	php-phpunit-Text_Template >= 1.1.1
Suggests:	php(soap)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mock Object library for PHPUnit

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%{php_pear_dir}/PHPUnit/Framework/MockObject
