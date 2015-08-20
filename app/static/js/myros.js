var ros = new ROSLIB.Ros({
  url : 'ws://192.168.0.108:9090'
});

ros.on('connection', function() {
  console.log('Connected to websocket server.');
});

ros.on('error', function(error) {
  console.log('Error connecting to websocket server: ', error);
});

ros.on('close', function() {
  console.log('Connection to websocket server closed.');
});


  var blink_pub = new ROSLIB.Topic({
    ros : ros,
    name : '/toggle_led',
    messageType : 'std_msgs/Empty'
  });

  var b = new ROSLIB.Message({});

  var change_pub = new ROSLIB.Topic({
    ros : ros,
    name : '/change_led',
    messageType : 'std_msgs/Int16'
  });

  var b = new ROSLIB.Message({});

  var clickFun = function() {
  	blink_pub.publish(b);
  }

  var slideFun = function(val) {
  	var num = new ROSLIB.Message({data: Number(val)});
  	  	console.log(num);

  	change_pub.publish(num);
  }





var gridster;
var margin = 15;
$(function(){
	gridster = $(".gridster ul").gridster({
		widget_base_dimensions: [120, 120],
		widget_margins: [10, 10],
		min_cols: 6,
	}).data('gridster');
});

var BaseWidget = function(r, c) {
	var li = document.createElement('LI');
	var div = document.createElement('DIV');

	console.log(div.style);
	li.appendChild(div);

	this.html = li;
	this.rows = r || 1;
	this.cols = c || 1;
	this.getWidget = function() {return [this.html, this.rows, this.cols];};
	this.getDiv = function() {return div;};
}

var RosPubWidget = function(topic, msg, r, c) {
	var pub = new ROSLIB.Topic({
   		ros : ros,
    	name : topic,
    	messageType : msg
  	});
	this.rows = r || 1;
	this.cols = c || 1;
  	this.topic = pub;
  	this.publish = function(msg) {this.topic.publish(msg)};
}
RosPubWidget.prototype = new BaseWidget;

var RosSubWidget = function(topic, msg, r, c) {
	var sub = new ROSLIB.Topic({
   		ros : ros,
    	name : topic,
    	messageType : msg
  	});
  	this.rows = r || 1;
	this.cols = c || 1;
  	this.topic = sub;
}
RosSubWidget.prototype = new BaseWidget;


var rosTest = new RosPubWidget('widget_topic', 'std_msgs/Int16');

var input = document.createElement('input'); 
var output = document.createElement('output');	
input.type = 'range';
input.value = '50';
input.onchange = function() {rosTest.publish({data: Number(input.value)}); };
rosTest.getDiv().appendChild(input);

var rosSub = new RosSubWidget('widget_topic', 'std_msgs/Int16');


var RosWidgetColor(topic_name) {
  RosSubWidget.call(this, topic_name, 'std_msgs/Int16');

  var canvas = document.createElement('canvas');  
  canvas.width  = rosSub.rows*120 - 2*margin;
  canvas.height = rosSub.cols*120 - 2*margin;

  var context = canvas.getContext('2d');
  var center  = rosSub.rows*120 / 2 - margin;
  var radius  = 40;

  var draw_path = function (o) {
    context.beginPath();
    o = o | 0;
    context.clearRect(0, 0, canvas.width, canvas.height);
    context.arc(center, center, radius, 0, 2 * Math.PI, false);
    colurfill = "rgba(color, 0, 255, 1)";
    context.fillStyle = colurfill.replace(new RegExp('color','g'), o);
    console.log(colurfill.replace(new RegExp('color','g'), o));
    context.fill();
    context.lineWidth = 1;
    context.strokeStyle = '#003300';
    context.stroke();
  }
  draw_path(50);
}

rosSub.topic.subscribe(function(d) {draw_path(Number(d.data)/100.0*255);});
rosSub.getDiv().appendChild(canvas);


$(function(){
	gridster.add_widget.apply(gridster, rosSub.getWidget());
	gridster.add_widget.apply(gridster, rosTest.getWidget());
}); 



