'use strict';
console.log('script running!');

const input = document.querySelector('.contact-container');
const images = document.querySelector('.ia-container');
const resetBtn = document.querySelector('.reset')

const pokeInput=document.querySelector('#poke-input');
const button=document.querySelector('.btn');
const message=document.querySelector('#message');


button.addEventListener('click', (e) => {
  let poke = true;
  
  if(pokeInput.value == ""){
    poke = false;
  }
  if(!(poke)){
    message.textContent = "You have yet to enter a Pokemon name";
  }else{
    pokeInput.value = "";
    message.textContent = "";
    input.classList.add("is-hidden");
    images.classList.remove("is-hidden");
    resetBtn.classList.remove("is-hidden");
    document.getElementById("img1").click();
  }
});

resetBtn.addEventListener('click', (e) => {
  input.classList.remove("is-hidden");
  images.classList.add("is-hidden");
  resetBtn.classList.add("is-hidden");
});

