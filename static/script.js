'use strict';
console.log('script running!');

const input = document.querySelector('.contact-container');
const images = document.querySelector('.ia-container');
const resetBtn = document.querySelector('.reset')

const pokeInput=document.querySelector('#poke-input');
const button=document.querySelector('.btn');
const message=document.querySelector('#message');

/*
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
});*/

resetBtn.addEventListener('click', (e) => {
  input.classList.remove("is-hidden");
  images.classList.add("is-hidden");
  resetBtn.classList.add("is-hidden");
});

document.querySelector("#search").addEventListener("click", getPokemon);

function lowerCaseName(string) {
  return string.toLowerCase();
}

function getPokemon(e) {
  const name = document.querySelector("#poke-input").value;
  const pokemonName = lowerCaseName(name);

  if(pokemonName == ""){
    message.textContent = "You have yet to enter a Pokemon name";
  }else{
    fetch(`https://pokeapi.co/api/v2/pokemon/${pokemonName}`)
      .then((response) => response.json())
      .then((data) => {
        pokeInput.value = "";
        message.textContent = "";
        input.classList.add("is-hidden");
        images.classList.remove("is-hidden");
        resetBtn.classList.remove("is-hidden");
        document.getElementById("img1").click();
      })
      .catch((err) => {
        message.textContent = "Pokemon not found";
      });

    e.preventDefault();
  }
}