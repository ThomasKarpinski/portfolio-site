import VanillaTilt from "vanilla-tilt";
VanillaTilt.init(document.querySelector(".background"), {
    glare: true,
    reverse: true,
    "max-glare": 0.5,
    startX: 45,
    startY: 45,
    reset: false
});