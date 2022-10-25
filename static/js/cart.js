console.log('connected')


var updateBtn = document.getElementsByClassName("updateCart")



// updateBtn.forEach(addEventListener("click", function(){
//     var productId = this.dataset.product
//     var action = this.dataset.action
//     console.log('productId:',productId, 'Action:',action)
// }));




for( let i = 0; i < updateBtn.length; i++){
    updateBtn[i].addEventListener('click',function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId, 'action:',action)

        console.log('user',user)
        if (user ==="AnonymousUser"){
            console.log('not logged in')
        }else{
            updateUserOrder(productId, action)
        }
        
    })
}


function updateUserOrder(productId,action){
    console.log('User is logged in ')

    var url = '/update_item/'

    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action})
    })
    .then((response)=>{
        return response.json()

    })
    .then((data)=>{
        
        console.log('data',data)
        
    })


}