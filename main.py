import types

'''
Задание 1
Доработать класс FlatIterator в коде ниже.
Должен получиться итератор, который принимает список списков и возвращает их плоское представление,
т. е. последовательность, состоящую из вложенных элементов.
'''


class FlatIterator:

    def __init__(self, new_list):
        self.new_list = [object for item in new_list for object in item]

    def __iter__(self):
        self.count = -1
        return self

    def __next__(self):
        self.count += 1
        if self.count == len(self.new_list):
            raise StopIteration
        return self.new_list[self.count]


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    print("Начало первой проверки")
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print("Конец первой проверки")


'''
Задание 2
Доработать функцию flat_generator.
Должен получиться генератор, который принимает список списков и возвращает их плоское представление.
'''


def flat_generator(list_of_lists):
    for item in list_of_lists:
        for elem in item:
            yield elem


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    print("Начало второй проверки")
    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print("Конец второй проверки")


'''
Задание 4
Написать генератор, аналогичный генератору из задания 2,
но обрабатывающий списки с любым уровнем вложенности..
'''


def flat_generator_second(list_of_list):
    for item in list_of_list:
        if isinstance(item, list):
            for j in flat_generator_second(item):
                yield j
        else:
            yield item


def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]
    print("Начало четвёртой проверки")
    for flat_iterator_item, check_item in zip(
            flat_generator_second(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator_second(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator_second(list_of_lists_2), types.GeneratorType)
    print("Конец четвёртой проверки")


if __name__ == '__main__':
    test_1()
    test_2()
    test_4()
