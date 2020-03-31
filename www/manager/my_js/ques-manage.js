// 问题列表显示
$.ajax({
    type: "GET",
    dataType: "json",
    url: "http://49.235.105.136/q_and_a?num=200",
    success: (data) => {
        // 显示表头
        $("#ques_list").css("display", "");
        let i = 1;
        data.forEach((every_ques) => {
            let tr = $(document.createElement("tr"));
            let td = $(document.createElement("td"));
            td.text(i++);
            tr.append(td);
            for (let key in every_ques) {
                // 将非答案的信息打印出来
                if (key !== 'answers') {
                    let td = $(document.createElement("td"));
                    let p = $(document.createElement("p"));
                    p.attr("class", "my_info");
                    p.text(every_ques[key]);
                    td.append(p);
                    tr.append(td);
                }
            }
            let oper = $(document.createElement("td"));
            let button = $(document.createElement("button"));
            button.text("查看详情");
            button.attr("class", "btn btn-info btn-sm");
            // 点击查看详情 调用该问题的display_detail()方法进行查询
            button.click(()=>{
                $("#ques_list").remove();
                display_detail(every_ques['_id']);
            });
            oper.append(button);
            tr.append(oper);
            $("#ques_list").append(tr);
        });
    },
    error: () => {
        // 失败则打印提示语
        let p = $(document.createElement("p"));
        p.text("问题列表加载失败，请刷新页面重试！");
        p.css("margin-top", "15%");
        p.css("text-align", "center");
        let row = $("#row");
        row.append(p);
    }
});

// 详情显示
function display_detail(ques_id) {
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "http://49.235.105.136/q_and_a",
        data: "_id=" + ques_id,
        success: (data) => {
            let row = $("#row");
            if (data.length === 0) {
                alert("查询的问题已被删除，请刷新！");
                return;
            }
            data = data[0];

            // 创建答案
            let answers = data['answers'];

            let h3 = $(document.createElement("h3"));
            h3.attr("id", "h3");
            h3.text('该问题一共有 ' + answers.length + ' 条答案');
            row.append(h3);

            let table = $(document.createElement("table"));

            // 创建表标签
            table.attr("class", "table table-bordered");
            table.attr("id", "ques_list");
            row.append(table);

            // 创建问题id
            let ques_id = data["_id"];
            let ques_id_tr = createTr();
            let ques_id_1 = createTd();
            ques_id_1.text("问题ID");
            ques_id_1.css("width", "7%");
            let ques_id_2 = createTd();
            ques_id_2.text(ques_id);
            ques_id_tr.append(ques_id_1);
            ques_id_tr.append(ques_id_2);
            table.append(ques_id_tr);

            // 创建问题描述
            let que_des = data['q_decribe'];
            let que_des_tr = createTr();
            let que_des_1 = createTd();
            let que_des_2 = createTd();
            que_des_1.text("问题描述");
            que_des_2.text(que_des);
            que_des_tr.append(que_des_1);
            que_des_tr.append(que_des_2);
            table.append(que_des_tr);

            // 创建问题内容
            let que_cont = data['q_name'];
            let que_cont_tr = createTr();
            let que_cont_1 = createTd();
            let que_cont_2 = createTd();
            que_cont_1.text("问题内容");
            que_cont_2.text(que_cont);
            que_cont_tr.append(que_cont_1);
            que_cont_tr.append(que_cont_2);
            table.append(que_cont_tr);

            // 创建问题标签
            let que_tag = data['q_tag'];
            let que_tg_tr = createTr();
            let que_tg_1 = createTd();
            let que_tg_2 = createTd();
            que_tg_1.text("问题标签");
            que_tg_2.text(que_tag);
            que_tg_tr.append(que_tg_1);
            que_tg_tr.append(que_tg_2);
            table.append(que_tg_tr);

            // 创建人以及创建时间
            let que_create_user = data['create_user'];
            let que_create_time = data['create_time'];
            let que_create_tr = createTr();
            let que_create_1 = createTd();
            let que_create_2 = createTd();
            que_create_1.text("创建信息");
            que_create_2.text('创建人：' + que_create_user + "   创建时间：" + que_create_time);
            que_create_tr.append(que_create_1);
            que_create_tr.append(que_create_2);
            table.append(que_create_tr);

            let i = 1;
            // 答案
            answers.forEach((sing_ans)=>{
                let space_tr = createTr();
                let space_td = createTd();
                space_td.css("font-weight", '900');
                space_td.css("color", 'coral');
                space_td.text("答案 " + (i++));
                space_tr.append(space_td);
                let space_td_ = createTd();
                space_tr.append(space_td_);
                table.append(space_tr);
                let ans_cont = sing_ans["content"];
                let ans_cont_tr = createTr();
                let ans_cont_1 = createTd();
                let ans_cont_2 = createTd();
                ans_cont_1.text("答案内容");
                ans_cont_2.text(ans_cont);
                ans_cont_tr.append(ans_cont_1);
                ans_cont_tr.append(ans_cont_2);
                table.append(ans_cont_tr);
                let ans_create_user = sing_ans['create_user'];
                let ans_create_time = sing_ans['create_time'];
                let ans_create_tr = createTr();
                let ans_create_1 = createTd();
                let ans_create_2 = createTd();
                ans_create_1.text("创建信息");
                ans_create_2.text('创建人：' + ans_create_user + "   创建时间：" + ans_create_time);
                ans_create_tr.append(ans_create_1);
                ans_create_tr.append(ans_create_2);
                table.append(ans_create_tr);
                let ans_update = sing_ans['update_time'];
                let ans_update_tr = createTr();
                let ans_update_1 = createTd();
                let ans_update_2 = createTd();
                ans_update_1.text("更新时间");
                ans_update_2.text(ans_update);
                ans_update_tr.append(ans_update_1);
                ans_update_tr.append(ans_update_2);
                table.append(ans_update_tr);
            })


            // for(let k in data){
            //     console.log(k);
            //     // 创建行
            //     let row = $(document.createElement("tr"));
            //     table.append(row);
            //     // 创建列
            //     let tr_title = $(document.createElement("td"));
            //     tr_title.text(k);
            //     let tr_content = $(document.createElement("td"));
            //     tr_content.text(data[k]);
            //     table.append(tr_title);
            //     table.append(tr_content);
            // }
        },
        error: () => {
            // console.log("查找失败");
            let no_result = $(document.createElement("p"));
            no_result.text("未查询到结果，请检查输入的问题id是否正确！");
            no_result.css("margin-top", "15%");
            let no_result_div = $(document.createElement("div"));
            no_result_div.css("text-align", "center");
            no_result_div.append(no_result);
            let row = $("#row");
            row.append(no_result_div);
        }
    })
}


let input = $("#exampleInputName2");
input.change(() => {
    input.attr("value", input.val());
    // console.log(input.attr("value"));
});
let search = $("#search");
search.click(() => {
    if (input.attr("value") === "")
        alert("输入正确的问题id进行查询");
    else {
        // 先不显示
        // $("#ques_list").css("display", 'none');
        // 删除原有块
        $("#ques_list").remove();
        $("#h3").remove();
        // 传入输入的内容进行检索
        // console.log(input.attr("value"));
        display_detail(input.attr("value"));
    }
});

function createTr() {
    return $(document.createElement("tr"));
}

function createTd() {
    return $(document.createElement("td"));
}