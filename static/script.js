// Delete confirmation
const deleteButtons = document.querySelectorAll(".delete");

deleteButtons.forEach(button => {
    button.addEventListener("click", function (e) {
        const confirmDelete = confirm("Are you sure you want to delete this product?");

        if (!confirmDelete) {
            e.preventDefault();
        }
    });
});


// Update confirmation
const updateButtons = document.querySelectorAll(".update");

updateButtons.forEach(button => {
    button.addEventListener("click", function (e) {
        const confirmUpdate = confirm("Save changes to this product?");

        if (!confirmUpdate) {
            e.preventDefault();
        }
    });
});


// Highlight low-stock products
const statusCells = document.querySelectorAll(".low");

statusCells.forEach(cell => {
    cell.title = "This product should be restocked soon.";
});


// Success message after adding/updating
const forms = document.querySelectorAll("form");

forms.forEach(form => {
    form.addEventListener("submit", function () {
        console.log("Request sent successfully.");
    });
});