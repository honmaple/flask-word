var socket;
$(document).ready(function(){
  socket = io.connect('http://' + document.domain + ':' + location.port + '/chat');
  socket.on('connect', function() {
    socket.emit('joined', {});
  });
  socket.on('status', function(data) {
    var exdata = $('#chat').html();
    var addata = exdata + '<div class="text-center" style="margin-bottom:8px;"><span class="msg">' +  data.msg + '</span></div>';
    $('#chat').html(addata);
    $('#chat').scrollTop($('#chat')[0].scrollHeight);
  });
  socket.on('message', function(data) {
    var exdata = $('#chat').html();
    var addata = exdata + data.html;
    $('#chat').html(addata);
    $('#chat').scrollTop($('#chat')[0].scrollHeight);
  });
  $('#text').keypress(function(e) {
    var code = e.keyCode || e.which;
    if (code == 13) {
      text = $('#text').val();
      if (text === ''){
        alert('输入不能为空!');
        return false;
      }else{
        $('#text').val('');
        socket.emit('text', {msg: text});
      }
    }
  });
  $('.send-msg').click(function() {
    text = $('#text').val();
    if (text === ''){
      alert('输入不能为空!');
      return false;
    }else{
      $('#text').val('');
      socket.emit('text', {msg: text});
    }
  });
});
