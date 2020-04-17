


<html lang="en">
<head>
<link href="https://files.realpython.com" rel="preconnect">
<link href="/static/favicon.68cbf4197b0c.png" rel="icon">
<link href="https://realpython.com/atom.xml" rel="alternate" title="Real Python" type="application/atom+xml">
<link rel="manifest" href="/manifest.json">

</head>
<body>


<div class="container main-content">
<div class="row justify-content-center">
<div class="col-md-11 col-lg-8 article">
<h1>Python 3 Installation &amp; Setup Guide</h1>

<div class="article-body">
<div class="bg-light sidebar-module sidebar-module-inset" id="toc">
<p class="h3 mb-2 text-muted">Table of Contents</p>
<div class="toc">
<ul>
<li><a href="#windows">Windows</a><ul>
<li><a href="#step-1-download-the-python-3-installer">Step 1: Download the Python 3 Installer</a></li>
<li><a href="#step-2-run-the-installer">Step 2: Run the Installer</a></li>
</ul>
</li>
<li><a href="#windows-subsystem-for-linux-wsl">Windows Subsystem for Linux (WSL)</a></li>
<li><a href="#linux">Linux</a><ul>
<li><a href="#ubuntu">Ubuntu</a></li>
<li><a href="#linux-mint">Linux Mint</a></li>
<li><a href="#debian">Debian</a></li>
<li><a href="#opensuse">openSUSE</a></li>
<li><a href="#centos">CentOS</a></li>
<li><a href="#fedora">Fedora</a></li>
<li><a href="#arch-linux">Arch Linux</a></li>
<li><a href="#compiling-python-from-source">Compiling Python From Source</a></li>
</ul>
</li>
<li><a href="#macos-mac-os-x">macOS / Mac OS X</a><ul>
<li><a href="#step-1-install-homebrew-part-1">Step 1: Install Homebrew (Part 1)</a></li>
<li><a href="#step-2-install-homebrew-part-2">Step 2: Install Homebrew (Part 2)</a></li>
<li><a href="#step-3-install-python">Step 3: Install Python</a></li>
</ul>
</li>
<li><a href="#ios-iphone-ipad">iOS (iPhone / iPad)</a></li>
<li><a href="#android-phones-tablets">Android (Phones &amp; Tablets)</a></li>
<li><a href="#online-python-interpreters">Online Python Interpreters</a></li>
<li><a href="#conclusion">Conclusion</a></li>
</ul>
</div>
</div>
<div class="sidebar-module sidebar-module-inset p-0" style="overflow:hidden;">
<div style="display:block;position:relative;">
<div style="display:block;width:100%;padding-top:12.5%;"></div>
<div class="rpad" data-unit="8x1" style="position:absolute;left:0;top:0;right:0;bottom:0;overflow:hidden;"></div>
</div>
</div>
<div class="border rounded p-3 card mb-2">
<p class="mb-0"><span class="badge badge-pill badge-success"><i class="fa fa-play-circle" aria-hidden="true"></i> Watch Now</span> This tutorial has a related video course created by the Real Python team. Watch it together with the written tutorial to deepen your understanding: <a class="stretched-link text-success" href="/courses/installing-python-windows-macos-linux/"><strong>Installing Python on Windows, macOS, and Linux</strong></a></p>
</div>
<p>To get started working with Python 3, you&rsquo;ll need to have access to the Python interpreter. There are several common ways to accomplish this:</p>
<ul>
<li>Python can be obtained from the <strong>Python Software Foundation</strong> website at <a href="https://www.python.org">python.org</a>. Typically, that involves downloading the appropriate <strong>installer</strong> for your operating system and running it on your machine.</li>
<li>Some operating systems, notably Linux, provide a <strong>package manager</strong> that can be run to install Python.</li>
<li>On macOS, the best way to install Python 3 involves installing a package manager called <strong>Homebrew</strong>. You&rsquo;ll see how to do this in the relevant section in the tutorial.</li>
<li>On mobile operating systems like Android and iOS, you can install apps that provide a Python programming environment. This can be a great way to practice your coding skills on the go.</li>
</ul>
<p>Alternatively, there are several websites that allow you to access a Python interpreter online without installing anything on your computer at all.</p>
<div class="alert alert-primary" role="alert">
<p><strong>Note:</strong> There is a chance that Python may have been shipped with your operating system and is already installed. Even if that is the case, it may be that the installed version is outdated, in which case you will want to obtain the latest version anyhow.</p>
</div>
<p>In this Python installation guide, you&rsquo;ll see step by step how to set up a working Python 3 distribution on Windows, macOS, Linux, iOS, and Android. So let&rsquo;s get started!</p>
<div class="w-100 text-center js-needs-scaling" style="transform-origin: 0 0;"><div id="waldo-tag-4996"></div> <a class="small text-muted js-disclosure" href="/account/join/" rel="nofollow" style="display: none;"> <i aria-hidden="true" class="fa fa-info-circle"> </i> Remove ads</a></div><h2 id="windows">Windows</h2>
<p>It is highly unlikely that your Windows system shipped with Python already installed. Windows systems typically do not. Fortunately, installing does not involve much more than downloading the Python installer from the <a href="https://www.python.org">python.org website</a> and running it. Let&rsquo;s take a look at how to install Python 3 on Windows:</p>
<h3 id="step-1-download-the-python-3-installer">Step 1: Download the Python 3 Installer</h3>
<ol>
<li>Open a browser window and navigate to the <a href="https://www.python.org/downloads/windows/">Download page for Windows</a> at <a href="https://www.python.org/">python.org</a>.</li>
<li>Underneath the heading at the top that says <strong>Python Releases for Windows</strong>, click on the link for the <strong>Latest Python 3 Release - Python 3.x.x</strong>. (As of this writing, the latest is Python 3.6.5.)</li>
<li>Scroll to the bottom and select either <strong>Windows x86-64 executable installer</strong> for 64-bit or <strong>Windows x86 executable installer</strong> for 32-bit. (See below.)</li>
</ol>
<blockquote>
<h4 id="sidebar-32-bit-or-64-bit-python">Sidebar: 32-bit or 64-bit Python?</h4>
<p>For Windows, you can choose either the 32-bit or 64-bit installer. Here&rsquo;s what the difference between the two comes down to:</p>
<ul>
<li>If your system has a 32-bit processor, then you should choose the 32-bit installer.</li>
<li>On a 64-bit system, either installer will actually work for most purposes. The 32-bit version will generally use less memory, but the 64-bit version performs better for applications with intensive computation.</li>
<li>If you&rsquo;re unsure which version to pick, go with the 64-bit version.</li>
</ul>
<p><strong>Note:</strong> Remember that if you get this choice &ldquo;wrong&rdquo; and would like to switch to another version of Python, you can just uninstall Python and then re-install it by downloading another installer from <a href="https://python.org">python.org</a>.</p>
</blockquote>
<h3 id="step-2-run-the-installer">Step 2: Run the Installer</h3>
<p>Once you have chosen and downloaded an installer, simply run it by double-clicking on the downloaded file. A dialog should appear that looks something like this:</p>
<p><a href="https://files.realpython.com/media/win-install-dialog.40e3ded144b0.png" target="_blank"><img loading="lazy" class="img-fluid mx-auto d-block w-66" src="https://files.realpython.com/media/win-install-dialog.40e3ded144b0.png" width="549" height="338" srcset="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/win-install-dialog.40e3ded144b0.png&amp;w=137&amp;sig=7b376ba736d80de386e1ebd01774161a3aac1fc5 137w, https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/win-install-dialog.40e3ded144b0.png&amp;w=274&amp;sig=684abcec4e2e4bcdd2b674144a07faf5a82ca26e 274w, https://files.realpython.com/media/win-install-dialog.40e3ded144b0.png 549w" sizes="75vw" alt="Windows installation dialog" /></a></p>
<div class="alert alert-primary" role="alert">
<p><strong>Important:</strong> You want to be sure to check the box that says <strong>Add Python 3.x to PATH</strong> as shown to ensure that the interpreter will be placed in your execution path.</p>
</div>
<p>Then just click <strong>Install Now</strong>. That should be all there is to it. A few minutes later you should have a working Python 3 installation on your system.</p>
<h2 id="windows-subsystem-for-linux-wsl">Windows Subsystem for Linux (WSL)</h2>
<p>If you are running Windows 10 Creators or Anniversary Update, you actually have another option for installing Python. These versions of Windows 10 include a feature called the <strong>Windows Subsystem for Linux,</strong> which allows you to run a Linux environment directly in Windows, unmodified and without the overhead of a virtual machine.</p>
<ul>
<li>For more information, see the <a href="https://docs.microsoft.com/en-us/windows/wsl/about">Windows Subsystem for Linux Documentation</a> article on the Microsoft website.</li>
<li>For instructions on how to enable the subsystem in Windows 10 and install a Linux distribution, see the <a href="https://docs.microsoft.com/en-us/windows/wsl/install-win10">Windows 10 Installation Guide</a>.</li>
<li>You can also check out this presentation on YouTube by <a href="https://www.youtube.com/watch?v=JZCPYWrTLTg">Sarah Cooley</a>, one of the members of the WSL development team.</li>
</ul>
<p>Once you have installed the Linux distribution of your choice, you can install Python 3 from a Bash console window, just as you would if you were running that Linux distribution natively. (See below.)</p>
<h2 id="linux">Linux</h2>
<p>There is a very good chance your Linux distribution has Python installed already, but it probably won&rsquo;t be the latest version, and it may be Python 2 instead of Python 3.</p>
<p>To find out what version(s) you have, open a terminal window and try the following commands:</p>
<ul>
<li><code>python --version</code></li>
<li><code>python2 --version</code></li>
<li><code>python3 --version</code></li>
</ul>
<p>One or more of these commands should respond with a version, as below:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> python3 --version
<span class="go">Python 3.6.5</span>
</code></pre></div>
<p>If the version shown is Python 2.x.x or a version of Python 3 that is not the latest (3.6.5 as of this writing), then you will want to install the latest version. The procedure for doing this will depend on the Linux distribution you are running.</p>
<div class="alert alert-primary" role="alert">
<p>Note that it is frequently easier to use a tool called <code>pyenv</code> to manage multiple Python versions on Linux. To learn more about it, see our article <a href="https://realpython.com/python-virtual-environments-a-primer/#using-different-versions-of-python">here</a>.</p>
</div>
<div class="w-100 text-center js-needs-scaling" style="transform-origin: 0 0;"><div id="waldo-tag-4998"></div> <a class="small text-muted js-disclosure" href="/account/join/" rel="nofollow" style="display: none;"> <i aria-hidden="true" class="fa fa-info-circle"> </i> Remove ads</a></div><h3 id="ubuntu">Ubuntu</h3>
<p>Depending on the version of the Ubuntu distribution you run, the Python install instructions vary. You can determine your local Ubuntu version by running the following command:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> lsb_release -a
<span class="go">No LSB modules are available.</span>
<span class="go">Distributor ID: Ubuntu</span>
<span class="go">Description:    Ubuntu 16.04.4 LTS</span>
<span class="go">Release:        16.04</span>
<span class="go">Codename:       xenial</span>
</code></pre></div>
<p>Depending on the version number you see under <code>Release</code> in the console output, follow the instructions below:</p>
<ul>
<li>
<p><strong>Ubuntu 17.10, Ubuntu 18.04</strong> (and above) come with Python 3.6 by default. You should be able to invoke it with the command <code>python3</code>.</p>
</li>
<li>
<p><strong>Ubuntu 16.10 and 17.04</strong> do not come with Python 3.6 by default, but it is in the Universe repository. You should be able to install it with the following commands:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> sudo apt-get update
<span class="gp">$</span> sudo apt-get install python3.6
</code></pre></div>
<p>You can then invoke it with the command <code>python3.6</code>.</p>
</li>
<li>
<p>If you are using <strong>Ubuntu 14.04 or 16.04</strong>, Python 3.6 is not in the Universe repository, and you need to get it from a Personal Package Archive (PPA). For example, to install Python from the <a href="https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa">&ldquo;deadsnakes&rdquo; PPA</a>, do the following:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> sudo add-apt-repository ppa:deadsnakes/ppa
<span class="gp">$</span> sudo apt-get update
<span class="gp">$</span> sudo apt-get install python3.6
</code></pre></div>
<p>As above, invoke with the command <code>python3.6</code>.</p>
</li>
</ul>
<h3 id="linux-mint">Linux Mint</h3>
<p>Mint and Ubuntu use the same package management system, which frequently makes life easier. You can follow the instructions above for <strong>Ubuntu 14.04</strong>. The <a href="https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa">&ldquo;deadsnakes&rdquo; PPA</a> works with Mint.</p>
<h3 id="debian">Debian</h3>
<p>We found sources that indicated that the Ubuntu 16.10 method would work for Debian, but we never found a path to get it to work on Debian 9. Instead, we ended up making Python from source as listed below.</p>
<p>One issue with Debian, however, is that it generally does not install the <code>sudo</code> command by default. To install it, you&rsquo;ll need to do the following before you carry out the <a href="#compiling-python-from-source">Compiling Python From Source</a> instructions below:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> su
<span class="gp">$</span> apt-get install sudo
<span class="gp">$</span> vi /etc/sudoers
</code></pre></div>
<p>After that, open the <code>/etc/sudoers</code> file using the <code>sudo vim</code> command (or your favorite text editor.) Add the following line of text to the end of the file, replacing <code>your_username</code> with your actual username:</p>
<div class="highlight text"><pre><span></span><code>your_username ALL=(ALL) ALL
</code></pre></div>
<h3 id="opensuse">openSUSE</h3>
<p>We found several sites describing how to get <code>zypper</code> to install the latest version of Python, but they seemed problematic or outdated. We did not manage to get any of them to work successfully, so we fell back to building Python from source. To do that, you will need to install the development tools, which can be done in <code>YaST</code> (via the menus) or by using <code>zypper</code>:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> sudu zypper install -t pattern devel_C_C++
</code></pre></div>
<p>This step took a while and involved the installation of 154 packages, but once it was completed, we were able to build the source as shown in the <a href="#compiling-python-from-source">Compiling Python From Source</a> section above.</p>
<h3 id="centos">CentOS</h3>
<p>The <a href="https://ius.io/">IUS Community</a> does a nice job of providing newer versions of software for &ldquo;Enterprise Linux&rdquo; distros (i.e. Red Hat Enterprise and CentOS). You can use their work to help you install Python 3.</p>
<p>To install, you should first update your system with the <a href="https://www.centos.org/docs/5/html/yum/">yum package manager</a>:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> sudo yum update
<span class="gp">$</span> sudo yum install yum-utils
</code></pre></div>
<p>You can then install the CentOS IUS package which will get you up to date with their site:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> sudo yum install https://centos7.iuscommunity.org/ius-release.rpm
</code></pre></div>
<p>Finally you can then install Python and Pip:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> sudo yum install python36u
<span class="gp">$</span> sudo yum install python36u-pip
</code></pre></div>
<p>Thanks to Jani Karhunen for his <a href="https://janikarhunen.fi/how-to-install-python-3-6-1-on-centos-7.html">excellent writeup</a> for CentOS 7.</p>
<div class="w-100 text-center js-needs-scaling" style="transform-origin: 0 0;"><div id="waldo-tag-5000"></div> <a class="small text-muted js-disclosure" href="/account/join/" rel="nofollow" style="display: none;"> <i aria-hidden="true" class="fa fa-info-circle"> </i> Remove ads</a></div><h3 id="fedora">Fedora</h3>
<p>Fedora has a roadmap to switch to Python 3 as the default Python published <a href="https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3">here</a>. It indicates that the current version and the next few versions will all ship with Python 2 as the default, but Python 3 will be installed. If the <code>python3</code> installed on your version is not 3.6, you can use the following command to install it:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> sudo dnf install python36
</code></pre></div>
<h3 id="arch-linux">Arch Linux</h3>
<p>Arch Linux is fairly aggressive about keeping up with Python releases. It is likely you already have the latest version. If not, you can use this command:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> packman -S python
</code></pre></div>
<h3 id="compiling-python-from-source">Compiling Python From Source</h3>
<p>Sometimes your Linux distribution will not have the latest version of Python, or maybe you just want to be able to build the latest, greatest version yourself. Here are the steps you need to take to build Python from source:</p>
<h4 id="step-1-download-the-source-code">Step 1: Download the Source Code</h4>
<p>To start, you need to get the Python source code. Python.org makes this fairly easy. If you go to the <a href="https://www.python.org/downloads/source/">Downloads</a> page, you will see the latest source for Python 3 at the top. (Make sure you don&rsquo;t grab Legacy Python, Python 2.)</p>
<p>When you select the version, at the bottom of the page there is a <strong>Files</strong> section. Select the <strong>Gzipped source tarball</strong> and download it to your machine. If you prefer a command line method, you can easily use <code>wget</code> to download it to your current directory:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> wget https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tgz
</code></pre></div>
<h4 id="step-2-prepare-your-system">Step 2: Prepare Your System</h4>
<p>There are a few distro-specific steps involved in building Python from scratch. The goal of each step is the same on all distros, but you might need to translate to your distribution if it does not use <code>apt-get</code>:</p>
<ol>
<li>
<p>The first step you should take when doing an operation like this is to update the system packages on your machine before you start. On Debian, this is what that looks like:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> sudo apt-get update
<span class="gp">$</span> sudo apt-get upgrade
</code></pre></div>
</li>
<li>
<p>Next, we want to make sure the system has the tools needed to build Python. There are a bunch of them and you might already have some, but that&rsquo;s fine. I&rsquo;ve listed them all in one command line, but you can break the list into shorter commands by just repeating the <code>sudo apt-get install -y</code> portion:</p>
<div class="highlight sh"><pre><span></span><code><span class="c1"># For apt-based systems (like Debian, Ubuntu, and Mint)</span>
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev  libncursesw5-dev xz-utils tk-dev

<span class="c1"># For yum-based systems (like CentOS)</span>
$ sudo yum -y groupinstall development
$ sudo yum -y install zlib-devel
</code></pre></div>
</li>
</ol>
<h4 id="step-3-build-python">Step 3: Build Python</h4>
<ol>
<li>
<p>Once you have the prerequisites and the tar file, you can unpack the source into a directory. Note that the following command will create a new directory called <code>Python-3.6.5</code> under the one you are in:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> tar xvf Python-3.6.5.tgz
<span class="gp">$</span> <span class="nb">cd</span> Python-3.6.5
</code></pre></div>
</li>
<li>
<p>Now you need to run the <code>./configure</code> tool to prepare the build:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> ./configure --enable-optimizations --with-ensurepip<span class="o">=</span>install
</code></pre></div>
</li>
<li>
<p>Next, you build the Python programs using <code>make</code>. The <code>-j</code> option simply tells <code>make</code> to split the building into parallel steps to speed up the compilation. Even with the parallel builds, this step can take a several minutes:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> make -j <span class="m">8</span>
</code></pre></div>
</li>
<li>
<p>Then, you&rsquo;ll want to install your new version of Python. You&rsquo;ll use the <code>altinstall</code> target here in order to <strong>not</strong> overwrite the system&rsquo;s version of Python. Since you&rsquo;re installing Python into <code>/usr/bin</code>, you&rsquo;ll need to run as root:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> sudo make altinstall
</code></pre></div>
<blockquote>
<p><strong>Warning</strong>: Please only use the <code>altinstall</code> target on <code>make</code>. Using the <code>install</code> target will overwrite the <code>python</code> binary. While this seems like it would be cool, there are big portions of the system that rely on the pre-installed version of Python.</p>
</blockquote>
</li>
</ol>
<h4 id="step-4-verify-your-python-install">Step 4: Verify Your Python Install</h4>
<p>Finally, you can test out your new Python version:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> python3.6 -V
<span class="go">Python 3.6.5</span>
</code></pre></div>
<div class="w-100 text-center js-needs-scaling" style="transform-origin: 0 0;"><div id="waldo-tag-5002"></div> <a class="small text-muted js-disclosure" href="/account/join/" rel="nofollow" style="display: none;"> <i aria-hidden="true" class="fa fa-info-circle"> </i> Remove ads</a></div><h2 id="macos-mac-os-x">macOS / Mac OS X</h2>
<p>While current versions of macOS (previously known as &ldquo;Mac OS X&rdquo;) include a version of Python 2, it is likely out of date by a few months. Also, this tutorial series uses Python 3, so let&rsquo;s get you upgraded to that.</p>
<p>The best way we found to install Python 3 on macOS is through the <a href="https://brew.sh">Homebrew package manager</a>. This approach is also recommended by community guides like <a href="http://docs.python-guide.org/en/latest/starting/install3/osx/">The Hitchhiker&rsquo;s Guide to Python</a>.</p>
<h3 id="step-1-install-homebrew-part-1">Step 1: Install Homebrew (Part 1)</h3>
<p>To get started, you first want to install Homebrew:</p>
<ol>
<li>Open a browser and navigate to <a href="http://brew.sh/">http://brew.sh/</a>. After the page has finished loading, <strong>select the Homebrew bootstrap code under &ldquo;Install Homebrew&rdquo;</strong>. Then hit <span class="keys"><kbd class="key-command">Cmd</kbd><span>+</span><kbd class="key-c">C</kbd></span> to copy it to the clipboard. Make sure you&rsquo;ve captured the text of the complete command because otherwise the installation will fail.</li>
<li>Now you need to <strong>open a Terminal.app window, paste the Homebrew bootstrap code, and then hit</strong> <span class="keys"><kbd class="key-enter">Enter</kbd></span>. This will begin the Homebrew installation.</li>
<li>If you&rsquo;re doing this on a fresh install of macOS, you may get a pop up alert <strong>asking you to install Apple&rsquo;s &ldquo;command line developer tools&rdquo;</strong>. You&rsquo;ll need those to continue with the installation, so please <strong>confirm the dialog box by clicking on &ldquo;Install&rdquo;</strong>.</li>
</ol>
<p>At this point, you&rsquo;re likely waiting for the command line developer tools to finish installing, and that&rsquo;s going to take a few minutes. Time to grab a coffee or tea!</p>
<h3 id="step-2-install-homebrew-part-2">Step 2: Install Homebrew (Part 2)</h3>
<p>You can continue installing Homebrew and then Python after the command line developer tools installation is complete:</p>
<ol>
<li>Confirm the &ldquo;The software was installed&rdquo; dialog from the developer tools installer.</li>
<li>Back in the terminal, hit <span class="keys"><kbd class="key-enter">Enter</kbd></span> to continue with the Homebrew installation.</li>
<li>Homebrew asks you to enter your password so it can finalize the installation. <strong>Enter your user account password and hit</strong> <span class="keys"><kbd class="key-enter">Enter</kbd></span> to continue.</li>
<li>Depending on your internet connection, Homebrew will take a few minutes to download its required files. Once the installation is complete, you&rsquo;ll end up back at the command prompt in your terminal window.</li>
</ol>
<p>Whew! Now that the Homebrew package manager is set up, let&rsquo;s continue on with installing Python 3 on your system.</p>
<h3 id="step-3-install-python">Step 3: Install Python</h3>
<p>Once Homebrew has finished installing, <strong>return to your terminal and run the following command</strong>:</p>
<div class="highlight sh"><pre><span></span><code><span class="gp">$</span> brew install python3
</code></pre></div>
<div class="alert alert-primary" role="alert">
<p><strong>Note:</strong> When you copy this command, be sure you don&rsquo;t include the <code>$</code> character at the beginning. That&rsquo;s just an indicator that this is a console command.</p>
</div>
<p>This will download and install the latest version of Python. After the Homebrew <code>brew install</code> command finishes, Python 3 should be installed on your system.</p>
<p>You can make sure everything went correctly by testing if Python can be accessed from the terminal:</p>
<ol>
<li>Open the terminal by launching <strong>Terminal.app</strong>.</li>
<li>Type <code>pip3</code> and hit <span class="keys"><kbd class="key-enter">Enter</kbd></span>.</li>
<li>You should see the help text from Python&rsquo;s &ldquo;Pip&rdquo; package manager. If you get an error message running <code>pip3</code>, go through the Python install steps again to make sure you have a working Python installation.</li>
</ol>
<p>Assuming everything went well and you saw the output from Pip in your command prompt window&hellip;congratulations! You just installed Python on your system, and you&rsquo;re all set to continue with the next section in this tutorial.</p>
<h2 id="ios-iphone-ipad">iOS (iPhone / iPad)</h2>
<p>The <a href="http://omz-software.com/pythonista/">Pythonista app</a> for iOS is a full-fledged Python development environment that you can run on your iPhone or iPad. It&rsquo;s basically a combination of a Python editor, documentation, and interpreter rolled into one single app.</p>
<p>Pythonista is surprisingly fun to use. It&rsquo;s a great little tool when you&rsquo;re stuck without a laptop and want to work on your Python skills on the go. It comes with the complete Python 3 standard library and even includes full documentation you can browse offline.</p>
<p>To install and set up Pythonista you need to <a href="https://geo.itunes.apple.com/us/app/pythonista-3/id1085978097?ls=1&amp;mt=8&amp;at=1000lqsw">download it from the iOS app store</a>.</p>
<div class="w-100 text-center js-needs-scaling" style="transform-origin: 0 0;"><div id="waldo-tag-5004"></div> <a class="small text-muted js-disclosure" href="/account/join/" rel="nofollow" style="display: none;"> <i aria-hidden="true" class="fa fa-info-circle"> </i> Remove ads</a></div><h2 id="android-phones-tablets">Android (Phones &amp; Tablets)</h2>
<p>If you have an Android tablet or phone and want to practice Python on the go, there are a several options available. The one that we found most reliably supports Python 3.6 is <a href="https://play.google.com/store/apps/details?id=ru.iiec.pydroid3">Pydroid 3</a>.</p>
<p>Pydroid 3 features an interpreter you can use for REPL sessions, and it also provides the ability to edit, save, and execute Python code:</p>
<p><a href="https://files.realpython.com/media/pydroid3-editor.e249ee239a85.png" target="_blank"><img loading="lazy" class="img-fluid mx-auto d-block w-50" src="https://files.realpython.com/media/pydroid3-editor.e249ee239a85.png" width="620" height="480" srcset="https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/pydroid3-editor.e249ee239a85.png&amp;w=155&amp;sig=ce82d2151beef996cf2b2e4e14996898ef733f1c 155w, https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/pydroid3-editor.e249ee239a85.png&amp;w=310&amp;sig=bc7d4ab0e221f015996820f3eaea3ef533c0a2ef 310w, https://files.realpython.com/media/pydroid3-editor.e249ee239a85.png 620w" sizes="75vw" alt="Pydroid 3 editor" /></a></p>
<p>You can <a href="https://play.google.com/store/apps/details?id=ru.iiec.pydroid3">download and install Pydroid 3 from the Google Play store</a>. There is a free version and also a paid Premium version which supports code prediction and code analysis.</p>
<h2 id="online-python-interpreters">Online Python Interpreters</h2>
<p>If you want to try out the examples in this tutorial without installing Python on your machine, there are several web sites available where you can interact with a Python interpreter online:</p>
<ul>
<li>Python.org Online Console: <a href="https://www.python.org/shell">www.python.org/shell</a></li>
<li>Python Fiddle: <a href="http://pythonfiddle.com">pythonfiddle.com</a></li>
<li>Repl.it: <a href="https://repl.it">repl.it</a></li>
<li>Trinket: <a href="https://trinket.io">trinket.io</a></li>
<li>Python Anywhere: <a href="https://www.pythonanywhere.com/">www.pythonanywhere.com</a></li>
</ul>
<p>These cloud-based Python interpreters may not be able to execute some of the more complex examples in this tutorial, but they will be adequate for running most of the simpler ones and may be a nice way to get you started. More information on using these sites is presented in the next section.</p>
<h2 id="conclusion">Conclusion</h2>
<p>This section provided you with the information you need to gain access to a Python 3 interpreter. You are now ready to head to the next section and begin interacting with Python!</p>
<div class="container py-3 series-nav mb-3">
<div class="row justify-content-between">
<div class="col-12 col-md-3 text-left text-muted ml-1"><a href="https://realpython.com/python-introduction/"> «&nbsp;Introduction to Python</a></div>
<div class="col-12 col-md-3 text-center text-muted"><a href="#">Installing Python</a></div>
<div class="col-12 col-md-3 text-right text-muted mr-1"><a href="https://realpython.com/interacting-with-python/">Interacting with Python&nbsp;»</a></div>
</div>
</div>
<div class="border rounded p-3 card mb-2">
<p class="mb-0"><span class="badge badge-pill badge-success"><i class="fa fa-play-circle" aria-hidden="true"></i> Watch Now</span> This tutorial has a related video course created by the Real Python team. Watch it together with the written tutorial to deepen your understanding: <a class="stretched-link text-success" href="/courses/installing-python-windows-macos-linux/"><strong>Installing Python on Windows, macOS, and Linux</strong></a></p>
</div>
</div>
<div class="card mt-4 mb-4 bg-secondary">
<p class="card-header h3 text-center bg-light">🐍 Python Tricks 💌</p>
<div class="card-body">
<div class="container">
<div class="row">
<div class="col-xs-12 col-sm-7">
<p>Get a short &amp; sweet <strong>Python Trick</strong> delivered to your inbox every couple of days. No spam ever. Unsubscribe any time. Curated by the Real Python team.</p>
</div>
<div class="col-xs-12 col-sm-5">
<img class="img-fluid rounded mb-3" src="/static/pytrick-dict-merge.4201a0125a5e.png" width="738" height="490" alt="Python Tricks Dictionary Merge">
</div>
</div>
<div class="row mb-3">
<form class="col-12" action="/optins/process/" method="post">
<input type="hidden" name="csrfmiddlewaretoken" value="gQL7KelAUMRddWN4osiJDkx1673ZSgNXImMd6K6s2MwmRszRKI7ScT3SmXmX6iUj">
<input type="hidden" name="slug" value="static-python-tricks-footer">
<div class="form-group">
<input name="email" type="email" class="form-control form-control-lg" placeholder="Email Address" required>
</div>
<button name="submit" type="submit" class="btn btn-primary btn-lg btn-block">Send Me Python Tricks »</button>
</form>
</div>
</div>
</div>
</div>
<div class="card mt-4" id="team">
<p class="card-header h3">About The Team</p>
<div class="card-body pb-0">
<div class="container">
<div class="row">
<p><em>Each tutorial at Real Python is created by a team of developers so that it meets our high quality standards. The team members who worked on this tutorial are:</em></p>
</div>
<div class="row align-items-center w-100 mx-auto">
<div class="col-4 col-sm-2 align-self-center">
<a href="/team/dbader/"><img src="https://files.realpython.com/media/daniel-square.d58bf4388750.jpg" class="rounded-circle img-fluid w-100" alt="Dan Bader"></a>
</div>
<div class="col pl-0 d-none d-sm-block">
<a href="/team/dbader/" class="card-link"><p>Dan</p></a>
</div>
<div class="col-4 col-sm-2 align-self-center">
<a href="/team/janderson/"><img src="https://files.realpython.com/media/jima.0b8f990b951a.jpg" class="rounded-circle img-fluid w-100" alt="Jim Anderson"></a>
</div>
<div class="col pl-0 d-none d-sm-block">
<a href="/team/janderson/" class="card-link"><p>Jim</p></a>
</div>
<div class="col-4 col-sm-2 align-self-center">
<a href="/team/jjablonski/"><img src="https://files.realpython.com/media/jjablonksi-avatar.e37c4f83308e.jpg" class="rounded-circle img-fluid w-100" alt="Joanna Jablonski"></a>
</div>
<div class="col pl-0 d-none d-sm-block">
<a href="/team/jjablonski/" class="card-link"><p>Joanna</p></a>
</div>
</div>
<div class="row align-items-center w-100 mx-auto">
<div class="col-4 col-sm-2 align-self-center">
<a href="/team/jsturtz/"><img src="https://files.realpython.com/media/img007.18d0e80683f7.jpg" class="rounded-circle img-fluid w-100" alt="John Sturtz"></a>
</div>
<div class="col pl-0 d-none d-sm-block">
<a href="/team/jsturtz/" class="card-link"><p>John</p></a>
</div>
</div>
</div>
</div>
</div>
<div class="bg-light rounded py-4 my-4 shadow shadow-sm mx-n2">
<div class="col-12 text-center d-block d-md-none">
<p class="h2 mb-3">Master <u><span class="marker-highlight">Real-World Python Skills</mark></u> With Unlimited Access to Real&nbsp;Python</p>
<p class="mb-1"><img class="w-75" src="/static/videos/lesson-locked.f5105cfd26db.svg"></p>
<p class="mx-auto w-75 mb-3 small"><strong>Join us and get access to hundreds of tutorials, hands-on video courses, and a community of expert&nbsp;Pythonistas:</strong></p>
<p class="mb-0"><a href="/account/join/?utm_source=rp_article_footer&utm_content=installing-python" class="btn btn-primary btn-sm px-4 mb-0">Level Up Your Python Skills »</a>
</div>
<div class="col-12 text-center d-none d-md-block">
<p class="h2 mb-2">Master <u><span class="marker-highlight">Real-World Python Skills</span></u><br>With Unlimited Access to Real&nbsp;Python</p>
<p class="mb-2"><img class="w-50 mb-2" src="/static/videos/lesson-locked.f5105cfd26db.svg"></p>
<p class="mx-auto w-50 mb-3"><strong>Join us and get access to hundreds of tutorials, hands-on video courses, and a community of expert Pythonistas:</strong></p>
<p><a href="/account/join/?utm_source=rp_article_footer&utm_content=installing-python" class="btn btn-primary btn-lg px-4">Level Up Your Python Skills »</a>
</div>
</div>
<div class="card mt-4" id="reader-comments">
<p class="card-header h3">What Do You Think?</p>
<div class="text-center mt-3 mb-0 p-0">
<span>
<a target="_blank" rel="nofollow" href="https://twitter.com/intent/tweet/?text=Check out this %23Python tutorial: Python%203%20Installation%20%26%20Setup%20Guide by @realpython&url=https%3A//realpython.com/installing-python/" class="mr-1 badge badge-twitter text-light mb-1"><i class="mr-1 fa fa-twitter text-light"></i>Tweet</a>
<a target="_blank" rel="nofollow" href="https://facebook.com/sharer/sharer.php?u=https%3A//realpython.com/installing-python/" class="mr-1 badge badge-facebook text-light mb-1"><i class="mr-1 fa fa-facebook text-light"></i>Share</a>
<a target="_blank" rel="nofollow" href="mailto:?subject=Python article for you&body=Check out this Python tutorial:%0A%0APython%203%20Installation%20%26%20Setup%20Guide%0A%0Ahttps%3A//realpython.com/installing-python/" class="mr-1 badge badge-red text-light mb-1"><i class="mr-1 fa fa-envelope text-light"></i>Email</a>
</span>
</div>
<div class="card-body">
<div class="alert alert-dark">
<p class="mb-0"><strong>Real Python Comment Policy:</strong> The most useful comments are those written with the goal of learning from or helping out other readers—after reading the whole article and all the earlier comments. Complaints and insults generally won’t make the cut here.</p>
</div>
<p>What’s your #1 takeaway or favorite thing you learned? How are you going to put your newfound skills to use? Leave a comment below and let us know.</p>
<div class="mb-4" id="disqus_thread">
</div>
</div>
</div>
<div class="card mt-4 mb-4">
<p class="card-header h3">Keep Learning</p>
<div class="card-body">
<p class="mb-0">Related Tutorial Categories:
<a href="/tutorials/basics/" class="badge badge-light text-muted">basics</a>
<a href="/tutorials/best-practices/" class="badge badge-light text-muted">best-practices</a>
<a href="/tutorials/python/" class="badge badge-light text-muted">python</a>
</p>
<p class="mt-3 mb-0">Recommended Video Course: <a class="text-success" href="/courses/installing-python-windows-macos-linux/">Installing Python on Windows, macOS, and Linux</a></p>
</div>
</div>
<div class="modal fade" tabindex="-1" role="dialog" id="rpvc">
<div class="modal-dialog modal-lg modal-dialog-centered" role="document">
<div class="modal-content">
<div class="modal-header border-0 mt-3">
<div class="col-12 modal-title text-center">
<h2 class="my-0 mx-5">Master <u>Real-World Python Skills</u> With Unlimited Access to Real Python</h2>
<p class="text-center text-muted mt-2 mb-1">Already a member? <a href="/account/login/">Sign-In</a></p>
</div>
</div>
<div class="modal-body bg-light">
<div class="col-12 text-center">
<p class="mb-2 mt-3"><a href="/account/join/?utm_source=rp&utm_medium=web&utm_campaign=pwn&utm_content=v1"><img class="w-50 mb-2" src="/static/videos/lesson-locked.f5105cfd26db.svg"></a></p>
<p class="mx-auto w-66 mb-3"><strong>Join us and get access to hundreds of tutorials, hands-on video courses, and a community of expert Pythonistas:</strong></p>
<p><a href="/account/join/?utm_source=rp&utm_medium=web&utm_campaign=pwn&utm_content=v1" class="btn btn-primary btn-lg px-4">See Membership Options »</a>
</div>
</div>
<div class="modal-footer border-0">
<a href="#!" class="text-muted btn" data-dismiss="modal">Close</a>
</div>
</div>
</div>
</div>
</div>
<aside class="col-md-7 col-lg-4">
<div class="card mb-3 bg-secondary">
<form class="card-body" action="/optins/process/" method="post">
<div class="form-group">
<p class="h5 text-muted text-center">— FREE Email Series —</p>
<p class="h3 text-center">🐍 Python Tricks 💌</p>
<p><img class="img-fluid rounded" src="/static/pytrick-dict-merge.4201a0125a5e.png" width="738" height="490" alt="Python Tricks Dictionary Merge"></p>
</div>
<div class="form-group">
<input type="hidden" name="csrfmiddlewaretoken" value="gQL7KelAUMRddWN4osiJDkx1673ZSgNXImMd6K6s2MwmRszRKI7ScT3SmXmX6iUj">
<input type="hidden" name="slug" value="static-python-tricks-sidebar">
<input type="email" class="form-control form-control-md" name="email" placeholder="Email&hellip;" required>
</div>
<button type="submit" name="submit" class="btn btn-primary btn-md btn-block">Get Python Tricks »</button>
<p class="mb-0 mt-2 text-muted text-center">🔒 No spam. Unsubscribe any time.</p>
</form>
</div>
<div class="sidebar-module sidebar-module-inset border">
<p class="h4"><a class="link-unstyled" href="/tutorials/all/">All Tutorial Topics</a></p>
<a href="/tutorials/advanced/" class="badge badge-light text-muted">advanced</a>
<a href="/tutorials/api/" class="badge badge-light text-muted">api</a>
<a href="/tutorials/basics/" class="badge badge-light text-muted">basics</a>
<a href="/tutorials/best-practices/" class="badge badge-light text-muted">best-practices</a>
<a href="/tutorials/community/" class="badge badge-light text-muted">community</a>
<a href="/tutorials/databases/" class="badge badge-light text-muted">databases</a>
<a href="/tutorials/data-science/" class="badge badge-light text-muted">data-science</a>
<a href="/tutorials/devops/" class="badge badge-light text-muted">devops</a>
<a href="/tutorials/django/" class="badge badge-light text-muted">django</a>
<a href="/tutorials/docker/" class="badge badge-light text-muted">docker</a>
<a href="/tutorials/flask/" class="badge badge-light text-muted">flask</a>
<a href="/tutorials/front-end/" class="badge badge-light text-muted">front-end</a>
<a href="/tutorials/intermediate/" class="badge badge-light text-muted">intermediate</a>
<a href="/tutorials/machine-learning/" class="badge badge-light text-muted">machine-learning</a>
<a href="/tutorials/python/" class="badge badge-light text-muted">python</a>
<a href="/tutorials/testing/" class="badge badge-light text-muted">testing</a>
<a href="/tutorials/tools/" class="badge badge-light text-muted">tools</a>
<a href="/tutorials/web-dev/" class="badge badge-light text-muted">web-dev</a>
<a href="/tutorials/web-scraping/" class="badge badge-light text-muted">web-scraping</a>
</div>
<div class="sidebar-module sidebar-module-inset p-0" style="overflow:hidden;">
<div style="display:block;position:relative;">
<div style="display:block;width:100%;padding-top:100%;"></div>
<div class="rpad" data-unit="1x1" style="position:absolute;left:0;top:0;right:0;bottom:0;overflow:hidden;"></div>
</div>
</div>
<div class="sidebar-sticky">
<div class="sidebar-module sidebar-module-inset border">
<p class="h4"><a class="link-unstyled" href="#toc">Table of Contents</a></p>
<div class="toc">
<ul>
<li><a href="#windows">Windows</a><ul>
<li><a href="#step-1-download-the-python-3-installer">Step 1: Download the Python 3 Installer</a></li>
<li><a href="#step-2-run-the-installer">Step 2: Run the Installer</a></li>
</ul>
</li>
<li><a href="#windows-subsystem-for-linux-wsl">Windows Subsystem for Linux (WSL)</a></li>
<li><a href="#linux">Linux</a><ul>
<li><a href="#ubuntu">Ubuntu</a></li>
<li><a href="#linux-mint">Linux Mint</a></li>
<li><a href="#debian">Debian</a></li>
<li><a href="#opensuse">openSUSE</a></li>
<li><a href="#centos">CentOS</a></li>
<li><a href="#fedora">Fedora</a></li>
<li><a href="#arch-linux">Arch Linux</a></li>
<li><a href="#compiling-python-from-source">Compiling Python From Source</a></li>
</ul>
</li>
<li><a href="#macos-mac-os-x">macOS / Mac OS X</a><ul>
<li><a href="#step-1-install-homebrew-part-1">Step 1: Install Homebrew (Part 1)</a></li>
<li><a href="#step-2-install-homebrew-part-2">Step 2: Install Homebrew (Part 2)</a></li>
<li><a href="#step-3-install-python">Step 3: Install Python</a></li>
</ul>
</li>
<li><a href="#ios-iphone-ipad">iOS (iPhone / iPad)</a></li>
<li><a href="#android-phones-tablets">Android (Phones &amp; Tablets)</a></li>
<li><a href="#online-python-interpreters">Online Python Interpreters</a></li>
<li><a href="#conclusion">Conclusion</a></li>
</ul>
</div>
</div>
<div class="sidebar-module sidebar-module-inset text-center my-3 py-0">

</div>
<div class="sidebar-module sidebar-module-inset border card">
<p><span class="badge badge-pill badge-success"><i class="fa fa-play-circle mr-1" aria-hidden="true"></i> Recommended Video Course</span><br><a class="stretched-link text-success" href="/courses/installing-python-windows-macos-linux/">Installing Python on Windows, macOS, and Linux</a></p>
</div>
<div class="sidebar-module sidebar-module-inset p-0" style="overflow:hidden;">
<div style="display:block;position:relative;">
<div style="display:block;width:100%;padding-top:25%;"></div>
<div class="rpad" data-unit="4x1" style="position:absolute;left:0;top:0;right:0;bottom:0;overflow:hidden;"></div>
</div>
</div>
</div>
</aside>
</div>
</div>
<footer class="footer">

</footer>

<script src="/static/jquery.min.220afd743d9e.js"></script>
<script src="/static/popper.min.1022eaf388cc.js"></script>
<script src="/static/bootstrap.min.61f338f870fc.js"></script>
<script src="/static/repl-toggle.366cb6d72340.js"></script>
<script>window.rp_prop_id = '58946116052';</script>
<script src="https://srv.realpython.net/tag.js" async></script>
<script src="https://cdn.thisiswaldo.com/static/js/2153.js"></script>
<script>
  (function() {
    function throttle(a, b) { var c, d; return function () { var e = this, f = arguments, g = +new Date; c && g < c + a ? (clearTimeout(d), d = setTimeout(function () { c = g, b.apply(e, f) }, a)) : (c = g, b.apply(e, f)) } }
    var elems = document.getElementsByClassName("js-needs-scaling");
    var resizeAll = function() {
      Array.prototype.forEach.call(elems, function(elem) {
        var frames = elem.getElementsByTagName("iframe")
        if (frames.length === 0) {
          return;
        }
        var disclosure = elem.getElementsByClassName("js-disclosure");
        if (disclosure.length > 0) {
          disclosure[0].style.display = "";
        } else {
          disclosure[0].style.display = "none";
        }
        if (frames[0].clientWidth <= elem.parentElement.clientWidth) {
          elem.style.transform = "";
          elem.classList.add("text-center");
          return;
        }
        elem.classList.remove("text-center");
        elem.style.transform = "scale(" + elem.clientWidth / frames[0].width + ")";
      });
    }
    var periodicResize = function() {
      resizeAll();
      setTimeout(periodicResize, 100);
    }
    setTimeout(periodicResize, 100);
  })();
  </script>
<script id="dsq-count-scr" src="https://realpython.disqus.com/count.js" async></script>
<script>
      var disqus_config = function () {
        this.page.url = 'https://realpython.com/installing-python/';
        this.page.identifier = 'https://realpython.com/installing-python/';
        this.callbacks.onReady = [function() {
          if (window.onDisqusReady) {
            window.onDisqusReady();
          }
        }];
      };
      var disqus_script_url = 'https://realpython.disqus.com/embed.js';
    </script>
<script src="/static/lazydisqus.3a3e39583b32.js" defer></script>
<script src="https://cdn.onesignal.com/sdks/OneSignalSDK.js" async></script>
<script>
    var OneSignal = window.OneSignal || [];
    OneSignal.push(function() {
      OneSignal.init({
        appId: "c0081e20-a523-42bb-b0ac-04c5a9e8bf40"
      });
    });
  </script>
<script src="/static/articlevc.11f8c3a3f08d.js" defer></script>
<script type="application/ld+json">
  {
    "@context": "http://schema.org",
    "@type": "Article",
    "headline": "Python 3 Installation &amp; Setup Guide",
    
    "image": {
      "@type": "ImageObject",
      "url": "https://files.realpython.com/media/Introduction-to-Python_Watermarked.48eeee4e1109.jpg",
      "width": 1920,
      "height": 1080
    },
    
    "mainEntityOfPage": {
      "@type": "WebPage",
      "@id": "https://realpython.com/installing-python/"
    },
    "datePublished": "2018-05-23T14:00:00+00:00",
    "dateModified": "2018-09-05T15:41:15.845249+00:00",
     "publisher": {
      "@type": "Organization",
      "name": "Real Python",
      "logo": {
        "@type": "ImageObject",
        "url": "https://realpython.com/static/real-python-logo-square-tiny.b2452b6d3823.png",
        "width": 60,
        "height": 60
      }
    },
    "author": {
      "@type": "Organization",
      "name": "Real Python",
      "url": "https://realpython.com",
      "logo": "https://realpython.com/static/real-python-logo-square.146e987bf77c.png"
    },
    "description": "In this Python installation guide you&#39;ll see step by step how to get a working Python 3 distribution set up on Windows, macOS, Linux, iOS, and Android."
  }
  </script>
<script>
  var _dcq = _dcq || [];
  var _dcs = _dcs || {};
  _dcs.account = '6214500';

  (function() {
    var dc = document.createElement('script');
    dc.type = 'text/javascript'; dc.async = true;
    dc.src = '//tag.getdrip.com/6214500.js';
    var s = document.getElementsByTagName('script')[0];
    s.parentNode.insertBefore(dc, s);
  })();
</script>
<script>
  !function(f,b,e,v,n,t,s)
  {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
  n.callMethod.apply(n,arguments):n.queue.push(arguments)};
  if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
  n.queue=[];t=b.createElement(e);t.async=!0;
  t.src=v;s=b.getElementsByTagName(e)[0];
  s.parentNode.insertBefore(t,s)}(window, document,'script',
  'https://connect.facebook.net/en_US/fbevents.js');
  fbq('init', '2220911568135371');
  fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
  src="https://www.facebook.com/tr?id=2220911568135371&ev=PageView&noscript=1"
/></noscript>
</body>
</html>
