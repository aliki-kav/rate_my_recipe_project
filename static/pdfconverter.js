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
                pdf.setFontSize(30);
                pdf.text(50, 20, recipeTitle);
                pdf.setFontSize(12);

                var maxWidth = 180;
                var lineHeight = 7;

                var splitDescription = pdf.splitTextToSize("Description: " + recipeDescription, maxWidth);
                pdf.text(10, 60, splitDescription);

                var splitInstructions = pdf.splitTextToSize("Instructions: " + recipeInstructions, maxWidth);
                var instructionsY = 60 + (splitDescription.length * lineHeight) + 10; // Calculate Y position for instructions
                pdf.text(10, instructionsY, splitInstructions);

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
