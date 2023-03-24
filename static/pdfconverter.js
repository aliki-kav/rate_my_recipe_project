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
                var descriptionTextY = 60;
                for (var i = 0; i < splitDescription.length; i++) {
                    if (descriptionTextY > pdf.internal.pageSize.height - 20) {
                        pdf.addPage();
                        descriptionTextY = 20;
                    }
                    pdf.text(10, descriptionTextY, splitDescription[i]);
                    descriptionTextY += lineHeight;
                }

                pdf.text(10, descriptionTextY, "Instructions:");
                var splitInstructions = pdf.splitTextToSize(recipeInstructions, maxWidth);
                var instructionsTextY = descriptionTextY + lineHeight;
                for (var j = 0; j < splitInstructions.length; j++) {
                    if (instructionsTextY > pdf.internal.pageSize.height - 20) {
                        pdf.addPage();
                        instructionsTextY = 20;
                    }
                    pdf.text(10, instructionsTextY, splitInstructions[j]);
                    instructionsTextY += lineHeight;
                }

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
