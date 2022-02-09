from sorter import sorter
import sys
sys.setrecursionlimit(8000)

mysort = sorter()


mysort.init_list()
mysort.print_list(0)

mysort.bubble_sort()
mysort.print_list(1)

mysort.insertion_sort()
mysort.print_list(2)

mysort.selection_sort()
mysort.print_list(3)

mysort.quick_sort(0, 99)
mysort.print_list(4)

mysort.merge_sort(mysort.list5)
mysort.print_list(5)

mysort.print_cmp()

	






