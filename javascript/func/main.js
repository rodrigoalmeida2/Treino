let myImage = document.querySelector('img');

myImage.onclick = () => {
    let mySrc = myImage.getAttribute('src');
    if (mySrc === 'images/fire.jpg') {
        myImage.setAttribute('src', 'images/chrom.png');
    } else {
        myImage.setAttribute('src', 'images/fire.jpg');
    }
}

// New

let myButton = document.querySelector('button');
let myHeading = document.querySelector('h1');

function setUserName() {
    const myName = prompt("Enter your name.");
    if (!myName) {
        setUserName();
    }else{
        localStorage.setItem('name', myName);
        myHeading.textContent = `Mozilla is cool, ${myName}`;
    }
}

myButton.onclick = () => {
    setUserName();
}