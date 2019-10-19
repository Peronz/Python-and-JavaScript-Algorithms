class Node {
	constructor(data, next=null){
		this.data = data;
		this.next = next

	}
}

class LinkedList {
	constructor(){
		this.head = null;
		this.size = 0;
	}

	// insert first node
	insertFirst(data){
		this.head = new Node(data, this.head);
		this.size++                                                                                               
	}


	// insert last node
	insertLast(data){
		let node = new Node(data);
		let current;

		// if empty, make head
		if(!this.head){
			this.head = node;
		} else {
			current = this.head;

			while(current.next){
				current = current.next;
			}
			current.next = node;
		}

		this.size ++
	}


	// insert at index
	insertAt(data, index){
		// if index is out of range
		if(index > 0 && index > this.size){
			return;
		}
		// if first index
		if(index === 0) {
			this.head = new Node(data, this.head);
			return;
		}
		const node = new Node(data);
		let current, previous;

		// Set current to first
		current = this.head;
		let count = 0;

		while(count < index) {
			previous = current; // Node before index
			count++;
			current = current.next; // Node after index
		}

		node.next = current;
		previous.next = node;

		this.size++;
	}



	// get at index
	getAt(index){
		let current = this.head;
		let count = 0;


		while(current) {
			if(count == index) {

			}
			count ++
			current = current.next;
		}
		return;
	}


	// remove at index
	removeAt(index){
		if(index > 0 && index > this.size) {
			return;
		}
		let current = this.head;
		let previous;
		let count = 0;
		// remove first
		if(index === 0){
			this.head = current.next;
		} else {
		  while(count < index){
		  	count++
		  	previous = current;
		  	current = current.next;

		  }

		  previous.next = current.next;	

		}

		this.size--;
	}



	// clear list
	clearList(){
		this.head = null;
		this.size = 0;
	}



	// print list data
	printListData(){
		let current = this.head;

		while (current) {
			current = current.next;
		}
	}
}

