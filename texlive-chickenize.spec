Name:		texlive-chickenize
Version:	0.2.5
Release:	3
Summary:	Use lua callbacks for "interesting" textual effects
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/generic/chickenize
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chickenize.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chickenize.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chickenize.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows manipulations of any LuaTeX document (it is
known to work with Plain LuaTeX and LuaLaTeX). Most of the
package's functions are merely for fun or educational use, but
some functions (for example, colorstretch for visualising the
badness and font expansion of each line, and letterspaceadjust
doing what its name says) could be useful in a "normal" LuaTeX
document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/luatex/chickenize
%doc %{_texmfdistdir}/doc/luatex/chickenize
#- source
%doc %{_texmfdistdir}/source/luatex/chickenize

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
