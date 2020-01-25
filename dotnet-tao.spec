Summary:	Tao Framework
Summary(pl.UTF-8):	Framework Tao
Name:		dotnet-tao
Version:	20050606
Release:	1
License:	MIT
Group:		Libraries
Source0:	tao-%{version}.tar.bz2
# Source0-md5:	170e143b8035644eb3c24db4cc7a2c3b
URL:		http://www.mono-project.com/Tao
BuildRequires:	mono >= 1.1.7
BuildRequires:	rpmbuild(monoautodeps)
Requires:	mono >= 1.1.7
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

%description -l pl.UTF-8
Framework Tao dla .NET jest kolekcją wiązań umożliwiającą
międzyplatformowe tworzenie gier opartych na platformie .NET.

Aktualnie zawarte są wiązania do OpenGL 2.0, GLU 1.3, GLUT 3.7.6, WGL,
różnych rozszerzeń GL i WGL, OpenAL 1.0, Cg 1.2.1, DevIL 1.6.6, SDL
1.2.7 i GLFW 2.4.2 (i kilku innych).

Wszystkie te wiązania zdatne są do użytku na wielu platformach
sprzętowych i w wielu środowiskach uruchomieniowych. Obsługiwane jest
microsoftowe .NET 1.0 i 1.1 pod Windows oraz Mono pod Windows i
Linuksem. Inne platformy i środowiska nie zostały przetestowane, lecz
prawdopodobnie również będą działać z minimalną ilością zmian.

Wiązania są również zgodne z CLS, co znaczy, że mogą być używane przez
różnorakie języki .NET, pośród nich na przykład C# i Visual Basic
.NET.

%package examples
Summary:	Tao example programs
Summary(pl.UTF-8):	Przykładowe programy Tao
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description examples
Tao example programs.

%description examples -l pl.UTF-8
Przykładowe programy Tao.

%prep
%setup -q -n tao-%{version}

%build
%{__make} mono-1.1
%{__make} -C src \
	STRONG=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

for i in dist/bin/*.dll
do
	gacutil -root $RPM_BUILD_ROOT%{_prefix}/lib -package tao -i $i
done

cp -Rf examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt src/Tao.*/Tao.*.Readme.txt
%attr(755,root,root) %{_prefix}/lib/mono/gac/*/*/*.dll
%{_prefix}/lib/mono/gac/*/*/*.config
%{_prefix}/lib/mono/tao

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
