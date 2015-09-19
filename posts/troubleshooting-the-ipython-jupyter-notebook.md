<!--
.. title: troubleshooting
.. slug: troubleshooting
.. date: 2015-09-19 16:47:51 UTC+12:00
.. tags: ipython,notebook,troubleshooting
.. category:
.. link:
.. description:
.. type: text
-->

In this post I am giving some pointers to troubleshoot issues when installing packages via [conda](http://conda.pydata.org/docs/intro.html) or [pip](https://pip.pypa.io/en/stable/), as well
as some pointers to solve issues running the [ipython (now jupyter)](https://jupyter.org) notebook on a machine behind a proxy.

<br>
<!-- TEASER_END -->

## install packages via conda or pip behind a proxy

You might run into some problems installing additional libraries via `conda` or `pip` and / or running the IPython notebooks, especially on Windows machines behind a proxy, here are a few solutions that may work:

<br>
**1. Proxy settings for conda:**
<br>

<br>
create a `.condarc` file (the '.' is important) in your HOME directory (on windows it should be `C:\Users\YOU`) and add the following lines:

<br>
```
proxy_servers:
    http: http://url:port
    https: http://url:port
```  
<br>

<br>
**2. specify proxy when using pip**
<br>

<br>
If you are running into issues installing libraries via pip, try specifying the proxy to use at the command line, e.g.

<br>
```
pip install --proxy=http://url:port bearcart
```
<br>

**3. Set-up system-wide proxy settings**
<br>

<br>

On Macs: in your `${HOME}/.bash_profile`, insert these lines

```
export http_proxy=http://url:port
export https_proxy=http://url:port
```

<br>
On Linux machines, do the same as above in your `${HOME}/.bashrc`

<br>

On Windows machines:

As an administrator go to `Control Panel | System | Advanced Systems Settings | Advanced Tab | Environment Variables | System Variables | New` and set

```
HTTP_PROXY=http://url:port/
HTTPS_PROXY=https://url:port/
```

You can also do that in a command window by typing (the `$` represents the prompt)

<br>
```
$ SET HTTP_PROXY=http://url:port/
$ SET HTTPS_PROXY=http://url:port/
```
<br>

<br>
## troubleshooting the ipython notebook   

<br>
**1. use Firefox instead of internet explorer to open the notebooks**
<br>

<br>
The IPython notebook is an interactive web-based 'notebook', where executable python code can be weaved with rich comments, graphic outputs etc, which make it ideal for presenting interactive tutorials. When (in a command prompt) you navigate to the directory where you have downloaded the notebooks and type (the $ sign represent the prompt):

<br>
```
$ ipython notebook
```
<br>

<br>
a 'dashboard' with the list of notebooks should come up in your browser ... now if you are on windows, chances are that your default browser is Internet Explorer, which is generally bad news. If you encounter problems (blank page, notebooks not loading, kernel interruptions etc), it's probably because of Internet Explorer. What I suggest is that you download Firefox for windows and make it the default browser to open IPython notebooks. To do that you need (once firefox is installed) to do the following :

in a command prompt type (again $ is the prompt):

<br>
```
$ ipython profile create default
```
<br>

<br>
it should create a bunch of configuration files in the following directory:
<br>

<br>
```
C:\Users\YOU\.ipython\profile_default
```
<br>

<br>
go and edit the `ipython_notebook_config.py` file
<br>

<br>
search for the line
<br>

<br>
```
#c.NotebookApp.browser =''
```
<br>

<br>
  and replace it by:
<br>

<br>
```
import webbrowser
webbrowser.register('firefox', None, webbrowser.GenericBrowser('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe'))
c.NotebookApp.browser = 'firefox'
```
<br>

<br>
**2. Specify localhost when calling the IPython notebook**
<br>

<br>
On some configurations, you might also need to call:
<br>

<br>
```
$ ipython notebook --ip=127.0.0.1
```
<br>

<br>
To specify that the browser should connect to *localhost*
<br>

<br>
**3. Clear the cache**
<br>

<br>
If you are still running into issues (notably dashboard or IPython notebook not displaying correctly), try clearing the cache of your browser
<br>

<br>
**4. Use an `incognito` window and the `no-browser` argument**
<br>

<br>
If all else fails (!), one thing that has been reported working is:
<br>

<br>
+ launch the `ipython notebook` in no-browser mode:
<br>

<br>
```
ipython notebook --no-browser
```
<br>

<br>
You should see an output in the terminal looking like:
<br>

<br>
```
...
The IPython Notebook is running at: http://localhost:8888/
...
```
<br>

<br>
Note that the URL and port could be different in your case.
<br>

<br>
Open an `incognito` window from your browser and copy the URL (`http://localhost:8888/`) in the address bar
<br>
