%global tl_name chickenize
%global tl_revision 78415

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	Use Lua callbacks for interesting textual effects
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/chickenize
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chickenize.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chickenize.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/chickenize.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows manipulations of any LuaTeX document (it is known to
work with Plain LuaTeX and LuaLaTeX). Most of the package's functions
are merely for fun or educational use, but some functions (for example,
colorstretch for visualising the badness and font expansion of each
line, and letterspaceadjust doing what its name says) could be useful in
a "normal" LuaTeX document.

