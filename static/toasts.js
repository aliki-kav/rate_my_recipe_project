function show_toast() {
    $("#myToast").toast('show');
    $("#myToast").toast({animation:true});
}

function confirmDeleteRecipe() {
    console.log('confirmDeleteRecipe() called');
    return confirm('Are you sure you want to delete this recipe?');
}

function confirmDeleteAccount() {
    console.log('confirmDeleteAccount() called');
    return confirm('Are you sure you want to delete your account? All your recipes and ratings will be lost.');
}

$(document).ready(function() {
    setTimeout(show_toast, 1000);
    $('.toast').toast('show');
});
