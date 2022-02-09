import random
import sys
sys.setrecursionlimit(8000)


#sorter class
class sorter:
	#constructor
	def __init__(self):
		self.bubble_cmp = self.select_cmp = self.insert_cmp = self.quick_cmp = self.merge_cmp = 0
		self.size = 0
		self.list0 = []
		self.list1 = []
		self.list2 = []
		self.list3 = []
		self.list4 = []
		self.list5 = []
		
	#initialize elements for random arrays
	def init_list(self):
		self.size = 100
		i = 0
		while(i < self.size):
			self.list0.append(random.randint(0, 100))
			self.list1.append(self.list0[i])
			self.list2.append(self.list0[i])
			self.list3.append(self.list0[i])
			self.list4.append(self.list0[i])
			self.list5.append(self.list0[i])
			i += 1
		
	#print lists
	def print_list(self, mlist):
		i = 0
		if(mlist == 0):
			print("Unsorted List:")
			while(i < self.size):
				print(str(self.list0[i]) + " ", end=" ")
				i += 1
				if((i + 1) % 21 == 0):
					print("")
			print("")
			print("")
		elif(mlist == 1):
			print("Bubble Sort:")
			while(i < self.size):
				print(str(self.list1[i]) + " ", end=" ")
				i += 1
				if((i + 1) % 21 == 0):
					print("")
			print("")
			print("")
		elif(mlist == 2):
			print("Insertion Sort:")
			while(i < self.size):
				print(str(self.list2[i]) + " ", end=" ")
				i += 1
				if((i + 1) % 21 == 0):
					print("")
			print("")
			print("")
		elif(mlist == 3):
			print("Selection Sort:")
			while(i < self.size):
				print(str(self.list3[i]) + " ", end=" ")
				i += 1
				if((i + 1) % 21 == 0):
					print("")
			print("")
			print("")
		elif(mlist == 4):
			print("Quick Sort:")
			while(i < self.size):
				print(str(self.list4[i]) + " ", end=" ")
				i += 1
				if((i + 1) % 21 == 0):
					print("")
			print("")
			print("")
		elif(mlist == 5):
			print("Merge Sort:")
			while(i < self.size):
				print(str(self.list5[i]) + " ", end=" ")
				i += 1
				if((i + 1) % 21 == 0):
					print("")
			print("")
			print("")
		else:
			print("Incorrect print choice. Choose 0, 1, 2, 3, 4, or 5")

	# bubble sort algorithm
	def bubble_sort(self):
		i = 0
		is_sorted = False
		while(i < self.size and not is_sorted):
			is_sorted = True
			j = self.size - 1
			while(j > i):
				if(self.list1[j] < self.list1[j - 1]):
					self.list1[j], self.list1[j - 1] = self.list1[j - 1], self.list1[j]
					is_sorted = False
				self.bubble_cmp += 1
				j -= 1
			i += 1

	#insertion sort algorithm
	def insertion_sort(self):
		first_unsorted = 1
		i = first_unsorted
		while(i < self.size):
			j = i
			while(j > 0):
				if(self.list2[j] < self.list2[j - 1]):
					self.list2[j], self.list2[j - 1] = self.list2[j - 1], self.list2[j]
				self.insert_cmp += 1
				j -= 1
			i += 1

	#selection sort algorithm
	def selection_sort(self):
		i = 0
		while(i < self.size):
			min_index = i
			j = i
			while(j < self.size):
				if(self.list3[min_index] > self.list3[j]):
					min_index = j
				self.select_cmp += 1
				j += 1
			self.list3[i], self.list3[min_index] = self.list3[min_index], self.list3[i]
			i += 1

	#partitioning function used in quick sort
	def partition(self, first, last):
		pivot = self.list4[first]
		last1 = first
		first_unknown = first + 1
		while(first_unknown <= last):
			if(self.list4[first_unknown] < pivot):
				last1 += 1
				self.list4[first_unknown], self.list4[last1] = self.list4[last1], self.list4[first_unknown]
			else:
				self.quick_cmp += 1
			first_unknown += 1
		self.list4[first], self.list4[last1] = self.list4[last1], self.list4[first]
		return last1	

	#quick sort algorithm
	def quick_sort(self, first, last):
		if(first <= last):
			pivot_index = self.partition(first, last)
			self.quick_sort(first, pivot_index - 1)
			self.quick_sort(pivot_index + 1, last)

	#function used to merge merge-sort list back together
	def merge(self, first, last):
		i = 0
		
	#merge sort algorithm
	def merge_sort(self, arr):
		if(len(arr) > 1):
			mid = len(arr) // 2
			left = arr[:mid]
			right = arr[mid:]

			self.merge_sort(left)
			self.merge_sort(right)

			i = j = k = 0

			while(i < len(left) and j < len(right)):
				if(left[i] < right[j]):
					arr[k] = left[i]
					i += 1
				else:
					arr[k] = right[j]
					j += 1
				k += 1
				self.merge_cmp += 1

			while(i < len(left)):
				arr[k] = left[i]
				i += 1
				k += 1
				self.merge_cmp += 1

			while(j < len(right)):
				arr[k] = right[j]
				j += 1
				k += 1
				self.merge_cmp += 1

	#print comparisons
	def print_cmp(self):
		print("SORTING COMPARISON RESULTS:")
		print()
		print("Algorithms\t" + "Comparisons")
		print("Bubble\t\t" + str(self.bubble_cmp))
		print("Insert\t\t" + str(self.insert_cmp))
		print("Select\t\t" + str(self.select_cmp))
		print("Quick\t\t" + str(self.quick_cmp))
		print("Merge\t\t" + str(self.merge_cmp))





