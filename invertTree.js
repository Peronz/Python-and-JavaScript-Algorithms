function invert(node) {
    if ( node !== null){
        const temp = node.left;
        node.left = invert(node.right)
        node.right = invert(temp)
    }
    return node;
}