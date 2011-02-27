%include	/usr/lib/rpm/macros.php
%define		status		stable
%define		pearname	PHPUnit_MockObject
Summary:	%{pearname} - Mock Object library for PHPUnit
Name:		php-phpunit-PHPUnit_MockObject
Version:	1.0.8
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.phpunit.de/get/%{pearname}-%{version}.tgz
# Source0-md5:	e597029c1b9f1de0a240b7c46c6e0f6c
URL:		http://pear.phpunit.de/
BuildRequires:	php-channel(pear.phpunit.de)
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR >= 1:1.9.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.571
Requires:	php-channel(pear.phpunit.de)
Requires:	php-pear
Requires:	php-phpunit-Text_Template >= 1.0.0
Requires:	php-reflection
Requires:	php-spl
Suggests:	php-soap
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
