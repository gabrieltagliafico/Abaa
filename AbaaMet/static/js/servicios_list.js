$(document).ready(function () {
  $('#datatable').DataTable({
  });
});

$(function () {
  let csrftoken = '{{ csrf_token }}'
  $('.btnTest').on('click', function () {
    $.ajax({
      url: '/principal/',
      headers:{'X-CSRFToken':csrftoken},
      type: 'POST',
      data:{'hola':String,csrfmiddlewaretoken: '{{ csrf_token }}'},
      dataType: 'json',
      success:function(response){
        console.log(data)
      }
    });
  });
});