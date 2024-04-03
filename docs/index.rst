About PyHam
===========

PyHam is a collection of applications and software libraries for ham radio
enthusiasts, written in Python.

The applications are intended to address real-world use cases for the ham while
keeping complexity to a minimum and focusing on ease of use. By avoiding the
lure of trying to be all things to all people, PyHam applications target the
majority of users at the possible expense of those few who may desire
additional capabilities.

The libraries are written in pure Python, and each focus on a particular
technology with the goal of making that technology easier to work with than
it otherwise would be. PyHam applications are themselves built upon these
libraries.

PyHam software has been developed with a primary focus on Direwolf as a
platform, since it is the dominant software TNC in use today. However, where
appropriate, the software has also been tested against other platforms such as
ldsped and AGWPE.

Applications
============

Paracon
-------

Paracon is a packet radio terminal application for Linux, Mac and Windows. It
runs in a terminal window, supports multiple simultaneous connected-mode
sessions, and has support for unproto mode.

`Learn more <https://paracon.readthedocs.io>`__

Libraries
=========

PyHam libraries are Python packages that can be installed from
`PyPI <https://pypi.org>`__, the Python Package Index, using ``pip``.

PyHam_AX25
----------

A set of modules for working with AX.25 packets in an amateur packet radio
environment on all platforms. Includes support for NET/ROM routing table
updates, and also facilities for working with the Linux native AX.25 stack.

`Learn more <https://pyham_ax25.readthedocs.io>`__

PyHam_KISS
----------

A client implementation of the KISS TNC protocol, providing send and receive
capability via a TCP/IP connection.

`Learn more <https://pyham_kiss.readthedocs.io>`__

PyHam_PE
--------

A full Packet Engine client library for the AGWPE protocol, enabling and
simplifying the creation of connected-mode and unconnected applications that
communicate through servers such as Direwolf or ldsped.

`Learn more <https://pyham_pe.readthedocs.io>`__

About Open Source
=================

Many libraries and applications in the ham radio arena are "closed source",
meaning that the source code is not made available by the author. While this
is something that many hams don't really think about, problems can arise when
the author becomes a Silent Key, or simply loses interest in maintaining the
software. At some point, a closed source application may cease to function on
a new version of an operating system, or may depend on old libraries that are
no longer available, leaving the users with no recourse but to seek alternative
software, if such even exists. Unfortunately, there are numerous instances in
which this has happened.

By making libraries and applications Open Source, the source code is available
to interested parties, such that these kinds of problems may be resolved should
they arise. The opportunity exists for a developer community to be created
around the code, in addition to a user community, and for that community to
pick up the torch in the event that the original author(s) are no longer
available to further develop it. In addition, Open Source provides an excellent
source for those who wish to learn how to construct their own libraries and
applications.
