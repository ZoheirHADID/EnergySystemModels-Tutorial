===============================
Humidity and Temperature Calculations
===============================

This guide provides detailed explanations of the equations, correlations, usage, and units for the Python functions calculating various thermodynamic properties related to humidity and temperature.

Important Equations and Correlations
=====================================

Pvs(T) - Saturation Vapor Pressure
-----------------------------------

Calculates the saturation vapor pressure of water in the air at a given temperature `T` using different equations for temperatures below and above 0°C.

- Units:
  - Input Temperature `T`: degrees Celsius (°C)
  - Output Pressure: Pascals (Pa)

.. math::

    \text{For } T < 0°C : P_{vs} = \exp\left(\frac{C1}{T_k} + C2 + \ldots + C7 \cdot \ln(T_k)\right)
    \text{For } T ≥ 0°C : P_{vs} = \exp\left(\frac{C8}{T_k} + C9 + \ldots + C13 \cdot \ln(T_k)\right)

Tw(Td, HR) - Wet-Bulb Temperature
---------------------------------

Computes the wet-bulb temperature based on dry-bulb temperature `Td` and relative humidity `HR`.

- Units:
  - Input `Td` (Dry-bulb temperature): degrees Celsius (°C)
  - Input `HR` (Relative humidity): percent (%)
  - Output Temperature: degrees Celsius (°C)

.. math::

    T_{w} = \ldots  - 4.686035

HA(Pvs, HR, P) - Absolute Humidity
----------------------------------

Calculates the absolute humidity using the saturation vapor pressure, relative humidity, and atmospheric pressure.

- Units:
  - Input `Pvs`: Function to calculate saturation vapor pressure
  - Input `HR`: Relative humidity in percent (%)
  - Input `P`: Atmospheric pressure in Pascals (Pa)
  - Output Humidity: grams per cubic meter (g/m³)

.. math::

    HA = 0.62198 \cdot \frac{P_{v}}{P - P_{v}} \cdot 1000

Enthalpie(T, HA) - Enthalpy of Moist Air
-----------------------------------------

Calculates the enthalpy of moist air, taking into account both sensible and latent heat.

- Units:
  - Input `T`: Temperature in degrees Celsius (°C)
  - Input `HA`: Absolute humidity in grams per kilogram (g/kg)
  - Output Enthalpy: kilojoules per kilogram (kJ/kg)

.. math::

    Enthalpie = 1.006 \cdot T + \left(\frac{HA}{1000}\right) \cdot (2501 + 1.0805 \cdot T)

rho_ah(T, HR, P) - Density of Humid Air
---------------------------------------

Calculates the density of humid air based on temperature, relative humidity, and atmospheric pressure.

- Units:
  - Input `T`: Temperature in degrees Celsius (°C)
  - Input `HR`: Relative humidity in percent (%)
  - Input `P`: Atmospheric pressure in Pascals (Pa)
  - Output Density: kilograms per cubic meter (kg/m³)

.. math::

    \rho_{ah} = \frac{(rho_a \cdot R_a + rho_v \cdot R_v)}{R_{ah}}

Usage Examples
==============

.. code-block:: python

    # Example of using Pvs function
    saturation_pressure = Pvs(25)
    print(f"Saturation Vapor Pressure at 25°C: {saturation_pressure} Pa")

... (Include detailed examples for each function, demonstrating how to call the function and interpret its output) ...

Notes
=====

- The functions are based on standard thermodynamic formulas and ideal gas approximations.
- These are commonly used in meteorology, HVAC systems, and other related fields.
- It is important to note that the accuracy of these calculations is dependent on the empirical correlations and constants used.

References
==========

- "Wet-Bulb Temperature from Relative Humidity and Air Temperature" by Roland Stull, University of British Columbia, Vancouver, British Columbia, Canada.

... (Additional references as applicable) ...
