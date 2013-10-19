# revision 27669
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-ode
# catalog-date 2012-09-14 20:13:55 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-pst-ode
Version:	0.2
Release:	3
Summary:	Solving initial value problems for sets of Ordinary Differential Equations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-ode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ode.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines \pstODEsolve for solving initial value
problems for sets of Ordinary Differential Equations (ODE)
using the Runge-Kutta-Fehlberg (RKF45) method with automatic
step size adjustment. The result is stored as a PostScript
object and may be plotted later using macros from other
PSTricks packages, such as \listplot (pst-plot) and
\listplotThreeD (pst-3dplot), or may be further processed by
user-defined PostScript procedures. Optionally, the computed
state vectors can be written as a table to a text file.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/pst-ode/pst-ode.pro
%{_texmfdistdir}/tex/generic/pst-ode/pst-ode.tex
%{_texmfdistdir}/tex/latex/pst-ode/pst-ode.sty
%doc %{_texmfdistdir}/doc/generic/pst-ode/ChangeLog
%doc %{_texmfdistdir}/doc/generic/pst-ode/README
%doc %{_texmfdistdir}/doc/generic/pst-ode/pst-ode-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-ode/pst-ode-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
