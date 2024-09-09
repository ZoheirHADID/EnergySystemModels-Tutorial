1. Thermodynamic Cycles Package
===============================

.. _installation:

1.1. Fluid Source
-----------------
1.1.1. Input parameters
+++++++++++++++++++++++

To use EnergySystemModels, first install it using pip:

   .. list-table:: Input parameters of Fluid Source module
      :widths: 25 25 25 25
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

1.1.2. Example
+++++++++++++++++++++++

Load the library:

>>> from ThermodynamicCycles.Source import Source

Create Source Object :

>>> SOURCE=Source.Object()

Input Data Setting : 

>>> SOURCE.Pi_bar=1.01325
>>> SOURCE.fluid="air"
>>> SOURCE.F_kgs=1
#SOURCE.F_Sm3s=2937.482966/3600 #SOURCE.F_m3s=2480.143675/3600
#SOURCE.F_Sm3h=1 #SOURCE.F_m3h=2480.143675 #SOURCE.F_kgh=3600
#SOURCE.Timestamp="2023-04-12 20:28:22"

Calculate Object :

>>> SOURCE.calculate()

Print the output data :

>>> print(SOURCE.df)
                          Source
Timestamp    2023-04-12 20:28:22
src_Ti_degC                 25.0
src_fluid                    air
src_F_Sm3h                3600.0
src_F_m3h            3725.299011
src_F_kgh            4411.940477
src_F_kgs               1.225539
src_F_m3s               1.034805
src_F_Sm3s                   1.0

If no timestamp is provided, the model will consider the time corresponding to when the simulation was launched.

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


