Name:           aquamarine
Version:        0.12.1
Release:        %autorelease
Summary:        A very light linux rendering backend library
License:        BSD-3-Clause
URL:            https://github.com/hyprwm/aquamarine
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  mesa-libEGL-devel

BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(hwdata)
BuildRequires:  pkgconfig(hyprutils) >= 0.8.0
BuildRequires:  cmake(hyprwayland-scanner) >= 0.4.0
BuildRequires:  pkgconfig(libdisplay-info)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libseat)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Development files for %{name}.

%prep
%autosetup -p1
# hyprwayland-scanner generates zero-length VTable arrays in protocol code
# which are a hard error under -Wpedantic in GCC; CMakeLists appends -Wpedantic
# after RPM flags so we can't override it via optflags
sed -i 's/-Wpedantic//' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md docs/env.md
%{_libdir}/lib%{name}.so.%{version}
%{_libdir}/lib%{name}.so.11

%files devel
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
