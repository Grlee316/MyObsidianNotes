```c
#include<stdlib.h> //to have access to mallloc, free

struct llist{
	struct process *head;
	struct process *tail;
	int size;
};

struct llist* create_new_queue(){
	struct llist = ready_queue = (struct llist*)malloc(sizeof(struct llist));
}

int main(){
	struct llist* ready_queue = create_new_queue();

	
}
```