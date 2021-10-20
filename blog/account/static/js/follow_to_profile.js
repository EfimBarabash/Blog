function Follow(url, user_id){
    options = {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({'user_id': user_id})
    }
    fetch(url, options).then(response=>response.json()).then(followChanges)
}



function followChanges(data){
    if (data.follow){
        let button = document.getElementById('follow')
        button.classList.remove('btn-success')
        button.classList.add('btn-danger')
        button.innerHTML = 'unfollow'
    }
    else{
        let button = document.getElementById('follow')
        button.classList.remove('btn-danger')
        button.classList.add('btn-success')
        button.innerHTML = 'follow'
    }
}


function getCookie(name){
    let cookieList = document.cookie.split(';');
    let cookieValue = null;
    for (let i = 0; i < cookieList.length; i++){
        if (cookieList[i].slice(0, name.length) === name){
            cookieValue = cookieList[i].slice(name.length + 1);
            break;
        }
    }
    return cookieValue
}
