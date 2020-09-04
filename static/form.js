
function submitForm() {

    //When user clicks the submit button POST the input to /form
    enteredText = document.getElementById('keywords').value

    let data = {
        'enteredText':enteredText
    };

    xhr = new XMLHttpRequest()
    xhr.open('POST', '/form')
    xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded")
    xhr.send(JSON.stringify(data))
    xhr.onreadystatechange = requestHandler

    function requestHandler() {
        statusCode = xhr.status
        // transfer complete
        if(xhr.readyState == 4){
            console.log('Sucess!');
   

            switch(statusCode){
                case 200:
                    alert('Sucess!');
                    break;
                case 401:
                    alert('Session has expired');
                    break;
                case 500:
                    alert('Invalid request, check parameters and try again');
                    break;
                default:
                    alert('Something went wrong. Status was: ' + xhr.status);
                    break;
            }

        }
    }

}