setInterval(() => {
    let a = new Date();
    let date = a.toLocaleDateString();
    let time = a.getHours() + ":" + a.getMinutes() + ":" + a.getSeconds();
    document.getElementById('clock').innerHTML = time + " On " + date;
}, 1000);