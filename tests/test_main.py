from unittest import TestCase
import turtle_hare, quadratic_equation, secretary

class TestMain(TestCase):

    def test_turtle_hare(self):
        hare_distances = [8, 5, 3, 2, 0, 1, 1]
        turtle_distances = [3, 3, 3, 3, 3, 3, 3]
        expected = "черепаха"
        result = turtle_hare.solve(hare_distances, turtle_distances)
        self.assertEqual(expected, result)

    def test_discriminant_all_ints(self):
        for i, (a, b, c, expected) in enumerate([
            (3, 4, 5, -44),
            (5, -7, -5, 149),
            (0, 2, 0, 4)
        ]):
            with self.subTest(i):
                self.assertEqual(expected, quadratic_equation.discriminant(a, b, c))

    def test_discriminant_with_string(self):
        a, b, c = 3, 5, '6'
        self.assertRaises(TypeError, quadratic_equation.discriminant, a, b, c)

    def test_quadratic_eduation(self):
        a, b, c = 1, 8, 15
        expected = (-3.0, -5.0)
        result = quadratic_equation.solution(a, b, c)
        self.assertEqual(expected, result)
        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], float)

    def test_quadratic_no_solution(self):
        tests = [(5,2,5),
                 (4,2,3),
                 (6,7,7)]
        for test in tests:
            result = quadratic_equation.solution(*test)
            self.assertEqual('корней нет', result)

    def test_secretary_exists(self):
        doc_number = '10006'
        expected = 'Аристарх Павлов'
        result = secretary.get_name(doc_number)
        self.assertEqual(expected, result)

    def test_secretary_add_document(self):
        document_type, number, name, shelf_number = ('international passport',
                                                     '311 020203',
                                                     'Александр Пушкин',
                                                     3)

        expected = 'Александр Пушкин'
        secretary.add(document_type, number, name, shelf_number)
        result = secretary.documents[-1]['name']
        self.assertEqual(expected, result)

    def test_secretary_find_doc(self):
        doc_number = '10006'
        result = secretary.get_directory(doc_number)
        self.assertIsInstance(result, int)
        self.assertEqual(result, 2)

