// event listener for presenting the payment type creation form on 
// the order detail view
$(".payment_type_option").on('click', function() {
    if (this.value === 'new') {
        $("#order_view_payment_form").removeClass('hidden')
    } else {
        $("#order_view_payment_form").addClass('hidden')
    }
});