aData={}
$( "#first_name" ).autocomplete({
    source: function(request,response){
        $.ajax({
            url:'http://localhost/Search%20in%20html/loader.php',
            type: 'GET',
            dataType:'json',
            success: function(data){
                aData=$.map(data,function(name){
                    return {
                        label:name.name
                    };
                });
                var results=$ui.autocomplete.filter(aData,request.term);
                response(results)
            }
        })
    }
  });