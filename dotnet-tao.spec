Summary:	Tao Framework
Summary(pl):	Framework Tao
Name:		tao
Version:	20050606
Release:	1
License:	MIT
Group:		Libraries
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	170e143b8035644eb3c24db4cc7a2c3b
URL:		http://www.mono-project.com/Tao
BuildRequires:	mono >= 1.1.0
Requires:	mono >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Tao Framework for .NET is a collection of bindings to facilitate
cross-platform game-related development utilizing the .NET platform.

Currently included bindings are OpenGL 1.5, GLU 1.3, GLUT 3.7.6, WGL,
various GL and WGL-related extensions, OpenAL 1.0, Cg 1.2.1, DevIL
1.6.6, SDL 1.2.7, and GLFW 2.4.2 (and some others).

These bindings all function in a cross-platform and cross-runtime
manner using Microsoft's .NET 1.0 and 1.1 runtimes on Windows and the
Mono runtime on Windows and Linux. Other platforms and runtimes have
not been tested, but, would most likely work with a minimal amount of
changes.

The bindings are also CLS-compliant, meaning that they can be used by
any .NET language, including C# and Visual Basic .NET, amongst others.

%description -l pl
Framework Tao dla .NET jest kolekcj± wi±zañ umo¿liwiaj±c±
miêdzyplatformowe tworzenie gier opartych na platformie .NET.

Aktualnie zawarte s± wi±zania do OpenGL 2.0, GLU 1.3, GLUT 3.7.6, WGL,
ró¿nych rozszerzeñ GL i WGL, OpenAL 1.0, Cg 1.2.1, DevIL 1.6.6, SDL
1.2.7 i GLFW 2.4.2 (i kilku innych).

Wszystkie te wi±zania zdatne s± do u¿ytku na wielu platformach
sprzêtowych i w wielu ¶rodowiskach uruchomieniowych. Obs³ugiwane jest
microsoftowe .NET 1.0 i 1.1 pod Windowsami oraz Mono pod Windowsami i
Linuksem. Inne platformy i ¶rodowiska nie zosta³y przetestowane, lecz
prawdopodobnie równie¿ bêd± dzia³aæ z minimaln± ilo¶ci± zmian.

Wi±zania s± równie¿ zgodne z CLS, co znaczy, ¿e mog± byæ u¿ywane przez
ró¿norakie jêzyki .NET, po¶ród nich na przyk³ad C# i Visual Basic
.NET.

%package examples
Summary:	Tao example programs
Summary(pl):	Przyk³adowe programy Tao
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description examples
Tao example programs.

%description examples -l pl
Przyk³adowe programy Tao.

%prep
%setup -q

%build
%{__make} mono-1.1
%{__make} -C src \
	STRONG=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/tao}

for i in dist/bin/*.dll
do
	gacutil -root $RPM_BUILD_ROOT%{_libdir} -package tao -i $i
done

cp -Rf examples/* $RPM_BUILD_ROOT%{_examplesdir}/tao

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt src/Tao.*/Tao.*.Readme.txt
%attr(755,root,root) %{_libdir}/mono/gac/*/*/*.dll
%{_libdir}/mono/gac/*/*/*.config
%{_libdir}/mono/tao

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/tao
