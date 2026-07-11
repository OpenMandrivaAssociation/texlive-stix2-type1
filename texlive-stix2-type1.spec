%global tl_name stix2-type1
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0.2
Release:	%{tl_revision}.1
Summary:	Type1 versions of the STIX Two OpenType fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/stix2-type1
License:	ofl lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stix2-type1.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stix2-type1.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/stix2-type1.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The stix2 package provides minimal support for using the STIX Two fonts
with versions of TeX that are limited to TFM files, Type 1 PostScript
fonts, and 8-bit font encodings. Version 2.0.0 of the STIX fonts are
being released in this format in hopes of easing the transition from
legacy TeX engines to modern fully Unicode-compatible systems. The Type
1 versions are merely a repackaging of the original OpenType versions
and should not be viewed as independent entities. Some glyphs that are
traditionally available in TeX math fonts are not yet available in the
STIX Two OpenType fonts. In such cases, we have chosen to omit them from
the stix2 package rather than create incompatibilities between the
OpenType and Type 1 versions. In addition, while development of the
OpenType versions is ongoing, no further updates are planned to the Type
1 versions of the fonts.

