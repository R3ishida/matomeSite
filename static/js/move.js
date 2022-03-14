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
            width: "70%",
            height: "80px",
            display: "block",
        });
        $(findElm).slideToggle();//アコーディオンの上下動作
    }
});

$('.add').on('click', function () {
    $('.photo_pop').css("display", "table")
    console.log("表示しました。")
    genre_num = $(this).siblings().children()[0].textContent
    console.log("------------------------")
    console.log(genre_num)
    formElement = document.getElementsByTagName("ul")[0]
    console.log(formElement)
    addform = `<li><input type="hidden" name="genre_num" value="${genre_num}"></li>`
    formElement.insertAdjacentHTML('beforeend', addform)

    $(document).on('click', function(e) {
        if (!$(e.target).closest('.photo_pop').length && !$(e.target).closest('.add').length) {
          $('.photo_pop').fadeOut();
        }
    });
})

$('.genre_button').on('click', function () {
    $('.genre_pop').css("display", "table")
    $(document).on('click', function(e) {
        if (!$(e.target).closest('.genre_pop').length && !$(e.target).closest('.genre_button').length) {
          $('.genre_pop').fadeOut();
        }
    });
})



$('.photo_item').on('click', function() {
    $(".photo_page").css("display", "block")
    id = $(this).children().children().children()[0].textContent
    title = $(this).children().children().children()[1].textContent
    memo = $(this).children().children().children()[2].textContent
    file_path = $(this).children().children().children()[3].textContent
    photo_page = document.getElementsByClassName("photo_container")[0]
    html_code = `
    <div class="photo_holder">
        <img src="${file_path}">
    </div>
    <div class="title">${title}</div>
    <div class="memo">${memo}</div>
    <form action="/delete_photo" method="POST" enctype=multipart/form-data>
        <input type="hidden" name="photo_id" value="${id}">
        <button id="delete_button" type="submit" value="id_submit">削除</button>
    </form>
    `
    photo_page.innerHTML = html_code 
})

$('.close').on('click', function() {
    $(".photo_page").css("display", "none")
})

$('.menu_text').on('click', function() {
    genre = $(this).siblings()[0].textContent
    console.log(genre)
    html_code = `
    <form action="/delete_genre" method="POST" enctype=multipart/form-data>
        <input type="hidden" name="genre" value="${genre}">
        <button id="button" type="submit" value="id_submit">削除</button>
    </form>
    `
    delete_genre = document.getElementsByClassName("delete_genre")[0]
    delete_genre.innerHTML = html_code 
    $('.delete_genre').css("display", "table")
    
})