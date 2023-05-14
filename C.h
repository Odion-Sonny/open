#include <stdio.h>

int main() {

    int num1 = 10;

    int num2 = 5;

    int sum = num1 + num2;

    int product = num1 * num2;

    

    printf("The sum of %d and %d is: %d\n", num1, num2, sum);

    printf("The product of %d and %d is: %d\n", num1, num2, product);

    

    if (sum > product) {

        printf("The sum is greater than the product.\n");

    } else if (sum < product) {

        printf("The product is greater than the sum.\n");

    } else {

        printf("The sum and product are equal.\n");

    }

    

    for (int i = 1; i <= 10; i++) {

        printf("%d\n", i);

    }

    

    int count = 0;

    while (count < 5) {

        printf("Count: %d\n", count);

        count++;

    }

    

    int array[] = {1, 2, 3, 4, 5};

    int arrayLength = sizeof(array) / sizeof(array[0]);

    

    printf("Array elements: ");

    for (int i = 0; i < arrayLength; i++) {

        printf("%d ", array[i]);

    }

    printf("\n");

    

    int factorial = 1;

    for (int i = 1; i <= 5; i++) {

        factorial *= i;

    }

    printf("Factorial of 5: %d\n", factorial);

    

    int num = 7;

    if (num % 2 == 0) {

        printf("%d is even.\n", num);

    } else {

        printf("%d is odd.\n", num);

    }

    

    int x = 10;

    int y = 5;

    int max = (x > y) ? x : y;

    printf("The maximum of %d and %d is: %d\n", x, y, max);

    

    int numArray[5] = {5, 2, 8, 1, 9};

    int maxNum = numArray[0];

    for (int i = 1; i < 5; i++) {

        if (numArray[i] > maxNum) {

            maxNum = numArray[i];

        }

    }

    printf("The maximum number in the array is: %d\n", maxNum);

    

    int a = 5;

    int b = 10;

    int temp;

    

    printf("Before swapping: a = %d, b = %d\n", a, b);

    

    temp = a;

    a = b;

    b = temp;

    

    printf("After swapping: a = %d, b = %d\n", a, b);

    

    return 0;

}

