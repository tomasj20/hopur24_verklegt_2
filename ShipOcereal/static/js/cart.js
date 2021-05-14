

var updateBtns = document.getElementsByClassName('addToCart')

for(var i = 0;i < updateBtns.length;i++){

    updateBtns[i].addEventListener('click',function(){
        var cerealId = this.dataset.cereal
        var action = this.dataset.action
        console.log("cerealID:", cerealId, "action: ", action)

        console.log ('User', User)
        if (User === 'AnonymousUser'){
            console.log('Not logged in')
        }
        else{
            updateUserOrder(cerealId, action)
            alert('Successfully added to cart')
        }
    })}

    function addToCartAlert(){
        console.log('inside alert')
        alert('Item added to cart.')
    }

    function updateUserOrder(cerealId, action){
        var url = '/update_item'

        fetch(url, {
            method:'POST',
            headers : {
                'Content-Type':'application/json',
                'X-CSRFToken' : csrftoken
            },
            body:JSON.stringify( {'cerealId':cerealId, 'action':action})
        })

            .then((response)=> {
                return response.json()
            })
            .then((data)=> {
                console.log('data',data)
                })
    }

