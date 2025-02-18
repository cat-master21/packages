# Generated by rust2rpm 23
%bcond_without check

%global crate tectonic

Name:           rust-tectonic
Version:        0.14.1
Release:        1%{?dist}
Summary:        Modernized, complete, embeddable TeX/LaTeX engine

License:        MIT
URL:            https://crates.io/crates/tectonic
Source:         %{crates_source}

BuildRequires:  pkgconfig(fontconfig) g++ libicu-devel freetype-devel openssl-devel graphite2-devel anda-srpm-macros rust-packaging >= 21

%global _description %{expand:
Modernized, complete, embeddable TeX/LaTeX engine. Tectonic is forked from the
XeTeX extension to the classic “Web2C” implementation of TeX and uses the
TeXLive distribution of support files.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%doc CARGO_README.md
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%{_bindir}/tectonic

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CARGO_README.md
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+external-harfbuzz-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+external-harfbuzz-devel %{_description}

This package contains library source intended for building other packages which
use the "external-harfbuzz" feature of the "%{crate}" crate.

%files       -n %{name}+external-harfbuzz-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+geturl-curl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+geturl-curl-devel %{_description}

This package contains library source intended for building other packages which
use the "geturl-curl" feature of the "%{crate}" crate.

%files       -n %{name}+geturl-curl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+geturl-reqwest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+geturl-reqwest-devel %{_description}

This package contains library source intended for building other packages which
use the "geturl-reqwest" feature of the "%{crate}" crate.

%files       -n %{name}+geturl-reqwest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+native-tls-vendored-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+native-tls-vendored-devel %{_description}

This package contains library source intended for building other packages which
use the "native-tls-vendored" feature of the "%{crate}" crate.

%files       -n %{name}+native-tls-vendored-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+profile-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+profile-devel %{_description}

This package contains library source intended for building other packages which
use the "profile" feature of the "%{crate}" crate.

%files       -n %{name}+profile-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serialization-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serialization-devel %{_description}

This package contains library source intended for building other packages which
use the "serialization" feature of the "%{crate}" crate.

%files       -n %{name}+serialization-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tectonic_docmodel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tectonic_docmodel-devel %{_description}

This package contains library source intended for building other packages which
use the "tectonic_docmodel" feature of the "%{crate}" crate.

%files       -n %{name}+tectonic_docmodel-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+toml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+toml-devel %{_description}

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%files       -n %{name}+toml-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep_online

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
