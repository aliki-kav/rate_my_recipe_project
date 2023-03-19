$j(document).ready(function() {
    function fetchRecipeData(recipe_id) {
        $j.ajax({
            url: "/rmr/get_recipe_data/" + recipe_id + "/",
            type: "GET",
            success: function(data) {

                var recipeTitle = data.title;
                var recipeDescription = data.description;
                var recipeInstructions = data.instructions;
                var pdf = new jspdf.jsPDF();
                //want to make pdf text bigger
                pdf.setFontSize(30);
                //want to center the text

                pdf.text(50, 20, recipeTitle);
                pdf.setFontSize(12);

                pdf.text(10, 60, "Description: "+recipeDescription);
                pdf.text(10, 80, "Instruction: "+recipeInstructions);
                pdf.save(recipeTitle + ".pdf");
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            }
        });
    }

    const pdfButton = document.getElementById("pdf");
    if (pdfButton) {
        pdfButton.addEventListener("click", function() {
            const recipeId = pdfButton.getAttribute("data-recipe-id");
            fetchRecipeData(recipeId);
        });
    }
});
