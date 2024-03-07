// static/app.js

function registerUser() {
    var username = $('#username').val();
    var password = $('#password').val();
    // 測試有無正確收到值=>測試正常
    // console.log(username,password)

    // 发送注册请求到Flask后端
    $.ajax({
        type: 'POST',
        url: 'http://127.0.0.1:5000/register',
        data: { 'username': username, 'password': password },
        success: function(response) {
            alert(response.message);
        },
        error: function(xhr, status, error) {
            console.log(error);
            alert('Registration failed. Please try again.');
        }
    });
}
