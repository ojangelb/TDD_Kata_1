from unittest import TestCase

from Estadistica import Estadistica


class EstadisticaTest(TestCase):
    def test_calculo_estadistica(self):
        self.assertEqual(Estadistica.calculoEstadistica(""), 0, "Vacio")
        
    def test_calculo_estadistica_un_numero(self):
        self.assertEqual(Estadistica.calculoEstadistica("1"), 1, "Un número")
