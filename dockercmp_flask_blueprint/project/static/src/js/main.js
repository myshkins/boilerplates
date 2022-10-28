const homeButton = document.querySelector('#btn-home');

homeButton.addEventListener('click', () => console.log(this));

const sayHi = document.querySelector('#btn-hi');
sayHi.addEventListener('click', (e) => {
    const loc = document.querySelector('#btn-hi').getAttribute('data-location');
    console.log(loc);
    window.location = loc
})