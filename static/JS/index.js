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
   if (document.getElementById("part1").style.display !="block" && document.getElementById("part2").style.display != "block" && document.getElementById("part3").style.display !="block" && document.getElementById("part4").style.display != "block") {
      window.alert("请多花只有一点点时间，观看工具演示！");
      return false;
   }

  if (document.getElementById("part1").style.display !="block" || document.getElementById("part2").style.display != "block" || document.getElementById("part4").style.display != "block" || document.getElementById("part3").style.display !="block") {
     window.alert("请完成演示的观看！");
     return false;
   }
    else {
        return true;
     }
}

function remindingb () {

}

function remindingen() {
   if (document.getElementById("enpart1").style.display !="block" && document.getElementById("enpart2").style.display != "block" && document.getElementById("enpart3").style.display !="block" && document.getElementById("enpart4").style.display != "block") {
      window.alert("Please watch the show!");
      return false;
    }

    if (document.getElementById("enpart1").style.display !="block" || document.getElementById("enpart2").style.display != "block" || document.getElementById("enpart4").style.display != "block" || document.getElementById("enpart3").style.display !="block") {
     window.alert("Please finish the watching!");
     return false;
    }
    else {
        return true;
     }
}

function removebutton(){
    document.getElementById("showbutton").style.display = "none";
    document.getElementById("part1").style.display = "block";
}

function removebuttonb(){
    document.getElementById("showbutton").style.display = "none";
    document.getElementById("part2B").style.display = "block";
}

function showpart2(){
    document.getElementById("part2").style.display = "block";
    document.getElementById("pbutton1").style.display = "none";
}

function showpart4(){
    document.getElementById("part4").style.display = "block";
    document.getElementById("pbutton2").style.display = "none";
}

function showpart4T(){
    document.getElementById("part4T").style.display = "block";
    document.getElementById("pbutton2").style.display = "none";
}

function showpart3(){
    document.getElementById("part3").style.display = "block";
    document.getElementById("pbutton3").style.display = "none";
}

function showpart3T(){
    document.getElementById("part3T").style.display = "block";
    document.getElementById("pbutton3").style.display = "none";
}

function showpart3S(){
    document.getElementById("part3S").style.display = "block";
    document.getElementById("pbutton3").style.display = "none";
}
function removebuttonen(){
    document.getElementById("showbuttonen").style.display = "none";
    document.getElementById("enpart1").style.display = "block";
    window.factor++;
}

function showpart2en(){
    document.getElementById("enpart2").style.display = "block";
    document.getElementById("enpbutton1").style.display = "none";
}

function showpart4en(){
    document.getElementById("enpart4").style.display = "block";
    document.getElementById("enpbutton2").style.display = "none";
}

function showpart3en() {
    document.getElementById("enpart3").style.display = "block";
    document.getElementById("enpbutton3").style.display = "none";
    }



