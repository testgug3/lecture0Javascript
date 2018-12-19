document.addEventListener('DOMContentLoaded', () => {
    //connect to the websocket
    var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

    //when connected, configure events
    //attach events to buttons
    socket.on('connect', () => {
        //each button should emit a submit vote event
        document.querySelectorAll('button').forEach(button => {
            button.onclick = () => {
                const selection = button.dataset.vote;
                socket.emit('submit vote', {'selection': selection});
            }
        });
    });

    //when a new vote is announced, add to the unordered list
    socket.on('announce vote', data => {
        const li = document.createElement('li');
        li.innerHTML = `Vote recorded: ${data.selection}`;
        document.querySelector('#votes').append(li);
    });
});