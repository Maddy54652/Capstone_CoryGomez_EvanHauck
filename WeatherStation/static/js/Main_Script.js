/**
 * Created by batman on 3/15/17.
 */
var today = new Date();
var dd  = today.getDate();
var mm = today.getMonth()+1;
var yyyy = today.getFullYear();
if(dd<10){
    dd='0'+ dd;
}
if(mm<10){
    mm='0'+ mm;
};
today = yyyy + '-' + mm + '-' + dd;
document.getElementById("dateField").setAttribute("max", today);

function update(){
    alert_string = '';
        alert_string = alert_string + document.getElementById('datefield1').value;
        alert_string = alert_string + ' ';
        alert_string = alert_string + document.getElementById('datefield2').value;

        alert(alert_string);
}
