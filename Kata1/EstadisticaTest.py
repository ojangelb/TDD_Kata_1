from unittest import TestCase

import Estadistica


class EstadisticaTest(TestCase):
    def test_calculo_estadistica(self):
        self.assertEqual(Estadistica.calculoEstadistica(""), 0, "Vacio")
