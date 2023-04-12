1. Thermodynamic Cycles Package
=====

.. _installation:

1.1. Fluid Source
-----------------

To use EnergySystemModels, first install it using pip:

   .. list-table:: Title
      :widths: 25 25 50
      :header-rows: 1
      
      * - Symbol 1, column 1
        - Description 1, column 2
        - Heading row 1, column 3
      * - Row 1, column 1
        -
        - Row 1, column 3
      * - Row 2, column 1
        - Row 2, column 2
        - Row 2, column 3

1.2. Sink
---------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For example:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']


