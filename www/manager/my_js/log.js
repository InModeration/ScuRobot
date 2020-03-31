let log = $("#login");
log.click(() => {
    let username = $("#input1").val();
    let password = $("#input2").val();
    if (username === '') {
        alert("请输入账号！");
        return;
    }
    if (password === '') {
        alert("请输入密码！");
        return;
    }

    $.ajax({
        type: "POST",
        url: "http://49.235.105.136/login",
        dataType: "json",
        data: {
            'username': username,
            'password': password,
        },
        success: (data) => {
            if (data['info'] === '密码错误') {
                alert(data['info'] + "！请重试！");
                location.reload();
                return;
            }
            alert("登录成功！欢迎您，" + username);
            window.location.href = "homePage.html";
        },
        error: () => {
            alert("网络错误！登录失败！");
        }
    });

});