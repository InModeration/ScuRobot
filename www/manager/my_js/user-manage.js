$.ajax({
    type: "GET",
    dataType: "json",
    url: "http://49.235.105.136/user/all_user",
    data: "num=2000",
    /*
        @param data 返回的json文件
     */
    success: (data) => {
        $("#if_any").css("display", "none");
        $("#if_any_2").css("display", "");
        let i = 1;
        // 遍历每一个json
        data.forEach((elem) => {
            let keys = [];
            console.log(elem);
            // 获取键值对的key
            for (let k in elem) keys.push(k);
            let tr = $(document.createElement("tr"));
            let th = $(document.createElement("td"));
            th.text(i++);
            th.css("fontSize", 18);
            tr.append(th);
            // 遍历每一个键值对
            keys.forEach((value_index) => {
                let th = $(document.createElement("td"));
                if (elem[value_index] == null)
                    th.text("（无）");
                else
                    th.text(elem[value_index]);
                tr.append(th);
            });
            let td = $(document.createElement("td"));
            let button = $(document.createElement("button"));
            button.addClass("btn btn-danger btn-sm");
            button.text("移除用户");
            button.attr('id', elem['_id']);
            button.click((e) => {
                $.ajax({
                    type: "DELETE",
                    url: "http://49.235.105.136/user/a_user" + "?_id=" + $(e.toElement).attr('id'),
                    data: {username: 'zjianfa2', password: '12345'},
                    success: (data) => {
                        alert("删除成功");
                        location.reload();
                    }
                });
            });
            td.append(button);
            tr.append(td);
            $("#user_info").append(tr);
        })
    }
});