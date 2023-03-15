
$(document).ready(function () {
    $(".btnsave").click(function () {
        let title = $('#title').val();
        let summary = $('#summary').val();
        let content = $('#content').val();

        if (title == "") {
            alert('Title Should Not Be Empty');
        }
        else if (summary == "") {
            alert('Summary Should Not Be Empty');
        }
        else if (content == "") {
            alert('Content Should Not Be Empty');
        }
    })

    let max_words = 15;
    let less_words = 10;
    

    $('.summary').each(function(){

        if($(this).text().split(" ").length > 15){
            var array = $(this).text().split(" ").slice(0,15).join(" ")
            console.log(array)
            $(this).text(array + " ....") 
       
        }  
    })

    setTimeout('$(".blogMessage").hide(100)',10000);
    setTimeout('$(".alert-register").hide(100)',10000);
})

