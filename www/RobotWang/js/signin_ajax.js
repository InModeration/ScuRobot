function signin_go(){
    var accountinfo = document.getElementById("signin_accountid");
    var passwordinfo = document.getElementById("signin_password");
    console.log(accountinfo.value);
    console.log(passwordinfo.value);

    let json_data = new FormData();
    json_data.append("username",accountinfo.value);
    json_data.append("password",passwordinfo.value);
    var aim_url = "http://scuker.xyz/login";

    console.log(json_data)
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
                alert("登陆失败");
                window.location.reload();
                return 0;
            }
            else{
                alert("登陆成功");
                Setcookie(data.data.username, data.data.token);
                window.location.replace("index-2.html");
                return 0;
            }
        }
    });
}

function Setcookie (name, value) {
    //设置名称为name,值为value的Cookie
    var expdate = new Date();   //初始化时间
    expdate.setTime(expdate.getTime() + 30 * 60 * 1000);   //时间单位毫秒
    document.cookie = name+"="+value + ";expires=" + expdate.toGMTString() + ";path=/";

    // 即document.cookie= name+"="+value+";path=/";  时间默认为当前会话可以不要
    // 路径要填写，因为JS的默认路径是当前页，如果不填，此cookie只在当前页面生效！
}

function getCookie(cname)
{
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++)
    {
        var c = ca[i];
        while (c.charAt(0) == ' ')
        {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}
