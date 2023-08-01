#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : perl
Version  : 5.38.0
Release  : 114
URL      : https://www.cpan.org/src/5.0/perl-5.38.0.tar.gz
Source0  : https://www.cpan.org/src/5.0/perl-5.38.0.tar.gz
Summary  : The Perl 5 language interpreter
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl Artistic-2.0 BSD-3-Clause GPL-1.0 GPL-1.0+ GPL-2.0+ MIT bzip2-1.0.6
Requires: perl-bin = %{version}-%{release}
Requires: perl-license = %{version}-%{release}
Requires: perl-man = %{version}-%{release}
Requires: perl-perl = %{version}-%{release}
Requires: perl-Math-BigInt-GMP
Requires: perl-Test-Simple
BuildRequires : bison
BuildRequires : flex
BuildRequires : gdbm-dev
BuildRequires : groff
BuildRequires : less-bin
BuildRequires : netbase
BuildRequires : pkgconfig(zlib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: config_h_delta.patch
Patch2: 0001-Add-perlbench-for-pgo-optimization.patch
Patch3: 0001-Add-option-for-pgo-profiling-test-with-perlbench.patch
Patch4: Search-vendorlib-for-prior-versions.patch
Patch5: 0005-Symlink-to-Configure.patch
Patch6: 0006-Ignore-unknown-options-in-configure.patch
Patch7: 0007-replace-clean-with-distclean.patch

%description
Perl 5 is a highly capable, feature-rich programming language with over 27 years of development.
Perl 5 runs on over 100 platforms from portables to mainframes and is suitable for both rapid
prototyping and large scale development projects.

%package bin
Summary: bin components for the perl package.
Group: Binaries
Requires: perl-license = %{version}-%{release}

%description bin
bin components for the perl package.


%package dev
Summary: dev components for the perl package.
Group: Development
Requires: perl-bin = %{version}-%{release}
Provides: perl-devel = %{version}-%{release}
Requires: perl = %{version}-%{release}

%description dev
dev components for the perl package.


%package license
Summary: license components for the perl package.
Group: Default

%description license
license components for the perl package.


%package man
Summary: man components for the perl package.
Group: Default

%description man
man components for the perl package.


%package perl
Summary: perl components for the perl package.
Group: Default
Requires: perl = %{version}-%{release}
Requires: perl(MIME::QuotedPrint)
Requires: perl(Scalar::Util)
Requires: perl(Storable)
Requires: perl(Test::Builder)
Requires: perl(Test::More)

%description perl
perl components for the perl package.


%prep
%setup -q -n perl-5.38.0
cd %{_builddir}/perl-5.38.0
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
pushd ..
cp -a perl-5.38.0 buildavx2
popd

%build
## build_prepend content
export PERL5LIB=$(find ${_builddir} -type f -name strict.pm -execdir pwd \; | head -1)
export PERL_MM_USE_DEFAULT=1
export PERL_CANARY_STABILITY_NOPROMPT=1
export BUILD_ZLIB=0
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1690933779
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CFLAGS_GENERATE="$CFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FCFLAGS_GENERATE="$FCFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export FFLAGS_GENERATE="$FFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CXXFLAGS_GENERATE="$CXXFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export LDFLAGS_GENERATE="$LDFLAGS -fprofile-generate -fprofile-dir=/var/tmp/pgo -fprofile-update=atomic "
export CFLAGS_USE="$CFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FCFLAGS_USE="$FCFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export FFLAGS_USE="$FFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export CXXFLAGS_USE="$CXXFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
export LDFLAGS_USE="$LDFLAGS -fprofile-use -fprofile-dir=/var/tmp/pgo -fprofile-correction "
CFLAGS="${CFLAGS_GENERATE}" CXXFLAGS="${CXXFLAGS_GENERATE}" FFLAGS="${FFLAGS_GENERATE}" FCFLAGS="${FCFLAGS_GENERATE}" LDFLAGS="${LDFLAGS_GENERATE}" %configure --disable-static -d \
-e \
-r \
-Dprefix=/usr \
-Dsiteprefix=/usr/local \
-Dvendorprefix=/usr \
-Dinstallman1dir='/usr/share/man/man1' \
-Dinstallman3dir='/usr/share/man/man3' \
-Dman1dir='/usr/share/man/man1' \
-Dman3dir='/usr/share/man/man3' \
-Dusethreads \
-Duseshrplib \
-Adefine:d_procselfexe \
-Adefine:procselfexe='"/proc/self/exe"' \
-Adefine:optimize="-O3 -ffunction-sections -fno-semantic-interposition -fopt-info-vec -ffat-lto-objects -flto=4 -fprofile-dir=/var/tmp/pgo " \
-Aappend:optimize="$(echo $LDFLAGS | grep -q fprofile.generate && echo "-fprofile-generate" || echo "-fprofile-use -fprofile-correction")" \
-Adefine:ccflags="$CFLAGS" \
-Adefine:ldflags="$LDFLAGS" \
-Adefine:lddflags="$LDFLAGS" \
-U d_off64_t \
-Dinc_version_list="5.36.1"
make  %{?_smp_mflags}

make test_pgo
make clean
CFLAGS="${CFLAGS_USE}" CXXFLAGS="${CXXFLAGS_USE}" FFLAGS="${FFLAGS_USE}" FCFLAGS="${FCFLAGS_USE}" LDFLAGS="${LDFLAGS_USE}" %configure --disable-static -d \
-e \
-r \
-Dprefix=/usr \
-Dsiteprefix=/usr/local \
-Dvendorprefix=/usr \
-Dinstallman1dir='/usr/share/man/man1' \
-Dinstallman3dir='/usr/share/man/man3' \
-Dman1dir='/usr/share/man/man1' \
-Dman3dir='/usr/share/man/man3' \
-Dusethreads \
-Duseshrplib \
-Adefine:d_procselfexe \
-Adefine:procselfexe='"/proc/self/exe"' \
-Adefine:optimize="-O3 -ffunction-sections -fno-semantic-interposition -fopt-info-vec -ffat-lto-objects -flto=4 -fprofile-dir=/var/tmp/pgo " \
-Aappend:optimize="$(echo $LDFLAGS | grep -q fprofile.generate && echo "-fprofile-generate" || echo "-fprofile-use -fprofile-correction")" \
-Adefine:ccflags="$CFLAGS" \
-Adefine:ldflags="$LDFLAGS" \
-Adefine:lddflags="$LDFLAGS" \
-U d_off64_t \
-Dinc_version_list="5.36.1"
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
## build_prepend content
export PERL5LIB=$(find ${_builddir} -type f -name strict.pm -execdir pwd \; | head -1)
export PERL_MM_USE_DEFAULT=1
export PERL_CANARY_STABILITY_NOPROMPT=1
export BUILD_ZLIB=0
## build_prepend end
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static -d \
-e \
-r \
-Dprefix=/usr \
-Dsiteprefix=/usr/local \
-Dvendorprefix=/usr \
-Dinstallman1dir='/usr/share/man/man1' \
-Dinstallman3dir='/usr/share/man/man3' \
-Dman1dir='/usr/share/man/man1' \
-Dman3dir='/usr/share/man/man3' \
-Dusethreads \
-Duseshrplib \
-Adefine:d_procselfexe \
-Adefine:procselfexe='"/proc/self/exe"' \
-Adefine:optimize="-O3 -ffunction-sections -fno-semantic-interposition -fopt-info-vec -ffat-lto-objects -flto=4 -fprofile-dir=/var/tmp/pgo " \
-Aappend:optimize="$(echo $LDFLAGS | grep -q fprofile.generate && echo "-fprofile-generate" || echo "-fprofile-use -fprofile-correction")" \
-Adefine:ccflags="$CFLAGS" \
-Adefine:ldflags="$LDFLAGS" \
-Adefine:lddflags="$LDFLAGS" \
-U d_off64_t \
-Dinc_version_list="5.36.1"
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
JOBS=1
JOBS_ARG="%{?_smp_mflags}"
if test -n "$JOBS_ARG"; then
  JOBS="${JOBS_ARG#-j}"
fi
LC_ALL=C TEST_JOBS=$JOBS make test_harness || :

%install
export SOURCE_DATE_EPOCH=1690933779
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl
cp %{_builddir}/perl-%{version}/Copying %{buildroot}/usr/share/package-licenses/perl/18eaf66587c5eea277721d5e569a6e3cd869f855 || :
cp %{_builddir}/perl-%{version}/cpan/Compress-Raw-Bzip2/bzip2-src/LICENSE %{buildroot}/usr/share/package-licenses/perl/ddf157bc55ed6dec9541e4af796294d666cd0926 || :
cp %{_builddir}/perl-%{version}/dist/ExtUtils-CBuilder/LICENSE %{buildroot}/usr/share/package-licenses/perl/6deba81fe267c399cbb316c1fb0d037b0fcdb187 || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/share/man/man3/ok.3
rm -f %{buildroot}*/usr/share/man/man3/List::Util.3
rm -f %{buildroot}*/usr/share/man/man3/List::Util::XS.3
rm -f %{buildroot}*/usr/share/man/man3/Scalar::Util.3
rm -f %{buildroot}*/usr/share/man/man3/Sub::Util.3
rm -f %{buildroot}*/usr/share/man/man3/Test*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/perl
/V3/usr/bin/perl5.38.0
/usr/bin/corelist
/usr/bin/cpan
/usr/bin/enc2xs
/usr/bin/encguess
/usr/bin/h2ph
/usr/bin/h2xs
/usr/bin/instmodsh
/usr/bin/json_pp
/usr/bin/libnetcfg
/usr/bin/perl
/usr/bin/perl5.38.0
/usr/bin/perlbug
/usr/bin/perldoc
/usr/bin/perlivp
/usr/bin/perlthanks
/usr/bin/piconv
/usr/bin/pl2pm
/usr/bin/pod2html
/usr/bin/pod2man
/usr/bin/pod2text
/usr/bin/pod2usage
/usr/bin/podchecker
/usr/bin/prove
/usr/bin/ptar
/usr/bin/ptardiff
/usr/bin/ptargrep
/usr/bin/shasum
/usr/bin/splain
/usr/bin/streamzip
/usr/bin/xsubpp
/usr/bin/zipdetails

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/AnyDBM_File.3
/usr/share/man/man3/App::Cpan.3
/usr/share/man/man3/App::Prove.3
/usr/share/man/man3/App::Prove::State.3
/usr/share/man/man3/App::Prove::State::Result.3
/usr/share/man/man3/App::Prove::State::Result::Test.3
/usr/share/man/man3/Archive::Tar.3
/usr/share/man/man3/Archive::Tar::File.3
/usr/share/man/man3/Attribute::Handlers.3
/usr/share/man/man3/AutoLoader.3
/usr/share/man/man3/AutoSplit.3
/usr/share/man/man3/B.3
/usr/share/man/man3/B::Concise.3
/usr/share/man/man3/B::Deparse.3
/usr/share/man/man3/B::Op_private.3
/usr/share/man/man3/B::Showlex.3
/usr/share/man/man3/B::Terse.3
/usr/share/man/man3/B::Xref.3
/usr/share/man/man3/Benchmark.3
/usr/share/man/man3/CORE.3
/usr/share/man/man3/CPAN.3
/usr/share/man/man3/CPAN::API::HOWTO.3
/usr/share/man/man3/CPAN::Debug.3
/usr/share/man/man3/CPAN::Distroprefs.3
/usr/share/man/man3/CPAN::FirstTime.3
/usr/share/man/man3/CPAN::HandleConfig.3
/usr/share/man/man3/CPAN::Kwalify.3
/usr/share/man/man3/CPAN::Meta.3
/usr/share/man/man3/CPAN::Meta::Converter.3
/usr/share/man/man3/CPAN::Meta::Feature.3
/usr/share/man/man3/CPAN::Meta::History.3
/usr/share/man/man3/CPAN::Meta::History::Meta_1_0.3
/usr/share/man/man3/CPAN::Meta::History::Meta_1_1.3
/usr/share/man/man3/CPAN::Meta::History::Meta_1_2.3
/usr/share/man/man3/CPAN::Meta::History::Meta_1_3.3
/usr/share/man/man3/CPAN::Meta::History::Meta_1_4.3
/usr/share/man/man3/CPAN::Meta::Merge.3
/usr/share/man/man3/CPAN::Meta::Prereqs.3
/usr/share/man/man3/CPAN::Meta::Requirements.3
/usr/share/man/man3/CPAN::Meta::Spec.3
/usr/share/man/man3/CPAN::Meta::Validator.3
/usr/share/man/man3/CPAN::Meta::YAML.3
/usr/share/man/man3/CPAN::Mirrors.3
/usr/share/man/man3/CPAN::Nox.3
/usr/share/man/man3/CPAN::Plugin.3
/usr/share/man/man3/CPAN::Plugin::Specfile.3
/usr/share/man/man3/CPAN::Queue.3
/usr/share/man/man3/CPAN::Tarzip.3
/usr/share/man/man3/CPAN::Version.3
/usr/share/man/man3/Carp.3
/usr/share/man/man3/Class::Struct.3
/usr/share/man/man3/Compress::Raw::Bzip2.3
/usr/share/man/man3/Compress::Raw::Zlib.3
/usr/share/man/man3/Compress::Zlib.3
/usr/share/man/man3/Config.3
/usr/share/man/man3/Config::Extensions.3
/usr/share/man/man3/Config::Perl::V.3
/usr/share/man/man3/Cwd.3
/usr/share/man/man3/DB.3
/usr/share/man/man3/DBM_Filter.3
/usr/share/man/man3/DBM_Filter::compress.3
/usr/share/man/man3/DBM_Filter::encode.3
/usr/share/man/man3/DBM_Filter::int32.3
/usr/share/man/man3/DBM_Filter::null.3
/usr/share/man/man3/DBM_Filter::utf8.3
/usr/share/man/man3/Data::Dumper.3
/usr/share/man/man3/Devel::PPPort.3
/usr/share/man/man3/Devel::Peek.3
/usr/share/man/man3/Devel::SelfStubber.3
/usr/share/man/man3/Digest.3
/usr/share/man/man3/Digest::MD5.3
/usr/share/man/man3/Digest::SHA.3
/usr/share/man/man3/Digest::base.3
/usr/share/man/man3/Digest::file.3
/usr/share/man/man3/DirHandle.3
/usr/share/man/man3/Dumpvalue.3
/usr/share/man/man3/DynaLoader.3
/usr/share/man/man3/Encode.3
/usr/share/man/man3/Encode::Alias.3
/usr/share/man/man3/Encode::Byte.3
/usr/share/man/man3/Encode::CJKConstants.3
/usr/share/man/man3/Encode::CN.3
/usr/share/man/man3/Encode::CN::HZ.3
/usr/share/man/man3/Encode::Config.3
/usr/share/man/man3/Encode::EBCDIC.3
/usr/share/man/man3/Encode::Encoder.3
/usr/share/man/man3/Encode::Encoding.3
/usr/share/man/man3/Encode::GSM0338.3
/usr/share/man/man3/Encode::Guess.3
/usr/share/man/man3/Encode::JP.3
/usr/share/man/man3/Encode::JP::H2Z.3
/usr/share/man/man3/Encode::JP::JIS7.3
/usr/share/man/man3/Encode::KR.3
/usr/share/man/man3/Encode::KR::2022_KR.3
/usr/share/man/man3/Encode::MIME::Header.3
/usr/share/man/man3/Encode::MIME::Name.3
/usr/share/man/man3/Encode::PerlIO.3
/usr/share/man/man3/Encode::Supported.3
/usr/share/man/man3/Encode::Symbol.3
/usr/share/man/man3/Encode::TW.3
/usr/share/man/man3/Encode::Unicode.3
/usr/share/man/man3/Encode::Unicode::UTF7.3
/usr/share/man/man3/English.3
/usr/share/man/man3/Env.3
/usr/share/man/man3/Errno.3
/usr/share/man/man3/Exporter.3
/usr/share/man/man3/Exporter::Heavy.3
/usr/share/man/man3/ExtUtils::CBuilder.3
/usr/share/man/man3/ExtUtils::CBuilder::Platform::Windows.3
/usr/share/man/man3/ExtUtils::Command.3
/usr/share/man/man3/ExtUtils::Command::MM.3
/usr/share/man/man3/ExtUtils::Constant.3
/usr/share/man/man3/ExtUtils::Constant::Base.3
/usr/share/man/man3/ExtUtils::Constant::Utils.3
/usr/share/man/man3/ExtUtils::Constant::XS.3
/usr/share/man/man3/ExtUtils::Embed.3
/usr/share/man/man3/ExtUtils::Install.3
/usr/share/man/man3/ExtUtils::Installed.3
/usr/share/man/man3/ExtUtils::Liblist.3
/usr/share/man/man3/ExtUtils::MM.3
/usr/share/man/man3/ExtUtils::MM_AIX.3
/usr/share/man/man3/ExtUtils::MM_Any.3
/usr/share/man/man3/ExtUtils::MM_BeOS.3
/usr/share/man/man3/ExtUtils::MM_Cygwin.3
/usr/share/man/man3/ExtUtils::MM_DOS.3
/usr/share/man/man3/ExtUtils::MM_Darwin.3
/usr/share/man/man3/ExtUtils::MM_MacOS.3
/usr/share/man/man3/ExtUtils::MM_NW5.3
/usr/share/man/man3/ExtUtils::MM_OS2.3
/usr/share/man/man3/ExtUtils::MM_OS390.3
/usr/share/man/man3/ExtUtils::MM_QNX.3
/usr/share/man/man3/ExtUtils::MM_UWIN.3
/usr/share/man/man3/ExtUtils::MM_Unix.3
/usr/share/man/man3/ExtUtils::MM_VMS.3
/usr/share/man/man3/ExtUtils::MM_VOS.3
/usr/share/man/man3/ExtUtils::MM_Win32.3
/usr/share/man/man3/ExtUtils::MM_Win95.3
/usr/share/man/man3/ExtUtils::MY.3
/usr/share/man/man3/ExtUtils::MakeMaker.3
/usr/share/man/man3/ExtUtils::MakeMaker::Config.3
/usr/share/man/man3/ExtUtils::MakeMaker::FAQ.3
/usr/share/man/man3/ExtUtils::MakeMaker::Locale.3
/usr/share/man/man3/ExtUtils::MakeMaker::Tutorial.3
/usr/share/man/man3/ExtUtils::Manifest.3
/usr/share/man/man3/ExtUtils::Miniperl.3
/usr/share/man/man3/ExtUtils::Mkbootstrap.3
/usr/share/man/man3/ExtUtils::Mksymlists.3
/usr/share/man/man3/ExtUtils::PL2Bat.3
/usr/share/man/man3/ExtUtils::Packlist.3
/usr/share/man/man3/ExtUtils::ParseXS.3
/usr/share/man/man3/ExtUtils::ParseXS::Constants.3
/usr/share/man/man3/ExtUtils::ParseXS::Eval.3
/usr/share/man/man3/ExtUtils::ParseXS::Utilities.3
/usr/share/man/man3/ExtUtils::Typemaps.3
/usr/share/man/man3/ExtUtils::Typemaps::Cmd.3
/usr/share/man/man3/ExtUtils::Typemaps::InputMap.3
/usr/share/man/man3/ExtUtils::Typemaps::OutputMap.3
/usr/share/man/man3/ExtUtils::Typemaps::Type.3
/usr/share/man/man3/ExtUtils::testlib.3
/usr/share/man/man3/Fatal.3
/usr/share/man/man3/Fcntl.3
/usr/share/man/man3/File::Basename.3
/usr/share/man/man3/File::Compare.3
/usr/share/man/man3/File::Copy.3
/usr/share/man/man3/File::DosGlob.3
/usr/share/man/man3/File::Fetch.3
/usr/share/man/man3/File::Find.3
/usr/share/man/man3/File::Glob.3
/usr/share/man/man3/File::GlobMapper.3
/usr/share/man/man3/File::Path.3
/usr/share/man/man3/File::Spec.3
/usr/share/man/man3/File::Spec::AmigaOS.3
/usr/share/man/man3/File::Spec::Cygwin.3
/usr/share/man/man3/File::Spec::Epoc.3
/usr/share/man/man3/File::Spec::Functions.3
/usr/share/man/man3/File::Spec::Mac.3
/usr/share/man/man3/File::Spec::OS2.3
/usr/share/man/man3/File::Spec::Unix.3
/usr/share/man/man3/File::Spec::VMS.3
/usr/share/man/man3/File::Spec::Win32.3
/usr/share/man/man3/File::Temp.3
/usr/share/man/man3/File::stat.3
/usr/share/man/man3/FileCache.3
/usr/share/man/man3/FileHandle.3
/usr/share/man/man3/Filter::Simple.3
/usr/share/man/man3/Filter::Util::Call.3
/usr/share/man/man3/FindBin.3
/usr/share/man/man3/GDBM_File.3
/usr/share/man/man3/Getopt::Long.3
/usr/share/man/man3/Getopt::Std.3
/usr/share/man/man3/HTTP::Tiny.3
/usr/share/man/man3/Hash::Util.3
/usr/share/man/man3/Hash::Util::FieldHash.3
/usr/share/man/man3/I18N::Collate.3
/usr/share/man/man3/I18N::LangTags.3
/usr/share/man/man3/I18N::LangTags::Detect.3
/usr/share/man/man3/I18N::LangTags::List.3
/usr/share/man/man3/I18N::Langinfo.3
/usr/share/man/man3/IO.3
/usr/share/man/man3/IO::Compress::Base.3
/usr/share/man/man3/IO::Compress::Bzip2.3
/usr/share/man/man3/IO::Compress::Deflate.3
/usr/share/man/man3/IO::Compress::FAQ.3
/usr/share/man/man3/IO::Compress::Gzip.3
/usr/share/man/man3/IO::Compress::RawDeflate.3
/usr/share/man/man3/IO::Compress::Zip.3
/usr/share/man/man3/IO::Dir.3
/usr/share/man/man3/IO::File.3
/usr/share/man/man3/IO::Handle.3
/usr/share/man/man3/IO::Pipe.3
/usr/share/man/man3/IO::Poll.3
/usr/share/man/man3/IO::Seekable.3
/usr/share/man/man3/IO::Select.3
/usr/share/man/man3/IO::Socket.3
/usr/share/man/man3/IO::Socket::INET.3
/usr/share/man/man3/IO::Socket::IP.3
/usr/share/man/man3/IO::Socket::UNIX.3
/usr/share/man/man3/IO::Uncompress::AnyInflate.3
/usr/share/man/man3/IO::Uncompress::AnyUncompress.3
/usr/share/man/man3/IO::Uncompress::Base.3
/usr/share/man/man3/IO::Uncompress::Bunzip2.3
/usr/share/man/man3/IO::Uncompress::Gunzip.3
/usr/share/man/man3/IO::Uncompress::Inflate.3
/usr/share/man/man3/IO::Uncompress::RawInflate.3
/usr/share/man/man3/IO::Uncompress::Unzip.3
/usr/share/man/man3/IO::Zlib.3
/usr/share/man/man3/IPC::Cmd.3
/usr/share/man/man3/IPC::Msg.3
/usr/share/man/man3/IPC::Open2.3
/usr/share/man/man3/IPC::Open3.3
/usr/share/man/man3/IPC::Semaphore.3
/usr/share/man/man3/IPC::SharedMem.3
/usr/share/man/man3/IPC::SysV.3
/usr/share/man/man3/Internals.3
/usr/share/man/man3/JSON::PP.3
/usr/share/man/man3/JSON::PP::Boolean.3
/usr/share/man/man3/Locale::Maketext.3
/usr/share/man/man3/Locale::Maketext::Cookbook.3
/usr/share/man/man3/Locale::Maketext::Guts.3
/usr/share/man/man3/Locale::Maketext::GutsLoader.3
/usr/share/man/man3/Locale::Maketext::Simple.3
/usr/share/man/man3/Locale::Maketext::TPJ13.3
/usr/share/man/man3/MIME::Base64.3
/usr/share/man/man3/MIME::QuotedPrint.3
/usr/share/man/man3/Math::BigFloat.3
/usr/share/man/man3/Math::BigInt.3
/usr/share/man/man3/Math::BigInt::Calc.3
/usr/share/man/man3/Math::BigInt::FastCalc.3
/usr/share/man/man3/Math::BigInt::Lib.3
/usr/share/man/man3/Math::BigRat.3
/usr/share/man/man3/Math::Complex.3
/usr/share/man/man3/Math::Trig.3
/usr/share/man/man3/Memoize.3
/usr/share/man/man3/Memoize::AnyDBM_File.3
/usr/share/man/man3/Memoize::Expire.3
/usr/share/man/man3/Memoize::NDBM_File.3
/usr/share/man/man3/Memoize::SDBM_File.3
/usr/share/man/man3/Memoize::Storable.3
/usr/share/man/man3/Module::CoreList.3
/usr/share/man/man3/Module::CoreList::Utils.3
/usr/share/man/man3/Module::Load.3
/usr/share/man/man3/Module::Load::Conditional.3
/usr/share/man/man3/Module::Loaded.3
/usr/share/man/man3/Module::Metadata.3
/usr/share/man/man3/NEXT.3
/usr/share/man/man3/Net::Cmd.3
/usr/share/man/man3/Net::Config.3
/usr/share/man/man3/Net::Domain.3
/usr/share/man/man3/Net::FTP.3
/usr/share/man/man3/Net::NNTP.3
/usr/share/man/man3/Net::Netrc.3
/usr/share/man/man3/Net::POP3.3
/usr/share/man/man3/Net::Ping.3
/usr/share/man/man3/Net::SMTP.3
/usr/share/man/man3/Net::Time.3
/usr/share/man/man3/Net::hostent.3
/usr/share/man/man3/Net::libnetFAQ.3
/usr/share/man/man3/Net::netent.3
/usr/share/man/man3/Net::protoent.3
/usr/share/man/man3/Net::servent.3
/usr/share/man/man3/O.3
/usr/share/man/man3/Opcode.3
/usr/share/man/man3/POSIX.3
/usr/share/man/man3/Params::Check.3
/usr/share/man/man3/Parse::CPAN::Meta.3
/usr/share/man/man3/Perl::OSType.3
/usr/share/man/man3/PerlIO.3
/usr/share/man/man3/PerlIO::encoding.3
/usr/share/man/man3/PerlIO::mmap.3
/usr/share/man/man3/PerlIO::scalar.3
/usr/share/man/man3/PerlIO::via.3
/usr/share/man/man3/PerlIO::via::QuotedPrint.3
/usr/share/man/man3/Pod::Checker.3
/usr/share/man/man3/Pod::Escapes.3
/usr/share/man/man3/Pod::Html.3
/usr/share/man/man3/Pod::Html::Util.3
/usr/share/man/man3/Pod::Man.3
/usr/share/man/man3/Pod::ParseLink.3
/usr/share/man/man3/Pod::Perldoc.3
/usr/share/man/man3/Pod::Perldoc::BaseTo.3
/usr/share/man/man3/Pod::Perldoc::GetOptsOO.3
/usr/share/man/man3/Pod::Perldoc::ToANSI.3
/usr/share/man/man3/Pod::Perldoc::ToChecker.3
/usr/share/man/man3/Pod::Perldoc::ToMan.3
/usr/share/man/man3/Pod::Perldoc::ToNroff.3
/usr/share/man/man3/Pod::Perldoc::ToPod.3
/usr/share/man/man3/Pod::Perldoc::ToRtf.3
/usr/share/man/man3/Pod::Perldoc::ToTerm.3
/usr/share/man/man3/Pod::Perldoc::ToText.3
/usr/share/man/man3/Pod::Perldoc::ToTk.3
/usr/share/man/man3/Pod::Perldoc::ToXml.3
/usr/share/man/man3/Pod::Simple.3
/usr/share/man/man3/Pod::Simple::Checker.3
/usr/share/man/man3/Pod::Simple::Debug.3
/usr/share/man/man3/Pod::Simple::DumpAsText.3
/usr/share/man/man3/Pod::Simple::DumpAsXML.3
/usr/share/man/man3/Pod::Simple::HTML.3
/usr/share/man/man3/Pod::Simple::HTMLBatch.3
/usr/share/man/man3/Pod::Simple::JustPod.3
/usr/share/man/man3/Pod::Simple::LinkSection.3
/usr/share/man/man3/Pod::Simple::Methody.3
/usr/share/man/man3/Pod::Simple::PullParser.3
/usr/share/man/man3/Pod::Simple::PullParserEndToken.3
/usr/share/man/man3/Pod::Simple::PullParserStartToken.3
/usr/share/man/man3/Pod::Simple::PullParserTextToken.3
/usr/share/man/man3/Pod::Simple::PullParserToken.3
/usr/share/man/man3/Pod::Simple::RTF.3
/usr/share/man/man3/Pod::Simple::Search.3
/usr/share/man/man3/Pod::Simple::SimpleTree.3
/usr/share/man/man3/Pod::Simple::Subclassing.3
/usr/share/man/man3/Pod::Simple::Text.3
/usr/share/man/man3/Pod::Simple::TextContent.3
/usr/share/man/man3/Pod::Simple::XHTML.3
/usr/share/man/man3/Pod::Simple::XMLOutStream.3
/usr/share/man/man3/Pod::Text.3
/usr/share/man/man3/Pod::Text::Color.3
/usr/share/man/man3/Pod::Text::Overstrike.3
/usr/share/man/man3/Pod::Text::Termcap.3
/usr/share/man/man3/Pod::Usage.3
/usr/share/man/man3/SDBM_File.3
/usr/share/man/man3/Safe.3
/usr/share/man/man3/Search::Dict.3
/usr/share/man/man3/SelectSaver.3
/usr/share/man/man3/SelfLoader.3
/usr/share/man/man3/Socket.3
/usr/share/man/man3/Storable.3
/usr/share/man/man3/Symbol.3
/usr/share/man/man3/Sys::Hostname.3
/usr/share/man/man3/Sys::Syslog.3
/usr/share/man/man3/TAP::Base.3
/usr/share/man/man3/TAP::Formatter::Base.3
/usr/share/man/man3/TAP::Formatter::Color.3
/usr/share/man/man3/TAP::Formatter::Console.3
/usr/share/man/man3/TAP::Formatter::Console::ParallelSession.3
/usr/share/man/man3/TAP::Formatter::Console::Session.3
/usr/share/man/man3/TAP::Formatter::File.3
/usr/share/man/man3/TAP::Formatter::File::Session.3
/usr/share/man/man3/TAP::Formatter::Session.3
/usr/share/man/man3/TAP::Harness.3
/usr/share/man/man3/TAP::Harness::Beyond.3
/usr/share/man/man3/TAP::Harness::Env.3
/usr/share/man/man3/TAP::Object.3
/usr/share/man/man3/TAP::Parser.3
/usr/share/man/man3/TAP::Parser::Aggregator.3
/usr/share/man/man3/TAP::Parser::Grammar.3
/usr/share/man/man3/TAP::Parser::Iterator.3
/usr/share/man/man3/TAP::Parser::Iterator::Array.3
/usr/share/man/man3/TAP::Parser::Iterator::Process.3
/usr/share/man/man3/TAP::Parser::Iterator::Stream.3
/usr/share/man/man3/TAP::Parser::IteratorFactory.3
/usr/share/man/man3/TAP::Parser::Multiplexer.3
/usr/share/man/man3/TAP::Parser::Result.3
/usr/share/man/man3/TAP::Parser::Result::Bailout.3
/usr/share/man/man3/TAP::Parser::Result::Comment.3
/usr/share/man/man3/TAP::Parser::Result::Plan.3
/usr/share/man/man3/TAP::Parser::Result::Pragma.3
/usr/share/man/man3/TAP::Parser::Result::Test.3
/usr/share/man/man3/TAP::Parser::Result::Unknown.3
/usr/share/man/man3/TAP::Parser::Result::Version.3
/usr/share/man/man3/TAP::Parser::Result::YAML.3
/usr/share/man/man3/TAP::Parser::ResultFactory.3
/usr/share/man/man3/TAP::Parser::Scheduler.3
/usr/share/man/man3/TAP::Parser::Scheduler::Job.3
/usr/share/man/man3/TAP::Parser::Scheduler::Spinner.3
/usr/share/man/man3/TAP::Parser::Source.3
/usr/share/man/man3/TAP::Parser::SourceHandler.3
/usr/share/man/man3/TAP::Parser::SourceHandler::Executable.3
/usr/share/man/man3/TAP::Parser::SourceHandler::File.3
/usr/share/man/man3/TAP::Parser::SourceHandler::Handle.3
/usr/share/man/man3/TAP::Parser::SourceHandler::Perl.3
/usr/share/man/man3/TAP::Parser::SourceHandler::RawTAP.3
/usr/share/man/man3/TAP::Parser::YAMLish::Reader.3
/usr/share/man/man3/TAP::Parser::YAMLish::Writer.3
/usr/share/man/man3/Term::ANSIColor.3
/usr/share/man/man3/Term::Cap.3
/usr/share/man/man3/Term::Complete.3
/usr/share/man/man3/Term::ReadLine.3
/usr/share/man/man3/Text::Abbrev.3
/usr/share/man/man3/Text::Balanced.3
/usr/share/man/man3/Text::ParseWords.3
/usr/share/man/man3/Text::Tabs.3
/usr/share/man/man3/Text::Wrap.3
/usr/share/man/man3/Thread.3
/usr/share/man/man3/Thread::Queue.3
/usr/share/man/man3/Thread::Semaphore.3
/usr/share/man/man3/Tie::Array.3
/usr/share/man/man3/Tie::File.3
/usr/share/man/man3/Tie::Handle.3
/usr/share/man/man3/Tie::Hash.3
/usr/share/man/man3/Tie::Hash::NamedCapture.3
/usr/share/man/man3/Tie::Memoize.3
/usr/share/man/man3/Tie::RefHash.3
/usr/share/man/man3/Tie::Scalar.3
/usr/share/man/man3/Tie::StdHandle.3
/usr/share/man/man3/Tie::SubstrHash.3
/usr/share/man/man3/Time::HiRes.3
/usr/share/man/man3/Time::Local.3
/usr/share/man/man3/Time::Piece.3
/usr/share/man/man3/Time::Seconds.3
/usr/share/man/man3/Time::gmtime.3
/usr/share/man/man3/Time::localtime.3
/usr/share/man/man3/Time::tm.3
/usr/share/man/man3/UNIVERSAL.3
/usr/share/man/man3/Unicode::Collate.3
/usr/share/man/man3/Unicode::Collate::CJK::Big5.3
/usr/share/man/man3/Unicode::Collate::CJK::GB2312.3
/usr/share/man/man3/Unicode::Collate::CJK::JISX0208.3
/usr/share/man/man3/Unicode::Collate::CJK::Korean.3
/usr/share/man/man3/Unicode::Collate::CJK::Pinyin.3
/usr/share/man/man3/Unicode::Collate::CJK::Stroke.3
/usr/share/man/man3/Unicode::Collate::CJK::Zhuyin.3
/usr/share/man/man3/Unicode::Collate::Locale.3
/usr/share/man/man3/Unicode::Normalize.3
/usr/share/man/man3/Unicode::UCD.3
/usr/share/man/man3/User::grent.3
/usr/share/man/man3/User::pwent.3
/usr/share/man/man3/XSLoader.3
/usr/share/man/man3/attributes.3
/usr/share/man/man3/autodie.3
/usr/share/man/man3/autodie::Scope::Guard.3
/usr/share/man/man3/autodie::Scope::GuardStack.3
/usr/share/man/man3/autodie::Util.3
/usr/share/man/man3/autodie::exception.3
/usr/share/man/man3/autodie::exception::system.3
/usr/share/man/man3/autodie::hints.3
/usr/share/man/man3/autodie::skip.3
/usr/share/man/man3/autouse.3
/usr/share/man/man3/base.3
/usr/share/man/man3/bigfloat.3
/usr/share/man/man3/bigint.3
/usr/share/man/man3/bignum.3
/usr/share/man/man3/bigrat.3
/usr/share/man/man3/blib.3
/usr/share/man/man3/builtin.3
/usr/share/man/man3/bytes.3
/usr/share/man/man3/charnames.3
/usr/share/man/man3/constant.3
/usr/share/man/man3/deprecate.3
/usr/share/man/man3/diagnostics.3
/usr/share/man/man3/encoding.3
/usr/share/man/man3/encoding::warnings.3
/usr/share/man/man3/experimental.3
/usr/share/man/man3/feature.3
/usr/share/man/man3/fields.3
/usr/share/man/man3/filetest.3
/usr/share/man/man3/if.3
/usr/share/man/man3/integer.3
/usr/share/man/man3/less.3
/usr/share/man/man3/lib.3
/usr/share/man/man3/locale.3
/usr/share/man/man3/mro.3
/usr/share/man/man3/open.3
/usr/share/man/man3/ops.3
/usr/share/man/man3/overload.3
/usr/share/man/man3/overloading.3
/usr/share/man/man3/parent.3
/usr/share/man/man3/re.3
/usr/share/man/man3/sigtrap.3
/usr/share/man/man3/sort.3
/usr/share/man/man3/stable.3
/usr/share/man/man3/strict.3
/usr/share/man/man3/subs.3
/usr/share/man/man3/threads.3
/usr/share/man/man3/threads::shared.3
/usr/share/man/man3/utf8.3
/usr/share/man/man3/vars.3
/usr/share/man/man3/version.3
/usr/share/man/man3/version::Internals.3
/usr/share/man/man3/vmsish.3
/usr/share/man/man3/warnings.3
/usr/share/man/man3/warnings::register.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl/18eaf66587c5eea277721d5e569a6e3cd869f855
/usr/share/package-licenses/perl/6deba81fe267c399cbb316c1fb0d037b0fcdb187
/usr/share/package-licenses/perl/ddf157bc55ed6dec9541e4af796294d666cd0926

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/corelist.1
/usr/share/man/man1/cpan.1
/usr/share/man/man1/enc2xs.1
/usr/share/man/man1/encguess.1
/usr/share/man/man1/h2ph.1
/usr/share/man/man1/h2xs.1
/usr/share/man/man1/instmodsh.1
/usr/share/man/man1/json_pp.1
/usr/share/man/man1/libnetcfg.1
/usr/share/man/man1/perl.1
/usr/share/man/man1/perl5004delta.1
/usr/share/man/man1/perl5005delta.1
/usr/share/man/man1/perl5100delta.1
/usr/share/man/man1/perl5101delta.1
/usr/share/man/man1/perl5120delta.1
/usr/share/man/man1/perl5121delta.1
/usr/share/man/man1/perl5122delta.1
/usr/share/man/man1/perl5123delta.1
/usr/share/man/man1/perl5124delta.1
/usr/share/man/man1/perl5125delta.1
/usr/share/man/man1/perl5140delta.1
/usr/share/man/man1/perl5141delta.1
/usr/share/man/man1/perl5142delta.1
/usr/share/man/man1/perl5143delta.1
/usr/share/man/man1/perl5144delta.1
/usr/share/man/man1/perl5160delta.1
/usr/share/man/man1/perl5161delta.1
/usr/share/man/man1/perl5162delta.1
/usr/share/man/man1/perl5163delta.1
/usr/share/man/man1/perl5180delta.1
/usr/share/man/man1/perl5181delta.1
/usr/share/man/man1/perl5182delta.1
/usr/share/man/man1/perl5184delta.1
/usr/share/man/man1/perl5200delta.1
/usr/share/man/man1/perl5201delta.1
/usr/share/man/man1/perl5202delta.1
/usr/share/man/man1/perl5203delta.1
/usr/share/man/man1/perl5220delta.1
/usr/share/man/man1/perl5221delta.1
/usr/share/man/man1/perl5222delta.1
/usr/share/man/man1/perl5223delta.1
/usr/share/man/man1/perl5224delta.1
/usr/share/man/man1/perl5240delta.1
/usr/share/man/man1/perl5241delta.1
/usr/share/man/man1/perl5242delta.1
/usr/share/man/man1/perl5243delta.1
/usr/share/man/man1/perl5244delta.1
/usr/share/man/man1/perl5260delta.1
/usr/share/man/man1/perl5261delta.1
/usr/share/man/man1/perl5262delta.1
/usr/share/man/man1/perl5263delta.1
/usr/share/man/man1/perl5280delta.1
/usr/share/man/man1/perl5281delta.1
/usr/share/man/man1/perl5282delta.1
/usr/share/man/man1/perl5283delta.1
/usr/share/man/man1/perl5300delta.1
/usr/share/man/man1/perl5301delta.1
/usr/share/man/man1/perl5302delta.1
/usr/share/man/man1/perl5303delta.1
/usr/share/man/man1/perl5320delta.1
/usr/share/man/man1/perl5321delta.1
/usr/share/man/man1/perl5340delta.1
/usr/share/man/man1/perl5341delta.1
/usr/share/man/man1/perl5360delta.1
/usr/share/man/man1/perl5361delta.1
/usr/share/man/man1/perl5380delta.1
/usr/share/man/man1/perl561delta.1
/usr/share/man/man1/perl56delta.1
/usr/share/man/man1/perl581delta.1
/usr/share/man/man1/perl582delta.1
/usr/share/man/man1/perl583delta.1
/usr/share/man/man1/perl584delta.1
/usr/share/man/man1/perl585delta.1
/usr/share/man/man1/perl586delta.1
/usr/share/man/man1/perl587delta.1
/usr/share/man/man1/perl588delta.1
/usr/share/man/man1/perl589delta.1
/usr/share/man/man1/perl58delta.1
/usr/share/man/man1/perlaix.1
/usr/share/man/man1/perlamiga.1
/usr/share/man/man1/perlandroid.1
/usr/share/man/man1/perlapi.1
/usr/share/man/man1/perlapio.1
/usr/share/man/man1/perlartistic.1
/usr/share/man/man1/perlbook.1
/usr/share/man/man1/perlboot.1
/usr/share/man/man1/perlbot.1
/usr/share/man/man1/perlbs2000.1
/usr/share/man/man1/perlbug.1
/usr/share/man/man1/perlcall.1
/usr/share/man/man1/perlcheat.1
/usr/share/man/man1/perlclass.1
/usr/share/man/man1/perlclassguts.1
/usr/share/man/man1/perlclib.1
/usr/share/man/man1/perlcn.1
/usr/share/man/man1/perlcommunity.1
/usr/share/man/man1/perlcygwin.1
/usr/share/man/man1/perldata.1
/usr/share/man/man1/perldbmfilter.1
/usr/share/man/man1/perldebguts.1
/usr/share/man/man1/perldebtut.1
/usr/share/man/man1/perldebug.1
/usr/share/man/man1/perldelta.1
/usr/share/man/man1/perldeprecation.1
/usr/share/man/man1/perldiag.1
/usr/share/man/man1/perldoc.1
/usr/share/man/man1/perldocstyle.1
/usr/share/man/man1/perldsc.1
/usr/share/man/man1/perldtrace.1
/usr/share/man/man1/perlebcdic.1
/usr/share/man/man1/perlembed.1
/usr/share/man/man1/perlexperiment.1
/usr/share/man/man1/perlfaq.1
/usr/share/man/man1/perlfaq1.1
/usr/share/man/man1/perlfaq2.1
/usr/share/man/man1/perlfaq3.1
/usr/share/man/man1/perlfaq4.1
/usr/share/man/man1/perlfaq5.1
/usr/share/man/man1/perlfaq6.1
/usr/share/man/man1/perlfaq7.1
/usr/share/man/man1/perlfaq8.1
/usr/share/man/man1/perlfaq9.1
/usr/share/man/man1/perlfilter.1
/usr/share/man/man1/perlfork.1
/usr/share/man/man1/perlform.1
/usr/share/man/man1/perlfreebsd.1
/usr/share/man/man1/perlfunc.1
/usr/share/man/man1/perlgit.1
/usr/share/man/man1/perlglossary.1
/usr/share/man/man1/perlgov.1
/usr/share/man/man1/perlgpl.1
/usr/share/man/man1/perlguts.1
/usr/share/man/man1/perlhack.1
/usr/share/man/man1/perlhacktips.1
/usr/share/man/man1/perlhacktut.1
/usr/share/man/man1/perlhaiku.1
/usr/share/man/man1/perlhist.1
/usr/share/man/man1/perlhpux.1
/usr/share/man/man1/perlhurd.1
/usr/share/man/man1/perlintern.1
/usr/share/man/man1/perlinterp.1
/usr/share/man/man1/perlintro.1
/usr/share/man/man1/perliol.1
/usr/share/man/man1/perlipc.1
/usr/share/man/man1/perlirix.1
/usr/share/man/man1/perlivp.1
/usr/share/man/man1/perljp.1
/usr/share/man/man1/perlko.1
/usr/share/man/man1/perllexwarn.1
/usr/share/man/man1/perllinux.1
/usr/share/man/man1/perllocale.1
/usr/share/man/man1/perllol.1
/usr/share/man/man1/perlmacosx.1
/usr/share/man/man1/perlmod.1
/usr/share/man/man1/perlmodinstall.1
/usr/share/man/man1/perlmodlib.1
/usr/share/man/man1/perlmodstyle.1
/usr/share/man/man1/perlmroapi.1
/usr/share/man/man1/perlnewmod.1
/usr/share/man/man1/perlnumber.1
/usr/share/man/man1/perlobj.1
/usr/share/man/man1/perlootut.1
/usr/share/man/man1/perlop.1
/usr/share/man/man1/perlopenbsd.1
/usr/share/man/man1/perlopentut.1
/usr/share/man/man1/perlos2.1
/usr/share/man/man1/perlos390.1
/usr/share/man/man1/perlos400.1
/usr/share/man/man1/perlpacktut.1
/usr/share/man/man1/perlperf.1
/usr/share/man/man1/perlplan9.1
/usr/share/man/man1/perlpod.1
/usr/share/man/man1/perlpodspec.1
/usr/share/man/man1/perlpodstyle.1
/usr/share/man/man1/perlpolicy.1
/usr/share/man/man1/perlport.1
/usr/share/man/man1/perlpragma.1
/usr/share/man/man1/perlqnx.1
/usr/share/man/man1/perlre.1
/usr/share/man/man1/perlreapi.1
/usr/share/man/man1/perlrebackslash.1
/usr/share/man/man1/perlrecharclass.1
/usr/share/man/man1/perlref.1
/usr/share/man/man1/perlreftut.1
/usr/share/man/man1/perlreguts.1
/usr/share/man/man1/perlrepository.1
/usr/share/man/man1/perlrequick.1
/usr/share/man/man1/perlreref.1
/usr/share/man/man1/perlretut.1
/usr/share/man/man1/perlriscos.1
/usr/share/man/man1/perlrun.1
/usr/share/man/man1/perlsec.1
/usr/share/man/man1/perlsecpolicy.1
/usr/share/man/man1/perlsolaris.1
/usr/share/man/man1/perlsource.1
/usr/share/man/man1/perlstyle.1
/usr/share/man/man1/perlsub.1
/usr/share/man/man1/perlsyn.1
/usr/share/man/man1/perlsynology.1
/usr/share/man/man1/perlthanks.1
/usr/share/man/man1/perlthrtut.1
/usr/share/man/man1/perltie.1
/usr/share/man/man1/perltoc.1
/usr/share/man/man1/perltodo.1
/usr/share/man/man1/perltooc.1
/usr/share/man/man1/perltoot.1
/usr/share/man/man1/perltrap.1
/usr/share/man/man1/perltru64.1
/usr/share/man/man1/perltw.1
/usr/share/man/man1/perlunicode.1
/usr/share/man/man1/perlunicook.1
/usr/share/man/man1/perlunifaq.1
/usr/share/man/man1/perluniintro.1
/usr/share/man/man1/perluniprops.1
/usr/share/man/man1/perlunitut.1
/usr/share/man/man1/perlutil.1
/usr/share/man/man1/perlvar.1
/usr/share/man/man1/perlvms.1
/usr/share/man/man1/perlvos.1
/usr/share/man/man1/perlwin32.1
/usr/share/man/man1/perlxs.1
/usr/share/man/man1/perlxstut.1
/usr/share/man/man1/perlxstypemap.1
/usr/share/man/man1/piconv.1
/usr/share/man/man1/pl2pm.1
/usr/share/man/man1/pod2html.1
/usr/share/man/man1/pod2man.1
/usr/share/man/man1/pod2text.1
/usr/share/man/man1/pod2usage.1
/usr/share/man/man1/podchecker.1
/usr/share/man/man1/prove.1
/usr/share/man/man1/ptar.1
/usr/share/man/man1/ptardiff.1
/usr/share/man/man1/ptargrep.1
/usr/share/man/man1/shasum.1
/usr/share/man/man1/splain.1
/usr/share/man/man1/streamzip.1
/usr/share/man/man1/xsubpp.1
/usr/share/man/man1/zipdetails.1

%files perl
%defattr(-,root,root,-)
/V3/usr/lib/perl5/*
/usr/lib/perl5/*
