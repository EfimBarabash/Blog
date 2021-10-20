function LikePost(url, post_id){
    options = {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        },
        body: JSON.stringify({'post_id':post_id})
    }
    fetch(url, options).then(response => response.json()).then(likeСhanges)
}

function likeСhanges(data){
    if (data.like){
        let like = document.getElementById('like')
        like.classList.remove('btn-danger')
        like.classList.add('btn-success')
        like.innerHTML = 'like ' + data.like_count
    }
    else{
        let like = document.getElementById('like')
        like.classList.remove('btn-success')
        like.classList.add('btn-danger')
        like.innerHTML = 'like ' + data.like_count
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
