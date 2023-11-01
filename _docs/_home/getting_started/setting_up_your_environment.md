---
nav_title: Setting up your environment
article_title: Setting up your environment
page_order: 1
noindex: true
---

# Setting up your environment

> TODO

## Before you start

You'll need to complete the following:

- [Download the recommended software]()
- [Create a GitHub account](https://github.com/join)
- Set up your GitHub SSH key:
  - [macOS](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=mac)
  - [Windows](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=windows)
  - [Linux](https://docs.github.com/en/github-ae@latest/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent?platform=linux)

## Install Ruby version `2.7.4`

To build the docs locally, you'll need Ruby version `2.7.4` installed. In the terminal, open `braze-docs` and check for Ruby version `2.7.4`.

```bash
cd ~/braze-docs
ruby --version
```

If it's not, use a [supported version manager](https://www.ruby-lang.org/en/documentation/installation/#managers) to install Ruby version `2.7.4`. For example, using [rbenv](https://github.com/rbenv/rbenv):

```bash
rbenv install 2.7.4
```

## Install Braze Docs dependencies

Next, install project dependencies.

```bash
./bundle install
```

## Starting the local server

To start your local docs server on localhost `http://127.0.0.1:4000`, run:

```bash
./rake
```

## Stopping the local server

To stop your server, reopen the terminal and press **Control**+**C**.

## Troubleshooting

### bash: rvm: command not found

If you get an error about unknown ```-bash rvm``` command, RVM might need to be added to your ~/.bash_profile file. In your terminal, copy and paste the following command:

```bash
source ~/.rvm/scripts/rvm
```

Then:

```bash
type rvm | head -n 1
```

 You should then see:

```bash
rvm is a function
```

### Bundle install issue

If you get have issues with gems, make sure to do `bundle install`. If bundle install gives you an error, try `bundle install ruby` first.

#### Patch Level error

If you get an error like `Your Ruby patchlevel is 191, but your Gemfile specified -1`, try `gem update --system` then `bundle install`.

#### Rake Error

If you get an error like `(Bundler::GemNotFound)`, try `bundle exec rake` then `bundle install`. Enter `rake` after the missing gems are downloaded.

### Gem Install Error

If `bundle install` throws a gem error like

```bash
static const int puma_parser_en_main = 1;
                 ^
1 warning generated.
compiling io_buffer.c
compiling mini_ssl.c
mini_ssl.c:145:7: warning: unused variable 'min' [-Wunused-variable]
  int min, ssl_options;
      ^
mini_ssl.c:299:40: warning: function 'raise_error' could be declared with attribute 'noreturn' [-Wmissing-noreturn]
void raise_error(SSL* ssl, int result) {
                                       ^
2 warnings generated.
compiling puma_http11.c
puma_http11.c:203:22: error: implicitly declaring library function 'isspace' with type 'int (int)' [-Werror,-Wimplicit-function-declaration]
  while (vlen > 0 && isspace(value[vlen - 1])) vlen--;
                     ^
puma_http11.c:203:22: note: include the header <ctype.h> or explicitly provide a declaration for 'isspace'
1 error generated.
make: *** [puma_http11.o] Error 1
```

try this, from [fail-to-bundle-install-puma-4-3-5](https://stackoverflow.com/a/63201544/12982278)


```bash
It seems that the latest version of XCode tools (12 Beta 3) installs a version of Clang (the C compiler used by default on MacOS) that throws an error on implicit functions used on the native extension code of Puma.

The workaround as pointed out here(https://github.com/puma/puma/issues/2304#issuecomment-664448309) is to tell Clang not to treat this behavior as an error.
```

```bash
bundle config build.puma --with-cflags="-Wno-error=implicit-function-declaration"
bundle install
```

### Java Runtime (No longer needed as of Nov 2021)

For OSX Catalina (10.15.4 and after), you might get an error saying `Java for macOS 2017-001 can't be installed on this disk: A newer version of this package is already installed`. The workaround is to download the java installer from Apple Support [https://support.apple.com/kb/DL1572?locale=en_US](https://support.apple.com/kb/DL1572?locale=en_US), and use either command line or AppleScript to modify the package.

* Command Line - Mount `JavaForOSX.dmg` by opening it, and then run the following lines in a terminal. Resulting package file will be on the desktop as `Java.pkg`. Install as normal.

```bash
pkgutil --expand /Volumes/Java\ for\ macOS\ 2017-001/JavaForOSX.pkg ~/tmp
sed -i '' 's/return false/return true/g' ~/tmp/Distribution
pkgutil --flatten ~/tmp ~/Desktop/CatalinaJava.pkg
rm -rf ~/tmp
```

If you get a `Could not open package for expansion: /Volumes/Java for macOS 2017-001/JavaForOSX.pkg`, make sure to mount/open `JavaForOSX.dmg` first.

* AppleScript - Open AppleScript from `Applications > Utilities > Script Editor`, or from `Launchpad`.
Paste the following script into the Script Editor, and click run. Select `JavaForOSX.dmg`. Resulting package file will be on the desktop as `Java.pkg`. Install as normal. 

```bash
set theDMG to choose file with prompt "Please select javaforosx.dmg:" of type {"dmg"}
do shell script "hdiutil mount " & quoted form of POSIX path of theDMG
do shell script "pkgutil --expand /Volumes/Java\\ for\\ macOS\\ 2017-001/JavaForOSX.pkg ~/tmp"
do shell script "hdiutil unmount /Volumes/Java\\ for\\ macOS\\ 2017-001/"
do shell script "sed -i '' 's/return false/return true/g' ~/tmp/Distribution"
do shell script "pkgutil --flatten ~/tmp ~/Desktop/CatalinaJava.pkg"
do shell script "rm -rf ~/tmp"
display dialog "Modified ModifiedJava6Install.pkg saved on desktop" buttons {"Ok"}
```

If successfully installed, then running `java -version` in cmd should show:

```bash
java version "1.6.0_65"
Java(TM) SE Runtime Environment (build 1.6.0_65-b14-468)
Java HotSpot(TM) 64-Bit Server VM (build 20.65-b04-468, mixed mode)
```
