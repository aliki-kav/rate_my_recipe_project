$j(document).ready(function() {
    function fetchRecipeData(recipe_id) {
        $j.ajax({
            url: "/rmr/get_recipe_data/" + recipe_id + "/",
            type: "GET",
            success: function(data) {
                // console.log(data);

                var recipeTitle = data.title;
                var recipeDescription = data.description;
                var recipeInstructions = data.instructions;
                var pdf = new jspdf.jsPDF();
                pdf.text(30, 20, recipeTitle);
                pdf.text(20, 30, recipeDescription);
                pdf.text(20, 40, recipeInstructions);
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
