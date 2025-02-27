Name:		texlive-pst-ode
Version:	69296
Release:	1
Summary:	Solving initial value problems for sets of Ordinary Differential Equations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-ode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ode.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ode.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/dvips/pst-ode
%{_texmfdistdir}/tex/generic/pst-ode
%{_texmfdistdir}/tex/latex/pst-ode
%doc %{_texmfdistdir}/doc/generic/pst-ode

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips tex doc %{buildroot}%{_texmfdistdir}
