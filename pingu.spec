Name:           pingu
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        ping command but with pingu
License:        MIT
URL:            https://github.com/KyleGospo/pingu

Source:         {{{ git_dir_pack }}}

BuildRequires:  golang
BuildRequires:  git

%description
ping command implementation but with pingu ascii art

# Disable debug packages
%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build
go build .

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 ./%{name} %{buildroot}/%{_bindir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
{{{ git_dir_changelog }}}