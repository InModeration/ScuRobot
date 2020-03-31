$.ajax({
    type:"GET",
    dataType:"json",
    url:"http://49.235.105.136/tag?num=200",
    success:(data)=>{
        let table = $("#ques_list");
        table.css("display","");
        data = data;
        let i = 1;
        data.forEach((sing_tag)=>{
            let tr = createTr();
            let td_1 = createTd();
            let td_2 = createTd();
            let td_3 = createTd();
            td_1.text(i++);
            td_2.text(sing_tag['tag']);
            td_3.text(sing_tag['num']);
            tr.append(td_1);
            tr.append(td_2);
            tr.append(td_3);
            table.append(tr);
        });
    },
    error: () => {
        // 失败则打印提示语
        let p = $(document.createElement("p"));
        p.text("词条列表加载失败，请刷新页面重试！");
        p.css("margin-top", "15%");
        p.css("text-align", "center");
        let row = $("#row");
        row.append(p);
    }
});
function createTr() {
    return $(document.createElement("tr"));
}

function createTd() {
    return $(document.createElement("td"));
}