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
      data:{csrfmiddlewaretoken: '{{ csrf_token }}'},
      success:function(response){
        console.log(data)
      }
    });
  });
});
