var i = 0;

function addImg(){
    if(i == 0 && document.getElementById('img_1').value == ''){
        alert('Вы не выбрали изображение!')
    }
    else if(i == 1 && document.getElementById('img_2').value == ''){
        alert('Вы не выбрали изображение!')
    }
    else if(i == 2 && document.getElementById('img_3').value == ''){
        alert('Вы не выбрали изображение!')
    }
    else if(i == 3 && document.getElementById('img_4').value == ''){
        alert('Вы не выбрали изображение!')
    }
    else if(i == 4 && document.getElementById('img_5').value == ''){
        alert('Вы не выбрали изображение!')
    }
    else{

        if(i == 0){
            el = document.getElementById('img_1').value;
            var spl = el.split('\\')[2];
            
            title = document.getElementById('title').value;
            spl = '<img src="/media/cases/case_' + title + '/' + spl + '">'
    
            text = document.getElementById('description').value + '\n' + '\n' + spl + '\n' + '\n';
            document.getElementById('description').value = text;
        }
        else if(i == 1){
            el = document.getElementById('img_2').value;
            var spl = el.split('\\')[2];
    
            title = document.getElementById('title').value;
            spl = '<img src="/media/cases/case_' + title + '/' + spl + '">'
    
            text = document.getElementById('description').value + '\n' + '\n' + spl + '\n' + '\n';
            document.getElementById('description').value = text;
        }
        else if(i == 2){
            el = document.getElementById('img_3').value;
            var spl = el.split('\\')[2];
    
            title = document.getElementById('title').value;
            spl = '<img src="/media/cases/case_' + title + '/' + spl + '">'
    
            text = document.getElementById('description').value + '\n' + '\n' + spl + '\n' + '\n';
            document.getElementById('description').value = text;
        }
        else if(i == 3){
            el = document.getElementById('img_4').value;
            var spl = el.split('\\')[2];
    
            title = document.getElementById('title').value;
            spl = '<img src="/media/cases/case_' + title + '/' + spl + '">'
    
            text = document.getElementById('description').value + '\n' + '\n' + spl + '\n' + '\n';
            document.getElementById('description').value = text;
        }
        else if(i == 4){
            el = document.getElementById('img_5').value;
            var spl = el.split('\\')[2];
    
            title = document.getElementById('title').value;
            spl = '<img src="/media/cases/case_' + title + '/' + spl + '">'
    
            text = document.getElementById('description').value + '\n' + '\n' + spl + '\n' + '\n';
            document.getElementById('description').value = text;
        }

        document.getElementById('addImg').style.display  = "none";
    }
    

}

function showAddImg(){
    if(document.getElementById('img_1').value != ''){
        document.getElementById('img_1').style.display = "none";
        document.getElementById('img_2').style.display = "block";
        i = 1;
    }
    if((document.getElementById('img_1').value != '') && 
            (document.getElementById('img_2').value != '')){
        document.getElementById('img_2').style.display = "none";
        document.getElementById('img_3').style.display = "block";
        i = 2;
    }
    if(document.getElementById('img_1').value != '' && 
            document.getElementById('img_2').value != '' && 
            document.getElementById('img_3').value != ''){
        document.getElementById('img_3').style.display = "none";
        document.getElementById('img_4').style.display = "block";
        i = 3;
    }
    if(document.getElementById('img_1').value != '' && 
            document.getElementById('img_2').value != '' && 
            document.getElementById('img_3').value != ''&& 
            document.getElementById('img_4').value != ''){
        document.getElementById('img_4').style.display = "none";
        document.getElementById('img_5').style.display = "block";
        i = 4;
    }
    document.getElementById('addImg').style.display  = "block";
}