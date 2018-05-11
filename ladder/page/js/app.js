function checkqqNo(qq_no) {

    return "1"

}

function doGet(url,data) {
    var m;
    m=$.ajax({
        method:'GET',
        url:url,
        data:{data:data}
    })
        .done(process);
    return m.responseText;
}

function process(msg) {
    console.log('Data Saved' + msg);
    var j_data;
    // var m="{'trans_cd': '1001', 'buss_no': '20180509125410178000', 'resp_no': '0000', 'resp_msg': '注册成功', 'user_id': '201805090002'}"
     j_data=eval('(' + msg + ')');
    // console.log("user_id="+j_data["user_id"]);

    return msg;
}