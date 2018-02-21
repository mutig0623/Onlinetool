function two_char(n) {
            return n >= 10 ? n : "0" + n;
        }
        
function time_fun() {
            var sec=0;
            setInterval(function () {
                sec++;
                var date = new Date(0, 0)
                date.setSeconds(sec);
                var h = date.getHours(), m = date.getMinutes(), s = date.getSeconds();
                document.getElementById("mytime").innerText = two_char(h) + ":" + two_char(m) + ":" + two_char(s);
            }, 1000);
  }        


function remindingcn(){
   if (document.getElementById("part1").style.visibility !="visible" && document.getElementById("part2").style.visibility != "visible" && document.getElementById("part3").style.visibility !="visible" && document.getElementById("part4").style.visibility != "visible") {
      window.alert("请点击 “显示介绍” 并阅读介绍");
      return false;
   }

  if (document.getElementById("part1").style.visibility !="visible" || document.getElementById("part2").style.visibility != "visible" || document.getElementById("part4").style.visibility != "visible" || document.getElementById("part3").style.visibility !="visible") {
     window.alert("请完成演示的观看！");
     return false;
   }
    else {
        return true;
     }
}

function remindingcnu(){
   if (document.getElementById("part1").style.visibility !="visible" && document.getElementById("part2up").style.visibility != "visible" && document.getElementById("part3S").style.visibility !="visible" && document.getElementById("part4").style.visibility != "visible") {
      window.alert("请点击 “显示介绍” 并阅读介绍");
      return false;
   }

  if (document.getElementById("part1").style.visibility !="visible" || document.getElementById("part2up").style.visibility != "visible" || document.getElementById("part4").style.visibility != "visible" || document.getElementById("part3S").style.visibility !="visible") {
     window.alert("请完成演示的观看！");
     return false;
   }
    else {
        return true;
     }
}

function remindingcnup(){
   if (document.getElementById("part1img").style.visibility !="visible" && document.getElementById("part2").style.visibility != "visible" && document.getElementById("part3S").style.visibility !="visible" && document.getElementById("part4").style.visibility != "visible") {
      window.alert("请点击 “显示介绍” 并阅读介绍");
      return false;
   }

  if (document.getElementById("part1img").style.visibility !="visible" || document.getElementById("part2").style.visibility != "visible" || document.getElementById("part4").style.visibility != "visible" || document.getElementById("part3S").style.visibility !="visible") {
     window.alert("请完成演示的观看！");
     return false;
   }
    else {
        return true;
     }
}

function remindingb(){
   if (document.getElementById("part2Bing").style.visibility != "visible" && document.getElementById("part3S").style.visibility !="visible" && document.getElementById("part4").style.visibility != "visible") {
      window.alert("请点击 “显示介绍” 并阅读介绍");
      return false;
   }

  if (document.getElementById("part2Bing").style.visibility != "visible" || document.getElementById("part4").style.visibility != "visible" || document.getElementById("part3S").style.visibility !="visible") {
     window.alert("请完成演示的观看！");
     return false;
   }
    else {
        return true;
     }
}

function remindingblank() {
   if (document.getElementById("part2B").style.visibility != "visible" && document.getElementById("part3S").style.visibility !="visible" && document.getElementById("part4").style.visibility != "visible") {
      window.alert("请点击 “显示介绍” 并阅读介绍");
      return false;
   }

  if (document.getElementById("part2B").style.visibility != "visible" || document.getElementById("part4").style.visibility != "visible" || document.getElementById("part3S").style.visibility !="visible") {
     window.alert("请完成演示的观看！");
     return false;
   }
    else {
        return true;
     }
}


function remindingcnt(){
   if (document.getElementById("part1").style.visibility !="visible" && document.getElementById("part2").style.visibility != "visible" && document.getElementById("part3T").style.visibility !="visible" && document.getElementById("part4T").style.visibility != "visible") {
      window.alert("请点击 “显示介绍” 并阅读介绍");
      return false;
   }

  if (document.getElementById("part1").style.visibility !="visible" || document.getElementById("part2").style.visibility != "visible" || document.getElementById("part4T").style.visibility != "visible" || document.getElementById("part3T").style.visibility !="visible") {
     window.alert("请完成演示的观看！");
     return false;
   }
    else {
        return true;
     }
}

function remindingcnc(){
   if (document.getElementById("part1tag").style.visibility !="visible" && document.getElementById("part2tag").style.visibility != "visible" && document.getElementById("part3Stag").style.visibility !="visible" && document.getElementById("part4tag").style.visibility != "visible") {
      window.alert("请点击 “显示介绍” 并阅读介绍");
      return false;
   }

  if (document.getElementById("part1tag").style.visibility !="visible" || document.getElementById("part2tag").style.visibility != "visible" || document.getElementById("part4tag").style.visibility != "visible" || document.getElementById("part3Stag").style.visibility !="visible") {
     window.alert("请完成演示的观看！");
     return false;
   }
    else {
        return true;
     }
}

function remindingcncloud() {
    if (document.getElementById("part1cloud").style.visibility !="visible" && document.getElementById("part2cloud").style.visibility != "visible" && document.getElementById("part3S").style.visibility !="visible" && document.getElementById("part4").style.visibility != "visible") {
      window.alert("请点击 “显示介绍” 并阅读介绍");
      return false;
   }

  if (document.getElementById("part1cloud").style.visibility !="visible" || document.getElementById("part2cloud").style.visibility != "visible" || document.getElementById("part4").style.visibility != "visible" || document.getElementById("part3S").style.visibility !="visible") {
     window.alert("请完成演示的观看！");
     return false;
   }
    else {
        return true;
     }
}

function remindingen() {
   if (document.getElementById("Eenpart1").style.visibility !="visible" && document.getElementById("Eenpart2").style.visibility != "visible" && document.getElementById("Eenpart3").style.visibility !="visible" && document.getElementById("Eenpart4").style.visibility != "visible") {
      window.alert("Please watch the show!");
      return false;
    }

    if (document.getElementById("Eenpart1").style.visibility !="visible" || document.getElementById("Eenpart2").style.visibility != "visible" || document.getElementById("Eenpart4").style.visibility != "visible" || document.getElementById("Eenpart3").style.visibility !="visible") {
     window.alert("Please finish the watching!");
     return false;
    }
    else {
        return true;
     }
}

function remindingenE() {
   if (document.getElementById("enpart1").style.visibility !="visible" && document.getElementById("enpart2").style.visibility != "visible" && document.getElementById("enpart3").style.visibility !="visible" && document.getElementById("enpart4").style.visibility != "visible") {
      window.alert("Please watch the show!");
      return false;
    }

    if (document.getElementById("enpart1").style.visibility !="visible" || document.getElementById("enpart2").style.visibility != "visible" || document.getElementById("enpart4").style.visibility != "visible" || document.getElementById("enpart3").style.visibility !="visible") {
     window.alert("Please finish the watching!");
     return false;
    }
    else {
        return true;
     }
}

function remindingenblank() {
   if (document.getElementById("Eenpart2").style.visibility != "visible" && document.getElementById("Eenpart3").style.visibility !="visible" && document.getElementById("Eenpart4").style.visibility != "visible") {
      window.alert("Please watch the show!");
      return false;
    }

    if (document.getElementById("Eenpart2").style.visibility != "visible" || document.getElementById("Eenpart4").style.visibility != "visible" || document.getElementById("Eenpart3").style.visibility !="visible") {
     window.alert("Please finish the watching!");
     return false;
    }
    else {
        return true;
     }
}

function remindingenb() {
    if (document.getElementById("enpart2").style.visibility != "visible" && document.getElementById("enpart3").style.visibility !="visible" && document.getElementById("enpart4").style.visibility != "visible") {
      window.alert("Please watch the show!");
      return false;
    }

    if (document.getElementById("enpart2").style.visibility != "visible" || document.getElementById("enpart4").style.visibility != "visible" || document.getElementById("enpart3").style.visibility !="visible") {
     window.alert("Please finish the watching!");
     return false;
    }
    else {
        return true;
     }
}

function removebutton(){
    document.getElementById("showbutttest").style.visibility = "hidden";
    document.getElementById("part1").style.visibility = "visible";
}

function removebuttontop(){
    document.getElementById("showbutton").style.visibility = "hidden";
    document.getElementById("part1").style.visibility = "visible";
}

function removebuttontag(){
    document.getElementById("showbutttest").style.visibility = "hidden";
    document.getElementById("part1tag").style.visibility = "visible";
}
function removebuttoncloud(){
     document.getElementById("showbutttest").style.visibility = "hidden";
    document.getElementById("part1cloud").style.visibility = "visible";
}

function removebuttonimg(){
    document.getElementById("showbutttest").style.visibility = "hidden";
    document.getElementById("part1img").style.visibility = "visible";
}

function removebuttonb(){
    document.getElementById("showbutttest").style.visibility = "hidden";
    document.getElementById("part2B").style.visibility = "visible";
}

function removebuttonbig() {

    document.getElementById("showbig").style.visibility = "hidden";
}

function removebuttonbiging(){
    document.getElementById("showbutttest").style.visibility = "hidden";
    document.getElementById("part2Bing").style.visibility = "visible";
}



function showpart2(){
    document.getElementById("part2").style.visibility = "visible";
    document.getElementById("pbutton1").style.display = "none";
}

function showpart2up(){
    document.getElementById("part2up").style.visibility = "visible";
    document.getElementById("pbutton1").style.display = "none";
}

function showpart2tag(){
    document.getElementById("part2tag").style.visibility = "visible";
    document.getElementById("pbutton1").style.display = "none";
}

function showpart2cloud(){
    document.getElementById("part2cloud").style.visibility = "visible";
    document.getElementById("pbutton1").style.display = "none";
}
function showpart4(){
    document.getElementById("part4").style.visibility = "visible";
    document.getElementById("pbutton2").style.display = "none";
}

function showpart4tag(){
    document.getElementById("part4tag").style.visibility = "visible";
    document.getElementById("pbutton2").style.display = "none";
}

function showpart4T(){
    document.getElementById("part4T").style.visibility = "visible";
    document.getElementById("pbutton2").style.display = "none";
}

function showpart3(){
    document.getElementById("part3").style.display = "block";
    document.getElementById("pbutton3").style.display = "none";
}

function showpart3T(){
    document.getElementById("part3T").style.visibility = "visible";
    document.getElementById("pbutton3").style.display = "none";
}

function showpart3S(){
    document.getElementById("part3S").style.visibility = "visible";
    document.getElementById("pbutton3").style.display = "none";
}

function showpart3Stag(){
    document.getElementById("part3Stag").style.visibility = "visible";
    document.getElementById("pbutton3").style.display = "none";
}

function removebuttonen(){
    document.getElementById("showbutttest").style.visibility = "hidden";
    document.getElementById("Eenpart1").style.visibility = "visible";
    window.factor++;
}

function removebuttonenE(){
    document.getElementById("showbutttest").style.visibility = "hidden";
    document.getElementById("Eenpart2").style.visibility = "visible";
    window.factor++;
}

function removebuttonentop(){
    document.getElementById("showbutttest").style.visibility = "hidden";
    document.getElementById("enpart1").style.visibility = "visible";
    window.factor++;
}

function showpart2en(){
    document.getElementById("enpart2").style.visibility = "visible";
    document.getElementById("enpbutton1").style.visibility = "visible";
}

function showpart2enE(){
    document.getElementById("Eenpart2").style.visibility = "visible";
    document.getElementById("enpbutton1").style.visibility = "visible";
}

function removebuttonenblank() {
     document.getElementById("showbutttest").style.visibility = "hidden";
    document.getElementById("Eenpart2").style.visibility = "visible";
    window.factor++;
}

function removebuttonenbl() {
     document.getElementById("showbutttest").style.visibility = "hidden";
    document.getElementById("enpart2").style.visibility = "visible";
    window.factor++;
}
function showpart4en(){
    document.getElementById("enpart4").style.visibility = "visible";
    document.getElementById("enpbutton2").style.display = "none";
}

function showpart4enE(){
    document.getElementById("Eenpart4").style.visibility = "visible";
    document.getElementById("enpbutton2").style.display = "none";
}

function showpart3en() {
    document.getElementById("enpart3").style.visibility = "visible";
    document.getElementById("enpbutton3").style.display = "none";
    }

function showpart3enE() {
    document.getElementById("Eenpart3").style.visibility = "visible";
    document.getElementById("enpbutton3").style.display = "none";
}

function checknull() {
    var arr=document.getElementsByName("pronu");
    var ear = false;
    for(var i=0;i<arr.length;i++) {
        if(arr[i].checked) {
           return true;
           ear = true;
           break;
        }
    }
    if(ear ==false ){
        document.getElementById("pronuname").style.border ="green solid ";
        document.getElementById("pronuname").style.backgroundColor ="red";
        return false;
    }
}

