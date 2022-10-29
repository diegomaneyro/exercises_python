import unittest
import sys
sys.path.append(r'/C:/Henry/ejercicios/clases_objetos/herramientas.py')
from ejercicios.clases_objetos.herramientas import Herramientas as H

class Test_Caja_Negra(unittest.TestCase):
    def test_Herramienta_caja_negra_1(self):#busca falla
        arg = "a"
        h1 = H(arg)
        self.assertRaises(TypeError, h1, arg)
    def test_Herramientas_caja_negra_2(self):#busca ok, prueba de integracion
        arg = [1,2,5,4,5,6,8,4,4,2]
        h2 = H(arg)
        self.assertEqual(h2.lista,arg)
        """instancia clase herramientas se pasa una lista y luego se compara pidiendo ese valor desde la clase
        """
    def test_valor_modal_caja_negra_3(self):#busca ok. prueba unitaria
        lista = [1,5,2,5,1,2,5,1,2,5]
        h1 = H(lista)
        resultado = (5,4)
        self.assertEqual(h1.valor_modal(False),resultado)

    def test_valor_modal_caja_negra_4(self):#busca ok
        lista = [1,2,1,2,1]
        h1 = H(lista)
        moda, repite = h1.valor_modal(False)
        moda = [moda]
        moda.append(repite)
        resultado = [1, 3]
        self.assertEqual(moda, resultado)

    def test_valor_modal_caja_negra_5(self):#busca  fallar tipo dato entrada
        lista = []
        h5 = H(lista)
        moda, repite = h5.valor_modal(True)
        moda = [moda]
        moda.append(repite)
        resultado = [1,3]
        self.assertEqual(moda,resultado)

    def test_verifica_primo_6(self):
        lista = [2,3,8,10,13]
        h = H(lista)
        lista_primo = h.verifica_primo(lista)
        lista_esperada = [True,True,False,False,True]
        self.assertEqual(lista_primo,lista_esperada)





unittest.main(argv=[''], verbosity=2, exit=False)
