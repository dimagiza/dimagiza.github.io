var arrCloth = [];

arrCloth[0] = {
    id: "1",
    brand: "Supreme",
    model: "Jacket",
    price: "$2.000",
    img: './img/cloth01.jpeg'
}
arrCloth[1] = {
    id: "2",
    brand: "Supreme",
    model: "Jacket",
    price: "$3.000",
    img: './img/cloth02.jpeg'
}
arrCloth[2] = {
    id: "3",
    brand: "Supreme",
    model: "Jacket",
    price: "$1.500",
    img: './img/cloth03.jpeg'
}
arrCloth[3] = {
    id: "4",
    brand: "Supreme",
    model: "Jacket",
    price: "$5.000",
    img: './img/cloth04.jpeg'
}
arrCloth[4] = {
    id: "5",
    brand: "Supreme",
    model: "Jacket",
    price: "$2.200",
    img: './img/cloth05.jpeg'
}
arrCloth[5] = {
    id: "6",
    brand: "Supreme",
    model: "Jacket",
    price: "$6.000",
    img: './img/cloth06.jpeg'
}
arrCloth[6] = {
    id: "7",
    brand: "Supreme",
    model: "Jacket",
    price: "$5.000",
    img: './img/cloth07.jpeg'
}
arrCloth[7] = {
    id: "8",
    brand: "Supreme",
    model: "Jacket",
    price: "$7.700",
    img: './img/cloth08.jpeg'
}
arrCloth[8] = {
    id: "9",
    brand: "Supreme",
    model: "Jacket",
    price: "$5.000",
    img: './img/cloth09.jpeg'
}
arrCloth[9] = {
    id: "10",
    brand: "Supreme",
    model: "Jacket",
    price: "$9.000",
    img: './img/cloth10.jpeg'
}

var num = 0;

function next() {

    num++;

    if (num >= arrCloth.length) {num = 0;}

    $('#cloth img') // Ищем IMG в родителе
    .eq(0) // Берём первую картинку 
    .attr('src', arrCloth[num].img); // Меняем значение атрибута SRC на своё
    document.getElementById('brand').innerHTML = arrCloth[num].brand;
    document.getElementById('model').innerHTML = arrCloth[num].model;
    document.getElementById('price').innerHTML = arrCloth[num].price;
}

function prev() {

    num--;

    if (num < 0) {num = arrCloth.length-1;}

    $('#cloth img') // Ищем IMG в родителе
    .eq(0) // Берём первую картинку 
    .attr('src', arrCloth[num].img); // Меняем значение атрибута SRC на своё
    document.getElementById('brand').innerHTML = arrCloth[num].brand;
    document.getElementById('model').innerHTML = arrCloth[num].model;
    document.getElementById('price').innerHTML = arrCloth[num].price;
}