%define debug_package %{nil}

Name:           ayugram-desktop
Version:        %{_version}
Release:        1%{?dist}
Summary:        AyuGram Desktop messaging app

License:        GPLv3
URL:            https://ayugram.one
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  cmake, gcc-c++, qt6-qtbase-devel, libstdc++-devel
Requires:       qt6-qtbase, xdg-utils

%description
AyuGram is a fork of Telegram Desktop with extra features like Ghost Mode and Anti-recall.

%prep
# No prep needed as we build inside the container and just package the result

%install
mkdir -p %{buildroot}/usr/bin
# Stripping debug symbols for a clean final package
strip %{_out_dir}/Telegram
cp %{_out_dir}/Telegram %{buildroot}/usr/bin/ayugram

%files
/usr/bin/ayugram

%changelog
* Sat Feb 28 2026 Radolyn <admin@ayugram.one> - %{_version}-1
- Initial RPM release for AyuGram Desktop
