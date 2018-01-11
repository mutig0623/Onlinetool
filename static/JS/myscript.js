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
        }
    if(num == 2){
        document.getElementById("same2").value="";
        document.getElementById("sam2").style.display="none";
        }
    if(num == 3){
        document.getElementById("same3").value="";
        document.getElementById("sam3").style.display="none";
        }
    }


function two_char(n) {
            return n >= 10 ? n : "0" + n;
        }
        
function time_funch() {
    document.getElementById("same1").innerText = ""; 
    document.getElementById("same2").innerText = "";
    document.getElementById("same3").innerText = "";
    var sec=5;
    setInterval(function () {
        sec--;
        var date = new Date(0, 0)
        date.setSeconds(sec);
        var m = date.getMinutes(), s = date.getSeconds();
        document.getElementById("mytime").innerText = m + " 分 " + two_char(s) + "秒";
    }, 1000);
        setTimeout("Repeated()", 3000 )
}

function Repeated() {
     var sec=3;
    setInterval(function () {
        sec--;
        var date = new Date(0, 0)
        date.setSeconds(sec);
        var m = date.getMinutes(), s = date.getSeconds();
        document.getElementById("mytime").innerText = m + " 分 " + two_char(s) + "秒";
    }, 1000);
    document.getElementById('queren').click();
}

function time_funen() {
    document.getElementById("same1").innerText = ""; 
    document.getElementById("same2").innerText = "";
    document.getElementById("same3").innerText = "";
    var sec=300;
    setInterval(function () {
        sec--;
        var date = new Date(0, 0)
        date.setSeconds(sec);
        var m = date.getMinutes(), s = date.getSeconds();
        document.getElementById("mytime").innerText = m + " min " + two_char(s) + " sec ";
    }, 1000);
  }  

function addtech(obj){   
    var cba = obj.previousSibling;
    if(document.getElementById("sam1").style.display!="block"){
        document.getElementById("same1").value = cba.innerText;
        document.getElementById("sam1").style.display ="block";
        document.getElementById("same11").style.display = "block";        
    }
    else if(document.getElementById("sam2").style.display!="block"){
        document.getElementById("same2").value = cba.innerText;
        document.getElementById("sam2").style.display ="block";
        document.getElementById("same22").style.display = "block";  
        }
    else if(document.getElementById("sam3").style.display!="block"){
        document.getElementById("same3").value = cba.innerText;
        document.getElementById("sam3").style.display ="block";
        document.getElementById("same33").style.display = "block";  
        }
    else{
        window.alert("超过三个了,\n 请删除一个再选择！");
        }   

}

function addtechen(obj){   
    var cba = obj.previousSibling;
    if(document.getElementById("sam1").style.display!="block"){
        document.getElementById("same1").value = cba.innerText;
        document.getElementById("sam1").style.display ="block";
        document.getElementById("same11").style.display = "block";        
    }
    else if(document.getElementById("sam2").style.display!="block"){
        document.getElementById("same2").value = cba.innerText;
        document.getElementById("sam2").style.display ="block";
        document.getElementById("same22").style.display = "block";  
        }
    else if(document.getElementById("sam3").style.display!="block"){
        document.getElementById("same3").value = cba.innerText;
        document.getElementById("sam3").style.display ="block";
        document.getElementById("same33").style.display = "block";  
        }
    else{
        window.alert("You have select more then \nthree techniques, please \ndelete one or reselect again!");
        }   

}

function addtechde(obj){   
    var cba = obj.previousSibling;
    if(document.getElementById("sam1").style.display!="block"){
        document.getElementById("same1").innerText = cba.innerText;
        document.getElementById("sam1").style.display ="block";
        document.getElementById("same11").style.display = "block";        
    }
    else if(document.getElementById("sam2").style.display!="block"){
        document.getElementById("same2").innerText = cba.innerText;
        document.getElementById("sam2").style.display ="block";
        document.getElementById("same22").style.display = "block";  
        }
    else if(document.getElementById("sam3").style.display!="block"){
        document.getElementById("same3").innerText = cba.innerText;
        document.getElementById("sam3").style.display ="block";
        document.getElementById("same33").style.display = "block";  
        }
    else{
        window.alert("More than three options, \nplease delete one and choice \nagain!");
        }        
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

            var alertdiv = '<div id="alertdiv" style="position:absolute; width:auto; display:none ; overflow:hidden; padding:10px 10px 8px; top: 50%; left: 50%; text-align:center; line-height:22px; background-color:#A9A9A9; border-radius: 17px; border:1px solid #ccc">' + text + '<br /><input type="submit" name="button" id="button" value="确定" style="margin-top:8px; width:90%;"onclick="$(this).parent().remove(); " /></div>';
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