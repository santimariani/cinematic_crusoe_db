"use strict";

const button = document.getElementById("button")

const beachVideo = document.getElementById("beachVideo");
const beachAudio = document.getElementById("beachAudio");

const topLid = document.getElementById("topLid");
const bottomLid = document.getElementById("bottomLid");

const firstPhrase = document.getElementById("firstPhrase");
const secondPhrase = document.getElementById("secondPhrase");
const thirdPhrase = document.getElementById("thirdPhrase");
const fourthPhrase = document.getElementById("fourthPhrase");

const inputPanel = document.getElementById("inputPanel");


document.addEventListener("DOMContentLoaded", async() => {
    console.log("SUUUUUUP");
    button.addEventListener('click', () => {
        button.classList.add('buttonBegone');
        button.addEventListener('animationend', () => {
            button.style.display = 'none';
            firstPhrase.classList.add('fadeInOut');
            beachAudio.play();
        });
    });
    
    firstPhrase.addEventListener('animationend', () => {
        secondPhrase.classList.add('fadeInOut');
    });

    secondPhrase.addEventListener('animationend', () => {
        thirdPhrase.classList.add('fadeInOut');
    });

    thirdPhrase.addEventListener('animationend', () => {
        fourthPhrase.classList.add('fadeInOut');
    });

    fourthPhrase.addEventListener('animationend', () => {
        beachVideo.classList.add('clearVideo');
        topLid.classList.add('topOpen');
        bottomLid.classList.add('bottomOpen');
    });
    
    topLid.addEventListener('animationend', () => {
        topLid.classList.add('fullyOpen');
    });

    bottomLid.addEventListener('animationend', () => {
        bottomLid.classList.add('fullyOpen');
    });

    beachVideo.addEventListener('animationend', () => {
        inputPanel.classList.add('appear');
    });

    // inputPanel.addEventListener('animationend', () => {
    // });
    const itemsResponse = await fetch ('http://localhost:8000/items');
    const items = await itemsResponse.json();
    const itemsEl = document.querySelector('#showItems');
    items.map((id) => {
        const paragraph = document.createElement('p');
        paragraph.innerText = id.name;
        itemsEl.appendChild(paragraph);
    });

});
