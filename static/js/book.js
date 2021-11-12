$(document).ready(function(){
    $(document).on('click','#book-btn',function(){
        let session_id = $(this).attr('data-index')
        $.ajax({
            type: "POST",
            url: "/book_session",
            datatype:"json",
            action: "booking",
            data: {
                id:session_id
            },
            success:function(resp){
                swal({
                    title: "Good job!",
                    text: "You clicked the button!",
                    icon: "success",
                    button: "Aww yiss!",
                });
            }
        })
    })
})