
.. index::
  single: module; new functionality

Installing new functionality
=============================

All of Open ERP's functionality is contained in its many and various modules. Many of these, the
core modules, are automatically loaded during the initial installation of the system and can be
updated online later. Although they're mostly not installed in your database at the outset, they're
available on your computer for immediate installation. Additional modules can also be loaded online
from the official Open ERP site http://openerp.com. These modules are inactive when they're loaded
into the system, and can then be installed in a separate step.

You'll start by checking if there are any updates available online that apply to your initial
installation. Then you'll install a CRM module to complete your existing database.

.. index::
  single: module; upgrading

Updating the Modules list
---------------------------

Click :menuselection:`Administration --> Modules Management --> Update Modules List` to start the
updating tool. The :guilabel:`Scan for new modules` window opens showing the addresses that
Open ERP will look in for downloading new modules (known as the repositories), and updating
existing ones.

.. tip:: Remote module repositories

	If the repository list doesn't reflect your needs then you can edit it from
	:menuselection:`Administration --> Modules Management --> Repository List`. There you can link to new
	repositories by adding their URLs and disable listed ones by unchecking their 
	:guilabel:`Active` checkbox. If
	you're not connected to the Internet then you probably want to disable anything there.

	Your Open ERP installation must be configured with its ``addons`` directory as writable for you to be
	able to download anything at all. If it hasn't been, then you may need the assistance of a systems
	administrator to change your server's settings so that you can install new modules.

Click :guilabel:`Check New Modules` to start the download from the specified locations. When it's
complete you'll see a :guilabel:`New Modules` window indicating how many new modules were downloaded
and how many existing modules were updated. Click :guilabel:`OK` to return to the updated list.

It won't matter in this chapter if you can't download anything, but some of the later chapters refer
to modules that aren't part of the core installation and have to be obtained from a remote
repository.

.. note:: Modules

	All the modules available on your computer can be found in the addons directory of your Open ERP
	server. Each module there is represented by a directory carrying the name of the module or by a
	file with the module name and .zip appended to it. The file is in ZIP archive format and replicates
	the directory structure of unzipped modules.

.. tip:: Searching through the whole list

	The list of modules shows only the first available modules. In the web client you can search or
	follow the First / Previous / Next / Last links to get to any point in the whole list, and you can
	change the number of entries listed by clicking the row number indicators between :guilabel:`Previous` 
	and :guilabel:`Next`
	and selecting a different number from the default of 20.

	If you use the GTK client you can search, as you would with the web client, or use the + icon to
	the top left of the window to change the number of entries returned by the search from its default
	limit of 80, or its default offset of 0 (starting at the first entry) in the whole list.

.. index::
  single: module; installing


Installing a module
---------------------

.. index::
   single: module; product

You'll now install a module named :mod:`product`, which will enable you to manage the company's
products. This is part of the core installation, so you don't need to load anything to make this
work, but isn't installed in the Minimal Profile.

Open the list of uninstalled modules from :menuselection:`Administration --> Modules Management -->
Modules --> Uninstalled modules`. Search for the module by entering the name :mod:`product` in the search
screen then clicking it in the list that appears below it to open it. The form that describes the
module gives you useful information such as its version number, its status and a review of its
functionality. Click :guilabel:`Schedule for Installation` 
and the status of the module changes to :guilabel:`To be installed`.


.. figure:: images/install_product_module.png
   :scale: 75
   :align: center

   *Installation of the product module*


.. tip::  Technical Guide

	If you select a module in any of the module lists by clicking on a module line and then on
	:guilabel:`Technical Guide` at the top right of the window, Open ERP produces a technical report
	on that module. It's helpful only if the module is installed, so the menu
	:menuselection:`Administration --> Modules Management --> Modules --> Installed Modules` produces the most
	fruitful list.

	This report comprises a list of all the objects and all the fields along with their descriptions.
	The report adapts to your system and reflects any modifications you've made and all the other
	modules you've installed.

Click :guilabel:`Apply Scheduled Upgrades` then :guilabel:`Start Upgrade` on the :guilabel:`System Upgrade`
form that appears. Close the window when the operation has completed. Return to the main menu you'll
see the new menu :menuselection:`Products` has become available.

.. tip::  Refreshing the menu in the GTK client

	After an update in the GTK client you'll have to open a new menu to refresh the content –
	otherwise you won't see the new menu item. To do that use the window menu :menuselection:`Form -->
	Refresh/Cancel`.

Installing a module with its dependencies
-----------------------------------------

.. index::
   single: module; crm

Now install the CRM module (Customer Relationship Management) using the same process as before.
Start from :menuselection:`Administration --> Modules Management --> Modules --> Uninstalled modules`.

	#. 	Get the list of modules to install, and search for the :mod:`crm` module in that list.
	
	#.	Schedule the module for installation by clicking :guilabel:`Schedule for Installation`.
	
	#.  Do the same for :mod:`account`. 
	
	#.  Click :guilabel:`Apply Scheduled Upgrades` on the action toolbar to the right.

	#.	Click :guilabel:`Start Upgrade` to install both modules. 
	
	#.  After a wait, when the installation is complete, click :guilabel:`Start Configuration`.
	
	#.  Accept the defaults for accounts setup and select ``None`` for the chart of accounts.
	
	#.  You'll see details of all the features installed by the modules on a new
	    :guilabel:`Features` tab on the module form. 

When you return to the main menu you'll find the new customer relationship management menu
:menuselection:`CRM & SRM`. You'll also see all the accounting functions that are now available in
the :menuselection:`Financial Management` menu.

There is no particular relationship between the modules installed and the menus added. Most of the
core modules add complete menus but some also add submenus to menus already in the system. Other
modules add menus and submenus as they need. Modules can also add additional fields to existing
forms, or simply additional demonstration data or some settings specific to a given requirement.

.. index::
  single: module; dependencies
..

.. note::  Dependencies between modules

	The module form shows two tabs before it's installed. 
	The first tab gives basic information about the module and the
	second gives a list of modules that this module depends on. So when you install a module, Open ERP
	automatically selects all the necessary dependencies to install this module.

	That's also how you develop the profile modules: they simply define a list of modules that you want
	in your profile as a set of dependencies.

Although you can install a module and all its dependencies at once, you can't remove them in one
fell swoop – you'd have to uninstall module by module. Uninstalling is more complex than
installing because you have to handle existing system data.

.. note::  Uninstalling modules

	Although it works quite well, uninstalling modules isn't perfect in Open ERP. It's not guaranteed
	to return the system exactly to the state it was in before installation.

	So it's recommended that you make a backup of the database before installing your new modules so
	that you can test the new modules and decide whether they're suitable or not. If they're not then
	you can return to your backup. If they are, then you'll probably still reinstall the modules on
	your backup so that you don't have to delete all your test data.

	If you wanted to uninstall you would use the menu :menuselection:`Administration --> Modules
	Management --> Modules --> Installed Modules` and then uninstall them in the inverse order of their
	dependencies: ``crm``, ``account``, ``product``.

Installing additional functionality
-------------------------------------

To discover the full range of Open ERP's possibilities you can install many additional modules.
Installing them with their demonstration data provides a convenient way of exploring the whole core
system. When you build on the \ ``openerp_ch02``\   database you'll automatically include
demonstration data because you checked the :guilabel:`Load Demonstration Data` checkbox when you originally
created the database.

.. index::
   single: module; importing
..

Click :menuselection:`Administration --> Modules Management --> Modules --> Uninstalled modules` to give you an
overview of all of the modules available for installation.

To test several modules you won't have to install them all one by one. You can use the dependencies
between modules to load several at once. For example, try loading the following modules:

.. index::
   single: modules; profile_

* :mod:`profile_accounting`,

* :mod:`profile_crm`,

* :mod:`profile_manufacturing`,

* :mod:`profile_service`.

To find these quickly, enter the word \ ``profile``\   in the :guilabel:`Name` field of the search
form and click :guilabel:`Filter` to search for the relevant modules. Then install them one by one
or all at once.

As you update you'll see thirty or so modules to be installed. Move on from the 
:guilabel:`System upgrade done` form by clicking :guilabel:`Start configuration` and then
accepting the default crm configuration and picking configuration in turn.

Finally install the additional modules :guilabel:`Analytic Accounting` and :guilabel:`Document Management`
when you're offered that configuration option. Don't install any more - you now have quite a 
fully-loaded system to look at.

Click :guilabel:`Home` and you'll be returned to a dashboard, not the main menu you had before. To get to
the main menu, use the :guilabel:`MAIN MENU` link. 

.. Copyright © Open Object Press. All rights reserved.

.. You may take electronic copy of this publication and distribute it if you don't
.. change the content. You can also print a copy to be read by yourself only.

.. We have contracts with different publishers in different countries to sell and
.. distribute paper or electronic based versions of this book (translated or not)
.. in bookstores. This helps to distribute and promote the Open ERP product. It
.. also helps us to create incentives to pay contributors and authors using author
.. rights of these sales.

.. Due to this, grants to translate, modify or sell this book are strictly
.. forbidden, unless Tiny SPRL (representing Open Object Press) gives you a
.. written authorisation for this.

.. Many of the designations used by manufacturers and suppliers to distinguish their
.. products are claimed as trademarks. Where those designations appear in this book,
.. and Open Object Press was aware of a trademark claim, the designations have been
.. printed in initial capitals.

.. While every precaution has been taken in the preparation of this book, the publisher
.. and the authors assume no responsibility for errors or omissions, or for damages
.. resulting from the use of the information contained herein.

.. Published by Open Object Press, Grand Rosière, Belgium
