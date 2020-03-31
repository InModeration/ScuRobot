window.onload = function ()
{
    let aim_url = "http://scuker.xyz/q_and_a";

    $.ajax({
        type:"GET",
        dataType: "json",
        url: aim_url,
        contentType : "application/json",
        data: {"num":10},
        success:function (data) {
            print_data(data);
        }
    });

    aim_url = "http://scuker.xyz/tag";
    $.ajax({
        type:"GET",
        dataType: "json",
        url: aim_url,
        contentType : "application/json",
        data: {"num":15},
        success:function (data) {
            print_data_tag(data);
        }
    });
};

let html_1 = "<article class=\"format-standard type-post hentry clearfix\"><header class=\"clearfix\"><h3 class=\"post-title\"><a href=\"single.html";
let html_1_2 = "\">";
let html_2 = "</a> </h3> <div class=\"post-meta clearfix\"><span class=\"date\">";
let html_3 = "</span><span class=\"category\"><a href=\"#\"></a>";
let html_4 = "</span></div></header><p>";
let html_5 = "<a class=\"readmore-link\" href=\"single.html"
let html_6 = "\">Read more</a></p></article>";

function print_data(in_data) {
    let container_div = document.getElementById('article_list');
    container_div.innerHTML="";
    let len = Object.keys(in_data).length;
    for(let i =0;i<len;i++)
    {
        let html_content = "";
        html_content += html_1;
        html_content += "?id=" + in_data[i]['_id'];
        html_content += html_1_2;
        html_content += in_data[i]['q_name'];
        html_content += html_2;
        html_content += in_data[i]['create_time'];
        html_content += html_3;
        for(var j in in_data[i]['q_tag']){
            html_content += in_data[i]['q_tag'][j] + " ";
        }
        html_content += html_4;
        html_content += in_data[i]['answers'][0].content;
        html_content += html_5;
        html_content += "?id=" + in_data[i]['_id'];
        html_content += html_6;

        let DomObj = document.createElement("div");
        DomObj.style.margin = "5px";
        DomObj.innerHTML = html_content;
        container_div.appendChild(DomObj);

    }

}

function print_data_tag(in_data) {
    container_div = document.getElementById('tag_container');
    for(let i in in_data)
    {
        let DomObj = document.createElement("a");
        DomObj.setAttribute('class', "btn btn-mini");
        DomObj.href = "#";
        DomObj.innerText = in_data[i]['tag'];
        container_div.appendChild(DomObj);
    }
}

function doSub(){

    var info = new FormData();
    info.append("q_name", $("#s").val())
    console.log(info)
    $.ajax({
        type: "POST",
        url: "http://scuker.xyz/search_question",
        data: info,
        dataType : "json",
        processData: false,
        contentType: false,
        success: function(data){
            print_data(data)
        }
    });

    return false;
}

function jumplogin(){
    window.location.replace("login.html");
}