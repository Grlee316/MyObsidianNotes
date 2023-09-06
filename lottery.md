```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct process{
    int size;       //size of the process
    char name;      //name of the process
    struct process* next;
    struct process* prev;
    
    //unused
    //int sLow;    //lowest number of the span
    //int sHigh;   //highest number of the span
};  

struct llist {
    struct process *head;
    struct process *tail;
    int size;
};

struct llist* create_new_queue(){
    struct llist* ready_queue = (struct llist*)malloc(sizeof(struct llist));
    ready_queue->head = NULL;
    ready_queue->tail = NULL;
    ready_queue->size = 0;
    return ready_queue;
}

struct process* create_new_process(int size, char name){ 
    struct process* pr = (struct process*)malloc(sizeof(struct process));
    pr->name = name;
    pr->size = size;
    pr->next = NULL;
    pr->prev = NULL;
    return pr;
    
    //unused:
    
    //, int beginSpan, int endSpan
    //pr->sLow = beginSpan;
    //pr->sHigh = endSpan;
}

int add_process_at_end(struct llist* queue, struct process* pA) {
    if(queue->head == NULL) {
        queue->head = pA;
        queue->tail = pA;
        queue->size = 1;
        return 0;
    }

    queue->tail->next = pA;
    pA->prev = queue->tail;
    queue->tail = pA;
    ++queue->size;

}

struct process* pop_first_process(struct llist* queue) {
    struct process* pr = NULL;
    if(queue == NULL)
        return pr;

    if(queue->size == 0)
        return pr;

    if(queue->size == 1) {
        pr = queue->head;
        queue->size = 0;
        queue->head = NULL;
        queue->tail = NULL;
        return pr;
    }

    --queue->size;
    pr = queue->head;
    queue->head = pr->next;
    pr->next = NULL;
    queue->head->prev = NULL;

    return pr;
}

struct process* pop_n_process(struct llist* queue, struct process* pN){
    struct process* pr = NULL;
    if(queue == NULL)
        return pr;

    if(queue->size == 0)
        return pr;

    if(queue->size == 1) {
        pr = queue->head;
        queue->size = 0;
        queue->head = NULL;
        queue->tail = NULL;
        return pr;
    }
    
    --queue->size;
    pr = pN;
    pr->prev->next = pN->next;
    pr->next->prev = pN->prev;
    
    return pr;
    
}

int executeLottery(int a, struct llist* queue){
    //a is the lottery number
    //queue is the queue with (size, head, and tail information)
    int totalPassed = 0;
    
    
    if(a <= queue->head->size && queue->head->size != 1){                  //if a is less than the "span or the size" of the head, then a is part of that process
        int temp = queue->head->size;
        --temp;
        queue->head->size = temp;               //reduce the size of the process
        printf("The lottery number is a part of Process [%c], the size is reduced to [%d]\n",queue->head->name, queue->head->size);
        return 0;
    }else if(a == 1 && queue->head->size == 1){
        printf("Process [%c] is finished, the process will be removed from the queue\n",queue->head->name);
        pop_first_process(queue);
    }else if(a > queue->head->size){
        totalPassed = queue->head->size; //to count the "a"
        struct process* pA = queue->head->next;
        
        while(a > (totalPassed + pA->size)){    //trying to skip pointer
            totalPassed = totalPassed + pA->size;
            struct process*pB = pA->next;
            pA = pB;
            printf("we are in process [%c]\n",pA->name);
        }
        
        //create temp process pointer
        if(a <= (totalPassed + pA->size) && pA->size != 1){
            int temp = pA->size;
            --temp;
            pA->size = temp;
            
            printf("The lottery number is a part of Process [%c], the size is reduced to [%d]\n",pA->name, pA->size);
            return 0;
        }else if(a == (1 + pA->size) && pA->size == 1){
            printf("Process [%c] is finished, the process will be removed from the queue\n",queue->head->name);
            pop_n_process(queue,pA);
        }
    }
}


int main(){
    //int seed = time(NULL);
    int sizeofQueue;
    int allotedSpan;
    char name = 'A';
    int endspan;
    int seed = time(NULL);
    int totalSize = 0;      //to calculate the total size of all of our processes
    
    struct llist* mainQueue = create_new_queue(); 
    
    printf("Please enter the length of the queue you're trying to create\n");
    scanf("%d",&sizeofQueue);
    printf("You choose %d",sizeofQueue);
    mainQueue->size = sizeofQueue;
    
    int sizeOfProcess = 0;
    for(int a = 0; a < sizeofQueue; a++){
        printf("\n\nPlease enter the size for Process %c. The size of the process will be the size being alloted\n",name);
        scanf("%d",&sizeOfProcess);
        
        totalSize = totalSize + sizeOfProcess;
        struct process* pr = create_new_process(sizeOfProcess, name);
    
        printf("\nSUMMARY of Process %c\n",name);
        printf("Alloted size: %d",pr->size);
        
        add_process_at_end(mainQueue,pr);
        name = name + 1;       //name will be shifted + 1
    }
    
    //Testing Part to see if List is at the good condition
    printf("\nCompleted Initialization");
    
    printf("\nFirst Process : %c",mainQueue->head->name);
    printf("\nLast Process : %c", mainQueue->tail->name);
    printf("\nTotal size : %d",totalSize);
    printf("\n==========================================================\n");
    
    int backwardSize = totalSize;
    while(totalSize > 0 && mainQueue->head->size > 0){
        srand(seed);
        int a = (rand() % backwardSize )+ 1;
        printf("Lottery number is %d\n",a);
        
        //Check which process have the "lottery number", and remove it from the queue
        executeLottery(a, mainQueue);
        
        seed = a;
        --backwardSize;
        --totalSize;
    }
    
    
}

/*
int main() {
    char name = 'A';
    int time_slice = 10;
    struct llist* ready_queue = create_new_queue();

    ///loop over how many processes
    for(int ix = 0; ix < 4; ++ix)
    {
        struct process* pr = create_new_process(45, name++);
        add_process_at_end(ready_queue, pr);
    }


    //ROUND ROBIN
    while(ready_queue->size > 0) {
        struct process* pr = pop_first_process(ready_queue);
        //// run process
        pr->size -= time_slice;
        if(pr->size > 0)
            add_process_at_end(ready_queue, pr);
        else {
            free(pr);
        }
    
        
    }
    
    return 0;
}*/


/**
 * int count = 10; //User input
    while(count > 0){
        srand(seed);
        int a = rand() % 101;
        printf( " num = %d",a);
        seed = a;
        --count;
    }
 *
 
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 *  //IF the span is determined by the user (equal span)
    printf("\nPlease enter the span of the process\n");
    scanf("%d",&allotedSpan);
    printf("You alloted %d spans per process", allotedSpan);
    
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    int sizeOfProcess = 0;
    for(int a = 0; a < sizeofQueue; a++){
        printf("\n\nPlease enter the size for Process %c. The size of the process will be the size being alloted\n",name);
        scanf("%d",&sizeOfProcess);
        //printf("Size of Process %c will be %d",name, sizeOfProcess);
        
        totalSize = totalSize + sizeOfProcess;
        //endspan = current + sizeOfProcess - 1; //might not need this if we just utilize the size
        struct process* pr = create_new_process(sizeOfProcess, name); //, current, endspan
    
        printf("\n\nSUMMARY of Process %c\n",name);
        printf("Alloted size: %d\n",pr->size);
        //printf("Beginning of the Allotment: %d\n",pr->sLow);
        //printf("End of the Allotment: %d\n",pr->sHigh);
        
        add_process_at_end(mainQueue,pr);
        
        //current = endspan + 1; //become the new current 
        name = name + 1;       //name will be shifted + 1
    }
    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
 */
```