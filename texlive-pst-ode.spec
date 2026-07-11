%global tl_name pst-ode
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.19
Release:	%{tl_revision}.1
Summary:	Solving initial value problems for sets of Ordinary Differential Equations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-ode
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-ode.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines \pstODEsolve for solving initial value problems for
sets of Ordinary Differential Equations (ODE) using the Runge-Kutta-
Fehlberg (RKF45) method with automatic step size adjustment. The result
is stored as a PostScript object and may be plotted later using macros
from other PSTricks packages, such as \listplot (pst-plot) and
\listplotThreeD (pst-3dplot), or may be further processed by user-
defined PostScript procedures. Optionally, the computed state vectors
can be written as a table to a text file.

