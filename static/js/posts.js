function deleteConfirmation(){
    const Response = confirm("¿Estas seguro?")

    if(Response){
        window.location.href= "/posts/delete/"+id

    }
}