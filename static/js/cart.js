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
    })
}
