
<script>
  $(document).ready(function() {
    $.getJSON('liveData.json', function(data) {
      var html = [];
      $.each(data, function(i, item) {
        html.push('<div >');
        html.push('<h3 >' + item.firstName + '</h3>');
        html.push('<div >' + item.lastName + '</div>');
        html.push('<div >' + item.age + '</div>');
        html.push('<div >' + item.address.streetAddress + '</div>');
        html.push('<div >' + item.phoneNumber[0].type + '</div>');
        html.push('</div>'); html.push('</div>');

        //html.push('<li id="' + key + '">' + val + '</li>'); });

        console.log(html); $('#target').html(html.join(''));
      });
    });
  </script>
</head>

<body> <div id="target" /></body>
