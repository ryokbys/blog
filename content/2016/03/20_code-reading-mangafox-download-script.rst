
:title: MangaFox-Download-Script
:date: 2016-03-20 14:32:50
:category: misc
:slug: code-reading-mangafox-download-script
:authors: Ryo KOBAYASHI
:tags: python, code-reading

`MangaFox <http://mangafox.me>`_ is a manga database site which provide a lot of mangas traslated to English.
(I don't know if their copyrights are OK...) 
Anyways, when you want to read mangas hosted at the site, you have to have the internet connection.
But, for example, if you want to read mangas during long flight or travelling abroad where the internet connection is not available,
basically you cannot read those mangas.
Since so many people want to download whole chapter or volume of mangas to their portable, 
there are some scripts and programs that can download **manga** data from MangaFox or other sites.

`MangaFox-Download-Script <https://github.com/techwizrd/MangaFox-Download-Script>`_ is one of those scripts.
Since I was interested in how to do scraping website using **Python** with some useful modules,
I read the script and learned some from the script.
Here is my memorandum of the code-reading.

Usage of MangaFox-Download-Script
-----------------------------------

The script is open at github.

* `techwizrd/MangaFox-Download-Script <https://github.com/techwizrd/MangaFox-Download-Script>`_

And its usage is simple.
::

   $ python mfdl.py [manga_name]
   or
   $ python mfdl.py [manga_name] [chapter_number]
   or
   $ python mfdl.py [manga_name] [chapter_start] [chapter_end]


Bugfix
-------
The script does not work without the following bugfix.

Original form of the ``get_page_soup``, which translates webpage data to a ``BeautifulSoup`` object,
is written with ``urllib.urlopen()`` as,

.. code-block:: python

   def get_page_soup(url):
       """Download a page and return a BeautifulSoup object of the html"""
       with closing(urllib.urlopen(url)) as html_file:
           return BeautifulSoup(html_file.read())

but this did not work for a specific webpage in MangaFox presumably because of text encoding problem.
So I changed the code as follows.

.. code-block:: python

   def get_page_soup(url):
       """Download a page and return a BeautifulSoup object of the html"""
       req = requests.get(url)
       return BeautifulSoup(req.text.encode(req.encoding))


Things learned from this code-reading
----------------------------------------

BeautifulSoup (BS)
^^^^^^^^^^^^^^^^^^^^
It is a library which enables us to parse **html** and **xml**.
So the BS helps us to analyze websites without coding a lot about messy task about parsing html.

There seems to be alternatives for BS, such as **lxml** which is more efficient than BS since it uses C libraries.

It is easy to create a BS object from the website URL by doing

.. code-block:: python

   req = requests.get(url)
   return BeautifulSoup(req.text.encode(req.encoding))


Lambda expression
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
I did not know *lambda expression* can be used in python, or maybe I have heard of that...

The deffinition of it is

.. code-block:: python

   lambda <arg1>, <arg2>, <arg3>,...: <expression>

and you can use like the following

.. code-block:: python

   >>> func = lambda x,y,z: x + y + z
   >>> func(1,2,3)
   6

To be honest, I still don't know how useful it is, but it can be used even where you can not use ``def`` statements like,

.. code-block:: python

   >>> l = [(lambda x: x**2), (lambda x:x**3)]
   >>> for f in l:
   ...     print f(2)
   ...
   4
   8



