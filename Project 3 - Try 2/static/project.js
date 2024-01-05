


// Genre Pie chart script _______

document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/get-movie-genres')
    .then(response => response.json())
    .then(data => {
        Highcharts.chart('genreContainer', {
            chart: {
                type: 'pie'
            },
            title: {
                text: 'Movie Genre Distribution'
            },
            series: [{
                name: 'Genres',
                colorByPoint: true,
                data: data.map(item => {
                    return {
                        name: item[0], // genre name
                        y: item[1]    // genre count
                    };
                })
            }]
        });
    });
});



// Yearly data script __________ INCLUDED DIRECTLY IN HTML file

// function loadChart() {
//     fetch('/api/get-release-year')
//     .then(response => response.json())
//     .then(data => {
//         // Process the data
//         let years = data.map(item => item[1]);
//         let counts = data.map(item => item[0]);

//         // Render the chart using Highcharts
//         Highcharts.chart('releaseYearContainer', {
//             chart: {
//                 type: 'line'
//             },
//             title: {
//                 text: 'Movie Release Years'
//             },
//             xAxis: {
//                 categories: years,
//                 title: {
//                     text: 'Release Year'
//                 }
//             },
//             yAxis: {
//                 title: {
//                     text: 'Number of Movies'
//                 }
//             },
//             series: [{
//                 name: 'Movies',
//                 data: counts
//             }]
//         });
//     })
//     .catch(error => {
//         console.error('There has been a problem with your fetch operation:', error);
//     });
// }

// // Check if Highcharts is loaded
// if (typeof Highcharts !== 'undefined') {
//     loadChart();
// } else {
//     // If not, set a callback to load the chart when Highcharts is ready
//     document.addEventListener('readystatechange', event => {
//         if (event.target.readyState === 'complete') {
//             loadChart();
//         }
//     });
// }

