  
var editor;

$(function() {
  /*logconsole = CodeMirror.fromTextArea(document.getElementById('pm'), {
    lineNumbers: false,
    readOnly: true,
    styleActiveLine: true,
    matchBrackets: true,
    theme: "3024-night"
  });*/

  editor = CodeMirror.fromTextArea(document.getElementById('code'), {
    lineNumbers: true,
    styleActiveLine: true,
    mode: "text/x-c++src"
  });
});

var saveSketch = function(id) {
  var sketch = { code: editor.getDoc().getValue() };
  $.ajax({
    url: '/api/v1.0/sketches/' + id + '/',
    type: 'PUT',
    contentType: "application/json",
    data: JSON.stringify(sketch),
    success: function(result) {
        console.log("uploaded");
    }
});
}

var Console = function() {
  this.log = function(data) {
    $("#my_console").append('<p>'+ data +'</p>');
    $("#my_console").scrollTop($("#my_console")[0].scrollHeight);
  };
  this.empty = function() {
    $("#my_console").empty();
  }
}

var my_console = new Console()

var compFun =  function(s_id) {
  my_console.empty();
  var valeur = 0;
  s_id = s_id || 1
  $("#devprogress").css('width', valeur+'%').attr('aria-valuenow', valeur); 
  var url =  '/api/v1.0/compile/'+ s_id + '/';
  var evtSrc = new EventSource(url);

  evtSrc.onmessage = function(e) {   
    if (e.data === 'STOP'){
      console.log("STOP");
      e.target.close();
      valeur = 100;
      $("#devprogress").css('width', valeur+'%').attr('aria-valuenow', valeur); 
    } else {
      my_console.log(e.data);
      console.log(e.data);
      valeur = valeur+0.1;
      $("#devprogress").css('width', valeur+'%').attr('aria-valuenow', valeur); 
    }
  };
  return false;
}

var Buffer = function() {
  this.cnt = 0;
  this.str = "";
  this.addline = function(line) {
    this.str += line+'\n';
    if (this.cnt >= 100) {
      console.log(this.cnt, this.str.indexOf('\n'))
      this.str = this.str.substr(this.str.indexOf('\n')+1, this.str.length);
    } else {
      this.cnt+=1;
      console.log(this.cnt)
    }
    return this.str
  };
}



var monitorFun =  function() {
  var url =  '/api/v1.0/monitor?' + jQuery.param({
    monitor:'start',
    baud: $('input[id="inputBaud"]').val()
  });
  var evtSrc = new EventSource(url);
  my_console.empty()

  evtSrc.onmessage = function(e) {   
    if (e.data === 'STOP'){
      console.log("STOP");
      e.target.close();
    } else {
      console.log(e.data);
      my_console.log(e.data);
    }
  };
  return false;
}

var stopMonitor = function() {
$.ajax({
    url: '/api/v1.0/monitor?' + jQuery.param({
    monitor:'stop',
  });,
    type: 'GET',
    success: function(result) {
        console.log("Monitor Stop");
    }
  });
}

