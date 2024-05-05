

#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int sum(vector<int>& basearr);
int max(vector<int>& basearr);
int min(vector<int>& basearr);
void bubbleSort(vector<int>& arr);
void selectionSort(vector<int>& arr);
void shellSort(vector<int>& arr);
void heapSort(vector<int>& arr);
void mergeSort(vector<int>& arr);
void quickSort(vector<int>& arr);
int binarySearch(const vector<int>& arr, int target);
int interpolationSearch(const vector<int>& arr, int target);


int main()
{
	vector<int> arr = { 64, 34, 25, 12, -50, 22, 11, 90, -5};
	//bubbleSort(arr);
	//selectionSort(arr);
	//shellSort(arr);
	//heapSort(arr);
	mergeSort(arr);
	//quickSort(arr);
	for (int i : arr) {
		cout << i << " ";
	}
	

	cout << "\n" << "";
	cout << sum(arr) << "\n";
	cout << max(arr) << "\n";
	cout << min(arr) << "\n";

	int target = 90;

	int result = binarySearch(arr, target);
	//int result = interpolationSearch(arr, target);

	if (result != -1) {
		cout << "Item found, its number = " << result << endl;
	}
	else {
		cout << "Item not found" << endl;
	}



}
int sum(vector<int>& basearr)
{
	int suum = 0;
	;
	for (int i = 0; i < basearr.size(); i++)
	{
		suum += basearr[i];
	}
	return suum;
}
int max(vector<int>& basearr)
{
	int maximum = basearr[0];
	;
	for (int i = 0; i < basearr.size(); i++)
	{
		if (basearr[i] > maximum)
		{
			maximum = basearr[i];
		}

	}
	return maximum;
}
int min(vector<int>& basearr)
{
	int minimum = basearr[0];
	;
	for (int i = 0; i < basearr.size(); i++)
	{
		if (basearr[i] < minimum)
		{
			minimum = basearr[i];
		}

	}
	return minimum;
}

void bubbleSort(vector<int>& arr) {
	int n = arr.size();
	cout << "bubble" << "\n";
	for (int i = 0; i < n - 1; i++) {
		for (int j = 0; j < n - i - 1; j++) {
			if (arr[j] > arr[j + 1]) {
				swap(arr[j], arr[j + 1]);
			}
		}
	}
}
void selectionSort(vector<int>& arr) {
	int n = arr.size();
	cout << "selection" << "\n";
	for (int i = 0; i < n - 1; i++) {
		int minIndex = i;
		for (int j = i + 1; j < n; j++) {
			if (arr[j] < arr[minIndex]) {
				minIndex = j;
			}
		}
		swap(arr[minIndex], arr[i]);
	}
}
void shellSort(vector<int>& arr) {
	int n = arr.size();
	cout << "shell" << "\n";
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
void heapify(vector<int>& arr, int n, int i) {
	int largest = i;
	int l = 2 * i + 1;
	int r = 2 * i + 2;

	if (l < n && arr[l] > arr[largest])
		largest = l;

	if (r < n && arr[r] > arr[largest])
		largest = r;

	if (largest != i) {
		swap(arr[i], arr[largest]);
		heapify(arr, n, largest);
	}
}

void heapSort(vector<int>& arr) {
	int n = arr.size();
	cout << "heap" << "\n";
	for (int i = n / 2 - 1; i >= 0; i--)
		heapify(arr, n, i);

	for (int i = n - 1; i >= 0; i--) {
		swap(arr[0], arr[i]);
		heapify(arr, i, 0);
	}
}
void merge(vector<int>& arr, int left, int mid, int right) {
	int n1 = mid - left + 1;
	int n2 = right - mid;

	vector<int> L(n1), R(n2);

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

void mergeSort(vector<int>& arr, int left, int right) {
	if (left < right) {
		int mid = left + (right - left) / 2;
		mergeSort(arr, left, mid);
		mergeSort(arr, mid + 1, right);
		merge(arr, left, mid, right);
	}
}

void mergeSort(vector<int>& arr) {
	mergeSort(arr, 0, arr.size() - 1);
}

void quickSort(vector<int>& arr, int low, int high) {
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
				swap(arr[i], arr[j]);
			}
		}

		swap(arr[pivotIndex], arr[j]);

		quickSort(arr, low, j - 1);
		quickSort(arr, j + 1, high);
	}
}

void quickSort(vector<int>& arr) {
	quickSort(arr, 0, arr.size() - 1);
}

int binarySearch(const vector<int>& arr, int left, int right, int target) {
	if (right >= left) {
		int mid = left + (right - left) / 2;

		if (arr[mid] == target) {
			return mid;
		}

		if (arr[mid] > target) {
			return binarySearch(arr, left, mid - 1, target);
		}

		return binarySearch(arr, mid + 1, right, target);
	}

	return -1;
}

int binarySearch(const vector<int>& arr, int target) {
	return binarySearch(arr, 0, arr.size() - 1, target);
}
int interpolationSearch(const vector<int>& arr, int left, int right, int target) {
	if (left <= right && target >= arr[left] && target <= arr[right]) {
		int pos = left + (static_cast<double>(right - left) / (arr[right] - arr[left])) * (target - arr[left]);

		if (arr[pos] == target) {
			return pos;
		}

		if (arr[pos] < target) {
			return interpolationSearch(arr, pos + 1, right, target);
		}

		return interpolationSearch(arr, left, pos - 1, target);
	}

	return -1;
}

int interpolationSearch(const vector<int>& arr, int target) {
	return interpolationSearch(arr, 0, arr.size() - 1, target);
}
