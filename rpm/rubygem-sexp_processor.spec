#
# spec file for package rubygem-sexp_processor (Version 3.0.5)
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
Name:           rubygem-sexp_processor
Version:        3.0.5
Release:        0
%define mod_name sexp_processor
#
Group:          Development/Languages/Ruby
License:        GPLv2+ or Ruby
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  rubygems_with_buildroot_patch
%rubygems_requires
#
Url:            http://rubyforge.org/projects/parsetree/
Source:         %{mod_name}-%{version}.gem
#
Summary:        Generic sexp processing tools for Ruby
%description
sexp_processor branches from ParseTree bringing all the generic sexp
processing tools with it. Sexp, SexpProcessor, Environment, etc... all
for your language processing pleasure.

%prep
%build
%install
%gem_install %{S:0}
# fix /usr/local/bin/ruby usage
ruby -p -i -e 'gsub(%r{#!.*/bin/ruby}, "#!/usr/bin/ruby")' \
  %{buildroot}/%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/test/*.rb

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/ruby/gems/%{rb_ver}/cache/%{mod_name}-%{version}.gem
%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_name}-%{version}/
%{_libdir}/ruby/gems/%{rb_ver}/specifications/%{mod_name}-%{version}.gemspec
%doc %{_libdir}/ruby/gems/%{rb_ver}/doc/%{mod_name}-%{version}/

%changelog
