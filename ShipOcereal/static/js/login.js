const wrapper = document.querySelector('.center'),
    form      = wrapper.querySelectorAll('.loginForm'),
    submitInput = form[0].querySelector('input[type="submit"]');



// getDataForm gets data from Form when submit is clicked,
// This function extracts the Username and Password from the form and sends them to loginCheck()
function getDataForm(e){
    e.preventDefault();
    var formData = new FormData(form[0]);
    let username = formData.get('username');
    let password = formData.get('password');
    console.log(username,password);
    return loginCheck(username,password)
}
//loginCheck looks up the user in the DB and compares the password if its a match the user is logged in
// If the username doesnt exist in the DB or no User with the right name has a password match an Error message is sent
function loginCheck(username, password){
    console.log('Here we want to check if the user exists in database')
}

document.addEventListener('DOMContentLoaded', function(){
    submitInput.addEventListener('click', getDataForm, false)
}, false);