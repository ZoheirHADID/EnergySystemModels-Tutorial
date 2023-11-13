.. _titre_section:

Description des Fonctions de Calcul Thermodynamique avec Équations
==================================================================

Ce document fournit une explication détaillée des fonctions Python pour divers calculs thermodynamiques, en mettant l'accent sur les équations et corrélations utilisées.

from math import *
-------------------

Pvs(T)
-------

.. function:: Pvs(T)

   Calcule la pression de vapeur saturée à une température donnée.

   :param T: Température en degrés Celsius.
   :type T: float
   :returns: Pression de vapeur saturée en Pascal.
   :rtype: float

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

   Basée sur l'étude de Roland Stull de l'Université de Colombie-Britannique.

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
      HA = 0.62198 \cdot \frac{Pv}{P - Pv} \cdot 1000

   Calcul de l'humidité absolue en utilisant la pression de vapeur et la pression atmosphérique.

... (autres fonctions) ...

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
      Pv = Psat \cdot \frac{HR}{100}
      \rho_v = \frac{Pv}{Rv \cdot Tk}
      \rho_a = \frac{P - Pv}{Ra \cdot Tk}
      Rah = \frac{Ra}{1 - \left(\frac{HR}{100} \cdot \frac{Psat}{P}\right) 
                  \cdot \left(1 - \frac{Ra}{Rv}\right)}
      \rho_ah = \frac{\rho_a \cdot Ra + \rho_v \cdot Rv}{Rah}

   Cette formule calcule la densité de l'air humide en prenant en compte la température, l'humidité relative et la pression atmosphérique.
