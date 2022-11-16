Name:		texlive-stix2-type1
Version:	57448
Release:	1
Summary:	Type1 versions of the STIX Two OpenType fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/stix2-type1
License:	ofl lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stix2-type1.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stix2-type1.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/stix2-type1.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The stix2 package provides minimal support for using the STIX
Two fonts with versions of TeX that are limited to TFM files,
Type 1 PostScript fonts, and 8-bit font encodings. Version
2.0.0 of the STIX fonts are being released in this format in
hopes of easing the transition from legacy TeX engines to
modern fully Unicode-compatible systems. The Type 1 versions
are merely a repackaging of the original OpenType versions and
should not be viewed as independent entities. Some glyphs that
are traditionally available in TeX math fonts are not yet
available in the STIX Two OpenType fonts. In such cases, we
have chosen to omit them from the stix2 package rather than
create incompatibilities between the OpenType and Type 1
versions. In addition, while development of the OpenType
versions is ongoing, no further updates are planned to the Type
1 versions of the fonts.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/fonts/stix2-type1
%{_texmfdistdir}/tex/latex/stix2-type1
%{_texmfdistdir}/fonts/type1/public/stix2-type1
%{_texmfdistdir}/fonts/tfm/public/stix2-type1
%{_texmfdistdir}/fonts/map/dvips/stix2-type1
%{_texmfdistdir}/fonts/enc/dvips/stix2-type1
%doc %{_texmfdistdir}/doc/fonts/stix2-type1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
