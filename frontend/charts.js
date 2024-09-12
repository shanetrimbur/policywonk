const ctx = document.getElementById('policyChart').getContext('2d');
const policyChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Policy A', 'Policy B', 'Policy C'],
        datasets: [{
            label: 'Cost to Taxpayers',
            data: [200, 300, 150],
        }]
    }
});
