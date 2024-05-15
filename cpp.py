import cppyy
import time


cppyy.cppdef("""
class my_vector {
public:
    my_vector(int n) {
		int start = -10000, end = 10000;
		for(int i = 0; i < n; i++)
			arr.push_back((rand() % (end - start + 1) + start));
    }
    std::vector<int> arr;

	int sum() {
		int suum = 0;
		for (int i = 0; i < arr.size(); i++)
		{
			suum += arr[i];
		}
		return suum;
	}
	int max() {
		int maximum = arr[0];
		for (int i = 0; i < arr.size(); i++)
		{
			if (arr[i] > maximum)
			{
				maximum = arr[i];
			}

		}
		return maximum;
	}
	int min() {
		int minimum = arr[0];
		for (int i = 0; i < arr.size(); i++)
		{
			if (arr[i] < minimum)
			{
				minimum = arr[i];
			}

		}
		return minimum;
	}

	void bubbleSort() {
		int n = arr.size();
		std::cout << "bubble" << std::endl;;
		for (int i = 0; i < n - 1; i++) {
			for (int j = 0; j < n - i - 1; j++) {
				if (arr[j] > arr[j + 1]) {
					std::swap(arr[j], arr[j + 1]);
				}
			}
		}
	}
	void selectionSort() {
		int n = arr.size();
		std::cout << "selection" << std::endl;
		for (int i = 0; i < n - 1; i++) {
			int minIndex = i;
			for (int j = i + 1; j < n; j++) {
				if (arr[j] < arr[minIndex]) {
					minIndex = j;
				}
			}
			std::swap(arr[minIndex], arr[i]);
		}
	}
	void shellSort() {
		int n = arr.size();
		std::cout << "shell" << std::endl;
		for (int gap = n / 2; gap > 0; gap /= 2) {
			for (int i = gap; i < n; i += 1) {
				int temp = arr[i];
				int j;
				for (j = i; j >= gap && arr[j - gap] > temp; j -= gap) {
					arr[j] = arr[j - gap];
				}
				arr[j] = temp;
			}
		}
	}
	void heapify(int n, int i) {
		int largest = i;
		int l = 2 * i + 1;
		int r = 2 * i + 2;

		if (l < n && arr[l] > arr[largest])
			largest = l;

		if (r < n && arr[r] > arr[largest])
			largest = r;

		if (largest != i) {
			std::swap(arr[i], arr[largest]);
			heapify(n, largest);
		}
	}

	void heapSort() {
		int n = arr.size();
		std::cout << "heap" << std::endl;
		for (int i = n / 2 - 1; i >= 0; i--)
			heapify(n, i);

		for (int i = n - 1; i >= 0; i--) {
			std::swap(arr[0], arr[i]);
			heapify(i, 0);
		}
	}
	void merge(int left, int mid, int right) {
		int n1 = mid - left + 1;
		int n2 = right - mid;

		std::vector<int> L(n1), R(n2);

		for (int i = 0; i < n1; i++) {
			L[i] = arr[left + i];
		}
		for (int j = 0; j < n2; j++) {
			R[j] = arr[mid + 1 + j];
		}

		int i = 0, j = 0, k = left;

		while (i < n1 && j < n2) {
			if (L[i] <= R[j]) {
				arr[k] = L[i];
				i++;
			}
			else {
				arr[k] = R[j];
				j++;
			}
			k++;
		}

		while (i < n1) {
			arr[k] = L[i];
			i++;
			k++;
		}

		while (j < n2) {
			arr[k] = R[j];
			j++;
			k++;
		}
	}

	void mergeSort(int left, int right) {
		if (left < right) {
			int mid = left + (right - left) / 2;
			mergeSort(left, mid);
			mergeSort(mid + 1, right);
			merge(left, mid, right);
		}
	}

	void mergeSort() {
		mergeSort(0, arr.size() - 1);
	}

	void quickSort(int low, int high) {
		if (low < high) {
			int pivotIndex = low;
			int i = low;
			int j = high;

			while (i <= j) {
				while (arr[i] <= arr[pivotIndex]) {
					i++;
				}

				while (arr[j] > arr[pivotIndex]) {
					j--;
				}

				if (i <= j) {
					std::swap(arr[i], arr[j]);
				}
			}

			std::swap(arr[pivotIndex], arr[j]);

			quickSort(low, j - 1);
			quickSort(j + 1, high);
		}
	}

	void quickSort() {
		quickSort(0, arr.size() - 1);
	}

	int binarySearch(int left, int right, int target) {
		if (right >= left) {
			int mid = left + (right - left) / 2;

			if (arr[mid] == target) {
				return mid;
			}

			if (arr[mid] > target) {
				return binarySearch(left, mid - 1, target);
			}

			return binarySearch(mid + 1, right, target);
		}

		return -1;
	}

	int binarySearch(int target) {
		return binarySearch(0, arr.size() - 1, target);
	}
	int interpolationSearch(int left, int right, int target) {
		if (left <= right && target >= arr[left] && target <= arr[right]) {
			int pos = left + (static_cast<double>(right - left) / (arr[right] - arr[left])) * (target - arr[left]);

			if (arr[pos] == target) {
				return pos;
			}

			if (arr[pos] < target) {
				return interpolationSearch(pos + 1, right, target);
			}

			return interpolationSearch(left, pos - 1, target);
		}

		return -1;
	}

	int interpolationSearch(int target) {
		return interpolationSearch(0, arr.size() - 1, target);
	}
};""")

from cppyy.gbl import my_vector
vect = my_vector(10000000)
start_time_sum = time.time()
vect.sum()
end_time_sum = time.time()
start_time_max = time.time()
vect.max()
end_time_max = time.time()
start_time_min = time.time()
vect.min()
end_time_min = time.time()
start_time_sort = time.time()
#vect.bubbleSort()
#vect.selectionSort()
#vect.shellSort()
vect.heapSort()
#vect.mergeSort()
#vect.quickSort()
end_time_sort = time.time()
#print(vect.arr)
target = 45;
start_time_bin = time.time()
result = vect.binarySearch(target)
end_time_bin = time.time()
if(result != -1):
    print("Item found, its number = ", result)
else:
    print("Item not found")
start_time_inter = time.time()
result = vect.interpolationSearch(target);
end_time_inter = time.time()
if(result != -1):
    print("Item found, its number = ", result)
else:
    print("Item not found")


print(f"Время для суммы = {end_time_sum-start_time_sum},\nВремя для максимума = {end_time_max - start_time_max},\nВремя для минимума = {end_time_min - start_time_min},\n"
      f"Время для сортировки = {end_time_sort - start_time_sort},\nВремя для бинарного поиска = {end_time_bin - start_time_bin},\nВремя для интерполяционного поиска = {end_time_inter - start_time_inter}.")


"""
N = 1000000
Item found, its number =  5021360
Item found, its number =  5021498
Время для суммы = 0.02482771873474121,
Время для максимума = 0.017409324645996094,
Время для минимума = 0.01685166358947754,
Время для сортировки = 3.8947665691375732,
Время для бинарного поиска = 0.015524625778198242,
Время для интерполяционного поиска = 0.01667189598083496.
"""