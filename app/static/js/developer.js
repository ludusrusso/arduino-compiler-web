  
var logconsole;
var editor;

$(function() {
  logconsole = CodeMirror.fromTextArea(document.getElementById('pm'), {
    lineNumbers: false,
    readOnly: true,
    styleActiveLine: true,
    matchBrackets: true,
    theme: "3024-night"
  });

  editor = CodeMirror.fromTextArea(document.getElementById('code'), {
    lineNumbers: true,
    styleActiveLine: true,
    mode: "text/x-c++src"
  });
});




var compFun =  function() {
  var valeur = 0;
  $("#devprogress").css('width', valeur+'%').attr('aria-valuenow', valeur); 
  logconsole.getDoc().setValue('');
  var url =  '/_compile?' + jQuery.param({
    prog: editor.getDoc().getValue(),
    args: $('input[name="args"]').val()
  });
  var eventOutputContainer = document.getElementById("output");
  var evtSrc = new EventSource(url);

  evtSrc.onmessage = function(e) {   
    if (e.data === 'STOP'){
      console.log("STOP");
      e.target.close();
      valeur = 100;
      $("#devprogress").css('width', valeur+'%').attr('aria-valuenow', valeur); 

    } else {
      logconsole.getDoc().setValue(logconsole.getDoc().getValue() + e.data + '\n');
      logconsole.setCursor({line: logconsole.getDoc().getValue().split(/\r\n|\r|\n/).length});
      valeur = valeur+0.1;
      $("#devprogress").css('width', valeur+'%').attr('aria-valuenow', valeur); 
    }
  };
  return false;
}

var monitorFun =  function() {
  var url =  '/_monitor'
  var eventOutputContainer = document.getElementById("output");
  var evtSrc = new EventSource(url);

  evtSrc.onmessage = function(e) {   
    if (e.data === 'STOP'){
      console.log("STOP");
      e.target.close();
    } else {
      logconsole.getDoc().setValue(logconsole.getDoc().getValue() + e.data + '\n');
      logconsole.setCursor({line: logconsole.getDoc().getValue().split(/\r\n|\r|\n/).length});
    }
  };
  return false;
}


