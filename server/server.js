
const app = require('express')();
const httpServer = require('http').createServer(app);
const io = require('socket.io')(httpServer, {
    cors: { origin: '*' }
});

const port = process.env.PORT || 3000;

var connectedUsers = {};

console.log(connectedUsers)

io.on('connection', (socket) => {
    console.log('a user connected');

    socket.emit('newconnection')

    /*Register connected user*/
    socket.on('register', function (user) {
        socket.username = user.username;
        connectedUsers[user.username] = socket;
    });

    /* New message posted */
    socket.on('group_posted', function (question) {
        console.log(question)
        socket.broadcast.emit('group_posted', question.message);
    });

    /*Private chat*/
    socket.on('private_chat', function (data) {
        console.log(data.to)
        const to = data.to,
            message = data.message;
        if (to == '' || message == '') {
            console.log('Cannot send empty message')
            return
        }
        if (connectedUsers.hasOwnProperty(to)) {
            connectedUsers[to].emit('private_chat', {
                //to user
                to,
                //The sender's username
                username: socket.username,
                //Message sent to receiver
                message: message
            });
        }
        console.log(data)
    });


    socket.on('disconnect', () => {
        console.log('a user disconnected!');
    });
});

httpServer.listen(port, () => console.log(`listening on port ${port}`));
