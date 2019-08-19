#include <stdio.h>
#define MAX 10000


int Answ(int arr[], int targ) {
    int length = sizeof(arr) / sizeof(int);
    for (int i = 0; i < length; i++)
    {   
        int s[MAX] = {0};
        int temp = targ - arr[i];
        if (s[temp] == 1) {
            return 0;
        }
        s[arr[i]] = 1;
    }
    return 1;
    
}
int main() {
    int arr[] = {10, 15, 3, 7};
    int targ = 13;
    int answer = Answ(arr, targ);
    if (answer == 1) {
        printf("True\n");
    } else {
        printf("False\n");
    }
    return 0;
}