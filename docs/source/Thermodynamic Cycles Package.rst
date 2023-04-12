1. Thermodynamic Cycles Package
===============================

.. _installation:

1.1. Fluid Source
-----------------
1.1.1. Input parameters
+++++++++++++++++++++++

To use EnergySystemModels, first install it using pip:

   .. list-table:: Input parameters of Fluid Source module
      :widths: 25 25 50 50
      :header-rows: 1
      
      * - Symbol
        - Description
        - SI Units
        - Used Units
      * - Ti_degC
        - Inlet temerature
        - K
        - °C
      * - fluid
        - Fluid/Refrigerant name
        - String
        - air,ammonia,R134a,...
      * - F_kgs, F_Sm3s, F_m3s, F_Sm3h, F_m3h, F_kgh
        - Input Flow rate
        - kg/s
        - kg/s, Sm3/s, m3/s, Sm3/h, m3/h, kg/h
      * - Pi_bar
        - Inlet Pressure
        - Pa
        - bara

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


