Description

    Theme product for College of Information Sciences and Technology at Penn State.

Installation

    1.  Add the following to buildout.cfg:

    [buildout]
    eggs =
        (other eggs)
        plonetheme.ist_theme

    ...
    zcml =
        plonetheme.ist_theme

2.  Re-run buildout (typically 'bin/buildout').

3.  Restart Zope (typically 'bin/instance restart' -- or 'bin/instance fg' on development).
