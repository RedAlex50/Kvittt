function addImg_2(){
    document.getElementById('img_2').style.display  = "block";
    document.getElementById('img_btn_2').style.display  = "none";
    document.getElementById('img_btn_3').style.display  = "block";
}
 
function addImg_3(){
    document.getElementById('img_3').style.display  = "block";
    document.getElementById('img_btn_3').style.display  = "none";
    document.getElementById('img_btn_4').style.display  = "block";
}

function addImg_4(){
    document.getElementById('img_4').style.display  = "block";
    document.getElementById('img_btn_4').style.display  = "none";
    document.getElementById('img_btn_5').style.display  = "block";
}

function addImg_5(){
    document.getElementById('img_5').style.display  = "block";
    document.getElementById('img_btn_5').style.display  = "none";
}
function proverka(){
    el = document.getElementById('img_1').value;
    var a = el.split('\\')[2];
    alert(a);
    text = document.getElementById('text').value + '\n' + a;
    document.getElementById('text').value = text;
}