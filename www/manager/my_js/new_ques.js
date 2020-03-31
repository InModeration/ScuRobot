let create_ques = $("#create_ques");
let q_content = $("#q_content");
let q_describe = $("#q_describe");
let q_tag = $("#q_tag");
let q_creater = $("#q_creater");
create_ques.click(() => {
    if (q_content.val() === '') {
        alert("请输入问题内容!");
        return;
    }
    if (q_describe.val() === '') {
        alert("请输入问题描述!");
        return;
    }
    if (q_tag.val() === '') {
        alert("请输入问题标签!");
        return;
    }
    if (q_creater.val() === '') {
        alert("请输入问题创建者!");
        return;
    }
    // console.log(q_content.val());
    // console.log(q_describe.val());
    // console.log(q_tag.val());
    // console.log(q_creater.val());
    $.ajax({
        type: "POST",
        dataType: "Text",
        url: "http://49.235.105.136/question",
        data: {
            q_name : q_content.val(),
            q_decribe: q_describe.val(),
            q_tag: q_tag.val(),
            creater_user: q_creater.val()
        },
        success: (data) => {
            if (data === '200 OK')
                alert("成功新建问题！");
            else if (data === '已存在该问题!')
                alert(data);
            location.reload();
            $("#new_q")[0].click();
        },
        error: (data) => {
            alert("请求超时，创建失败！请稍后重试！");
        }
    });
});