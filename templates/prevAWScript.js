const inputAW = document.querySelector('.contact-container-aw');
const pokeInputAW=document.querySelector('#poke-input-aw');
const buttonAW=document.querySelector('.btn-aw');
const messageAW=document.querySelector('#message-aw');
const columnsAW=document.querySelector('.columns');

buttonAW.addEventListener('click', (e) => {
  let pokeAW = true;
  if(pokeInputAW.value == ""){
    pokeAW = false;
  }
  if(!(pokeAW)){
    messageAW.textContent = "You have yet to enter a Pokemon name";
  }else{
    pokeInputAW.value = "";
    messageAW.textContent = "";
    columnsAW.classList.remove("is-hidden");
  }
});

