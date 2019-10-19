class Tree{
    constructor(){
        this.root=null
    }

    insertNode(data, left=null, right=null){
        let Node={data, left, right}

        let number;

        if(!this.root){
            this.root = Node;
        } else {
            number = this.root
            while (number){
                if(data<number.data){
                    if(!number.left){
                        number.left = Node;
                        break;
                    } else{
                        number = number.left;
                    }
                } else if (data>number.data){
                    if(!number.right){
                        number.right=Node;
                        break;
                    } else{
                        number = number.right;
                    }

                } else {
                    break;
                }
            }
        }


    }
    search(data){
        if(!this.root) return;

        let curr = this.root;

        while(curr){
            if(data==curr.data){ 
                 return curr;
            } else if(data<curr.data){
                curr = curr.left;
            } else if (data > curr.data){
                curr = curr.right;
            }
        }
    }

    
}

