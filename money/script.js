let sum = 0;
document.getElementById("total").innerHTML = sum;

function add() {

	let name = document.getElementById("inname").value;
	let comment = document.getElementById("incomment").value;
	let price = document.getElementById("inprice").value;

if (name!="" && price!="") {

//add new row
container.insertAdjacentHTML('beforeend', `<div class="row"><div class="column">${name}</div><div class="column">${comment}</div><div class="column">${price}</div></div>`);

//clear input's values
document.getElementById("inname").value = "";
document.getElementById("incomment").value = "";
document.getElementById("inprice").value = "";

//hide example row
document.getElementById("examplerow").style.display = "none";

//total price
sum += +price;
document.getElementById("total").innerHTML = sum;

} else alert("ooops");

}