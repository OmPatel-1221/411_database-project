$(document).ready(function () {

    $('#create_button').click(function () {
        console.log("hello world")
        const tID = $('#task-form-display').attr('taskID');
        var name_input_val = document.getElementById("name_input").value;
        var username_input_val = document.getElementById("username_input").value;
        var password_input_val = document.getElementById("password_input").value;
        console.log($('#task-modal').find('.form-control').val());
        $.ajax({
            type: 'POST',
            url: '/create',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': [name_input_val, username_input_val, password_input_val]
            }),
            success: function (res) {
                console.log(res.response)
                console.log("hello world")
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });


    $('#delete_button').click(function () {
        console.log("hello world")
        const tID = $('#task-form-display').attr('taskID');
        var name_input_val = document.getElementById("name_input").value;
        var username_input_val = document.getElementById("username_input").value;
        var password_input_val = document.getElementById("password_input").value;
        console.log($('#task-modal').find('.form-control').val());
        $.ajax({
            type: 'POST',
            url: '/delete',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': [name_input_val, username_input_val, password_input_val]
            }),
            success: function (res) {
                console.log(res.response)
                console.log("hello world")
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#search_button').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        var manufacturer_input_val = document.getElementById("manufacturer_input").value;
        var model_input_val = document.getElementById("model_input").value;
        var year_input_val = document.getElementById("year_input").value;
        var color_input_val = document.getElementById("color_input").value;
        console.log($('#task-modal').find('.form-control').val());
        $.ajax({
            type: 'POST',
            url: '/search',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': [manufacturer_input_val, model_input_val, year_input_val, color_input_val]
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });


    $('.reviews').click(function () {
        
        var car_id1 = $(this).data('source');
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('.form-control').val());
        $.ajax({
            type: 'POST',
            url: '/fetch_reviews',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': [car_id1]
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.upvotes').click(function () {
        
        var review_id1 = $(this).data('source');
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('.form-control').val());
        $.ajax({
            type: 'POST',
            url: '/upvote',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': [review_id1]
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('.downvotes').click(function () {
        
        var review_id1 = $(this).data('source');
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('.form-control').val());
        $.ajax({
            type: 'POST',
            url: '/downvote',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': [review_id1]
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#query1').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        var manufacturer_input_val = document.getElementById("manufacturer_input").value;
        var model_input_val = document.getElementById("model_input").value;
        var year_input_val = document.getElementById("year_input").value;
        var color_input_val = document.getElementById("color_input").value;
        console.log($('#task-modal').find('.form-control').val());
        $.ajax({
            type: 'POST',
            url: '/query1',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': [manufacturer_input_val, model_input_val, year_input_val, color_input_val]
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#query2').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        var manufacturer_input_val = document.getElementById("manufacturer_input").value;
        var model_input_val = document.getElementById("model_input").value;
        var year_input_val = document.getElementById("year_input").value;
        var color_input_val = document.getElementById("color_input").value;
        console.log($('#task-modal').find('.form-control').val());
        $.ajax({
            type: 'POST',
            url: '/query2',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': [manufacturer_input_val, model_input_val, year_input_val, color_input_val]
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

    $('#storedProcedure').click(function () {
        const tID = $('#task-form-display').attr('taskID');
        console.log($('#task-modal').find('.form-control').val());
        $.ajax({
            type: 'POST',
            url: '/ratings',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'description': []
            }),
            success: function (res) {
                console.log(res.response)
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        });
    });

});


