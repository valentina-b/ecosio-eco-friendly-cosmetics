// Disable +/- buttons outside 1-99 range
function handleEnableDisable(itemId) {
    let currentValue = parseInt($(`#id-quantity-${itemId}`).val());
    let minusDisabled = currentValue < 2;
    let plusDisabled = currentValue > 98;
    $(`#decrement-quantity-${itemId}`).prop('disabled', minusDisabled);
    $(`#increment-quantity-${itemId}`).prop('disabled', plusDisabled);
}

// Ensure proper enabling/disabling of all inputs on page load
let allQtyInputs = $('.quantity-input');
for(let i = 0; i < allQtyInputs.length; i++){
    let itemId = $(allQtyInputs[i]).data('item-id');
    handleEnableDisable(itemId);
}

// Check enable/disable every time the input is changed
$('.quantity-input').change(function() {
    let itemId = $(this).data('item-id');
    handleEnableDisable(itemId);
});

// Increment quantity
$('.increment-quantity').click(function(e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.quantity-input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue + 1);
    let itemId = $(this).data('item-id');
    handleEnableDisable(itemId);
});

// Decrement quantity
$('.decrement-quantity').click(function(e) {
    e.preventDefault();
    let closestInput = $(this).closest('.input-group').find('.quantity-input')[0];
    let currentValue = parseInt($(closestInput).val());
    $(closestInput).val(currentValue - 1);
    let itemId = $(this).data('item-id');
    handleEnableDisable(itemId);
});
