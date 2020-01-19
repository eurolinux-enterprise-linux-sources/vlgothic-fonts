%global	priority	65-1
%global	ppriority	65-0
%global	fontname	vlgothic
%global	archivename	VLGothic-%{version}
%global	fontconf	%{priority}-%{fontname}-gothic
%global	pfontconf	%{ppriority}-%{fontname}-pgothic
%global	common_desc	\
VLGothic provides Japanese TrueType fonts from the Vine Linux project.\
Most of the glyphs are taken from the M+ and Sazanami Gothic fonts,\
but some have also been improved by the project.

Name:		%{fontname}-fonts
Version:	20130607
Release:	2%{?dist}
Summary:	Japanese TrueType font

License:	mplus and BSD
Group:		User Interface/X
URL:		http://dicey.org/vlgothic
Source0:	http://osdn.dl.sourceforge.jp/vlgothic/58961/%{archivename}.tar.bz2
Source1:	%{name}-fontconfig-pgothic.conf
Source2:	%{name}-fontconfig-gothic.conf
BuildArch:	noarch
BuildRequires:	fontpackages-devel

Requires:	fontpackages-filesystem
Obsoletes:	%{name}-common < 20121230-2
Provides:	%{name}-common = %{version}-%{release}
%description
%common_desc

This package provides the monospace VLGothic font.


%package -n	%{fontname}-p-fonts
Summary:	Proportional Japanese TrueType font
Group:		User Interface/X
Requires:	fontpackages-filesystem
Obsoletes:	%{name}-common < 20121230-2
Provides:	%{name}-common = %{version}-%{release}

%description -n	%{fontname}-p-fonts
%common_desc

This package provides the VLGothic font with proportional glyphs for some
non-Japanese characters.

%prep
%setup -q -n VLGothic


%build
%{nil}


%install
install -m 0755 -d $RPM_BUILD_ROOT%{_fontdir}
install -m 0644 -p *.ttf $RPM_BUILD_ROOT%{_fontdir}

install -m 0755 -d	$RPM_BUILD_ROOT%{_fontconfig_templatedir} \
			$RPM_BUILD_ROOT%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{pfontconf}.conf
install -m 0644 -p %{SOURCE2} $RPM_BUILD_ROOT%{_fontconfig_templatedir}/%{fontconf}.conf

for fconf in %{pfontconf}.conf %{fontconf}.conf; do
	ln -s %{_fontconfig_templatedir}/$fconf $RPM_BUILD_ROOT%{_fontconfig_confdir}/$fconf
done


%_font_pkg -f %{fontconf}.conf VL-Gothic-Regular.ttf
%doc README* LICENSE*

%_font_pkg -n p -f %{pfontconf}.conf VL-PGothic-Regular.ttf
%doc README* LICENSE*


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 20130607-2
- Mass rebuild 2013-12-27

* Mon Jun 10 2013 Akira TAGOH <tagoh@redhat.com> - 20130607-1
- New upstream release. (#972223)

* Fri May 24 2013 Akira TAGOH <tagoh@redhat.com> - 20130510-2
- Work around unnecessary leading whitespace in the pattern. (#966785)

* Mon May 13 2013 Akira TAGOH <tagoh@redhat.com> - 20130510-1
- New upstream release (#956040)

* Wed Feb 20 2013 Akira TAGOH <tagoh@redhat.com> - 20121230-4
- Drop more older Obsoletes and Provides line.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20121230-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Akira TAGOH <tagoh@redhat.com> - 20121230-2
- Drop -common package and keep consistent state of the directory
  by using the macro. (#893789)
- Drop old Obsoletes and Provides line.

* Fri Jan  4 2013 Akira TAGOH <tagoh@redhat.com> - 20121230-1
- New upstream release. (#890992)

* Fri Nov 23 2012 Akira TAGOH <tagoh@redhat.com> - 20121109-2
- the spec file cleanup

* Fri Nov 16 2012 Akira TAGOH <tagoh@redhat.com> - 20121109-1
- New upstream release. (#874981)

* Mon Oct  1 2012 Akira TAGOH <tagoh@redhat.com> - 20120928-1
- New upstream release. (#861431)

* Thu Sep  6 2012 Akira TAGOH <tagoh@redhat.com> - 20120905-1
- New upstream release. (#854525)

* Wed Aug 29 2012 Akira TAGOH <tagoh@redhat.com> - 20120829-1
- New upstream release. (#852673)

* Mon Aug 27 2012 Akira TAGOH <tagoh@redhat.com> - 20120827-1
- New upstream release. (#851879)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120629-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Akira TAGOH <tagoh@redhat.com> - 20120629-1
- New upstream release.

* Mon Jun 18 2012 Akira TAGOH <tagoh@redhat.com> - 20120618-1
- New upstream release.

* Mon Jun 11 2012 Akira TAGOH <tagoh@redhat.com> - 20120610-1
- New upstream release.

* Mon Mar 25 2012 Akira TAGOH <tagoh@redhat.com> - 20120325-1
- New upstream release.

* Wed Mar 14 2012 Akira TAGOH <tagoh@redhat.com> - 20120312-1
- New upstream release.

* Fri Feb 03 2012 Akira TAGOH <tagoh@redhat.com> - 20120130-1
- New upstream release.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20111122-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov 22 2011 Akira TAGOH <tagoh@redhat.com> - 20111122-1
- New upstream release.

* Mon Jul 25 2011 Akira TAGOH <tagoh@redhat.com> - 20110722-1
- New upstream release.

* Thu Apr 14 2011 Akira TAGOH <tagoh@redhat.com> - 20110414-1
- New upstream release.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101218-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 22 2010 Akira TAGOH <tagoh@redhat.com> - 20101218-1
- New upstream release.

* Thu Aug 19 2010 Akira TAGOH <tagoh@redhat.com> - 20100818-1
- New upstream release.

* Wed May 26 2010 Akira TAGOH <tagoh@redhat.com> - 20100416-3
- Improve the fontconfig config file to match ja as well.

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 20100416-2
- Get rid of compare="contains" again.

* Mon Apr 19 2010 Akira TAGOH <tagoh@redhat.com> - 20100416-1
- New upstream release.
- Get rid of binding="same" from the fontconfig config file. (#578048)

* Fri Mar 12 2010 Akira TAGOH <tagoh@redhat.com> - 20100126-2
- Fix the locale-specific overrides rule to match with "ja" as well. (#572841)

* Mon Mar  1 2010 Akira TAGOH <tagoh@redhat.com> - 20100126-1
- New upstream release.
- Set the priority to 65-0 for vlgothic-p-fonts to avoid the effects
  of 65-nonlatin.conf and similarly 65-1 to vlgothic-fonts. (#476459)

* Mon Dec  7 2009 Akira TAGOH <tagoh@redhat.com> - 20091202-1
- New upstream release.
- Set the priority to 65 for vlgothic-p-fonts to override the rule in
  vlgothic-fonts for sans-serif.
- Set the priority to 66 and contains both rules for sans-serif and monospace
  to avoid picking up the unrelated fonts in Live. where doesn't have
  vlgothic-p-fonts installed. (#544957)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090612-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Akira TAGOH <tagoh@redhat.com> - 20090612-1
- New upstream release.

* Thu Apr 23 2009 Akira TAGOH <tagoh@redhat.com> - 20090422-1
- New upstream release.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090204-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Akira TAGOH <tagoh@redhat.com> - 20090204-2
- clean up.

* Wed Feb  4 2009 Akira TAGOH <tagoh@redhat.com> - 20090204-1
- New upstream release.
- Update spec file for new packaging policy.
  - Renamed VLGothic-fonts to vlgothic-fonts.
  - Renamed VLGothic-fonts-proportional to vlgothic-p-fonts.
  - Added vlgothic-fonts-common.

* Fri Dec  5 2008 Akira TAGOH <tagoh@redhat.com> - 20081203-2
- update fontconfig config according to Fontconfig packaging tips.

* Thu Dec  4 2008 Akira TAGOH <tagoh@redhat.com> - 20081203-1
- update to 20081203 release.
- clean up spec file.
- changed the priority prefix for fontconfig to 66 according to Fontconfig packaging tips.

* Wed Oct 29 2008 Akira TAGOH <tagoh@redhat.com> - 20081029-1
- update to 20081029 release.

* Tue Sep  9 2008 Akira TAGOH <tagoh@redhat.com> - 20080908-1
- update to 20080908 release.

* Thu Jul 31 2008 Jens Petersen <petersen@redhat.com> - 20080624-1.fc10
- update to 20080624 release

* Wed May  7 2008 Jens Petersen <petersen@redhat.com> - 20080429-1
- update to 20080429 release
- rename 59-VLGothic-sans.conf to 59-VLGothic-proportional.conf

* Thu Jan 17 2008 Jens Petersen <petersen@redhat.com> - 20071215-2.fc9
- move monospace font to main package and obsolete monospace subpackage
- rename sans subpackage to proportional and obsolete sans subpackage
- use a separate font dir for the proportional font subpackage
- add fc-cache scriptlets and drop superfluous removal of old font config
- drop the docs subpackage
- use fontname, fontdir, and fontconfdir macros
- improve summaries and descriptions
- do not require fontconfig
- drop VLGothic obsoletes and provides

* Sat Jan 12 2008 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20071215-1
- Update to 20071215

* Thu Oct 18 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20071015-2
- Rename the font directory.
- Fix font selection problem in Flash 9.
- Make it remove the old configuration files on updating.

* Thu Oct 18 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20071015-1
- Update to 20071015
- Make it separated into subpackages

* Sat Sep 09 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20070901-1
- Update to 20070901

* Sat Jun 02 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20070507-1
- Update to 20070507

* Sun Apr 22 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20070328-1
- Update to 20070328

* Wed Jan 03 2007 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20070101-1
- Update to 20070101

* Sun Dec 10 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20061026-5
- Decrease the priority of the VLGothic fonts lower than DejaVu fonts.
- Now config files are replaced by every updating.

* Wed Nov 29 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20061026-4
- Fix the mistyped dist tag.

* Sat Nov 18 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20061026-3
- Modify the specfile along with the Fedora Extras packaging policy.

* Sun Nov 12 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20061026-2
- Modify the specfile.

* Sun Nov 12 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20061026-1
- Preparing for Fedora Extras.

* Sat Oct 28 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20061021-2
- Update to 20061021.

* Tue Sep 19 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20060913-2
- Update to 20060913.

* Thu Aug 31 2006 Ryo Dairiki <ryo-dairiki@users.sourceforge.net> - 20060831-1
- Initial packaging.
