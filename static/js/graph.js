function drawGraph1() {
	var plotdata = document.getElementById('plotimg1');
	$.get("/plot1/", function(data) {
		plotdata.src = "data:image/png:base64," + data;
	});
}
$(document).ready(function() {
	var target = document.getElementById('graph1');
	drawGraph1(target);
});

function drawGraph2(obj) {
	var idx = obj.selectedIndex;
	var value = obj.options[idx].value;
	var plotdata = document.getElementById('plotimg2');
	$.get("/plot2/" + value, function(data) {
		plotdata.src = "data:image/png:base64," + data;
	});
}
$(document).ready(function() {
	var target = document.getElementById('selector');
	drawGraph2(target);
});

function drawGraph3() {
	var plotdata = document.getElementById('plotimg3');
	$.get("/plot3/", function(data) {
		plotdata.src = "data:image/png:base64," + data;
	});
}
$(document).ready(function() {
	var target = document.getElementById('graph3');
	drawGraph3(target);
});

function drawGraph4(obj) {
	var plotdata = document.getElementById('plotimg4');
	$.get("/plot4/", function(data) {
		plotdata.src = "data:image/png:base64," + data;
	});
}
$(document).ready(function() {
	var target = document.getElementById('graph4');
	drawGraph4(target);
});