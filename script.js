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

    const itemsResponse = await fetch ('http://localhost:8000/items');
    const items = await itemsResponse.json();
    const itemsEl = document.querySelector('#showItems');
    items.map((id) => {
        const paragraph = document.createElement('p');
        paragraph.innerText = id.name;
        itemsEl.appendChild(paragraph);
    });

    const form = document.querySelector("#petForm");
    async function sendData() {
      // Associate the FormData object with the form element
      const formData = new FormData(form);
      const petName = formData.get("dogName")
    
      try {
        const response = await fetch("http://localhost:8000/pets/add", {
          method: "POST",
          // Set the FormData instance as the request body
          headers: {"Content-Type": "application/json"},
          body: JSON.stringify({name: petName}),
        });
        console.log(await response.json());
      } catch (e) {
        console.error(e);
      }
    }
    
    // Take over form submission
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      sendData();
    });
});


