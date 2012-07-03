Summary:	CIM schema files for Small Footprint CIM Broker
Summary(pl.UTF-8):	Pliki schematów CIM dla SFCB (brokera CIM)
Name:		sblim-sfcb-schema
Version:	2.26.0
Release:	1
License:	Distributed Management Task Force
Group:		Applications/System
Source0:	http://dmtf.org/sites/default/files/cim/cim_schema_v2260/cim_schema_2.26.0Final-MOFs.zip
# Source0-md5:	c59d0528ea78df22b9d323bf06bda78c
URL:		http://dmtf.org/standards/cim/schemas
Requires(post):	sblim-sfcb
Requires:	sblim-sfcb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Distributed Management Task Force (DMTF) Common Information Model
(CIM) schema files that can be used with the Small Footprint CIM
Broker.

%description -l pl.UTF-8
Pliki schematów CIM (Common Information Model) stworzone przez DMTF
(Distributed Management Task Force), które można używać z brokerem
CIM SFCB.

%prep
%setup -q -c

%install
install -d $RPM_BUILD_ROOT%{_datadir}/sfcb/CIM

cp -a * $RPM_BUILD_ROOT%{_datadir}/sfcb/CIM
ln -sf cim_schema_%{version}.mof $RPM_BUILD_ROOT%{_datadir}/sfcb/CIM/CIM_Schema.mof

%clean
rm -rf $RPM_BUILD_ROOT 

%post
sfcbrepos -f 2>/dev/null || :

%files
%defattr(644,root,root,755)
%{_datadir}/sfcb/CIM
