# Generated by rust2rpm 10
%bcond_with check
%global debug_package %{nil}

%global crate twoway

Name:           rust-%{crate}
Version:        0.2.1
Release:        2%{?dist}
Summary:        Fast substring search for strings and byte strings

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/twoway
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Fast substring search for strings and byte strings. Optional SSE4.2
acceleration (if detected at runtime) using pcmpestri. Memchr is the only
mandatory dependency. The two way algorithm is also used by rust's libstd
itself, but here it is exposed both for byte strings, using memchr, and
optionally using a SSE4.2 accelerated version.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.rst
%license LICENSE-APACHE LICENSE-MIT
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+all-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+all-devel %{_description}

This package contains library source intended for building other packages
which use "all" feature of "%{crate}" crate.

%files       -n %{name}+all-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+benchmarks-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+benchmarks-devel %{_description}

This package contains library source intended for building other packages
which use "benchmarks" feature of "%{crate}" crate.

%files       -n %{name}+benchmarks-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+galil-seiferas-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+galil-seiferas-devel %{_description}

This package contains library source intended for building other packages
which use "galil-seiferas" feature of "%{crate}" crate.

%files       -n %{name}+galil-seiferas-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+jetscii-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+jetscii-devel %{_description}

This package contains library source intended for building other packages
which use "jetscii" feature of "%{crate}" crate.

%files       -n %{name}+jetscii-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+pattern-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pattern-devel %{_description}

This package contains library source intended for building other packages
which use "pattern" feature of "%{crate}" crate.

%files       -n %{name}+pattern-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+use_std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+use_std-devel %{_description}

This package contains library source intended for building other packages
which use "use_std" feature of "%{crate}" crate.

%files       -n %{name}+use_std-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 23 2019 Josh Stone <jistone@redhat.com> - 0.2.1-1
- Update to 0.2.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 14:03:41 EEST 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.2.0-1
- Initial package
