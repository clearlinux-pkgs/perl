Name:          perl
Version:       5.28.1
Release:       51
URL:           http://perl.org
Source0:       http://www.cpan.org/src/5.0/perl-5.28.1.tar.gz
Summary:       The perl interpreter
Group:         Development
License:       GPL-1.0+ GPL-1.0 bzip2-1.0.6 Artistic-1.0-Perl GPL-2.0+ MIT BSD-3-Clause
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Patch1: config_h_delta.patch

BuildRequires: groff
BuildRequires: gdbm-dev
BuildRequires: netbase 
BuildRequires: bison
BuildRequires: flex

Provides: perl(Archive::Tar) perl(autodie)
Provides: perl(base) perl(B::Debug) perl(bytes)
Provides: perl(Carp) perl(Compress::Raw::Bzip2)
Provides: perl(Compress::Raw::Zlib) perl(constant) perl(CPAN)
Provides: perl(CPAN::Meta) perl(CPAN::Meta::Requirements)
Provides: perl(CPAN::Meta::YAML) perl(Cwd)
Provides: perl(Data::Dumper) perl(DB_File) perl(DBIx::Simple) perl(Devel::PPPort)
Provides: perl(Digest) perl(Digest::MD5) perl(Digest::SHA) perl(DynaLoader)
Provides: perl(Encode) perl(encoding) perl(Env)
Provides: perl(experimental) perl(Exporter) perl(ExtUtils::CBuilder)
Provides: perl(ExtUtils::Command) perl(ExtUtils::Embed)
Provides: perl(ExtUtils::Install) perl(ExtUtils::MakeMaker)
Provides: perl(ExtUtils::Manifest) perl(ExtUtils::Miniperl)
Provides: perl(ExtUtils::ParseXS)
Provides: perl(File::Basename) perl(File::Copy) perl(File::Fetch) perl(File::Find) perl(File::Path) perl(File::Temp)
Provides: perl(Filter) perl(Filter::Simple)
Provides: perl(Getopt::Long)
Provides: perl(IO::Compress) perl(IO::File) perl(IO::Socket::IP) perl(IO::Zlib)
Provides: perl(IPC::Cmd) perl(IPC::Open3)
Provides: perl(HTTP::Tiny)
Provides: perl(JSON::PP)
Provides: perl(Locale::Codes) perl(Locale::Maketext)
Provides: perl(Locale::Maketext::Simple)
Provides: perl(Module::CoreList)
Provides: perl(Module::CoreList::tools) perl(Module::Load) perl(Module::Load::Conditional)
Provides: perl(Module::Loaded) perl(Module::Metadata)
Provides: perl(overload)
Provides: perl(parent) perl(Params::Check) perl(Parse::CPAN::Meta)
Provides: perl(PathTools) perl(Perl::OSType) perl(Pod::Checker) perl(Pod::Escapes) perl(POSIX)
Provides: perl(Pod::Parser) perl(Pod::Perldoc) perl(Pod::Simple) perl(Pod::Usage) perl(podlators)
Provides: perl(Safe) perl(Scalar::List::Utils) perl(Socket) perl(Storable) perl(strict) perl(Sys::Syslog)
Provides: perl(Scalar::Util)
Provides: perl(Term::ANSIColor) perl(Test::Harness) perl(Text::ParseWords)
Provides: perl(Text::Tabs+Wrap) perl(Text::Wrap) perl(Thread::Queue) perl(Time::HiRes) perl(Time::Local)
Provides: perl(Time::Piece) perl(threads) perl(threads::shared)
Provides: perl(vars) perl(version) perl(warnings) perl(YAML::Any)

Provides: perl(DBD::SQLite) perl(FLTK)
Provides:  perl(Qt) perl(Qt::slots) perl(Cocoa::EventLoop)  perl(Qt::isa) perl(Irssi) perl(EV) = 4.11
Provides: /opt/bin/perl
Provides: perl(:MODULE_COMPAT_5.18.0) perl(:MODULE_COMPAT_5.20.0) perl(:MODULE_COMPAT_5.20.2) perl(:MODULE_COMPAT_5.22.0) perl(:MODULE_COMPAT_5.16.2) perl(:MODULE_COMPAT_5.28.1)
Provides: perl(unicore::Name) perl(mtr_misc.pl)  perl(Win32::ODBC)
Provides: perl(Git::SVN::Utils) perl(Memoize) perl(Memoize::Storable) perl(SVN::Client)
Provides: perl(SVN::Core) perl(SVN::Delta) perl(SVN::Ra) perl(Term::ReadKey) perl(Curses)


# fake provides
Provides: perl(NDBM_File) perl(Your::Module::Here) perl(VMS::Stdio) perl(bigint.pl) perl(Tk::Pod) perl(VMS::Filespec) perl(Mac::InternetConfig)
Provides: perl(Tk) perl(Mac::BuildTools)
Provides: perl = 1:5.16.2
Provides: perl = 1:5.18.0
Provides: perl = 1:5.20.0
Provides: perl = 1:5.20.2
Provides: perl = 1:5.22.0
Provides: perl = 1:5.28.1
Provides: perl = 1:5.010001
Provides: /usr/bin/perl /usr/sbin/perl /bin/perl /sbin/perl
Provides: perl(RRDs) perl(Win32API::File)  perl(Win32::Process)



Requires: perl-Test-Simple
Requires: perl-Math-BigInt-GMP

%description
Perl 5 is a highly capable, feature-rich programming language with over 27 years of development.
Perl 5 runs on over 100 platforms from portables to mainframes and is suitable for both rapid 
prototyping and large scale development projects.



%package doc
Summary: doc components for the perl package.
Group: Documentation

%description doc
doc components for the perl package.




%prep
%setup -q
%patch1 -p1

%build
export CFLAGS="$CFLAGS -O3 -ffunction-sections -fno-semantic-interposition -fopt-info-vec -ffat-lto-objects -flto=4"
export CXXFLAGS="$CXXFLAGS -O3 -ffunction-sections -fno-semantic-interposition -fopt-info-vec -ffat-lto-objects -flto=4"
export AR=gcc-ar
export RANLIB=gcc-ranlib

./Configure -d -e -Dprefix=/usr -Dsiteprefix=/usr/local -Dvendorprefix=/usr -Dinstallman1dir='/usr/share/man/man1' -Dinstallman3dir='/usr/share/man/man3' -Dusethreads -Duseshrplib -Adefine:d_procselfexe -Adefine:procselfexe='"/proc/self/exe"' -Dotherlibdirs=/usr/lib/perl5/site_perl/5.28.1

sed -i sqman1dir=\'\'qman1dir=\'/usr/share/man/man1\'q config.sh
sed -i sqman3dir=\'\'qman3dir=\'/usr/share/man/man3\'q config.sh

./Configure -der

sed -i sqman1dir=\'\'qman1dir=\'/usr/share/man/man1\'q config.sh
sed -i sqman3dir=\'\'qman3dir=\'/usr/share/man/man3\'q config.sh

sed -i   "s/optimize=.*/optimize=\'\-O3 -ffunction-sections -fno-semantic-interposition -fopt-info-vec -ffat-lto-objects -flto=4 \'/g" config.sh

sed -i "s/-fstack-protector-strong/-D_FORTIFY_SOURCE=2/g" config.sh

make  %{?_smp_mflags}

%install
%make_install
rm -f $RPM_BUILD_ROOT/usr/lib*/perl5/5.28.1/i686-linux/CORE/libperl.a

%check
LC_ALL=C make test ||:

%clean

%files 
%defattr(-, root, root, -)
#/usr/bin/c2ph
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
/usr/bin/perl5.28.1
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
/usr/bin/podselect
/usr/bin/prove
#/usr/bin/pstruct
/usr/bin/ptar
/usr/bin/ptardiff
/usr/bin/ptargrep
/usr/bin/shasum
/usr/bin/splain
/usr/bin/xsubpp
/usr/bin/zipdetails
/usr/lib/perl5/5.28.1/AnyDBM_File.pm
/usr/lib/perl5/5.28.1/App/*
/usr/lib/perl5/5.28.1/Archive/Tar.pm
/usr/lib/perl5/5.28.1/Archive/Tar/*.pm
/usr/lib/perl5/5.28.1/Attribute/Handlers.pm
/usr/lib/perl5/5.28.1/AutoLoader.pm
/usr/lib/perl5/5.28.1/AutoSplit.pm
/usr/lib/perl5/5.28.1/B/*.pm
/usr/lib/perl5/5.28.1/Benchmark.pm
/usr/lib/perl5/5.28.1/CORE.pod
/usr/lib/perl5/5.28.1/CPAN.pm
/usr/lib/perl5/5.28.1/CPAN/*
/usr/lib/perl5/5.28.1/Carp.pm
/usr/lib/perl5/5.28.1/Carp/Heavy.pm
/usr/lib/perl5/5.28.1/Class/Struct.pm
/usr/lib/perl5/5.28.1/Compress/Zlib.pm
/usr/lib/perl5/5.28.1/Config/*
/usr/lib/perl5/5.28.1/DB.pm
/usr/lib/perl5/5.28.1/DBM_Filter.pm
/usr/lib/perl5/5.28.1/DBM_Filter/*
/usr/lib/perl5/5.28.1/Devel/SelfStubber.pm
/usr/lib/perl5/5.28.1/Digest.pm
/usr/lib/perl5/5.28.1/Digest/base.pm
/usr/lib/perl5/5.28.1/Digest/file.pm
/usr/lib/perl5/5.28.1/DirHandle.pm
/usr/lib/perl5/5.28.1/Dumpvalue.pm
/usr/lib/perl5/5.28.1/Encode/*
/usr/lib/perl5/5.28.1/English.pm
/usr/lib/perl5/5.28.1/Env.pm
/usr/lib/perl5/5.28.1/Exporter.pm
/usr/lib/perl5/5.28.1/Exporter/Heavy.pm
/usr/lib/perl5/5.28.1/ExtUtils/*
/usr/lib/perl5/5.28.1/Fatal.pm
/usr/lib/perl5/5.28.1/File/*
/usr/lib/perl5/5.28.1/FileCache.pm
/usr/lib/perl5/5.28.1/FileHandle.pm
/usr/lib/perl5/5.28.1/Filter/Simple.pm
/usr/lib/perl5/5.28.1/FindBin.pm
/usr/lib/perl5/5.28.1/Getopt/Long.pm
/usr/lib/perl5/5.28.1/Getopt/Std.pm
/usr/lib/perl5/5.28.1/HTTP/Tiny.pm
/usr/lib/perl5/5.28.1/I18N/*
/usr/lib/perl5/5.28.1/IO/*
/usr/lib/perl5/5.28.1/IPC/*
/usr/lib/perl5/5.28.1/JSON/PP.pm
/usr/lib/perl5/5.28.1/JSON/PP/Boolean.pm
/usr/lib/perl5/5.28.1/Locale/*
/usr/lib/perl5/5.28.1/Math/Trig.pm
/usr/lib/perl5/5.28.1/Math/Complex.pm
/usr/lib/perl5/5.28.1/Math/BigInt*
/usr/lib/perl5/5.28.1/Math/BigFloat*
/usr/lib/perl5/5.28.1/Math/BigRat*
/usr/lib/perl5/5.28.1/Memoize.pm
/usr/lib/perl5/5.28.1/Memoize/*
/usr/lib/perl5/5.28.1/Module/*
/usr/lib/perl5/5.28.1/NEXT.pm
/usr/lib/perl5/5.28.1/Net/*
/usr/lib/perl5/5.28.1/Params/Check.pm
/usr/lib/perl5/5.28.1/Parse/CPAN/Meta.pm
/usr/lib/perl5/5.28.1/Perl/OSType.pm
/usr/lib/perl5/5.28.1/PerlIO.pm
/usr/lib/perl5/5.28.1/PerlIO/via/QuotedPrint.pm
/usr/lib/perl5/5.28.1/Pod/*
/usr/lib/perl5/5.28.1/Safe.pm
/usr/lib/perl5/5.28.1/Search/Dict.pm
/usr/lib/perl5/5.28.1/SelectSaver.pm
/usr/lib/perl5/5.28.1/SelfLoader.pm
/usr/lib/perl5/5.28.1/Symbol.pm
/usr/lib/perl5/5.28.1/TAP/*
/usr/lib/perl5/5.28.1/Term/*
/usr/lib/perl5/5.28.1/Test.pm
# /usr/lib/perl5/5.28.1/Test/*
/usr/lib/perl5/5.28.1/Internals.pod
/usr/lib/perl5/5.28.1/Test/Builder/Formatter.pm
/usr/lib/perl5/5.28.1/Test/Builder/TodoDiag.pm
/usr/lib/perl5/5.28.1/Test2.pm
/usr/lib/perl5/5.28.1/Test2/*
/usr/lib/perl5/5.28.1/Test/Harness.pm
/usr/lib/perl5/5.28.1/Text/*
/usr/lib/perl5/5.28.1/Thread.pm
/usr/lib/perl5/5.28.1/Thread/*
/usr/lib/perl5/5.28.1/Tie/*
/usr/lib/perl5/5.28.1/Time/*
/usr/lib/perl5/5.28.1/UNIVERSAL.pm
/usr/lib/perl5/5.28.1/Unicode/*
/usr/lib/perl5/5.28.1/User/*
/usr/lib/perl5/5.28.1/XSLoader.pm
/usr/lib/perl5/5.28.1/_charnames.pm
/usr/lib/perl5/5.28.1/autodie.pm
/usr/lib/perl5/5.28.1/autodie/*
/usr/lib/perl5/5.28.1/autouse.pm
/usr/lib/perl5/5.28.1/base.pm
/usr/lib/perl5/5.28.1/bigint.pm
/usr/lib/perl5/5.28.1/bignum.pm
/usr/lib/perl5/5.28.1/bigrat.pm
/usr/lib/perl5/5.28.1/blib.pm
/usr/lib/perl5/5.28.1/bytes.pm
/usr/lib/perl5/5.28.1/bytes_heavy.pl
/usr/lib/perl5/5.28.1/charnames.pm
/usr/lib/perl5/5.28.1/constant.pm
/usr/lib/perl5/5.28.1/deprecate.pm
/usr/lib/perl5/5.28.1/diagnostics.pm
/usr/lib/perl5/5.28.1/dumpvar.pl
/usr/lib/perl5/5.28.1/encoding/warnings.pm
/usr/lib/perl5/5.28.1/experimental.pm
/usr/lib/perl5/5.28.1/feature.pm
/usr/lib/perl5/5.28.1/fields.pm
/usr/lib/perl5/5.28.1/filetest.pm
/usr/lib/perl5/5.28.1/if.pm
/usr/lib/perl5/5.28.1/integer.pm
/usr/lib/perl5/5.28.1/less.pm
/usr/lib/perl5/5.28.1/locale.pm
/usr/lib/perl5/5.28.1/meta_notation.pm
/usr/lib/perl5/5.28.1/open.pm
/usr/lib/perl5/5.28.1/overload.pm
/usr/lib/perl5/5.28.1/overload/numbers.pm
/usr/lib/perl5/5.28.1/overloading.pm
/usr/lib/perl5/5.28.1/parent.pm
/usr/lib/perl5/5.28.1/perl5db.pl
/usr/lib/perl5/5.28.1/perlfaq.pm
/usr/lib/perl5/5.28.1/pod/*
/usr/lib/perl5/5.28.1/sigtrap.pm
/usr/lib/perl5/5.28.1/sort.pm
/usr/lib/perl5/5.28.1/strict.pm
/usr/lib/perl5/5.28.1/subs.pm
/usr/lib/perl5/5.28.1/unicore/*
/usr/lib/perl5/5.28.1/utf8.pm
/usr/lib/perl5/5.28.1/utf8_heavy.pl
/usr/lib/perl5/5.28.1/vars.pm
/usr/lib/perl5/5.28.1/version.pm
/usr/lib/perl5/5.28.1/version.pod
/usr/lib/perl5/5.28.1/version/Internals.pod
/usr/lib/perl5/5.28.1/version/regex.pm
/usr/lib/perl5/5.28.1/vmsish.pm
/usr/lib/perl5/5.28.1/warnings.pm
/usr/lib/perl5/5.28.1/warnings/register.pm
/usr/lib/perl5/5.28.1/x86_64-linux*/*
/usr/lib/perl5/5.28.1/x86_64-linux*/.packlist
# Files included in perl-Test-Simple package
%exclude /usr/lib/perl5/5.28.1/Test/Builder.pm
%exclude /usr/lib/perl5/5.28.1/Test/Builder/IO/Scalar.pm
%exclude /usr/lib/perl5/5.28.1/Test/Builder/Module.pm
%exclude /usr/lib/perl5/5.28.1/Test/Builder/Tester.pm
%exclude /usr/lib/perl5/5.28.1/Test/Builder/Tester/Color.pm
%exclude /usr/lib/perl5/5.28.1/Test/More.pm
%exclude /usr/lib/perl5/5.28.1/Test/Simple.pm
%exclude /usr/lib/perl5/5.28.1/Test/Tester/Capture.pm
%exclude /usr/lib/perl5/5.28.1/Test/Tester/CaptureRunner.pm
%exclude /usr/lib/perl5/5.28.1/Test/Tester/Delegate.pm
%exclude /usr/lib/perl5/5.28.1/Test/Tester.pm
%exclude /usr/lib/perl5/5.28.1/Test/Tutorial.pod
%exclude /usr/lib/perl5/5.28.1/Test/use/ok.pm
%exclude /usr/lib/perl5/5.28.1/ok.pm

%files doc
/usr/share/man/man1/*
/usr/share/man/man3/App::*
/usr/share/man/man3/Archive::*
/usr/share/man/man3/Attribute::Handlers.3
/usr/share/man/man3/AutoLoader.3
/usr/share/man/man3/AutoSplit.3
/usr/share/man/man3/AnyDBM_File.3
/usr/share/man/man3/B.3
/usr/share/man/man3/B::*
/usr/share/man/man3/Benchmark.3
/usr/share/man/man3/CORE.3
/usr/share/man/man3/CPAN.3
/usr/share/man/man3/CPAN::*
/usr/share/man/man3/Carp.3
/usr/share/man/man3/Class::Struct.3
/usr/share/man/man3/Compress::*
/usr/share/man/man3/Config.3
/usr/share/man/man3/Config::*
/usr/share/man/man3/Cwd.3
/usr/share/man/man3/DB.3
/usr/share/man/man3/DBM_Filter.3
/usr/share/man/man3/DBM_Filter::*
/usr/share/man/man3/Data::Dumper.3
/usr/share/man/man3/Devel::*
/usr/share/man/man3/Digest.3
/usr/share/man/man3/Digest::*
/usr/share/man/man3/DirHandle.3
/usr/share/man/man3/Dumpvalue.3
/usr/share/man/man3/DynaLoader.3
/usr/share/man/man3/Encode.3
/usr/share/man/man3/Encode::*
/usr/share/man/man3/English.3
/usr/share/man/man3/Env.3
/usr/share/man/man3/Errno.3
/usr/share/man/man3/Exporter.3
/usr/share/man/man3/Exporter::Heavy.3
/usr/share/man/man3/ExtUtils::*
/usr/share/man/man3/Fatal.3
/usr/share/man/man3/Fcntl.3
/usr/share/man/man3/File::*
/usr/share/man/man3/FileCache.3
/usr/share/man/man3/FileHandle.3
/usr/share/man/man3/Filter::Simple.3
/usr/share/man/man3/Filter::Util::Call.3
/usr/share/man/man3/FindBin.3
/usr/share/man/man3/GDBM_File.3
/usr/share/man/man3/Getopt::Long.3
/usr/share/man/man3/Getopt::Std.3
/usr/share/man/man3/HTTP::Tiny.3
/usr/share/man/man3/Hash::*
/usr/share/man/man3/I18N::*
/usr/share/man/man3/IO.3
/usr/share/man/man3/IO::*
/usr/share/man/man3/IPC::*
/usr/share/man/man3/JSON::*
/usr/share/man/man3/List::*
/usr/share/man/man3/Locale::*
/usr/share/man/man3/MIME::*
/usr/share/man/man3/Math::*
/usr/share/man/man3/Memoize.3
/usr/share/man/man3/Memoize::*
/usr/share/man/man3/Module::*
/usr/share/man/man3/NDBM_File.3
/usr/share/man/man3/NEXT.3
/usr/share/man/man3/Net::*
/usr/share/man/man3/O.3
/usr/share/man/man3/ODBM_File.3
/usr/share/man/man3/Opcode.3
/usr/share/man/man3/POSIX.3
/usr/share/man/man3/Params::Check.3
/usr/share/man/man3/Parse::CPAN::Meta.3
/usr/share/man/man3/Perl::OSType.3
/usr/share/man/man3/PerlIO.3
/usr/share/man/man3/PerlIO::*
/usr/share/man/man3/Pod::*
/usr/share/man/man3/SDBM_File.3
/usr/share/man/man3/Safe.3
/usr/share/man/man3/Scalar::Util.3
/usr/share/man/man3/Search::Dict.3
/usr/share/man/man3/SelectSaver.3
/usr/share/man/man3/SelfLoader.3
/usr/share/man/man3/Socket.3
/usr/share/man/man3/Storable.3
/usr/share/man/man3/Sub::Util.3
/usr/share/man/man3/Symbol.3
/usr/share/man/man3/Sys::Hostname.3
/usr/share/man/man3/Sys::Syslog.3
/usr/share/man/man3/TAP::*
/usr/share/man/man3/Term::*
/usr/share/man/man3/Test.3
/usr/share/man/man3/Test::Harness.3
/usr/share/man/man3/Text::*
/usr/share/man/man3/Thread.3
/usr/share/man/man3/Thread::*
/usr/share/man/man3/Tie::*
/usr/share/man/man3/Time::*
/usr/share/man/man3/UNIVERSAL.3
/usr/share/man/man3/Unicode::*
/usr/share/man/man3/User::*
/usr/share/man/man3/XSLoader.3
/usr/share/man/man3/arybase.3
/usr/share/man/man3/attributes.3
/usr/share/man/man3/autodie.3
/usr/share/man/man3/autodie::*
/usr/share/man/man3/autouse.3
/usr/share/man/man3/base.3
/usr/share/man/man3/bigint.3
/usr/share/man/man3/bignum.3
/usr/share/man/man3/bigrat.3
/usr/share/man/man3/blib.3
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
/usr/share/man/man3/strict.3
/usr/share/man/man3/subs.3
/usr/share/man/man3/threads.3
/usr/share/man/man3/threads::shared.3
/usr/share/man/man3/utf8.3
/usr/share/man/man3/vars.3
/usr/share/man/man3/version.3
/usr/share/man/man3/version::*
/usr/share/man/man3/vmsish.3
/usr/share/man/man3/warnings.3
/usr/share/man/man3/warnings::*
/usr/share/man/man3/Internals.3
%exclude /usr/share/man/man3/Test2*
%exclude /usr/share/man/man3/Test::Builder::Formatter.3
%exclude /usr/share/man/man3/Test::Builder::TodoDiag.3


# Files included in perl-Test-Simple package
%exclude /usr/share/man/man3/Test::Builder.3
%exclude /usr/share/man/man3/Test::Builder::Module.3
%exclude /usr/share/man/man3/Test::Builder::IO::Scalar.3
%exclude /usr/share/man/man3/Test::Builder::Tester.3
%exclude /usr/share/man/man3/Test::Builder::Tester::Color.3
%exclude /usr/share/man/man3/Test::More.3
%exclude /usr/share/man/man3/Test::Simple.3
%exclude /usr/share/man/man3/Test::Tutorial.3
%exclude /usr/share/man/man3/Test::Tester.3
%exclude /usr/share/man/man3/Test::Tester::Capture.3
%exclude /usr/share/man/man3/Test::Tester::CaptureRunner.3
%exclude /usr/share/man/man3/Test::use::ok.3
%exclude /usr/share/man/man3/ok.3
%exclude /usr/share/man/man3/Test2*
