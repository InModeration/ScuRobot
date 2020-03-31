function signup_go(){
    var nameinfo = document.getElementById("signup_name");
    var accountinfo  = document.getElementById("signup_id");
    var passwordinfo = document.getElementById("signup_password");
    var password2info = document.getElementById("signup_password-ack");
    console.log(nameinfo.value);
    console.log(accountinfo.value);
    console.log(passwordinfo.value);

    if(passwordinfo.value != password2info.value){
        window.location.reload();
        alert("密码不相同！");
        return 0;
    }

    let json_data = new FormData();
    json_data.append("username",accountinfo.value);
    json_data.append("name",nameinfo.value);
    json_data.append("password",passwordinfo.value);

    console.log(json_data.getAll("username"));

    let aim_url = "http://scuker.xyz/sign";

    $.ajax({
        type:"POST",
        dataType: "json",
        url: aim_url,
        data: json_data,
        // contentType : "application/json",
        processData: false,
        contentType: false,
        success:function (data) {
            if(data.message == "fail") {
                console.log(data);
                alert("注册失败，尝试换一个手机号哦！");
                window.location.reload();
                return 0;
            }
            else{
                alert("注册成功");
                window.location.replace("login.html");
                return 0;
            }
        }

    });
}