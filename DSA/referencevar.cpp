#include <iostream>
using namespace std;

int update(int &n){
    return n++;
}

void jaggeredarr(){
    //jaggered arr
        //1
        //2 3 4
        //5 6
        //7 8 9
    
    int row;
    cout<<"row: ";
    cin>>row;
    int col[row];
    for (int j=0;j<row;j++){
        cin>>col[j];
    }
    cout<<endl;

    //create 2D dynamic arr
    int** arr = new int*[row];
    for (int i=0;i<row;i++){
        arr[i] = new int[col[i]];
    }

    // input 2D arr
    for (int i=0;i<row;i++){
        for(int j=0;j<col[i];j++){
            cin>>arr[i][j];
        }
    }

    // print arr
    for (int i=0;i<row;i++){
        for (int j=0;j<col[i];j++){
            cout<<arr[i][j]<<" ";
        }cout<<endl;
    }

    //delete arr
    for (int i=0;i<row;i++){
        delete []arr[i];
    }
    delete []arr;
    cout<<"Done"<<endl;
    
}

inline int Sumup(int a, int b){
    return a+b;
}

int main(){
       int a =1;
       int b =2;
       int sum;
       sum = Sumup(a,b);
       cout<< sum<<endl;
}