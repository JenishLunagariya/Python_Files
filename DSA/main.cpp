#include<iostream>
using namespace std;

int binarySearch(int arr[],int start,int end,int key){
    if (start>end){
        return -1;
    }
    int mid = start + (end-start)/2;
    if (arr[mid] == key){
        return mid;
    }else if (arr[mid]>key)
    {
        end = mid-1;
    }else{
        start = mid+1;
    }
    return binarySearch(arr,start,end,key);
}



int main(){
    int arr[6] = {3,4,6,8,9,10};
    cout<<binarySearch(arr,0,5,2)<<endl;
    return 0;
    
}