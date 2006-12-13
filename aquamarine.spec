Name:           aquamarine
Url:            http://www.beryl-project.org/
License:        GPL
Group:          User Interface/Desktops
Version:        0.1.3
Release:        1%{?dist}

Summary:        Themeable window decorator and compositing manager for Beryl
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Source0:        http://releases.beryl-project.org/%{version}/%{name}-%{version}.tar.bz2
Patch0:         aquamarine-0.1.3-Makefile.patch

# libdrm is not available on these arches
ExcludeArch:    s390 s390x ppc64

Requires:       beryl-core >= %{version}

BuildRequires:  beryl-core-devel >= %{version}
BuildRequires:  qt-devel, kdelibs-devel, kdebase-devel
BuildRequires:  libtool


%description
Aquamarine is themeable window decorator and compositing
manager for Beryl. Launch Theme Manager from
beryl-manager to change themes. Aquamarine is intended
for use with KDE.

%prep
%setup -q
%patch0 -p1 -b .make

%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -type f -name "*.a" -o -name "*.la" | xargs rm -f


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/aquamarine


%changelog
* Tue Dec 12 2006 Jarod Wilson <jwilson@redhat.com> 0.1.3-1
- New upstream release

* Fri Nov 17 2006 Jarod Wilson <jwilson@redhat.com> 0.1.2-3
- Remove R: qt, kdelibs, rely on auto-gen lib deps

* Thu Nov 16 2006 Jarod Wilson <jwilson@redhat.com> 0.1.2-2
- Trim BR:

* Fri Nov 10 2006 Jarod Wilson <jwilson@redhat.com> 0.1.2-1
- Initial build
