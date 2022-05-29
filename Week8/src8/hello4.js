document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(e) {
        alert('hello, ' + document.querySelector('#name').value);
        e.preventDefault();
    });
});
