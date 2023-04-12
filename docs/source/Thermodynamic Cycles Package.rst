1. Thermodynamic Cycles Package
=====

.. _installation:

1.1. Fluid Source
-----------------

To use EnergySystemModels, first install it using pip:

   .. list-table:: Title
      :widths: 25 25 50 50
      :header-rows: 1
      
      * - Symbol
        - Description
        - SI Units
        - Used Units
      * - Ti_degC
        - Inlet temerature
        - K
        - degC
      * - fluid
        - Fluid/Refrigerant name
        - String
        - air,ammonia,R134a,...
      * -
        -
        -
        -

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


