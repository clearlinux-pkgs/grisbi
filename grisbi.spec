#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : grisbi
Version  : 1.2.2
Release  : 2
URL      : https://sourceforge.net/projects/grisbi/files/grisbi%20stable/1.2.x/1.2.2/grisbi-1.2.2.tar.bz2
Source0  : https://sourceforge.net/projects/grisbi/files/grisbi%20stable/1.2.x/1.2.2/grisbi-1.2.2.tar.bz2
Summary  : Personal finance manager
Group    : Development/Tools
License  : GPL-2.0
Requires: grisbi-bin = %{version}-%{release}
Requires: grisbi-data = %{version}-%{release}
Requires: grisbi-license = %{version}-%{release}
Requires: grisbi-locales = %{version}-%{release}
Requires: grisbi-man = %{version}-%{release}
BuildRequires : gettext
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libgsf-1)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(zlib)

%description
Grisbi helps you to manage your personal finances with Linux.

%package bin
Summary: bin components for the grisbi package.
Group: Binaries
Requires: grisbi-data = %{version}-%{release}
Requires: grisbi-license = %{version}-%{release}

%description bin
bin components for the grisbi package.


%package data
Summary: data components for the grisbi package.
Group: Data

%description data
data components for the grisbi package.


%package doc
Summary: doc components for the grisbi package.
Group: Documentation
Requires: grisbi-man = %{version}-%{release}

%description doc
doc components for the grisbi package.


%package license
Summary: license components for the grisbi package.
Group: Default

%description license
license components for the grisbi package.


%package locales
Summary: locales components for the grisbi package.
Group: Default

%description locales
locales components for the grisbi package.


%package man
Summary: man components for the grisbi package.
Group: Default

%description man
man components for the grisbi package.


%prep
%setup -q -n grisbi-1.2.2
cd %{_builddir}/grisbi-1.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580940304
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1580940304
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/grisbi
cp %{_builddir}/grisbi-1.2.2/COPYING %{buildroot}/usr/share/package-licenses/grisbi/74a8a6531a42e124df07ab5599aad63870fa0bd4
%make_install
%find_lang grisbi

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/grisbi

%files data
%defattr(-,root,root,-)
/usr/share/applications/grisbi.desktop
/usr/share/glib-2.0/schemas/org.gtk.grisbi.gschema.xml
/usr/share/grisbi/categories/C/00_general.cgsb
/usr/share/grisbi/categories/C/empty.cgsb
/usr/share/grisbi/categories/de_AT/keine.cgsb
/usr/share/grisbi/categories/de_AT/kontenplan.cgsb
/usr/share/grisbi/categories/de_AT/minimal.cgsb
/usr/share/grisbi/categories/de_AT/standard.cgsb
/usr/share/grisbi/categories/de_DE/keine.cgsb
/usr/share/grisbi/categories/de_DE/minimal.cgsb
/usr/share/grisbi/categories/de_DE/standard.cgsb
/usr/share/grisbi/categories/fr/00_general.cgsb
/usr/share/grisbi/categories/fr/empty.cgsb
/usr/share/grisbi/categories/fr/liberal.cgsb
/usr/share/grisbi/categories/fr_FR/plan-associatif-simplifie.cgsb
/usr/share/grisbi/categories/fr_FR/plan-comptable.cgsb
/usr/share/grisbi/categories/it/00_general.cgsb
/usr/share/grisbi/categories/it/empty.cgsb
/usr/share/grisbi/categories/ru/00_general.cgsb
/usr/share/grisbi/categories/ru/empty.cgsb
/usr/share/grisbi/ui/bet_graph.ui
/usr/share/grisbi/ui/csv_template_rule.ui
/usr/share/grisbi/ui/etats_prefs.ui
/usr/share/grisbi/ui/grisbi.css
/usr/share/grisbi/ui/grisbi_menu.ui
/usr/share/grisbi/ui/grisbi_prefs.ui
/usr/share/grisbi/ui/grisbi_win.ui
/usr/share/grisbi/ui/prefs_page_accueil.ui
/usr/share/grisbi/ui/prefs_page_archives.ui
/usr/share/grisbi/ui/prefs_page_bet_account.ui
/usr/share/grisbi/ui/prefs_page_display_adr.ui
/usr/share/grisbi/ui/prefs_page_display_fonts.ui
/usr/share/grisbi/ui/prefs_page_display_gui.ui
/usr/share/grisbi/ui/prefs_page_divers.ui
/usr/share/grisbi/ui/prefs_page_files.ui
/usr/share/grisbi/ui/prefs_page_form_completion.ui
/usr/share/grisbi/ui/prefs_page_import_asso.ui
/usr/share/grisbi/ui/prefs_page_import_files.ui
/usr/share/grisbi/ui/prefs_page_metatree.ui
/usr/share/grisbi/ui/prefs_widget_loan.ui
/usr/share/icons/hicolor/scalable/apps/grisbi.svg
/usr/share/mime-info/grisbi.keys
/usr/share/mime-info/grisbi.mime
/usr/share/mime-packages/grisbi.xml
/usr/share/pixmaps/grisbi/flags/ADP.png
/usr/share/pixmaps/grisbi/flags/AED.png
/usr/share/pixmaps/grisbi/flags/AFN.png
/usr/share/pixmaps/grisbi/flags/ALL.png
/usr/share/pixmaps/grisbi/flags/AMD.png
/usr/share/pixmaps/grisbi/flags/ANG.png
/usr/share/pixmaps/grisbi/flags/ARS.png
/usr/share/pixmaps/grisbi/flags/ATS.png
/usr/share/pixmaps/grisbi/flags/AUD.png
/usr/share/pixmaps/grisbi/flags/AWG.png
/usr/share/pixmaps/grisbi/flags/AZM.png
/usr/share/pixmaps/grisbi/flags/BAM.png
/usr/share/pixmaps/grisbi/flags/BBD.png
/usr/share/pixmaps/grisbi/flags/BDT.png
/usr/share/pixmaps/grisbi/flags/BEF.png
/usr/share/pixmaps/grisbi/flags/BGN.png
/usr/share/pixmaps/grisbi/flags/BHD.png
/usr/share/pixmaps/grisbi/flags/BHU.png
/usr/share/pixmaps/grisbi/flags/BIF.png
/usr/share/pixmaps/grisbi/flags/BMD.png
/usr/share/pixmaps/grisbi/flags/BND.png
/usr/share/pixmaps/grisbi/flags/BOB.png
/usr/share/pixmaps/grisbi/flags/BRL.png
/usr/share/pixmaps/grisbi/flags/BSD.png
/usr/share/pixmaps/grisbi/flags/BTN.png
/usr/share/pixmaps/grisbi/flags/BWP.png
/usr/share/pixmaps/grisbi/flags/BYB.png
/usr/share/pixmaps/grisbi/flags/BZD.png
/usr/share/pixmaps/grisbi/flags/CAD.png
/usr/share/pixmaps/grisbi/flags/CAM.png
/usr/share/pixmaps/grisbi/flags/CDF.png
/usr/share/pixmaps/grisbi/flags/CHA.png
/usr/share/pixmaps/grisbi/flags/CHF.png
/usr/share/pixmaps/grisbi/flags/CLP.png
/usr/share/pixmaps/grisbi/flags/CNY.png
/usr/share/pixmaps/grisbi/flags/COO.png
/usr/share/pixmaps/grisbi/flags/COP.png
/usr/share/pixmaps/grisbi/flags/CO_.png
/usr/share/pixmaps/grisbi/flags/CRC.png
/usr/share/pixmaps/grisbi/flags/CUP.png
/usr/share/pixmaps/grisbi/flags/CVE.png
/usr/share/pixmaps/grisbi/flags/CYP.png
/usr/share/pixmaps/grisbi/flags/CZK.png
/usr/share/pixmaps/grisbi/flags/DEM.png
/usr/share/pixmaps/grisbi/flags/DJF.png
/usr/share/pixmaps/grisbi/flags/DKK.png
/usr/share/pixmaps/grisbi/flags/DOP.png
/usr/share/pixmaps/grisbi/flags/DZD.png
/usr/share/pixmaps/grisbi/flags/ECS.png
/usr/share/pixmaps/grisbi/flags/EEK.png
/usr/share/pixmaps/grisbi/flags/EGP.png
/usr/share/pixmaps/grisbi/flags/ERN.png
/usr/share/pixmaps/grisbi/flags/ESP.png
/usr/share/pixmaps/grisbi/flags/ETB.png
/usr/share/pixmaps/grisbi/flags/EUR.png
/usr/share/pixmaps/grisbi/flags/FIM.png
/usr/share/pixmaps/grisbi/flags/FJD.png
/usr/share/pixmaps/grisbi/flags/FKP.png
/usr/share/pixmaps/grisbi/flags/FRF.png
/usr/share/pixmaps/grisbi/flags/GBP.png
/usr/share/pixmaps/grisbi/flags/GEL.png
/usr/share/pixmaps/grisbi/flags/GHC.png
/usr/share/pixmaps/grisbi/flags/GIP.png
/usr/share/pixmaps/grisbi/flags/GMD.png
/usr/share/pixmaps/grisbi/flags/GNF.png
/usr/share/pixmaps/grisbi/flags/GRD.png
/usr/share/pixmaps/grisbi/flags/GRE.png
/usr/share/pixmaps/grisbi/flags/GTQ.png
/usr/share/pixmaps/grisbi/flags/GWP.png
/usr/share/pixmaps/grisbi/flags/GYD.png
/usr/share/pixmaps/grisbi/flags/HKD.png
/usr/share/pixmaps/grisbi/flags/HNL.png
/usr/share/pixmaps/grisbi/flags/HRK.png
/usr/share/pixmaps/grisbi/flags/HTG.png
/usr/share/pixmaps/grisbi/flags/HUF.png
/usr/share/pixmaps/grisbi/flags/IDR.png
/usr/share/pixmaps/grisbi/flags/IEP.png
/usr/share/pixmaps/grisbi/flags/ILS.png
/usr/share/pixmaps/grisbi/flags/INR.png
/usr/share/pixmaps/grisbi/flags/IQD.png
/usr/share/pixmaps/grisbi/flags/IRR.png
/usr/share/pixmaps/grisbi/flags/ISK.png
/usr/share/pixmaps/grisbi/flags/ITL.png
/usr/share/pixmaps/grisbi/flags/JMD.png
/usr/share/pixmaps/grisbi/flags/JOD.png
/usr/share/pixmaps/grisbi/flags/JPY.png
/usr/share/pixmaps/grisbi/flags/KES.png
/usr/share/pixmaps/grisbi/flags/KGS.png
/usr/share/pixmaps/grisbi/flags/KHR.png
/usr/share/pixmaps/grisbi/flags/KIR.png
/usr/share/pixmaps/grisbi/flags/KMF.png
/usr/share/pixmaps/grisbi/flags/KPW.png
/usr/share/pixmaps/grisbi/flags/KRW.png
/usr/share/pixmaps/grisbi/flags/KWD.png
/usr/share/pixmaps/grisbi/flags/KYD.png
/usr/share/pixmaps/grisbi/flags/KZT.png
/usr/share/pixmaps/grisbi/flags/LAK.png
/usr/share/pixmaps/grisbi/flags/LBP.png
/usr/share/pixmaps/grisbi/flags/LIE.png
/usr/share/pixmaps/grisbi/flags/LKR.png
/usr/share/pixmaps/grisbi/flags/LRD.png
/usr/share/pixmaps/grisbi/flags/LSL.png
/usr/share/pixmaps/grisbi/flags/LTL.png
/usr/share/pixmaps/grisbi/flags/LUF.png
/usr/share/pixmaps/grisbi/flags/LVL.png
/usr/share/pixmaps/grisbi/flags/LYD.png
/usr/share/pixmaps/grisbi/flags/MAD.png
/usr/share/pixmaps/grisbi/flags/MDL.png
/usr/share/pixmaps/grisbi/flags/MGF.png
/usr/share/pixmaps/grisbi/flags/MKD.png
/usr/share/pixmaps/grisbi/flags/MMK.png
/usr/share/pixmaps/grisbi/flags/MNT.png
/usr/share/pixmaps/grisbi/flags/MOP.png
/usr/share/pixmaps/grisbi/flags/MRO.png
/usr/share/pixmaps/grisbi/flags/MTL.png
/usr/share/pixmaps/grisbi/flags/MUR.png
/usr/share/pixmaps/grisbi/flags/MVR.png
/usr/share/pixmaps/grisbi/flags/MWK.png
/usr/share/pixmaps/grisbi/flags/MXP.png
/usr/share/pixmaps/grisbi/flags/MYR.png
/usr/share/pixmaps/grisbi/flags/MZM.png
/usr/share/pixmaps/grisbi/flags/NAD.png
/usr/share/pixmaps/grisbi/flags/NAU.png
/usr/share/pixmaps/grisbi/flags/NGN.png
/usr/share/pixmaps/grisbi/flags/NIG.png
/usr/share/pixmaps/grisbi/flags/NIO.png
/usr/share/pixmaps/grisbi/flags/NLG.png
/usr/share/pixmaps/grisbi/flags/NOK.png
/usr/share/pixmaps/grisbi/flags/NPR.png
/usr/share/pixmaps/grisbi/flags/NZD.png
/usr/share/pixmaps/grisbi/flags/OMR.png
/usr/share/pixmaps/grisbi/flags/PAB.png
/usr/share/pixmaps/grisbi/flags/PEN.png
/usr/share/pixmaps/grisbi/flags/PGK.png
/usr/share/pixmaps/grisbi/flags/PHP.png
/usr/share/pixmaps/grisbi/flags/PKR.png
/usr/share/pixmaps/grisbi/flags/PLN.png
/usr/share/pixmaps/grisbi/flags/PTE.png
/usr/share/pixmaps/grisbi/flags/PYG.png
/usr/share/pixmaps/grisbi/flags/QAR.png
/usr/share/pixmaps/grisbi/flags/ROL.png
/usr/share/pixmaps/grisbi/flags/RUR.png
/usr/share/pixmaps/grisbi/flags/RWF.png
/usr/share/pixmaps/grisbi/flags/SAN.png
/usr/share/pixmaps/grisbi/flags/SAR.png
/usr/share/pixmaps/grisbi/flags/SBD.png
/usr/share/pixmaps/grisbi/flags/SCR.png
/usr/share/pixmaps/grisbi/flags/SDD.png
/usr/share/pixmaps/grisbi/flags/SEK.png
/usr/share/pixmaps/grisbi/flags/SEN.png
/usr/share/pixmaps/grisbi/flags/SGD.png
/usr/share/pixmaps/grisbi/flags/SHP.png
/usr/share/pixmaps/grisbi/flags/SIT.png
/usr/share/pixmaps/grisbi/flags/SKK.png
/usr/share/pixmaps/grisbi/flags/SLC.png
/usr/share/pixmaps/grisbi/flags/SLL.png
/usr/share/pixmaps/grisbi/flags/SOS.png
/usr/share/pixmaps/grisbi/flags/SRD.png
/usr/share/pixmaps/grisbi/flags/STD.png
/usr/share/pixmaps/grisbi/flags/SVC.png
/usr/share/pixmaps/grisbi/flags/SYP.png
/usr/share/pixmaps/grisbi/flags/SZL.png
/usr/share/pixmaps/grisbi/flags/THB.png
/usr/share/pixmaps/grisbi/flags/TJS.png
/usr/share/pixmaps/grisbi/flags/TMM.png
/usr/share/pixmaps/grisbi/flags/TND.png
/usr/share/pixmaps/grisbi/flags/TOG.png
/usr/share/pixmaps/grisbi/flags/TOP.png
/usr/share/pixmaps/grisbi/flags/TPE.png
/usr/share/pixmaps/grisbi/flags/TRL.png
/usr/share/pixmaps/grisbi/flags/TTD.png
/usr/share/pixmaps/grisbi/flags/TUV.png
/usr/share/pixmaps/grisbi/flags/TWD.png
/usr/share/pixmaps/grisbi/flags/TZS.png
/usr/share/pixmaps/grisbi/flags/UAH.png
/usr/share/pixmaps/grisbi/flags/UGX.png
/usr/share/pixmaps/grisbi/flags/USD.png
/usr/share/pixmaps/grisbi/flags/UYU.png
/usr/share/pixmaps/grisbi/flags/UZS.png
/usr/share/pixmaps/grisbi/flags/VAT.png
/usr/share/pixmaps/grisbi/flags/VEB.png
/usr/share/pixmaps/grisbi/flags/VND.png
/usr/share/pixmaps/grisbi/flags/VUV.png
/usr/share/pixmaps/grisbi/flags/WST.png
/usr/share/pixmaps/grisbi/flags/XPF.png
/usr/share/pixmaps/grisbi/flags/YER.png
/usr/share/pixmaps/grisbi/flags/YUM.png
/usr/share/pixmaps/grisbi/flags/YUV.png
/usr/share/pixmaps/grisbi/flags/ZAR.png
/usr/share/pixmaps/grisbi/flags/ZMK.png
/usr/share/pixmaps/grisbi/flags/ZWD.png
/usr/share/pixmaps/grisbi/grisbi-32.png
/usr/share/pixmaps/grisbi/grisbi-logo.png
/usr/share/pixmaps/grisbi/grisbi.svg
/usr/share/pixmaps/grisbi/gsb-ac-asset-32.png
/usr/share/pixmaps/grisbi/gsb-ac-bank-16.png
/usr/share/pixmaps/grisbi/gsb-ac-bank-32.png
/usr/share/pixmaps/grisbi/gsb-ac-cash-32.png
/usr/share/pixmaps/grisbi/gsb-ac-home-32.png
/usr/share/pixmaps/grisbi/gsb-ac-liability-16.png
/usr/share/pixmaps/grisbi/gsb-ac-liability-24.png
/usr/share/pixmaps/grisbi/gsb-ac-liability-32.png
/usr/share/pixmaps/grisbi/gsb-addresses-32.png
/usr/share/pixmaps/grisbi/gsb-amount-32.png
/usr/share/pixmaps/grisbi/gsb-archive-16.png
/usr/share/pixmaps/grisbi/gsb-archive-24.png
/usr/share/pixmaps/grisbi/gsb-archive-32.png
/usr/share/pixmaps/grisbi/gsb-arrow-down-16.png
/usr/share/pixmaps/grisbi/gsb-balance_estimate-32.png
/usr/share/pixmaps/grisbi/gsb-banks-32.png
/usr/share/pixmaps/grisbi/gsb-budgetary_lines-32.png
/usr/share/pixmaps/grisbi/gsb-bug-16.png
/usr/share/pixmaps/grisbi/gsb-bug-32.png
/usr/share/pixmaps/grisbi/gsb-categories-32.png
/usr/share/pixmaps/grisbi/gsb-comments-16.png
/usr/share/pixmaps/grisbi/gsb-comments-24.png
/usr/share/pixmaps/grisbi/gsb-convert-16.png
/usr/share/pixmaps/grisbi/gsb-convert-24.png
/usr/share/pixmaps/grisbi/gsb-currencies-32.png
/usr/share/pixmaps/grisbi/gsb-display-gui-32.png
/usr/share/pixmaps/grisbi/gsb-down-16.png
/usr/share/pixmaps/grisbi/gsb-export-16.png
/usr/share/pixmaps/grisbi/gsb-export-24.png
/usr/share/pixmaps/grisbi/gsb-export-32.png
/usr/share/pixmaps/grisbi/gsb-export-archive-16.png
/usr/share/pixmaps/grisbi/gsb-export-archive-32.png
/usr/share/pixmaps/grisbi/gsb-files-32.png
/usr/share/pixmaps/grisbi/gsb-financial-years-32.png
/usr/share/pixmaps/grisbi/gsb-fonts-32.png
/usr/share/pixmaps/grisbi/gsb-form-32.png
/usr/share/pixmaps/grisbi/gsb-generalities-32.png
/usr/share/pixmaps/grisbi/gsb-graph-histo-24.png
/usr/share/pixmaps/grisbi/gsb-graph-line-24.png
/usr/share/pixmaps/grisbi/gsb-graph-sectors-24.png
/usr/share/pixmaps/grisbi/gsb-grille-16.png
/usr/share/pixmaps/grisbi/gsb-help-16.png
/usr/share/pixmaps/grisbi/gsb-import-16.png
/usr/share/pixmaps/grisbi/gsb-import-24.png
/usr/share/pixmaps/grisbi/gsb-import-32.png
/usr/share/pixmaps/grisbi/gsb-jump-16.png
/usr/share/pixmaps/grisbi/gsb-new-categ-16.png
/usr/share/pixmaps/grisbi/gsb-new-categ-24.png
/usr/share/pixmaps/grisbi/gsb-new-file-16.png
/usr/share/pixmaps/grisbi/gsb-new-file-24.png
/usr/share/pixmaps/grisbi/gsb-new-file-32.png
/usr/share/pixmaps/grisbi/gsb-new-ib-16.png
/usr/share/pixmaps/grisbi/gsb-new-ib-24.png
/usr/share/pixmaps/grisbi/gsb-new-payee-16.png
/usr/share/pixmaps/grisbi/gsb-new-payee-24.png
/usr/share/pixmaps/grisbi/gsb-new-report-16.png
/usr/share/pixmaps/grisbi/gsb-new-report-24.png
/usr/share/pixmaps/grisbi/gsb-new-scheduled-24.png
/usr/share/pixmaps/grisbi/gsb-new-sub-categ-24.png
/usr/share/pixmaps/grisbi/gsb-new-sub-ib-24.png
/usr/share/pixmaps/grisbi/gsb-new-transaction-16.png
/usr/share/pixmaps/grisbi/gsb-new-transaction-24.png
/usr/share/pixmaps/grisbi/gsb-organization-32.png
/usr/share/pixmaps/grisbi/gsb-payees-32.png
/usr/share/pixmaps/grisbi/gsb-payees-manage-16.png
/usr/share/pixmaps/grisbi/gsb-payees-manage-24.png
/usr/share/pixmaps/grisbi/gsb-payment-32.png
/usr/share/pixmaps/grisbi/gsb-pdf-24.png
/usr/share/pixmaps/grisbi/gsb-preferences-16.png
/usr/share/pixmaps/grisbi/gsb-reconat-32.png
/usr/share/pixmaps/grisbi/gsb-reconciliation-24.png
/usr/share/pixmaps/grisbi/gsb-reconciliation-32.png
/usr/share/pixmaps/grisbi/gsb-reports-32.png
/usr/share/pixmaps/grisbi/gsb-scheduler-32.png
/usr/share/pixmaps/grisbi/gsb-text-32.png
/usr/share/pixmaps/grisbi/gsb-title-32.png
/usr/share/pixmaps/grisbi/gsb-toolbar-32.png
/usr/share/pixmaps/grisbi/gsb-transaction-list-32.png
/usr/share/pixmaps/grisbi/gsb-transdisplay-32.png
/usr/share/pixmaps/grisbi/gsb-transfer-32.png
/usr/share/pixmaps/grisbi/gsb-up-16.png
/usr/share/pixmaps/grisbi/gsb-warnings-32.png
/usr/share/pixmaps/grisbi/gsb-web-browser-16.png
/usr/share/pixmaps/grisbi/gtk-about-16.png
/usr/share/pixmaps/grisbi/gtk-add-16.png
/usr/share/pixmaps/grisbi/gtk-apply-16.png
/usr/share/pixmaps/grisbi/gtk-close-16.png
/usr/share/pixmaps/grisbi/gtk-copy-16.png
/usr/share/pixmaps/grisbi/gtk-copy-24.png
/usr/share/pixmaps/grisbi/gtk-corbeille-32.png
/usr/share/pixmaps/grisbi/gtk-delete-16.png
/usr/share/pixmaps/grisbi/gtk-delete-24.png
/usr/share/pixmaps/grisbi/gtk-dialog-warning-16.png
/usr/share/pixmaps/grisbi/gtk-edit-16.png
/usr/share/pixmaps/grisbi/gtk-edit-24.png
/usr/share/pixmaps/grisbi/gtk-execute-16.png
/usr/share/pixmaps/grisbi/gtk-execute-24.png
/usr/share/pixmaps/grisbi/gtk-open-16.png
/usr/share/pixmaps/grisbi/gtk-open-24.png
/usr/share/pixmaps/grisbi/gtk-print-16.png
/usr/share/pixmaps/grisbi/gtk-print-24.png
/usr/share/pixmaps/grisbi/gtk-properties-16.png
/usr/share/pixmaps/grisbi/gtk-properties-24.png
/usr/share/pixmaps/grisbi/gtk-quit-16.png
/usr/share/pixmaps/grisbi/gtk-refresh-16.png
/usr/share/pixmaps/grisbi/gtk-remove-16.png
/usr/share/pixmaps/grisbi/gtk-save-16.png
/usr/share/pixmaps/grisbi/gtk-save-as-16.png
/usr/share/pixmaps/grisbi/gtk-search-16.png
/usr/share/pixmaps/grisbi/gtk-select-color-24.png
/usr/share/pixmaps/grisbi/gtk-window-new-16.png

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/grisbi/*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/grisbi/74a8a6531a42e124df07ab5599aad63870fa0bd4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/grisbi.1

%files locales -f grisbi.lang
%defattr(-,root,root,-)

