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
    document.getElementById("enpbutton1").style.visibility = "hidden";
}

function showpart2enE(){
    document.getElementById("Eenpart2").style.visibility = "visible";
    document.getElementById("enpbutton1").style.visibility = "hidden";
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

function checkPreB() {
    var arr3 = document.getElementsByName("edu");
    var arr3a = document.getElementById("eduother").value;
    var ear3 = false;
    for (var i = 0; i < arr3.length; i++) {
        if (arr3[i].checked || (arr3a!="" && arr3a !="Gib here ein..." && arr3a !="Enter here..." && arr3a !="在此输入...")) {
            document.getElementById("eduname").style.backgroundColor = "white";
            ear3 = true;
            break;
        }
    }
    if (ear3 == false) {
        document.getElementById("eduname").style.backgroundColor = "#FFA54F";
    }


    var arr = document.getElementsByName("role");
    var arrA = document.getElementById("roleother").value;
    var ear = false;
    for(var i=0;i<arr.length;i++ ) {
        if(arr[i].checked || (arrA!="" && arrA !="Gib here ein..." && arrA !="Enter here..." && arrA !="在此输入...")) {
            document.getElementById("rolename").style.backgroundColor ="#EEEEEE";
           ear = true;
           break;
        }
    }
    if(ear == false ){
        document.getElementById("rolename").style.backgroundColor ="#FFA54F";
    }

    var arr4 = document.getElementById("years").value;
    var ear4 = true;
    if( arr4 == null || arr4 == "" || arr4 == "在此输入..." || arr4 == "Enter here..." || arr4 == "Gib here ein..."){
        ear4 = false;
        document.getElementById("yearsname").style.backgroundColor ="#FFA54F";
    }
    else {
        var ear4 = true;
        document.getElementById("yearsname").style.backgroundColor ="white";
    }

    var arr1 = document.getElementsByName("pronu");
    var ear1 = false;
    for(var i=0;i<arr1.length;i++) {
        if(arr1[i].checked) {
            document.getElementById("pronuname").style.backgroundColor ="#EEEEEE";
           ear1 = true;
           break;
        }
    }
    if(ear1 ==false ){
        document.getElementById("pronuname").style.backgroundColor ="#FFA54F";
    }

    var arr5 = document.getElementsByName("cours");
    var ear5 = false;
    for(var i=0;i<arr5.length;i++) {
        if(arr5[i].checked) {
            document.getElementById("coursname").style.backgroundColor ="white";
           ear5 = true;
           break;
        }
    }
    if(ear5 == false ){
        document.getElementById("coursname").style.backgroundColor ="#FFA54F";
    }

    var arr6 = document.getElementsByName("tech");
    var ear6 = false;
    for(var i=0;i<arr6.length;i++) {
        if(arr6[i].checked) {
            document.getElementById("techname").style.backgroundColor ="#EEEEEE";
           ear6 = true;
           break;
        }
    }
    if(ear6 ==false ){
        document.getElementById("techname").style.backgroundColor ="#FFA54F";
    }

    var arr2 = document.getElementsByName("samtech");
    var ear2 = false;
    for(var i=0;i<arr2.length;i++) {
        if(arr2[i].checked) {
            document.getElementById("samtechname").style.backgroundColor ="white";
           ear2 = true;
           break;
        }
    }
    if(ear2 == false ){
        document.getElementById("samtechname").style.backgroundColor ="#FFA54F";
    }

    if(ear1 == false || ear == false || ear2 == false || ear3 == false || ear4 == false || ear5 == false || ear6 == false){
        return false;
    }
    else {
        return true;
    }

}

function Pretest() {
    var arr1 = document.getElementsByName("age");
    var ear1 = false;
    for(var i=0;i<arr1.length;i++) {
        if(arr1[i].checked) {
            document.getElementById("agename").style.backgroundColor ="white";
            ear1 = true;
            break;
        }
    }
    if(ear1 ==false ){
            document.getElementById("agename").style.backgroundColor ="#FFA54F";
    }

    var arr2 = document.getElementsByName("sex");
    var ear2 = false;
    for(var i=0;i<arr2.length;i++) {
        if(arr2[i].checked) {
            document.getElementById("sexname").style.backgroundColor ="#EEEEEE";
            ear2 = true;
            break;
        }
    }
    if(ear2 ==false ){
            document.getElementById("sexname").style.backgroundColor ="#FFA54F";
    }

    var arr3 = document.getElementById("national").value;
    var ear3 = true;
    if( arr3 == null || arr3 == "" || arr3 == "在此输入..." || arr3 == "Enter here..." || arr3 == "Gib here ein..."){
        ear3 = false;
        document.getElementById("nationalname").style.backgroundColor ="#FFA54F";
    }
    else {
        var ear3 = true;
        document.getElementById("nationalname").style.backgroundColor ="white";
    }

    var arr4 = document.getElementsByName("othercontry");
    var ear4 = false;
    for(var i=0;i<arr4.length;i++) {
        if(arr4[i].checked) {
            document.getElementById("othercontryname").style.backgroundColor ="#EEEEEE";
            ear4 = true;
            break;
        }
    }
    if(ear4 ==false ){
            document.getElementById("othercontryname").style.backgroundColor ="#FFA54F";
    }

    if(ear1 == false || ear2 == false || ear3 == false || ear4 == false){
        return false;
    }
    else {
        return true;
    }
}

function Pretest1() {
    var arr1 = document.getElementsByName("que11");
    var ear1 = false;
    for(var i=0;i<arr1.length;i++) {
        if(arr1[i].checked) {
            document.getElementById("que11name").style.backgroundColor ="#EEEEEE";
            ear1 = true;
            break;
        }
    }
    if(ear1 ==false ){
            document.getElementById("que11name").style.backgroundColor ="#FFA54F";
    }

    var arr2 = document.getElementsByName("que12");
    var ear2 = false;
    for(var i=0;i<arr2.length;i++) {
        if(arr2[i].checked) {
            document.getElementById("que12name").style.backgroundColor ="white";
            ear2 = true;
            break;
        }
    }
    if(ear2 ==false ){
            document.getElementById("que12name").style.backgroundColor ="#FFA54F";
    }

    var arr3 = document.getElementsByName("que13");
    var ear3 = false;
    for(var i=0;i<arr3.length;i++) {
        if(arr3[i].checked) {
            document.getElementById("que13name").style.backgroundColor ="#EEEEEE";
            ear3 = true;
            break;
        }
    }
    if(ear3 ==false ){
            document.getElementById("que13name").style.backgroundColor ="#FFA54F";
    }

    var arr4 = document.getElementsByName("que14");
    var ear4 = false;
    for(var i=0;i<arr4.length;i++) {
        if(arr4[i].checked) {
            document.getElementById("que14name").style.backgroundColor ="white";
            ear4 = true;
            break;
        }
    }
    if(ear4 ==false ){
            document.getElementById("que14name").style.backgroundColor ="#FFA54F";
    }

    var arr5 = document.getElementsByName("que15");
    var ear5 = false;
    for(var i=0;i<arr5.length;i++) {
        if(arr5[i].checked) {
            document.getElementById("que15name").style.backgroundColor ="#EEEEEE";
            ear5 = true;
            break;
        }
    }
    if(ear5 ==false ){
            document.getElementById("que15name").style.backgroundColor ="#FFA54F";
    }

    var arr6 = document.getElementsByName("que16");
    var ear6 = false;
    for(var i=0;i<arr6.length;i++) {
        if(arr6[i].checked) {
            document.getElementById("que16name").style.backgroundColor ="white";
            ear6 = true;
            break;
        }
    }
    if(ear6 ==false ){
            document.getElementById("que16name").style.backgroundColor ="#FFA54F";
    }

    var arr7 = document.getElementsByName("que17");
    var ear7 = false;
    for(var i=0;i<arr7.length;i++) {
        if(arr7[i].checked) {
            document.getElementById("que17name").style.backgroundColor ="#EEEEEE";
            ear7 = true;
            break;
        }
    }
    if(ear7 ==false ){
            document.getElementById("que17name").style.backgroundColor ="#FFA54F";
    }

    if(ear1 == false || ear2 == false || ear3 == false || ear4 == false || ear5 == false || ear6 == false || ear7 == false){
        return false;
    }
    else {
        return true;
    }
}

function Pretest2() {
    var arr1 = document.getElementsByName("que18");
    var ear1 = false;
    for(var i=0;i<arr1.length;i++) {
        if(arr1[i].checked) {
            document.getElementById("que18name").style.backgroundColor ="#EEEEEE";
            ear1 = true;
            break;
        }
    }
    if(ear1 ==false ){
            document.getElementById("que18name").style.backgroundColor ="#FFA54F";
    }

    var arr2 = document.getElementsByName("que19");
    var ear2 = false;
    for(var i=0;i<arr2.length;i++) {
        if(arr2[i].checked) {
            document.getElementById("que19name").style.backgroundColor ="white";
            ear2 = true;
            break;
        }
    }
    if(ear2 ==false ){
            document.getElementById("que19name").style.backgroundColor ="#FFA54F";
    }

    var arr3 = document.getElementsByName("que20");
    var ear3 = false;
    for(var i=0;i<arr3.length;i++) {
        if(arr3[i].checked) {
            document.getElementById("que20name").style.backgroundColor ="#EEEEEE";
            ear3 = true;
            break;
        }
    }
    if(ear3 ==false ){
            document.getElementById("que20name").style.backgroundColor ="#FFA54F";
    }

    var arr4 = document.getElementsByName("que21");
    var ear4 = false;
    for(var i=0;i<arr4.length;i++) {
        if(arr4[i].checked) {
            document.getElementById("que21name").style.backgroundColor ="white";
            ear4 = true;
            break;
        }
    }
    if(ear4 ==false ){
            document.getElementById("que21name").style.backgroundColor ="#FFA54F";
    }

    var arr5 = document.getElementsByName("que22");
    var ear5 = false;
    for(var i=0;i<arr5.length;i++) {
        if(arr5[i].checked) {
            document.getElementById("que22name").style.backgroundColor ="#EEEEEE";
            ear5 = true;
            break;
        }
    }
    if(ear5 ==false ){
            document.getElementById("que22name").style.backgroundColor ="#FFA54F";
    }

    var arr6 = document.getElementsByName("que23");
    var ear6 = false;
    for(var i=0;i<arr6.length;i++) {
        if(arr6[i].checked) {
            document.getElementById("que23name").style.backgroundColor ="white";
            ear6 = true;
            break;
        }
    }
    if(ear6 ==false ){
            document.getElementById("que23name").style.backgroundColor ="#FFA54F";
    }

    var arr7 = document.getElementsByName("que24");
    var ear7 = false;
    for(var i=0;i<arr7.length;i++) {
        if(arr7[i].checked) {
            document.getElementById("que24name").style.backgroundColor ="#EEEEEE";
            ear7 = true;
            break;
        }
    }
    if(ear7 ==false ){
            document.getElementById("que24name").style.backgroundColor ="#FFA54F";
    }

    var arr8 = document.getElementsByName("que25");
    var ear8 = false;
    for(var i=0;i<arr8.length;i++) {
        if(arr8[i].checked) {
            document.getElementById("que25name").style.backgroundColor ="white";
            ear8 = true;
            break;
        }
    }
    if(ear8 ==false ){
            document.getElementById("que25name").style.backgroundColor ="#FFA54F";
    }

    var arr9 = document.getElementsByName("que26");
    var ear9 = false;
    for(var i=0;i<arr9.length;i++) {
        if(arr9[i].checked) {
            document.getElementById("que26name").style.backgroundColor ="#EEEEEE";
            ear9 = true;
            break;
        }
    }
    if(ear9 ==false ){
            document.getElementById("que26name").style.backgroundColor ="#FFA54F";
    }

    var arr10 = document.getElementsByName("que27");
    var ear10 = false;
    for(var i=0;i<arr10.length;i++) {
        if(arr10[i].checked) {
            document.getElementById("que27name").style.backgroundColor ="white";
            ear10 = true;
            break;
        }
    }
    if(ear10 ==false ){
            document.getElementById("que27name").style.backgroundColor ="#FFA54F";
    }

    var arr11 = document.getElementsByName("que28");
    var ear11 = false;
    for(var i=0;i<arr11.length;i++) {
        if(arr11[i].checked) {
            document.getElementById("que28name").style.backgroundColor ="#EEEEEE";
            ear11 = true;
            break;
        }
    }
    if(ear11 ==false ){
            document.getElementById("que28name").style.backgroundColor ="#FFA54F";
    }

    var arr12 = document.getElementsByName("que29");
    var ear12 = false;
    for(var i=0;i<arr12.length;i++) {
        if(arr12[i].checked) {
            document.getElementById("que29name").style.backgroundColor ="white";
            ear12 = true;
            break;
        }
    }
    if(ear12 ==false ){
            document.getElementById("que29name").style.backgroundColor ="#FFA54F";
    }

    var arr13 = document.getElementsByName("que30");
    var ear13 = false;
    for(var i=0;i<arr13.length;i++) {
        if(arr13[i].checked) {
            document.getElementById("que30name").style.backgroundColor ="#EEEEEE";
            ear13 = true;
            break;
        }
    }
    if(ear13 ==false ){
            document.getElementById("que30name").style.backgroundColor ="#FFA54F";
    }

    var arr14 = document.getElementsByName("que31");
    var ear14 = false;
    for(var i=0;i<arr14.length;i++) {
        if(arr14[i].checked) {
            document.getElementById("que31name").style.backgroundColor ="white";
            ear14 = true;
            break;
        }
    }
    if(ear14 ==false ){
            document.getElementById("que31name").style.backgroundColor ="#FFA54F";
    }

     if(ear1 == false || ear2 == false || ear3 == false || ear4 == false || ear5 == false || ear6 == false || ear7 == false || ear8 == false || ear9 == false || ear10 == false || ear11 == false || ear12 == false || ear13 == false || ear14 == false){
        return false;
    }
    else {
        return true;
    }
}

function PretestA() {
    var arr1 = document.getElementById("countryname").value;
    var ear1 = true;
    if( arr1 == null || arr1 == "" || arr1 == "在此输入..." || arr1 == "Enter here..." || arr1 == "Gib here ein..."){
        ear1 = false;
        document.getElementById("countrynamename").style.backgroundColor ="#FFA54F";
    }
    else {
        var ear1 = true;
        document.getElementById("countrynamename").style.backgroundColor ="white";
    }

    var arr2 = document.getElementById("yearslong").value;
    var ear2 = true;
    if( arr2 == null || arr2 == "" || arr2 == "在此输入..." || arr2 == "Enter here..." || arr2 == "Gib here ein..."){
        ear2 = false;
        document.getElementById("yearslongname").style.backgroundColor ="#FFA54F";
    }
    else {
        var ear2 = true;
        document.getElementById("yearslongname").style.backgroundColor ="#EEEEEE";
    }

    var arr3 = document.getElementsByName("F1");
    var ear3 = false;
    for(var i=0;i<arr3.length;i++) {
        if(arr3[i].checked) {
            document.getElementById("F1name").style.backgroundColor ="#EEEEEE";
            ear3 = true;
            break;
        }
    }
    if(ear3 ==false ){
            document.getElementById("F1name").style.backgroundColor ="#FFA54F";
    }

    var arr4 = document.getElementsByName("F2");
    var ear4 = false;
    for(var i=0;i<arr4.length;i++) {
        if(arr4[i].checked) {
            document.getElementById("F2name").style.backgroundColor ="white";
            ear4 = true;
            break;
        }
    }
    if(ear4 ==false ){
            document.getElementById("F2name").style.backgroundColor ="#FFA54F";
    }

    var arr5 = document.getElementsByName("F3");
    var ear5 = false;
    for(var i=0;i<arr5.length;i++) {
        if(arr5[i].checked) {
            document.getElementById("F3name").style.backgroundColor ="#EEEEEE";
            ear5 = true;
            break;
        }
    }
    if(ear5 ==false ){
            document.getElementById("F3name").style.backgroundColor ="#FFA54F";
    }

    var arr6 = document.getElementsByName("F4");
    var ear6 = false;
    for(var i=0;i<arr6.length;i++) {
        if(arr6[i].checked) {
            document.getElementById("F4name").style.backgroundColor ="white";
            ear6 = true;
            break;
        }
    }
    if(ear6 ==false ){
            document.getElementById("F4name").style.backgroundColor ="#FFA54F";
    }

    var arr7 = document.getElementsByName("F5");
    var ear7 = false;
    for(var i=0;i<arr7.length;i++) {
        if(arr7[i].checked) {
            document.getElementById("F5name").style.backgroundColor ="#EEEEEE";
            ear7 = true;
            break;
        }
    }
    if(ear7 ==false ){
            document.getElementById("F5name").style.backgroundColor ="#FFA54F";
    }

    var arr8 = document.getElementsByName("F6");
    var ear8 = false;
    for(var i=0;i<arr8.length;i++) {
        if(arr8[i].checked) {
            document.getElementById("F6name").style.backgroundColor ="white";
            ear8 = true;
            break;
        }
    }
    if(ear8 ==false ){
            document.getElementById("F6name").style.backgroundColor ="#FFA54F";
    }



    if(ear1 == false || ear2 == false || ear3 == false || ear4 == false || ear5 == false || ear6 == false || ear7 == false || ear8 == false){
        return false;
    }
    else {
        return true;
    }
}

function Posttest() {
    var arr1 = document.getElementsByName("post1");
    var ear1 = false;
    for(var i=0;i<arr1.length;i++) {
        if(arr1[i].checked) {
            document.getElementById("post1name").style.backgroundColor ="#EEEEEE";
            ear1 = true;
            break;
        }
    }
    if(ear1 ==false ){
            document.getElementById("post1name").style.backgroundColor ="#FFA54F";
    }

    var arr2 = document.getElementsByName("post2");
    var ear2 = false;
    for(var i=0;i<arr2.length;i++) {
        if(arr2[i].checked) {
            document.getElementById("post2name").style.backgroundColor ="white";
            ear2 = true;
            break;
        }
    }
    if(ear2 ==false ){
            document.getElementById("post2name").style.backgroundColor ="#FFA54F";
    }

    var arr3 = document.getElementsByName("post3");
    var ear3 = false;
    for(var i=0;i<arr3.length;i++) {
        if(arr3[i].checked) {
            document.getElementById("post3name").style.backgroundColor ="#EEEEEE";
            ear3 = true;
            break;
        }
    }
    if(ear3 == false ){
            document.getElementById("post3name").style.backgroundColor ="#FFA54F";
    }

    var arr4 = document.getElementsByName("post4");
    var ear4 = false;
    for(var i=0;i<arr4.length;i++) {
        if(arr4[i].checked) {
            document.getElementById("post4name").style.backgroundColor ="#EEEEEE";
            ear4 = true;
            break;
        }
    }
    if(ear4 ==false ){
            document.getElementById("post4name").style.backgroundColor ="#FFA54F";
    }

    var arr5 = document.getElementsByName("post5");
    var ear5 = false;
    for(var i=0;i<arr5.length;i++) {
        if(arr5[i].checked) {
            document.getElementById("post5name").style.backgroundColor ="white";
            ear5 = true;
            break;
        }
    }
    if(ear5 ==false ){
            document.getElementById("post5name").style.backgroundColor ="#FFA54F";
    }

    var arr6 = document.getElementsByName("post6");
    var ear6 = false;
    for(var i=0;i<arr6.length;i++) {
        if(arr6[i].checked) {
            document.getElementById("post6name").style.backgroundColor ="#EEEEEE";
            ear6 = true;
            break;
        }
    }
    if(ear6 ==false ){
            document.getElementById("post6name").style.backgroundColor ="#FFA54F";
    }
     if(ear1 == false || ear2 == false || ear3 == false || ear4 == false || ear5 == false || ear6 == false){
        return false;
    }
    else {
        return true;
    }
}

function PosttestA() {
    var arr1 = document.getElementsByName("post7");
    var ear1 = false;
    for(var i=0;i<arr1.length;i++) {
        if(arr1[i].checked) {
            document.getElementById("post7name").style.backgroundColor ="#EEEEEE";
            ear1 = true;
            break;
        }
    }
    if(ear1 ==false ){
            document.getElementById("post7name").style.backgroundColor ="#FFA54F";
    }

    var arr2 = document.getElementsByName("post8");
    var ear2 = false;
    for(var i=0;i<arr2.length;i++) {
        if(arr2[i].checked) {
            document.getElementById("post8name").style.backgroundColor ="white";
            ear2 = true;
            break;
        }
    }
    if(ear2 ==false ){
            document.getElementById("post8name").style.backgroundColor ="#FFA54F";
    }

    var arr3 = document.getElementsByName("post9");
    var ear3 = false;
    for(var i=0;i<arr3.length;i++) {
        if(arr3[i].checked) {
            document.getElementById("post9name").style.backgroundColor ="#EEEEEE";
            ear3 = true;
            break;
        }
    }
    if(ear3 ==false ){
            document.getElementById("post9name").style.backgroundColor ="#FFA54F";
    }

    var arr4 = document.getElementsByName("post10");
    var ear4 = false;
    for(var i=0;i<arr4.length;i++) {
        if(arr4[i].checked) {
            document.getElementById("post10name").style.backgroundColor ="white";
            ear4 = true;
            break;
        }
    }
    if(ear4 ==false ){
            document.getElementById("post10name").style.backgroundColor ="#FFA54F";
    }

    var arr5 = document.getElementsByName("post11");
    var ear5 = false;
    for(var i=0;i<arr5.length;i++) {
        if(arr5[i].checked) {
            document.getElementById("post11name").style.backgroundColor ="#EEEEEE";
            ear5 = true;
            break;
        }
    }
    if(ear5 ==false ){
            document.getElementById("post11name").style.backgroundColor ="#FFA54F";
    }

    var arr6 = document.getElementsByName("post12");
    var ear6 = false;
    for(var i=0;i<arr6.length;i++) {
        if(arr6[i].checked) {
            document.getElementById("post12name").style.backgroundColor ="white";
            ear6 = true;
            break;
        }
    }
    if(ear6 ==false ){
            document.getElementById("post12name").style.backgroundColor ="#FFA54F";
    }

    var arr7 = document.getElementsByName("post13");
    var ear7 = false;
    for(var i=0;i<arr7.length;i++) {
        if(arr7[i].checked) {
            document.getElementById("post13name").style.backgroundColor ="#EEEEEE";
            ear7 = true;
            break;
        }
    }
    if(ear7 ==false ){
            document.getElementById("post13name").style.backgroundColor ="#FFA54F";
    }

    var arr8 = document.getElementsByName("post14");
    var ear8 = false;
    for(var i=0;i<arr8.length;i++) {
        if(arr8[i].checked) {
            document.getElementById("post14name").style.backgroundColor ="#EEEEEE";
            ear8 = true;
            break;
        }
    }
    if(ear8 ==false ){
            document.getElementById("post14name").style.backgroundColor ="#FFA54F";
    }

    var arr9 = document.getElementsByName("post15");
    var ear9 = false;
    for(var i=0;i<arr9.length;i++) {
        if(arr9[i].checked) {
            document.getElementById("post15name").style.backgroundColor ="white";
            ear9 = true;
            break;
        }
    }
    if(ear9 ==false ){
            document.getElementById("post15name").style.backgroundColor ="#FFA54F";
    }

    var arr10 = document.getElementsByName("post16");
    var ear10 = false;
    for(var i=0;i<arr10.length;i++) {
        if(arr10[i].checked) {
            document.getElementById("post16name").style.backgroundColor ="#EEEEEE";
            ear10 = true;
            break;
        }
    }
    if(ear10 ==false ){
            document.getElementById("post16name").style.backgroundColor ="#FFA54F";
    }
    if(ear1 == false || ear2 == false || ear3 == false || ear4 == false || ear5 == false || ear6 == false || ear7 == false || ear8 == false || ear9 == false || ear10 == false){
        return false;
    }
    else {
        return true;
    }
}

function PosttestB() {
    var arr1 = document.getElementsByName("post17");
    var ear1 = false;
    for(var i=0;i<arr1.length;i++) {
        if(arr1[i].checked) {
            document.getElementById("post17name").style.backgroundColor ="#EEEEEE";
            ear1 = true;
            break;
        }
    }
    if(ear1 ==false ){
            document.getElementById("post17name").style.backgroundColor ="#FFA54F";
    }

    var arr2 = document.getElementsByName("post18");
    var ear2 = false;
    for(var i=0;i<arr2.length;i++) {
        if(arr2[i].checked) {
            document.getElementById("post18name").style.backgroundColor ="white";
            ear2 = true;
            break;
        }
    }
    if(ear2 ==false ){
            document.getElementById("post18name").style.backgroundColor ="#FFA54F";
    }

    var arr3 = document.getElementsByName("post19");
    var ear3 = false;
    for(var i=0;i<arr3.length;i++) {
        if(arr3[i].checked) {
            document.getElementById("post19name").style.backgroundColor ="#EEEEEE";
            ear3 = true;
            break;
        }
    }
    if(ear3 ==false ){
            document.getElementById("post19name").style.backgroundColor ="#FFA54F";
    }

    var arr4 = document.getElementsByName("post20");
    var ear4 = false;
    for(var i=0;i<arr4.length;i++) {
        if(arr4[i].checked) {
            document.getElementById("post20name").style.backgroundColor ="#EEEEEE";
            ear4 = true;
            break;
        }
    }
    if(ear4 ==false ){
            document.getElementById("post20name").style.backgroundColor ="#FFA54F";
    }

    var arr5 = document.getElementsByName("post21");
    var ear5 = false;
    for(var i=0;i<arr5.length;i++) {
        if(arr5[i].checked) {
            document.getElementById("post21name").style.backgroundColor ="white";
            ear5 = true;
            break;
        }
    }
    if(ear5 ==false ){
            document.getElementById("post21name").style.backgroundColor ="#FFA54F";
    }

    var arr6 = document.getElementsByName("post22");
    var ear6 = false;
    for(var i=0;i<arr6.length;i++) {
        if(arr6[i].checked) {
            document.getElementById("post22name").style.backgroundColor ="#EEEEEE";
            ear6 = true;
            break;
        }
    }
    if(ear6 ==false ){
            document.getElementById("post22name").style.backgroundColor ="#FFA54F";
    }

     if(ear1 == false || ear2 == false || ear3 == false || ear4 == false || ear5 == false || ear6 == false){
        return false;
    }
    else {
        return true;
    }
}
