
%define name	m2vrequantizer
%define Name	M2VRequantizer
%define version	20030929
%define rel	2

# This is the version that is recommended for the VDR burn plugin.
# Feel free to upgrade after you've tested that the new version
# works with it too.

Summary:	Requantizes MPEG-2 streams
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.xeatre.tv/community/burn/contrib/
Source:		http://www.xeatre.tv/community/burn/contrib/%Name-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Requantizes MPEG-2 streams without recompressing the files.

This is the version that is recommended for the VDR burn plugin.

%prep
%setup -q -n %Name

%build
%__cc %optflags -lm -o requant main.c

%install
rm -rf %{buildroot}

install -D -m755 requant %{buildroot}%{_bindir}/requant

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/requant
