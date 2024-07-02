// Get the modal
var modal = document.getElementById('editModal');

// Get the <span> element that closes the modal
var span = document.getElementsByClassName('close')[0];

// Edit functionality
var editButtons = document.querySelectorAll('.edit-btn');
editButtons.forEach(function(button) {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        var row = button.closest('tr');
        var cells = row.querySelectorAll('td');
        
        // Populate form fields with current row data
        document.getElementById('editRowIndex').value = row.id; // Store row index for update
        document.getElementById('editName').value = cells[0].innerText.trim();
        document.getElementById('editEmail').value = cells[1].innerText.trim();
        document.getElementById('editAge').value = cells[2].innerText.trim();
        document.getElementById('editPhone').value = cells[3].innerText.trim();
        document.getElementById('editCourses').value = cells[4].innerText.trim();
        
        // Display the modal
        modal.style.display = 'block';
    });
});

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = 'none';
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = 'none';
    }
}

// Save edited data
document.getElementById('editUserForm').addEventListener('submit', function(e) {
    e.preventDefault();
    var rowIndex = document.getElementById('editRowIndex').value;
    var name = document.getElementById('editName').value;
    var email = document.getElementById('editEmail').value;
    var age = document.getElementById('editAge').value;
    var phone = document.getElementById('editPhone').value;
    var courses = document.getElementById('editCourses').value;
    
    // Update table row with edited data
    var row = document.getElementById(rowIndex);
    row.cells[0].innerText = name;
    row.cells[1].innerText = email;
    row.cells[2].innerText = age;
    row.cells[3].innerText = phone;
    row.cells[4].innerText = courses;
    
    // Close the modal after saving
    modal.style.display = 'none';
});

// Delete functionality
var deleteButtons = document.querySelectorAll('.delete-btn');
deleteButtons.forEach(function(button) {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        if (confirm('Are you sure you want to delete this record?')) {
            var row = button.closest('tr');
            row.parentNode.removeChild(row);
        }
    });
});
