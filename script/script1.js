var text = [
    'free shipping on orders of $150 & over',
    '20% off! use coupon - 20days',
    'new arrivals here'
];
var img = [
    './img/banner/06.png',
    './img/banner/04.jpg',
    './img/banner/07.jpg'
];

var num = 0;
var numimg = 0;
function next() {
    var slider = document.getElementById('slider');
    num++;
    if (num >= text.length) {
        num = 0;
    }
    document.getElementById('slider').innerHTML = text[num];
    
    var banner = document.getElementById('banner');
    document.getElementById('banner').style.backgroundImage = `url('${img[num]}')`;
}
function prev() {
    var slider = document.getElementById('slider');
    num--;
    if (num < 0) {
        num = text.length-1;
    }
    document.getElementById('slider').innerHTML = text[num];

    var banner = document.getElementById('banner');
    document.getElementById('banner').style.backgroundImage = `url('${img[num]}')`;
}