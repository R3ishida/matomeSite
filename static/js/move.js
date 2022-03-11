//アコーディオンをクリックした時の動作
property = 0
$('.button').on('click', function () {//タイトル要素をクリックしたら
    var findElm = $(this).next(".grid");//直後のアコーディオンを行うエリアを取得し
    if ($(findElm).css("display") == "none") {
        $(this).animate({
            width: "100%",
            height: "80px",
            borderRadius: "0",
        });
        $(findElm).slideToggle();//アコーディオンの上下動作
    } else {
        $(this).animate({
            width: "400px",
            height: "400px",
            display: "inline-block",
        });
        $(findElm).slideToggle();//アコーディオンの上下動作
    }
});

$('.add').on('click', function () {
    $('.pop').css("display", "table")
    console.log("表示しました。")
    genre_num = $(this).siblings().children()[0].textContent
    console.log("------------------------")
    console.log(genre_num)
    formElement = document.getElementsByTagName("ul")[0]
    console.log(formElement)
    addform = `<li><input type="hidden" name="genre_num" value="${genre_num}"></li>`
    formElement.insertAdjacentHTML('beforeend', addform)

    $(document).on('click', function(e) {
        if (!$(e.target).closest('.pop').length && !$(e.target).closest('.add').length) {
          $('.pop').fadeOut();
        }
    });
})

$('button').on('click', function () {
    $('.pop').css("display", "none")
})


$('.item').on('click', function() {
    $(".photo_page").css("display", "block")
    title = $(this).children().children().children()[0].textContent
    memo = $(this).children().children().children()[1].textContent
    file_path = $(this).children().children().children()[2].textContent
    photo_page = document.getElementsByClassName("photo_container")[0]
    html_code = `
    <div class="photo_holder">
        <img src="${file_path}">
    </div>
    <div class="title">${title}</div>
    <div class="memo">${memo}</div>
    `
    photo_page.innerHTML = html_code 
})

$('.close').on('click', function() {
    $(".photo_page").css("display", "none")
})
