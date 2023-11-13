.. _titre_section:

2. Centrale de traitement d'air
==================================================================

Ce document fournit une explication détaillée des fonctions Python pour divers calculs d'air humide.

Nomenclature des Variables
--------------------------

+----------+-------------------------------------+----------------+
| Variable | Description                         | Unité          |
+==========+=====================================+================+
| T        | Température                         | °C             |
+----------+-------------------------------------+----------------+
| Tk       | Température en Kelvin               | K              |
+----------+-------------------------------------+----------------+
| Pvs      | Pression de vapeur saturée          | Pascal         |
+----------+-------------------------------------+----------------+
| Td       | Température de rosée                | °C             |
+----------+-------------------------------------+----------------+
| HR       | Humidité relative                   | %              |
+----------+-------------------------------------+----------------+
| HA       | Humidité absolue                    | g/kg d'air sec |
+----------+-------------------------------------+----------------+
| Pv       | Pression partielle de vapeur d'eau  | Pascal         |
+----------+-------------------------------------+----------------+
| P        | Pression atmosphérique              | Pascal         |
+----------+-------------------------------------+----------------+
| rho_ah   | Densité de l'air humide             | kg/m³          |
+----------+-------------------------------------+----------------+
+----------+-------------------------------------+----------------+
| P_drop   | Perte de pression                   | Pascal         |
+----------+-------------------------------------+----------------+
| h_in     | Enthalpie à l'entrée                | kJ/kg          |
+----------+-------------------------------------+----------------+
| HA_in    | Humidité absolue à l'entrée         | g/kg d'air sec |
+----------+-------------------------------------+----------------+
| F_kgs    | Débit massique d'air                | kg/s           |
+----------+-------------------------------------+----------------+
| m_as     | Débit massique d'air sec            | kg/s           |
+----------+-------------------------------------+----------------+
| T_out_target | Température cible de sortie     | °C             |
+----------+-------------------------------------+----------------+
| h_out    | Enthalpie à la sortie               | kJ/kg          |
+----------+-------------------------------------+----------------+
| Qth      | Charge thermique                    | kW             |
+----------+-------------------------------------+----------------+
| HR_out   | Humidité relative à la sortie       | %              |
+----------+-------------------------------------+----------------+

2.1. Fonctions de calcul d'air humide
-------------------------------------


2.1.1. Pvs(T)
-------------

.. function:: Pvs(T)

   Calcule la pression de vapeur saturée à une température donnée.

   :param T: Température en degrés Celsius.
   :type T: float
   :returns: Pression de vapeur saturée en Pascal.
   :rtype: float

   **Coefficients utilisés**:

   +------+-----------------+------+-----------------+------+------------------+
   | C1   | -5.6745359e3    | C2   | 6.3925247       | C3   | -9.677843e-3     |
   +------+-----------------+------+-----------------+------+------------------+
   | C4   | 6.2215701e-7    | C5   | 2.0747825e-9    | C6   | -9.484024e-13    |
   +------+-----------------+------+-----------------+------+------------------+
   | C7   | 4.1635019       | C8   | -5.8002206e3    | C9   | 1.3914993        |
   +------+-----------------+------+-----------------+------+------------------+
   | C10  | -4.8640239e-2   | C11  | 4.1764768e-5    | C12  | -1.4452093e-8    |
   +------+-----------------+------+-----------------+------+------------------+
   | C13  | 6.5459673       |      |                 |      |                  |
   +------+-----------------+------+-----------------+------+------------------+

   **Équation utilisée**:

   Pour T < 0 °C (valable entre -100 et 0 °C) :

   .. math::

      Pvs = e^{(C1 / Tk + C2 + C3 \cdot Tk + C4 \cdot Tk^2 + 
               C5 \cdot Tk^3 + C6 \cdot Tk^4 + C7 \cdot \ln(Tk))}

   Pour T >= 0 °C (valable entre 0 et 200 °C) :

   .. math::

      Pvs = e^{(C8 / Tk + C9 + C10 \cdot Tk + C11 \cdot Tk^2 + 
               C12 \cdot Tk^3 + C13 \cdot \ln(Tk))}

   Où `Tk = T + 273.15` est la température en Kelvin.


Tw(Td, HR)
----------

.. function:: Tw(Td, HR)

   Calcule la température du bulbe humide.

   :param Td: Température de rosée en degrés Celsius.
   :param HR: Humidité relative en pourcentage.
   :type Td: float
   :type HR: float
   :returns: Température du bulbe humide en degrés Celsius.
   :rtype: float

   **Équation utilisée**:

   .. math::

      Tw = Td \cdot \atan(0.151977 \cdot (HR + 8.313659)^{1/2}) + 
           \atan(Td + HR) - \atan(HR - 1.676331) + 
           0.00391838 \cdot HR^{3/2} \cdot \atan(0.023101 \cdot HR) - 
           4.686035

   Cette formule est basée sur l'étude de Roland Stull de l'Université de Colombie-Britannique.


HA(Pvs, HR, P)
--------------

.. function:: HA(Pvs, HR, P)

   Calcule l'humidité absolue.

   :param Pvs: Pression de vapeur saturée en Pascal.
   :param HR: Humidité relative en pourcentage.
   :param P: Pression atmosphérique en Pascal.
   :type Pvs: float
   :type HR: float
   :type P: float
   :returns: Humidité absolue en g/kg d'air sec.
   :rtype: float

   **Équation utilisée**:

   .. math::

      Pv = Pvs \cdot \frac{HR}{100}

   .. math::

      HA = 0.62198 \cdot \frac{Pv}{P - Pv} \cdot 1000

HR(Pvs, HA, P)
--------------

.. function:: HR(Pvs, HA, P)

   Calcule l'humidité relative.

   :param Pvs: Pression de vapeur saturée en Pascal.
   :param HA: Humidité absolue.
   :param P: Pression atmosphérique en Pascal.
   :type Pvs: float
   :type HA: float
   :type P: float
   :returns: Humidité relative en pourcentage.
   :rtype: float

   **Équation utilisée**:

   .. math::

      Pv = P \cdot \frac{HA}{1000} / \left(\frac{HA}{1000} + 0.62198\right)

   .. math::

      HR = \frac{Pv}{Pvs} \cdot 100

T_sat(HA_target)
----------------

.. function:: T_sat(HA_target)

   Calcule la température de saturation.

   :param HA_target: Humidité absolue cible.
   :type HA_target: float
   :returns: Température de saturation en degrés Celsius.
   :rtype: float

   **Équation utilisée**:

   .. math::

      T = -100
   .. math::
      \text{Erreur} = HA(Pvs(T), 100) - HA_target
   .. math::
      \text{Tant que Erreur} \leq 0 :
   .. math::
         T = T + 0.02
   .. math::
         \text{Erreur} = HA(Pvs(T), 100) - HA_target
   .. math::
      T\_sat = T

T_Humidifier(HA_target, HA_init, Tinit)
---------------------------------------

.. function:: T_Humidifier(HA_target, HA_init, Tinit)

   Calcule la température pour un humidificateur.

   :param HA_target: Humidité absolue cible.
   :param HA_init: Humidité absolue initiale.
   :param Tinit: Température initiale en degrés Celsius.
   :type HA_target: float
   :type HA_init: float
   :type Tinit: float
   :returns: Température pour l'humidificateur en degrés Celsius.
   :rtype: float

   **Équation utilisée**:

   .. math::

      T = -100

   .. math::

      \text{Erreur} = -\text{Enthalpie}(Tinit, HA_init) + \text{Enthalpie}(T, HA_target)

   .. math::

      \text{Tant que Erreur} < 0 :
         T = T + 0.01
   .. math::

         \text{Erreur} = -\text{Enthalpie}(Tinit, HA_init) + \text{Enthalpie}(T, HA_target)
      T\_Humidifier = T - 0.01

T_rosee(Pv)
------------

.. function:: T_rosee(Pv)

   Calcule la température de rosée.

   :param Pv: Pression partielle de vapeur d'eau.
   :type Pv: float
   :returns: Température de rosée en degrés Celsius.
   :rtype: float

   **Équation utilisée**:

   .. math::

      T = -100
      \text{Erreur} = -Pv + Pvs(T)
   .. math::

      \text{Tant que Erreur} < 0 :
         T = T + 0.01
   .. math::

         \text{Erreur} = -Pv + Pvs(T)
      T\_rosee = T - 0.01

Enthalpie(T, HA)
-----------------

.. function:: Enthalpie(T, HA)

   Calcule l'enthalpie spécifique de l'air humide.

   :param T: Température en degrés Celsius.
   :param HA: Humidité absolue.
   :type T: float
   :type HA: float
   :returns: Enthalpie spécifique en kJ/kg d'air sec.
   :rtype: float

   **Équation utilisée**:

   .. math::

      Enthalpie = 1.006 \cdot T + \frac{HA}{1000} \cdot (2501 + 1.0805 \cdot T)

Temperature(Enthalpie, HA)
--------------------------

.. function:: Temperature(Enthalpie, HA)

   Calcule la température à partir de l'enthalpie et de l'humidité absolue.

   :param Enthalpie: Enthalpie spécifique.
   :param HA: Humidité absolue.
   :type Enthalpie: float
   :type HA: float
   :returns: Température en degrés Celsius.
   :rtype: float

   **Équation utilisée**:

   .. math::

      T = \frac{Enthalpie - \frac{HA}{1000} \cdot 2501}{1.006 + \frac{HA}{1000} \cdot 1.0805}

rho_ah(T, HR, P)
----------------

.. function:: rho_ah(T, HR, P)

   Calcule la densité de l'air humide.

   :param T: Température en degrés Celsius.
   :param HR: Humidité relative en pourcentage.
   :param P: Pression atmosphérique en Pascal.
   :type T: float
   :type HR: float
   :type P: float
   :returns: Densité de l'air humide en kg/m³.
   :rtype: float

   **Équation utilisée**:

   .. math::

      Tk = T + 273.15
      Psat = Pvs(T)

   .. math::
      Pv = Psat \cdot \frac{HR}{100}
   .. math::
      \rho_v = \frac{Pv}{Rv \cdot Tk}
   .. math::
      \rho_a = \frac{P - Pv}{Ra \cdot Tk}
   .. math::
      Rah = \frac{Ra}{1 - \left(\frac{HR}{100} \cdot \frac{Psat}{P}\right) 
                  \cdot \left(1 - \frac{Ra}{Rv}\right)}
      \rho_ah = \frac{\rho_a \cdot Ra + \rho_v \cdot Rv}{Rah}


2.2. Batterie chaude
-------------------------------------
