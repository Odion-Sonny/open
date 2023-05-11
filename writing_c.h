#include <stdio.h>

// Function to swap two integers
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to perform bubble sort
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}

// Function to print an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = { 64, 34, 25, 12, 22, 11, 90 };
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("Unsorted array: ");
    printArray(arr, n);

    bubbleSort(arr, n);

    printf("Sorted array: ");
    printArray(arr, n);

    return 0;
}

// Structure to represent a point in 2D space
struct Point {
    int x;
    int y;
};

// Function to calculate the distance between two points
float calculateDistance(struct Point p1, struct Point p2) {
    int dx = p2.x - p1.x;
    int dy = p2.y - p1.y;
    return sqrt(dx * dx + dy * dy);
}

int main() {
    struct Point p1 = { 1, 2 };
    struct Point p2 = { 4, 6 };

    float distance = calculateDistance(p1, p2);
    printf("Distance between p1 and p2: %.2f\n", distance);

    return 0;
}

// Function to find the maximum of two numbers
int max(int a, int b) {
    return (a > b) ? a : b;
}

int main() {
    int num1 = 10;
    int num2 = 20;

    int maximum = max(num1, num2);
    printf("Maximum of %d and %d is %d\n", num1, num2, maximum);

    return 0;
}

// Function to calculate the factorial of a number
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    int num = 5;
    int fact = factorial(num);

    printf("Factorial of %d is %d\n", num, fact);

    return 0;
}

// Function to check if a number is prime
int isPrime(int n) {
    if (n <= 1) {
        return 0;
    }

    for (int i = 2; i <= n / 2; ++i) {
        if (n % i == 0) {
            return 0;
        }
    }

    return 1;
}

int main() {
    int num = 17;

    if (isPrime(num)) {
        printf("%d is a prime number.\n", num);
    } else {
        printf("%d is not a prime number.\n", num);
    }

    return 0;
}



#include <stdio.h>

// Function to calculate the factorial of a number
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}

// Function to check if a number is prime
int isPrime(int n) {
    if (n <= 1) {
        return 0;
    }

    for (int i = 2; i <= n / 2; ++i) {
        if (n % i == 0) {
            return 0;
        }
    }

    return 1;
}

// Function to find the maximum of two numbers
int max(int a, int b) {
    return (a > b) ? a : b;
}

// Function to calculate the sum of an array of integers
int sumArray(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return sum;
}

// Function to print the elements of an array
void printArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int num = 5;
    int fact = factorial(num);

    printf("Factorial of %d is %d\n", num, fact);

    int primeNum = 17;

    if (isPrime(primeNum)) {
        printf("%d is a prime number.\n", primeNum);
    } else {
        printf("%d is not a prime number.\n", primeNum);
    }

    int num1 = 10;
    int num2 = 20;

    int maximum = max(num1, num2);
    printf("Maximum of %d and %d is %d\n", num1, num2, maximum);

    int numbers[] = { 2, 4, 6, 8, 10 };
    int arraySize = sizeof(numbers) / sizeof(numbers[0]);

    int arraySum = sumArray(numbers, arraySize);
    printf("Sum of array: %d\n", arraySum);

    printf("Array elements: ");
    printArray(numbers, arraySize);

    return 0;
}

// Structure to represent a point in 2D space
struct Point {
    int x;
    int y;
};

// Function to calculate the distance between two points
float calculateDistance(struct Point p1, struct Point p2) {
    int dx = p2.x - p1.x;
    int dy = p2.y - p1.y;
    return sqrt(dx * dx + dy * dy);
}

// Function to swap two integers
void swap(int* a, int* b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Function to perform bubble sort
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(&arr[j], &arr[j + 1]);
            }
        }
    }
}