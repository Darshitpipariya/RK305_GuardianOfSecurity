var load = '<div class="d-flex justify-content-center"><div class="spinner-border" role="status">  <span class="sr-only">Loading...</span></div></div>'
var ans = '<div class="container"><div class="row"><div class="col-sm p-3 mb-2 bg-dark text-white"><h2>LINK</h2>      <p>found as: <strong> </strong></p><h4><strong> <span id = "res"> </span> </strong> </h4> </div>'


var url = 'http://127.0.0.1:8000/api/'

$('#btn').click(function() {
    $("#loading").html(load);
    var link = $('#url').val();

    console.log(url);

    var data = {
        "url": link
    }
    fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            $("#loading").html(ans);
            if (data[link] == 1) {
                $('#res').text('Malicious Link !!');
                console.log("Malicious Link !!");
            } else {
                $('#res').text('Safe Link');
                console.log("Safe Link")
            }
        })
        .catch((error) => {
            $("#loading").html(data);
        });

});