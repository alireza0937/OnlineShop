function add_to_wishlist(product_id,product_slug){
    $.get('/wishlist/add-to-wishlist',{
        id:product_id,
        slug:product_slug

    }).then(res=>{
            Swal.fire({
  title: 'Alert',
  text: res.text,
  icon: res.icon,
  showCancelButton: false,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'ok'
})
    })

}


function add_to_order_basket(product_id){
    const count = $('#count').val();
    $.get('/orders/add_to_basket',{
        id:product_id,
        cnt:count
    }).then(res=>{
            Swal.fire({
  title: 'Alert',
  text: res.text,
  icon: res.icon,
  showCancelButton: false,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'ok'
})
    })
}


function change_count(product_id,operation,order_id){
    $.get('/orders/change-count',{
        id:product_id,
        operation:operation,
        order_id:order_id
    }).then(location.reload())

}


function get_product_info(product_id,order_id){
    $.get('/orders/remove-product',{
        id:product_id,
        order_id:order_id
    }).then()
}


function get_discount_code(){
    const code = $('#coupon_code').val();
    $.get('/orders/coupon-code',{
        code:code,

    }).then(location.reload())
}