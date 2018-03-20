 'use strict';
function changeImg(obj,todo){
    if(todo == 1){
    obj.src= "{% static 'img/chacha2.png'%}"; //todo是1就是换图片
        }
    if(todo == 2){
    obj.src= "{% static 'img/chacha3.png'%}"; //是2就换回图片
        }
    }

function Delete(num){
    if(num == 1){
        document.getElementById("same1").value="";
        document.getElementById("sam1").style.display="none";
        if(document.getElementById("same1").value =="" &&  document.getElementById("same2").value =="" && document.getElementById("same3").value =="")
        {
            document.getElementById("butt-next-detail").style.visibility = "hidden";
    }
        }
    if(num == 2){
        document.getElementById("same2").value="";
        document.getElementById("sam2").style.display="none";
        if(document.getElementById("same1").value =="" &&  document.getElementById("same2").value =="" && document.getElementById("same3").value =="")
        {
            document.getElementById("butt-next-detail").style.visibility = "hidden";
    }
        }
    if(num == 3){
        document.getElementById("same3").value="";
        document.getElementById("sam3").style.display="none";
        if(document.getElementById("same1").value =="" &&  document.getElementById("same2").value =="" && document.getElementById("same3").value =="")
        {
            document.getElementById("butt-next-detail").style.visibility = "hidden";
    }
        }
    }

function two_char(n) {
            return n >= 10 ? n : "0" + n;
}

function time_funch() {
    document.getElementById("same1").value="";
    document.getElementById("same2").value="";
    document.getElementById("same3").value="";
      var sec=300;
      setInterval(function () {
        sec--;
        var date = new Date(0, 0);
        date.setSeconds(sec);
        var m = date.getMinutes(), s = date.getSeconds();
        document.getElementById("mytime").innerHTML = m + " 分 " + two_char(s) + " 秒";
    }, 1000);
        setTimeout("peatedch()", 240000 );
  }

function peatedch(){
    window.alert("您还有1分钟时间！")
    var sec=60;
    setInterval(function () {
        sec--;
        var date = new Date(0, 0);
        date.setSeconds(sec);
        var m = date.getMinutes(), s = date.getSeconds();
        document.getElementById("mytime").innerHTML = m + " 分 " + two_char(s) + " 秒";
    }, 1000);
        setTimeout("Repeatedch()", 60000);
  }

function Repeatedch() {
    if(document.getElementById("same1").value == "" && document.getElementById("same2").value == "" && document.getElementById("same2").value == "")
    {
        document.getElementById("same1").value = "none1";
        document.getElementById("same2").value = "none2";
        document.getElementById("same3").value = "none3";
        document.getElementById("sam1").style.display ="block"
        document.getElementById("sam2").style.display ="block"
        document.getElementById("sam3").style.display ="block"
        document.getElementById('butt-next').click();
    }
    else{
        document.getElementById('butt-next').click();
    }
}


function time_funen() {
    document.getElementById("same1").value = "";
    document.getElementById("same2").value = "";
    document.getElementById("same3").value = "";
    var sec=300;
      setInterval(function () {
        sec--;
        var date = new Date(0, 0);
        date.setSeconds(sec);
        var m = date.getMinutes(), s = date.getSeconds();
        document.getElementById("mytime").innerHTML =  m  + " min " + two_char(s) + " sec";
    }, 1000);
        setTimeout("peateden()", 240000 );
}

function peateden() {
    window.alert("You have only one \n minute left!")
    var sec=60;
      setInterval(function () {
        sec--;
        var date = new Date(0, 0);
        date.setSeconds(sec);
        var s = date.getSeconds();
        document.getElementById("mytime").innerHTML = "0" + " min " + two_char(s) + " sec";
    }, 1000);
        setTimeout("Repeateden()", 60000);
}

function Repeateden() {
     if(document.getElementById("same1").value == "" && document.getElementById("same2").value == "" && document.getElementById("same2").value == "")
        {
            document.getElementById("same1").value = "none1";
            document.getElementById("same2").value = "none2";
            document.getElementById("same3").value = "none3";
            document.getElementById("sam1").style.display ="block"
            document.getElementById("sam2").style.display ="block"
            document.getElementById("sam3").style.display ="block"
            document.getElementById('butt-next').click();
    }
    else{
        document.getElementById('butt-next').click();
    }
}

function time_funde() {
    document.getElementById("same1").value = "";
    document.getElementById("same2").value = "";
    document.getElementById("same3").value = "";
     if(document.getElementById("sam1").style.display =="none" && document.getElementById("sam2").style.display =="none" && document.getElementById("sam3").style.display =="none"){
        document.getElementById("butt-next-detail").style.visibility = "hidden";
    }
      var sec=300;
      setInterval(function () {
        sec--;
        var date = new Date(0, 0)
        date.setSeconds(sec);
        var m = date.getMinutes(), s = date.getSeconds();
        document.getElementById("mytime").innerHTML = m +  " min " +  two_char(s) + " sec";
    }, 1000);
        setTimeout("peatedde()", 240000 );
}

function peatedde() {
    window.alert("Sie haben nur ein \n Miunte!")
    var sec=60;
    setInterval(function () {
    sec--;
    var date = new Date(0, 0)
    date.setSeconds(sec);
    var m = date.getMinutes(), s = date.getSeconds();
    document.getElementById("mytime").innerHTML = "0" +  " min " + two_char(s) + " sec";
    }, 1000);
        setTimeout("Repeatedde()", 60000);
}

function Repeatedde() {
    if(document.getElementById("same1").value == "" && document.getElementById("same2").value == "" && document.getElementById("same2").value == "")
    {
        document.getElementById("same1").value = "none1";
        document.getElementById("same2").value = "none2";
        document.getElementById("same3").value = "none3";
        document.getElementById("sam1").style.display ="block"
        document.getElementById("sam2").style.display ="block"
        document.getElementById("sam3").style.display ="block"
        document.getElementById('butt-next').click();
    }
    else{
        document.getElementById('butt-next').click();
    }
}

function addtech(obj){   
    var cba = obj.previousSibling;
    if(document.getElementById("sam1").style.display!="block"){
        document.getElementById("same1").value = cba.innerHTML;
        document.getElementById("sam1").style.display ="block";
        document.getElementById("same11").style.display = "block";
        document.getElementById("butt-next-detail").style.visibility = "visible";
    } else if(document.getElementById("sam1").style.display =="block"){
        if(document.getElementById("same1").value == cba.innerHTML)
            { alert("您的选择重复了！");}
        else if(document.getElementById("sam2").style.display!="block"){
            document.getElementById("same2").value = cba.innerText;
            document.getElementById("sam2").style.display ="block";
            document.getElementById("same22").style.display = "block";
        }else if(document.getElementById("sam2").style.display =="block"){
            if(document.getElementById("same2").value == cba.innerHTML)
            { alert("您的选择重复了！");}
            else if(document.getElementById("sam3").style.display!="block"){
                document.getElementById("same3").value = cba.innerText;
                document.getElementById("sam3").style.display ="block";
                document.getElementById("same33").style.display = "block";
            }else if(document.getElementById("sam3").style.display=="block"){
                if(document.getElementById("same3").value == cba.innerHTML){
                alert("您的选择重复了！");
            }

    else{
        window.alert("超过三个了,\n 请删除一个再选择！");
        }}}}
}

function addtechen(obj){   
    var cba = obj.previousSibling;
    if(document.getElementById("sam1").style.display!="block"){
        document.getElementById("same1").value = cba.innerHTML;
        document.getElementById("sam1").style.display ="block";
        document.getElementById("same11").style.display = "block";
        document.getElementById("butt-next-detail").style.visibility = "visible";
    } else if(document.getElementById("sam1").style.display =="block"){
        if(document.getElementById("same1").value == cba.innerHTML)
            { alert("Your choice is repeated!");}
        else if(document.getElementById("sam2").style.display!="block"){
            document.getElementById("same2").value = cba.innerText;
            document.getElementById("sam2").style.display ="block";
            document.getElementById("same22").style.display = "block";
        }else if(document.getElementById("sam2").style.display =="block"){
            if(document.getElementById("same2").value == cba.innerHTML)
            { alert("Your choice is repeated!");}
            else if(document.getElementById("sam3").style.display!="block"){
                document.getElementById("same3").value = cba.innerText;
                document.getElementById("sam3").style.display ="block";
                document.getElementById("same33").style.display = "block";
            }else if(document.getElementById("sam3").style.display=="block"){
                if(document.getElementById("same3").value == cba.innerHTML){
                alert("Your choice is repeated!");
            }
            else{
                window.alert("You have select more then \nthree techniques, please \ndelete one or reselect again!");
                }}}}
}

function addtechde(obj){   
    var cba = obj.previousSibling;
     if(document.getElementById("sam1").style.display!="block"){
        document.getElementById("same1").value = cba.innerHTML;
        document.getElementById("sam1").style.display ="block";
        document.getElementById("same11").style.display = "block";
        document.getElementById("butt-next-detail").style.visibility = "visible";
    } else if(document.getElementById("sam1").style.display =="block"){
        if(document.getElementById("same1").value == cba.innerHTML)
            { alert("Ihre Wahl ist wiederholt!");}
        else if(document.getElementById("sam2").style.display!="block"){
            document.getElementById("same2").value = cba.innerText;
            document.getElementById("sam2").style.display ="block";
            document.getElementById("same22").style.display = "block";
        }else if(document.getElementById("sam2").style.display =="block"){
            if(document.getElementById("same2").value == cba.innerHTML)
            { alert("Ihre Wahl ist wiederholt!");}
            else if(document.getElementById("sam3").style.display!="block"){
                document.getElementById("same3").value = cba.innerText;
                document.getElementById("sam3").style.display ="block";
                document.getElementById("same33").style.display = "block";
            }else if(document.getElementById("sam3").style.display=="block"){
                if(document.getElementById("same3").value == cba.innerHTML){
                alert("Ihre Wahl ist wiederholt!");
            }
            else{
                window.alert("Mehr als drei Techniken \nausgewählt, bitte löschen \noder erneut auswählen!");
                    }}}}
}





function checkrepeat(){
  if(document.getElementById("same1").value == "" && document.getElementById("same2").value == "" 
    && document.getElementById("same3").value == "")
    {
        window.alert("请至少选择一个技术！");
    } 

  else {
    if(
        (document.getElementById("same1").innerText == document.getElementById("same2").innerText && 
        document.getElementById("same1").innerText != "" && document.getElementById("same2").innerText != "")|| 
        (document.getElementById("same2").innerText == document.getElementById("same3").innerText && 
        document.getElementById("same2").innerText != "" && document.getElementById("same3").innerText != "") ||
        (document.getElementById("same1").innerText == document.getElementById("same3").innerText && 
        document.getElementById("same1").innerText != "" && document.getElementById("same3").innerText != "") 
    ){
         window.alert("您的选择重复了，请删除\n重复的选择再重新选择！");
      }
    else{
        window.location.href='TaskDetailtwo.html';
    }
  }
}

function checkrepeaten(){
    if(document.getElementById("same1").innerText == "" && document.getElementById("same2").innerText == "" 
    && document.getElementById("same3").innerText == "")
    {
         window.alert("Please select at least \none Technique!");
    } 

  else {
    if(
        (document.getElementById("same1").innerText == document.getElementById("same2").innerText && 
        document.getElementById("same1").innerText != "" && document.getElementById("same2").innerText != "")|| 
        (document.getElementById("same2").innerText == document.getElementById("same3").innerText && 
        document.getElementById("same2").innerText != "" && document.getElementById("same3").innerText != "") ||
        (document.getElementById("same1").innerText == document.getElementById("same3").innerText && 
        document.getElementById("same1").innerText != "" && document.getElementById("same3").innerText != "") 
    ){
         window.alert("Your choice is repeated, please \n delete the repeated choice \n and then choose again!");
      }
    else{
        window.location.href='TaskDetailtwo.html';
    }
  }
}

function showregistercn(){
    if (document.getElementById('username').value == "" || document.getElementById('username').value == "邮箱/任意名称") {
        window.alert("注册！\n 请输入您的邮箱或者\n 一个随机名称来注册本实验！");
    } 
    else{window.location.href='pre-test.html'};  
}

function showregisteren(){
     if (document.getElementById('username').value == "" || document.getElementById('username').value == "Email/Random Number") {
        window.alert("Register!\n Please enter an email address \n or a random number to register! ");
    } 
   else{
   window.location.href='pre-test.html'};
}

(function () {
        window.alert = function (text) {
            text = text.toString().replace(/\\/g, '\\').replace(/\n/g, '<br />').replace(/\r/g, '<br />');

            var alertdiv = '<div id="alertdiv" style="position:absolute; width:auto; display:none ; overflow:hidden; padding:10px 10px 8px; top: 50%; left: 50%; text-align:center; line-height:22px; background-color:#A9A9A9; border-radius: 17px; border:1px solid #ccc">' + text + '<br /><input type="submit" name="button" id="button" value="OK" style="margin-top:8px; width:90%;"onclick="$(this).parent().remove(); " /></div>';
            $(document.body).append(alertdiv);

            $("#alertdiv").css({
                "margin-left": $("#alertdiv").width() / 2 * (-1) - 20,
                "margin-top": $("#alertdiv").height() / 2 * (-1) - 20
            });

            $("#alertdiv").show(); 
            };
        }
)();

function enshow(){
    document.getElementById("intro-en").style.display = "block";
    document.getElementById("intro-ch").style.display = "none";
    document.getElementById("intro-de").style.display = "none";
    document.getElementById("butt-next").value = "Next";
}

function chshow(){
    document.getElementById("intro-en").style.display = "none";
    document.getElementById("intro-ch").style.display = "block";
    document.getElementById("intro-de").style.display = "none";
    document.getElementById("butt-next").value = "下一步";
}

function deshow(){
    document.getElementById("intro-en").style.display = "none";
    document.getElementById("intro-ch").style.display = "none";
    document.getElementById("intro-de").style.display = "block";
    document.getElementById("butt-next").value = "Nächst";
}

function check(){

    if(document.getElementById("sam1").style.display!="block" && document.getElementById("sam2").style.display!="block"
        && document.getElementById("sam3").style.display!="block"
    ){
        window.alert("请至少选择一个技术！");
         return false;
    }

    if(document.getElementById("same1").value == "" && document.getElementById("same2").value == "" 
    && document.getElementById("same3").value == "")
    {         
         window.alert("请至少选择一个技术！");
         return false;
    } 
    else {
        if(
            (document.getElementById("same1").value == document.getElementById("same2").value && 
            document.getElementById("same1").value != "" && document.getElementById("same2").value != "")|| 
            (document.getElementById("same2").value == document.getElementById("same3").value && 
            document.getElementById("same2").value != "" && document.getElementById("same3").value != "") ||
            (document.getElementById("same1").value == document.getElementById("same3").value && 
            document.getElementById("same1").value != "" && document.getElementById("same3").value != "") 
        ){
             window.alert("您的选择重复了，请删除\n重复的选择再重新选择！");
            return false
          }
        else{
           return true;
        }
  }
}

function checken(){
    if(document.getElementById("sam1").style.display!="block" && document.getElementById("sam2").style.display!="block"
        && document.getElementById("sam3").style.display!="block"
    ){
        window.alert("Please select at least \none Technique!");
         return false;
    }
    
    if(document.getElementById("same1").value == "" && document.getElementById("same2").value == "" 
    && document.getElementById("same3").value == "")
    {         
        window.alert("Please select at least \none Technique!");
        return false;
    } 
  else {
    if(
        (document.getElementById("same1").value == document.getElementById("same2").value && 
        document.getElementById("same1").value != "" && document.getElementById("same2").value != "")|| 
        (document.getElementById("same2").value == document.getElementById("same3").value && 
        document.getElementById("same2").value != "" && document.getElementById("same3").value != "") ||
        (document.getElementById("same1").value == document.getElementById("same3").value && 
        document.getElementById("same1").value != "" && document.getElementById("same3").value != "") 
    ){
        window.alert("Your choice is repeated, please \n delete the repeated choice \n and then choose again!");
        return false
      }
    else{
       return true;
    }
  }
}

function checkde(){
    if(document.getElementById("sam1").style.display!="block" && document.getElementById("sam2").style.display!="block"
        && document.getElementById("sam3").style.display!="block"
    ){
        window.alert("Bitte wählen Sie mindestens\neine Technik!");
         return false;
    }

    if(document.getElementById("same1").value == "" && document.getElementById("same2").value == ""
    && document.getElementById("same3").value == "")
    {
        window.alert("Bitte wählen Sie mindestens\neine Technik!");
        return false;
    }
  else {
    if(
        (document.getElementById("same1").value == document.getElementById("same2").value &&
        document.getElementById("same1").value != "" && document.getElementById("same2").value != "")||
        (document.getElementById("same2").value == document.getElementById("same3").value &&
        document.getElementById("same2").value != "" && document.getElementById("same3").value != "") ||
        (document.getElementById("same1").value == document.getElementById("same3").value &&
        document.getElementById("same1").value != "" && document.getElementById("same3").value != "")
    ){
        window.alert("Ihre Wahl wird wiederholt, bitte\nLöschen Sie die wiederholte Auswahl\nund dann wähle wieder!");
        return false
      }
    else{
       return true;
    }
  }
}

function repeating() {
     if(document.getElementById("repeated").innerText=""){
        document.getElementById("repeated").style.display="none";
    }
    else{
        document.getElementById("repeated").style.display="block";
    }
}

function remindingen(){
    if (window.factor == 0) {
     window.alert("Please watch the Introduction!");
     return false;
   }
   else {
      if (window.factor!=4) {
         window.alert("Please complete watching the Introduction!");
         return false;
     }
     else {
          return true;
      }
   }
}

function showtop1() {
    // event.preventDefault();
    document.getElementById("top1").style.visibility = "visible";

}

function showtop2(){
    document.getElementById("top2").style.visibility = "visible";

}

function hiddetop1() {
    document.getElementById("top1").style.visibility = "hidden";
    document.getElementById("topp").innerText="detele";
}