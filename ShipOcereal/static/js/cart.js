

var updateBtns = document.getElementsByClassName('addToCart')

for(var i = 0;i < updateBtns.length;i++){

    updateBtns[i].addEventListener('click',function(){
        var cerealId = this.dataset.cereal
        var action = this.dataset.action
        console.log("cerealID:", cerealId, "action: ", action)

        console.log ('User', User)
        if (User === 'AnonymousUser'){
            console.log('Not logged in')
            alert('Þú þarft að vera innskráð(ur) til að bæta í körfu')
        }
        else{
            updateUserOrder(cerealId, action)
            if (action === 'add') {
                alert('Vara sett í körfu')
            }
            else{
                alert('Vara fjarlægð úr körfu')
                location.reload()
            }
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

