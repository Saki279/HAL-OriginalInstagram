// スライドショー
$(function () {
  $('#js-slider-3').slick({
    arrows: true, // 前・次のボタンを表示する
    dots: true, // ドットナビゲーションを表示する
    // appendDots: $('.dots-3'), // ドットナビゲーションの生成位置を変更
    speed: 1000, // スライドさせるスピード（ミリ秒）
    slidesToShow: 1, // 表示させるスライド数
    centerMode: true, // slidesToShowが奇数のとき、現在のスライドを中央に表示する
    variableWidth: true, // スライド幅の自動計算を無効化
  });
});


// フェードイン
$(function() {
  $(window).on('scroll resize', function() {
    var setHeight = 100;
    var wHeight = $(window).height();
    var scrollTop = $(window).scrollTop();
    $('.animate').each(function() {
      var targetPosition = $(this).offset().top;
      if(scrollTop > targetPosition - wHeight + setHeight) {
        $(this).addClass('show');
      }
    })
  });
});


// ページトップリンク
//スクロールした際の動きを関数でまとめる
function PageTopAnime() {
  var scroll = $(window).scrollTop();
  if (scroll >= 100){//上から100pxスクロールしたら
    $('#page-top').removeClass('DownMove');//#page-topについているDownMoveというクラス名を除く
    $('#page-top').addClass('UpMove');//#page-topについているUpMoveというクラス名を付与
  }else{
    if($('#page-top').hasClass('UpMove')){//すでに#page-topにUpMoveというクラス名がついていたら
      $('#page-top').removeClass('UpMove');//UpMoveというクラス名を除き
      $('#page-top').addClass('DownMove');//DownMoveというクラス名を#page-topに付与
    }
  }
}

// 画面をスクロールをしたら動かしたい場合の記述
$(window).scroll(function () {
  PageTopAnime();/* スクロールした際の動きの関数を呼ぶ*/
});

// ページが読み込まれたらすぐに動かしたい場合の記述
$(window).on('load', function () {
  PageTopAnime();/* スクロールした際の動きの関数を呼ぶ*/
});


// #page-topをクリックした際の設定
$('#page-top').click(function () {
  var scroll = $(window).scrollTop(); //スクロール値を取得
  if(scroll > 0){
    $(this).addClass('floatAnime');//クリックしたらfloatAnimeというクラス名が付与
        $('body,html').animate({
            scrollTop: 0
        }, 2000,function(){//スクロールの速さ。数字が大きくなるほど遅くなる
            $('#page-top').removeClass('floatAnime');//上までスクロールしたらfloatAnimeというクラス名を除く
        }); 
  }
    return false;//リンク自体の無効化
});



bubbly({
  colorStart: '#fff4e6',
  colorStop: '#ffe9e4',
  blur: 1,
  compose: 'source-over',
  bubbleFunc:() => `hsla(${Math.random() * 50}, 100%, 50%, .3)`
});



// input要素
var fileInput = document.getElementById('example');
// changeイベントで呼び出す関数
var handleFileSelect = () => {
  var files = fileInput.files;
  for (let i = 0; i < files.length; i++) {
    console.log(files[i]);　// 1つ1つのファイルデータはfiles[i]で取得できる
  }
}
// ファイル選択時にhandleFileSelectを発火
fileInput.addEventListener('change', handleFileSelect);

function previewFile(file) {
  // プレビュー画像を追加する要素
  var preview = document.getElementById('preview');

  // FileReaderオブジェクトを作成
  var reader = new FileReader();

  // URLとして読み込まれたときに実行する処理
  reader.onload = function (e) {
    var imageUrl = e.target.result; // URLはevent.target.resultで呼び出せる
    var img = document.createElement("img"); // img要素を作成
    img.src = imageUrl; // URLをimg要素にセット
    preview.appendChild(img); // #previewの中に追加
  }

  // いざファイルをURLとして読み込む
  reader.readAsDataURL(file);
}


// // <input>でファイルが選択されたときの処理
var fileInput = document.getElementById('example');
var handleFileSelect = () => {
  var files = fileInput.files;
  for (let i = 0; i < files.length; i++) {
    previewFile(files[i]);
  }
}
fileInput.addEventListener('change', handleFileSelect);


// ファイルデータ
var file = document.getElementById("example").files[0];
// フォームデータを作成
var formData = new FormData();
// avatarというフィールド名でファイルを追加
formData.append("avatar", file);
// アップロード
fetch(送信先のURL, { method: "POST", body: formData });