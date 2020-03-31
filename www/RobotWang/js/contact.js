function doSub(){

    let info = new FormData();
    info.append("q_name", $("#question").val());
    info.append("q_tag", $("#tags").val() + ',');
    info.append("q_decribe", $("#detail").val());
    info.append("create_user", "12312312312")

    $.ajax({
        type: "POST",
        url: "http://scuker.xyz/question",
        data: info,
        dataType : "json",
        processData: false,
        contentType: false,
        success: function(){
            alert("提交成功");
            window.location.replace("index-2.html");
        }
    });

    alert("提交成功");
    window.location.replace("index-2.html");
}