
%define name	m2vrequantizer
%define Name	M2VRequantizer
%define version	20030929
%define rel	4

# This is the version that is recommended for the VDR burn plugin.
# Feel free to upgrade after you've tested that the new version
# works with it too.

Summary:	Requantizes MPEG-2 streams
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL+
URL:		http://www.xeatre.tv/community/burn/contrib/
Source:		http://www.xeatre.tv/community/burn/contrib/%Name-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Requantizes MPEG-2 streams without recompressing the files.

This is the version that is recommended for the VDR burn plugin.

%prep
%setup -q -n %Name

%build
%__cc %optflags %{?ldflags} -o requant main.c -lm

%install
rm -rf %{buildroot}

install -D -m755 requant %{buildroot}%{_bindir}/requant

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/requant


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 20030929-4mdv2011.0
+ Revision: 620284
- the mass rebuild of 2010.0 packages

* Sun Jul 12 2009 Anssi Hannula <anssi@mandriva.org> 20030929-3mdv2010.0
+ Revision: 395397
- update license tag for new license policy
- use %%ldflags

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 20030929-2mdv2008.1
+ Revision: 140934
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jul 14 2007 Anssi Hannula <anssi@mandriva.org> 20030929-2mdv2008.0
+ Revision: 51964
- annual rebuild
- replace dead URL
- Import m2vrequantizer



* Fri Jun 16 2006 Anssi Hannula <anssi@mandriva.org> 20030929-1mdv2007.0
- initial Mandriva release
