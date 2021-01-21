      $.getJSON("/homer",(response)=>{
    $("#so").html(hook(response));
    err.error('off');
    lazyload()
  })
//скрипт requstsнагрузка сайта

function hook(response){
$("#len").html("<h1>Найдено "+response[0].length+" обектов</h1>");
  html  = ''
  response.forEach((el)=>{
    for (var i in el){
      imgst = (el[i].img.length == 0) ? 'image_not.png' : el[i].img
      tit = err.cutter(el[i].name,8)
      slasser = err.cutter(el[i].opis,8)

      html += `
        <div class="col-lg-4 col-md-6 col-sm-7">
             <div class="card card__item" style="width: 18rem;">
              <div class='ait loading' style="width:288px; height:200px;">
              <img id='lazy' style="object-fit: cover;
          width: 288px;
          height: 200px;" class="card-img-top" data-src="/media/`+imgst+`" alt="Card image cap">
              </div>
               <div class="card-body">
          <h5 class="card-title">`+tit+`</h5>
          <div class="dropdown-divider"></div>
          <p class="card-text">`+slasser+`</p>
          <a id='per' href=`+el[i].typeOf+`/`+el[i].id+ ` class="btn btn-danger" id='rdenid' >Подробности</a>
          <a href="tel:`+el[i].phonnum+`" class="btn btn-success">Позвонить</a>
        </div>
             </div>
          </div>`
    }
  })
  return html
}

$(document).ready(()=>{
  pr = {'Дом':'/house','Квартира':'/apartament'}
  let fil
  
  $('#sen').click(()=>{
    if ($("#utt").val() != '',$("#duu").val() != '')
      (err.check_input($("#utt"),$("#duu")) != false) ? fil = true : err.error('on','Вы указали не верную цену');
    
    if($('#oni').text() == 'Дом' || $("#oni").text() == 'Квартира'){ 

      if ($("#navbarDropdown").text() == 'Все' || $("#navbarDropdown").text() == 'Аренда' || $("#navbarDropdown").text() == 'Покупка' || $("#navbarDropdown").text() == 'Продажа'){
        
        err.error('off');
        $.ajax({
          type:"POST",
          url: pr[$('#oni').text()],
          data:{
            addr:($("#navbarDropdown2").text() === "Все" ? 'False' : $("#navbarDropdown2").text()),
            utt:(fil==true ? $("#utt").val():'False'),
            dutt:(fil==true ? $("#duu").val():'False'),
            csrfmiddlewaretoken:$("input[name=csrfmiddlewaretoken]").val(),
            type:$("#navbarDropdown").text()
          },
          success:(response)=>{
            
            $('#so').html(hook(response));
            
            lazyload()
          }
        })
      }else{
        err.error('on','Ошибка Вы не выбрали тип сделки');
      }
    }else
      err.error('on','Ошибка Вы не выбрали тип обекта');
  })
})

function lazyload (){
  const placeholder = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z8BQDwAEhQGAhKmMIQAAAABJRU5ErkJggg=="
  const targets = document.querySelectorAll("img");
  targets.forEach(target => {
    target.src = placeholder
  });
  const options = {
    root: null,
    rootMargin: '0px' ,
    threshold: 0.03
  };
  const loadImage = function(entries, observer)
  {
    entries.forEach(entry => {
    if (entry.isIntersecting && entry.target.parentNode.classList.contains('loading')){
    entry.target.src = entry.target.getAttribute('data-src');
      entry.target.onload = () => {
      entry.target.parentNode.classList.remove('loading');
      entry.target.removeAttribute('data-src');
        };
      }
    });
  };
  const observer = new IntersectionObserver(loadImage, options);
  targets.forEach(target => {
  observer.observe(target);
    });
  }
  
class ErrorMessages{
  error(args,text=''){
    $('.col').html('<div class="alert alert-danger al" id="err" role="alert"></div>');
    (args == 'off') ? $("#err").hide():$("#err").show();
    $("#error_messeg").remove();$('#err').html("<p>"+text+"</p>");
  }
  cutter(zna,z){
    let res = '';

    if (zna.split(' ').length>2){
      let a = zna.split(' ');
      for(var i = 0;i<z;++i)
        if (a[i] != undefined)
          res += a[i]+' ';
    }else{
      let a = zna.split('');
        for(var i = 0;i<z;++i)
          if (a[i] != undefined)
            res+=a[i];
    }

    return res+='...'
  }
  check_input(o,d){
    let ar = (parseInt(o.val())); let am = (parseInt(d.val())); 
    return (isNaN(ar) ==  false && isNaN(am) == false) ? true : false;
  }
}

var err = new ErrorMessages();