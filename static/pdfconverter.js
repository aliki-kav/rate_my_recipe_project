$j(document).ready(function () {
    function fetchRecipeData(recipe_id) {
        $j.ajax({
            url: "/rmr/get_recipe_data/" + recipe_id + "/",
            type: "GET",
            success: function (data) {

                var recipeTitle = data.title;
                var recipeDescription = data.description;
                var recipeInstructions = data.instructions;
                var pdf = new jspdf.jsPDF();

                pdf.setFontSize(24);
                pdf.setFont("helvetica", "bold");

                var titleWidth = pdf.getTextWidth(recipeTitle);
                var title = (pdf.internal.pageSize.width - titleWidth) / 2;
                pdf.text(title, 30, recipeTitle);

                pdf.setFontSize(14);
                pdf.setFont("helvetica", "normal");

                var maxWidth = 180;
                var lineHeight = 7;

                pdf.text(10, 50, "Description:");
                var splitDescription = pdf.splitTextToSize(recipeDescription, maxWidth);
                pdf.text(10, 60, splitDescription);

                var instructions = 60 + (splitDescription.length * lineHeight) + 10;
                pdf.text(10, instructions, "Instructions:");
                var splitInstructions = pdf.splitTextToSize(recipeInstructions, maxWidth);
                var instructionsTextY = instructions + lineHeight;
                pdf.text(10, instructionsTextY, splitInstructions);

                pdf.save(recipeTitle + ".pdf");
            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            }
        });
    }

    const pdfButton = document.getElementById("pdf");
    if (pdfButton) {
        pdfButton.addEventListener("click", function () {
            const recipeId = pdfButton.getAttribute("data-recipe-id");
            fetchRecipeData(recipeId);
        });
    }
});
