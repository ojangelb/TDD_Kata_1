from unittest import TestCase

from Estadistica import Estadistica


class EstadisticaTest(TestCase):
    def test_calculo_estadistica(self):
        self.assertEqual(Estadistica.calculoEstadistica(Estadistica, ""), 0, "Vacio")

    def test_calculo_estadistica_un_numero(self):
        array = [1, 1, 1, 1]
        self.assertEqual(Estadistica.calculoEstadistica(Estadistica, "1"), array, "Un número")

    def test_calculo_estadistica_dos_numeros(self):
        array = [2, 1, 2, 1.5]
        self.assertEqual(Estadistica.calculoEstadistica(Estadistica, "1,2"), array, "Dos números")

    def test_calculo_estadistica_n_numeros(self):
        array = [5, 1, 5, 3]
        self.assertEqual(Estadistica.calculoEstadistica(Estadistica, "1,2,4,3,5"), array, "N números")
