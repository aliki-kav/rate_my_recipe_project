$(document).ready(function() {
    function show_toast() {
    $("#myToast").toast('show');
    $("#myToast").toast({animation:true});
    }
    setTimeout(show_toast, 1000)
});
