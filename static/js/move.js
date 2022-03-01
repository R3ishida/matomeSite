//アコーディオンをクリックした時の動作
property = 0
$('.button').on('click', function() {//タイトル要素をクリックしたら
    var findElm = $(this).next(".grid");//直後のアコーディオンを行うエリアを取得し
    if($(findElm).css("display")=="none"){
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
