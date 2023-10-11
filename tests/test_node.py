import sys
sys.path.append('../src')

import unittest
from node import Node  # Asegúrate de importar la clase Node desde el archivo node.py (o el nombre del archivo donde se encuentra la clase Node)

class TestNode(unittest.TestCase):
    def setUp(self):
        # Crea instancias de la clase Node para usar en las pruebas
        self.node1 = Node(1, firstpos=[1], lastpos=[1], nullable=True, value='a')
        self.node2 = Node(2, firstpos=[2], lastpos=[2], nullable=False, value='b')
        # Agrega más nodos para probar casos adicionales

    def test_node_attributes(self):
        # Verifica los atributos de los nodos
        self.assertEqual(self.node1._id, 1)
        self.assertEqual(self.node1.firstpos, [1])
        self.assertEqual(self.node1.lastpos, [1])
        self.assertTrue(self.node1.nullable)
        self.assertEqual(self.node1.value, 'a')
        self.assertEqual(self.node1.c1, None)
        self.assertEqual(self.node1.c2, None)

        self.assertEqual(self.node2._id, 2)
        self.assertEqual(self.node2.firstpos, [2])
        self.assertEqual(self.node2.lastpos, [2])
        self.assertFalse(self.node2.nullable)
        self.assertEqual(self.node2.value, 'b')
        self.assertEqual(self.node2.c1, None)
        self.assertEqual(self.node2.c2, None)

    def test_node_representation(self):
        # Verifica el método __repr__ para asegurar que devuelve una cadena esperada
        expected_repr1 = (
        '\n    id: {}\n    value: {}\n    firstpos: {}\n    lastpos: {}\n    followpos: {}\n    nullabe: {}\n    '
        .format(1, 'a', [1], [1], [], True)
        )
        expected_repr2 = (
        '\n    id: {}\n    value: {}\n    firstpos: {}\n    lastpos: {}\n    followpos: {}\n    nullabe: {}\n    '
        .format(2, 'b', [2], [2], [], False)
        )
    
        self.assertEqual(repr(self.node1), expected_repr1)
        self.assertEqual(repr(self.node2), expected_repr2)

if __name__ == '__main__':
    unittest.main()
