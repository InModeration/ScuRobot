window.onload = function () {
    var id = getUrlParam(window.location.href);
    console.log(id);

    let aim_url = "http://scuker.xyz/q_and_a";

    let json_data = new FormData();
    json_data.append("_id",id);

    $.ajax({
        type:"POST",
        dataType: "json",
        url: aim_url,
        //contentType : "application/json",
        data: json_data,
        processData: false,
        contentType: false,
        success:function (data) {
            print_question(data[0]);
            print_answers(data[0]['answers']);
        }
    });
};

function getUrlParam(name) {
    var good_id1 = name.match(/\?id=(\S*)/)[1];
    //alert(good_id1);
    return good_id1;
}

function print_question(data) {
    let title = document.getElementById("question_name");
    let date = document.getElementById("push_date");
    let tag = document.getElementById("tag");
    let num_answer = document.getElementById("comment_num");
    let description = document.getElementById("description");

    title.innerHTML = "<a href=\"#\">" + data['q_name']+ "</a>";
    date.innerText = data['create_time'];

    for(let i in data['q_tag']) {
        let DomObj = document.createElement("a");
        DomObj.setAttribute('class', "btn btn-mini");
        DomObj.href = "#";
        DomObj.innerText = data['q_tag'][i];
        tag.appendChild(DomObj);
    }

    num_answer.innerText = data['answers'].length + "   answers";
    description.innerText = data['q_decribe'];
}


let com_html_2_1 = "<a href=\"#\"><img alt=\"\" src=\"http://0.gravatar.com/avatar/2df5eab0988aa5ff219476b1d27df755?s=60&amp;d=http%3A%2F%2F0.gravatar.com%2Favatar%2Fad516503a11cd5ca435acc9bb6523536%3Fs%3D60&amp;r=G\" class=\"avatar avatar-60 photo\" height=\"60\" width=\"60\"></a><div class=\"comment-meta\"><h5 class=\"author\">";
let com_html_2_2 = "<cite class=\"fn\">";
let com_html_3 = "<a href=\"#\" rel=\"external nofollow\" class=\"url\">";
// 名字
let com_html_4 = "</a></cite><a class=\"comment-reply-link\" href=\"#\">的答案";
let com_html_5 = "</a></h5> <p class=\"date\"><a href=\"#\"><time datetime=\"2013-02-26T13:20:14+00:00\">";
// 时间
let com_html_6 = "</time> </a> </p></div><!-- end .comment-meta --><div class=\"comment-body\"><p class=\"info\">";
// 答案内容
let com_html_7 = "</p></div><!-- end of comment-body --></article><!-- end of comment -->";

function print_answers(data) {
    let comment_div = document.getElementById("li-comment");

    let i = 0;
    for(i = 0;i<data.length;i++){
        let DomObj = document.createElement("article");
        DomObj.id = "comment-" + i;
        let content_html = '';

        content_html += com_html_2_1 + com_html_2_2;
        content_html += com_html_3 +data[i]['create_user'];
        content_html += com_html_4 + com_html_5;
        content_html += data[i]['create_time'];
        content_html += com_html_6;
        content_html += data[i]['content'];
        content_html += com_html_7;
        DomObj.innerHTML = content_html;

        comment_div.appendChild(DomObj);
    }

};

