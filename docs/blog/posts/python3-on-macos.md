---
date: 2023-09-07
title: Python 3 on macOS
description: Setting up Python 3, virtual environments and package management on macOS
---

# Python 3 on macOS

From my explorations over the years it seems that Python is a particularly important language in the world of GIS. I thought it would be best to get comfortable with how to manage Python installations and the various external packages a project might use.

<!-- more -->

## Install Python with asdf

I use several different programming languages in my day-to-day and after using various tools over the years have settled on using [asdf](https://asdf-vm.com) to install and manage those languages.

asdf makes it easy to install multiple versions of a language and switch between them as your projects require. They provide extensive documentation on [Installing asdf](https://asdf-vm.com/guide/getting-started.html).

Once asdf is installed we can add its Python plugin, install the latest version of Python, and set that version as our default:

```bash
$ asdf plugin add python
$ asdf install python latest
$ asdf global python latest
$ which python
/Users/brian/.asdf/shims/python
$ python --version
Python 3.11.5
```

## Create a Project Directory

Now that Python is installed we can create a directory for our project:

```bash
$ mkdir lostmapper
$ cd lostmapper
$ asdf local python 3.11.5
```

Here we are making a directory for our project and switching into it. The last line creates a `.tools-version` file that lets asdf know what version of Python we want to use whenever we're working in that directory.

## Create and Activate a Virtual Environment

When you're working many different programming projects they are likely to use both the same and different external packages. In some cases, they may even use the same package but a different version of that package. This can get confusing for both people and computers!

To avoid conflicts between the packages in any two projects it is best to give each project its own space to exist in. In Python, these are known as Virtual Environments and are managed using Python's [venv module](https://docs.python.org/3/library/venv.html).

To create and activate a virtual environment, use the following commands:

```bash
$ python -m venv .venv
$ source .venv/bin/activate
```

The first line creates a virtual environment in the subdirectory `.venv`. The second line activates that virtual environment. After that, any packages we add will only be installed within that virtual environment.

!!! warning "Don't Check In Your Virtual Environment Directory"
    If you're using a version control system like [Git](https://git-scm.com) you'll want to add the `.venv` directory to your project's `.gitignore` file so that you're not checking all those packages in.

## Visualize Python Versions and Virtual Environments (Optional)

I use a tool called [Starship](https://starship.rs) that gives me a succinct and informational prompt in my terminal. It lets me know:

- What directory I'm currently in
- Which branch I'm on when using version control systems like [Git](https://git-scm.com)
- What languages and versions of languages are being used
- What virtual environment I'm currently in, if any

For example, at this point, my prompt looks like this:

```bash
~/workspace/lostmapper via 🐍 v3.11.5 (.venv)
```

And yes, different languages have their own little emoji!

## Add Packages Using pip

Now that we have a virtual environment set up we can start adding packages. To do that we'll use [pip](https://pip.pypa.io/) - package installer for Python.

If we want to add the [mkdocs]() package to our project, we would do the following:

```bash
$ python -m pip install mkdocs
```

If we look in `.venv/lib/python3.11/site-packages` we can see that `mkdocs` has been installed along with all the packages it depends on.

## Freeze and Share Required Packages

Now that we've added some packages it's a good idea to track what we've installed along with which specific version we're using. This is helpful if we're ever developing on another computer or collaborating with other people.

To generate a list of packages, run the following:

```bash
$ python -m pip freeze > requirements.txt
```

This creates a `requirements.txt` file in our project that we or others can use to install the same packages we're using. The file could be named anything but `requirements.txt` seems to be the agreed-upon standard for Python projects.

Here's what ours looks like now:

```text
click==8.1.7
ghp-import==2.1.0
Jinja2==3.1.2
Markdown==3.4.4
MarkupSafe==2.1.3
mergedeep==1.3.4
mkdocs==1.5.2
packaging==23.1
pathspec==0.11.2
platformdirs==3.10.0
python-dateutil==2.8.2
PyYAML==6.0.1
pyyaml_env_tag==0.1
six==1.16.0
watchdog==3.0.0
```

Of course, depending on when you do this the version numbers may differ.

!!! tip "Installing Packages On Another Computer"
    To install all the same packages on another computer, run the following command after creating and activating your virtual environment:

    ```
    $ python -m pip install -r requirements.txt
    ```

## Summary

We've learned how to install Python using asdf, create virtual environments using venv, and add and track packages using pip. This should help us feel a little less lost when working on Python projects moving forward.

As one might guess, these are not the only tools available for managing Python versions and packages but for the most part, we're leaning on what's built in with Python - modules that should always be available once Python is installed.
