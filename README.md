Программа реализует алгоритм сортировки пузырьком для списка случайных чисел.

Алгоритм сортировки пузырьком работает путем сравнения пар последовательных элементов и их перестановки в случае несоблюдения порядка. В этом коде происходит следующее:

1. Создается список `a` из 10 случайных чисел в диапазоне от 1 до 99 с помощью функции `randint` из модуля `random`.

2. Вычисляется длина списка `a` и сохраняется в переменной `b`.

3. Происходит сортировка списка методом сортировки пузырьком с использованием двойного цикла. Внешний цикл контролирует количество проходов по списку, внутренний производит
 сравнение и перестановку соседних элементов, если это необходимо.

5. После каждой перестановки производится вывод текущего состояния списка.

6. Если на каком-то проходе по списку не произошло ни одной перестановки элементов, значит список уже отсортирован по возрастанию, и процесс сортировки завершается.

Таким образом, данный код демонстрирует работу алгоритма сортировки пузырьком и выводит промежуточные состояния списка на каждой итерации в процессе сортировки.
