var a = 0;

function addImg(){
    if(a == 0 && document.getElementById('img_1').value == ''){
        alert('Вы не выбрали изображение!')
    }
    else if(a == 1 && document.getElementById('img_2').value == ''){
        alert('Вы не выбрали изображение!')
    }
    else if(a == 2 && document.getElementById('img_3').value == ''){
        alert('Вы не выбрали изображение!')
    }
    else if(a == 3 && document.getElementById('img_4').value == ''){
        alert('Вы не выбрали изображение!')
    }
    else if(a == 4 && document.getElementById('img_5').value == ''){
        alert('Вы не выбрали изображение!')
    }
    else{

        if(a == 0){
            el = document.getElementById('img_1').value;
            var b = el.split('\\')[2];
    
            b = '<img src="/media/case/' + b + '">'
    
            text = document.getElementById('description').value + '\n' + '\n' + b + '\n' + '\n';
            document.getElementById('description').value = text;
        }
        else if(a == 1){
            el = document.getElementById('img_2').value;
            var b = el.split('\\')[2];
    
            b = '<img src="/media/case/' + b + '">'
    
            text = document.getElementById('description').value + '\n' + '\n' + b + '\n' + '\n';
            document.getElementById('description').value = text;
        }
        else if(a == 2){
            el = document.getElementById('img_3').value;
            var b = el.split('\\')[2];
    
            b = '<img src="/media/case/' + b + '">'
    
            text = document.getElementById('description').value + '\n' + '\n' + b + '\n' + '\n';
            document.getElementById('description').value = text;
        }
        else if(a == 3){
            el = document.getElementById('img_4').value;
            var b = el.split('\\')[2];
    
            b = '<img src="/media/case/' + b + '">'
    
            text = document.getElementById('description').value + '\n' + '\n' + b + '\n' + '\n';
            document.getElementById('description').value = text;
        }
        else if(a == 4){
            el = document.getElementById('img_5').value;
            var b = el.split('\\')[2];
    
            b = '<img src="/media/case/' + b + '">'
    
            text = document.getElementById('description').value + '\n' + '\n' + b + '\n' + '\n';
            document.getElementById('description').value = text;
        }

        document.getElementById('addImg').style.display  = "none";
    }
    

}

function showAddImg(){
    if(document.getElementById('img_1').value != ''){
        document.getElementById('img_1').style.display = "none";
        document.getElementById('img_2').style.display = "block";
        a = 1;
    }
    if((document.getElementById('img_1').value != '') && 
            (document.getElementById('img_2').value != '')){
        document.getElementById('img_2').style.display = "none";
        document.getElementById('img_3').style.display = "block";
        a = 2;
    }
    if(document.getElementById('img_1').value != '' && 
            document.getElementById('img_2').value != '' && 
            document.getElementById('img_3').value != ''){
        document.getElementById('img_3').style.display = "none";
        document.getElementById('img_4').style.display = "block";
        a = 3;
    }
    if(document.getElementById('img_1').value != '' && 
            document.getElementById('img_2').value != '' && 
            document.getElementById('img_3').value != ''&& 
            document.getElementById('img_4').value != ''){
        document.getElementById('img_4').style.display = "none";
        document.getElementById('img_5').style.display = "block";
        a = 4;
    }
    document.getElementById('addImg').style.display  = "block";
}