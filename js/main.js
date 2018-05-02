// console.log(frozen_data);
var bulk_length = Object.keys(frozen_data).length;
bulk_length = 6500000 / 5000;
var c = document.getElementById("timeline");
var ctx = c.getContext("2d");
ctx.canvas.width  = window.innerWidth;
ctx.font="15px Arial";
window.temp_id   = [0, 10, 20, 30, 50];

$('.slider').on('change', function(){
	console.log("change");
	var ratio = $(this).val();
	generate_timeline(ratio);
});

ctx.lineWidth=2;
// $('.slider').value = 50
function generate_timeline(ratio){

	ctx.clearRect(0, 0, c.width, c.height);
	var temp_width = $('#timeline').width();
	console.log(ratio)
	// var ratio = 30
	var order = new Array(45);
	var sortable = [];
	for (const [key, value] of Object.entries(frozen_data)){
		// console.log(ratio);
		// console.log(value[1] * parseInt(ratio) + value[2] * (100 - parseInt(ratio)))
		sortable.push([key, value[1] * (100 - parseInt(ratio)) + value[2] * parseInt(ratio) / 2, value[0]])
		// console.log(value[1])
	}
	// console.log(sortable)

	sortable.sort(function(a, b) {
		return b[1] - a[1];
	});

	sortable = sortable.slice(0, 50)

	// console.log(sortable);
	var temp_sent = [];
	window.temp_id = [];
	var temp_x;
	for (var i = 0; i < sortable.length; i++) {
		// console.log(sortable[i][0] * 1.0 / bulk_length * temp_width);
		temp_x = sortable[i][0] * 1.0 / bulk_length * temp_width;
		// console.log(temp_x)
		ctx.beginPath();
		ctx.moveTo(temp_x, 0);
		ctx.lineTo(temp_x, 210);
		ctx.strokeStyle = 'rgba(200, 20, 20, ' + (i * 1.0 / sortable.length) + ')';
		// console.log((i * 1.0 / sortable.length) * 255)
		ctx.stroke();
		ctx.fillText(sortable[i][2], temp_x, Math.random() * 150 + 25);
		temp_sent.push(sortable[i][2] + ' ')
		window.temp_id.push(sortable[i][0])
	}
	window.temp_id.sort(function(a, b) {return a - b;});
	console.log(window.temp_id)
	$(".third-row").empty();
	$(".third-row").append(`<p>` + temp_sent + `</p>`);

	window.video_count = 0;
	videoPlayer.setAttribute("src","frozen_clip/"+ window.temp_id[video_count]+".mp4");
	window.video.load();
	window.video.play();
	window.video.currentTime = 0;
	$(".subtitle").empty();
	$(".subtitle").append(`<h5>` + 0 + `</h5>`);


}

window.video_count = 0;
videoPlayer = document.getElementById("ss");		
window.video=document.getElementById("myVideo");

function run(){
	window.video_count++;
	if (window.video_count == window.temp_id.length) {
		window.video_count = 0;
		videoPlayer.setAttribute("src","frozen_clip/"+ window.temp_id[video_count]+".mp4");
		window.video.currentTime = 0;
		$(".subtitle").empty();
		$(".subtitle").append(`<h5>` + 0 + `</h5>`);

	}
	else{
		videoPlayer.setAttribute("src","frozen_clip/"+ window.temp_id[video_count]+".mp4");
		$(".subtitle").empty();
		$(".subtitle").append(`<h5>` + window.video_count + `</h5>`);
		window.video.load();
		window.video.play();
	}
}

generate_timeline(50)