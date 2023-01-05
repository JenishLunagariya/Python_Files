#include<iostream>
using namespace std;

class Node{
    public:
    int data;
    Node* next;
    //constructor
    Node(int data){
        this->data = data;
        this->next = NULL;
    }
    //destructor
    ~Node(){
        int value = this->data;
        if (value!=NULL){
            delete next;
            this->next = NULL;
        }
        cout<<"memory freed for node with data: "<<value<<endl;
    }
};
// class LinkedList{
//     public:
//     Node* head;
//     Node* tail;
//     //constructor
//     LinkedList(){
//         this->head = NULL;
//         this->tail = NULL;
//     };
// };
void insertAtHead(Node* &head,int data){
    //new node create with data
    Node* temp = new Node(data);
    temp->next = head;
    head=temp;
};
void insertAtTail(Node* &tail,int data){
    //insert new node at the end
    Node* temp = new Node(data);
    tail->next = temp;
    tail = tail->next;
};
void insertAtPos(Node* &head,Node* &tail,int position, int data){
    // insert at head
    if (position==1){
        insertAtHead(head,data);
        return;
    }
    // traverse through LL to reach at pos.
    Node* temp = head;
    int cnt = 1;
    while(cnt<position-1){
        temp = temp->next;
        cnt++;
    }
    //insert at tail
    if (temp->next == NULL){
        insertAtTail(tail,data);
        return;
    }
    //create new node
    Node* node_new = new Node(data);
    node_new->next = temp->next;
    temp->next = node_new;
};
void deleteNodewithPos(Node* &head,Node* &tail,int position){
    //delete head
    if (position == 1){
        Node* temp = head;
        head = head->next;
        temp->next = NULL;
        delete temp;
    }else{
        Node* current = head;
        Node* prev = NULL;
        int cnt = 1;
        // traverse to reach at pos.
        while(cnt < position){
            prev = current;
            current = current->next;
            cnt++;
        }
        if (current->next==NULL){
            tail = prev;
        }
        prev->next = current->next;
        current->next = NULL;
        delete current;
    }
}
void deleteNodewithData(Node* &head,Node* &tail,int target_data){
    if (head->data == target_data){
        Node* temp = head;
        head = head->next;
        temp->next = NULL;
        delete temp;
    }else{
        Node* temp;
        Node* current = head;
        while (current->next != NULL){
            if(current->next->data == target_data){
                temp = current->next;
                current->next = current->next->next;
                delete temp;
                break;
            }
            current = current->next;
        }
        // delete current;
    }
}
void print(Node* head){
    //print linkedlist
    Node* temp = head;
    while(temp != NULL){
        cout<<temp->data<<"->";
        temp = temp->next;
    }cout<<endl;
};

int main(){
    Node* node0 = new Node(1);
    
    Node* head = node0;
    Node* tail = node0;
    print(head);
    insertAtTail(tail,2);
    insertAtTail(tail,3);
    insertAtTail(tail,4);
    insertAtTail(tail,5);
    print(head);
    // print(tail);
    // deleteNodewithPos(head,tail,5);
    // deleteNodewithData(head,tail,3);
    print(head);
    print(tail);

    // insertAtPos(head,tail,6,20);
    // print(head);
    // cout<<"head: "<<head->data<<endl;
    // cout<<"tail: "<<tail->data<<endl;
    // deleteNodewithPos(head,tail,4);
    // print(head);
    /*Fix below:*/
    /*deleting last node, tail shows garbag value */
}