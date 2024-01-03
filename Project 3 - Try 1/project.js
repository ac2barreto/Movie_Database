$(document).ready(function() {
    fetch('/get-movie-titles').then(response => response.json()).then(data => {
        const select = document.getElementById('movieDropdown');
        data.forEach(movie => {
            let option = document.createElement('option');
            option.text = movie[0];
            select.add(option);
        });
    });
});

function updateCharts(title) {
    // Fetch and display each chart
    // This will be a combination of fetch requests to '/get-movie-data/' and Highcharts rendering
    // Example for one chart:
    fetch(`/get-movie-data/${title}`).then(response => response.json()).then(data => {
        // Use data to render Highcharts (for each type of chart)
    });
}
