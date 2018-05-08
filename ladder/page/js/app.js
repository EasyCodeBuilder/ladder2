function checkqqNo(qq_no) {

    return "1"

}

function doGet(url,data) {
    $.ajax({
        method:'GET',
        url:url,
        data:{data:data}
    })
        .done(function (msg) {
            alert('Data Saved' + msg)
        });
}