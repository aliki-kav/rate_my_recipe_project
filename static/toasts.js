$(document).ready(function() {
    function show_toast() {
        $("#myToast").toast('show');
        $("#myToast").toast({animation:true});
    }
    setTimeout(show_toast, 1000);

   function confirmDelete() {
       console.log('confirmDelete() called');
       return confirm('Are you sure you want to delete this recipe?');
}


    $('.toast').toast('show');
});
