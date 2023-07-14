const backToTop = document.querySelector(".top");

const goToTop = () => {
  document.body.scrollIntoView({
    behavior: "smooth",
  });
}

document.addEventListener("scroll", () => {
  if (document.documentElement.scrollTop > 120) {
    backToTop.classList.remove("is-hidden");
  } else {
    backToTop.classList.add("is-hidden");
  }
});

backToTop.addEventListener("click", goToTop);
