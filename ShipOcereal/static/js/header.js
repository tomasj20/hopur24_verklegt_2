xhttp = new XMLHttpRequest()

function navToHealthyFilter(){
    console.log('Hello Healthyfilter')
    return location.href = 'http://127.0.0.1:8000/filter/healthy'
}
function navToFrontPage(){
    console.log('Hello Frontpage')
    return location.href = 'http://127.0.0.1:8000/'
}

function navToSugaryFilter(){
    console.log('Hello sugaryfilter')
    return location.href = 'http://127.0.0.1:8000/filter/sugary'
}

function navToVeganFilter(){
    console.log('Hello Veganfilter')
    return location.href = 'http://127.0.0.1:8000/filter/vegan'
}

function navToLoginPage(){
    console.log('Hello login page')
    return location.href = 'http://127.0.0.1:8000/login'
}
function navToCart(){
    console.log('Hello cart page')
    return location.href = 'http://127.0.0.1:8000/cart'
}

