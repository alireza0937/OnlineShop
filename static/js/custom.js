function user_choice(){
    const product = $('#search').val();
    $.get('',{
        pro:product
    })
}