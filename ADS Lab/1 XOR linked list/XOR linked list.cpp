#include<iostream>
#include<string>
#include<inttypes.h>

using namespace std;

class Node{
    public:
        int data;
        Node* npx;
};

Node* XOR(Node* a, Node* b){
    return (Node*) ((uintptr_t) (a) ^ (uintptr_t) (b));
}

Node* insertBeginning(Node* head, int data){
    Node* newNode = new Node();
    newNode->data = data;

    newNode->npx = head;

    if(head != NULL){
        head->npx = XOR(newNode, head->npx);
    }

    head = newNode;

    return head;
}

Node* insertEnd(Node* head, int data){
    Node* newNode = new Node();
    newNode->data = data;

    Node* curr = head;
    Node* prev = NULL;
    Node* next;

    if(curr == NULL){
        head = insertBeginning(head, data);
    }
    else{
        while(curr->npx != prev){
            next = XOR(prev, curr->npx);
            prev = curr;
            curr = next;
        }
        newNode->npx = curr;
        curr->npx = XOR(newNode, curr->npx);
    }

    return head;
}

void display(Node* head){
    Node* curr = head;
    Node* prev = NULL;
    Node* next;

    if(curr == NULL){
        cout<<"Empty List! \n No items to display \n"<<endl;
    }   

    else{
    	cout<<"Elements of List ";
        while(curr != NULL){
            cout<<curr->data<<"  ";
            next = XOR(prev, curr->npx);
            prev = curr;
            curr = next;
        }
        cout<<endl;
    }
}

int main(){
    Node* head = NULL;
    int choice, value;
    
    while(1){
        cout<<"Select the Operation :"<<endl;
        cout<<"1. INSERT AT BEGINNING"<<endl;
        cout<<"2. INSERT AT END"<<endl;
        cout<<"3. DISPLAY LIST"<<endl;
        cout<<"4. END"<<endl<<endl;
        cin>>choice;
        switch(choice){
            case 1:
                cout<<"Enter Value to be Inserted :"<<endl;
                cin>>value;
                head = insertBeginning(head, value);
                break;

            case 2:
                cout<<"Enter Value to be Inserted :"<<endl;
                cin>>value;
                head = insertEnd(head, value);
                break;

            case 3:
                display(head);
                break;

            case 4:
                exit(0);
                break;
            default:
                cout<<"Select a valid operation"<<endl;
        }
    }
    return 0;
}