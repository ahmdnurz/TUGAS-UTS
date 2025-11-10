// Tambahan animasi halus saat elemen muncul di layar
document.addEventListener("DOMContentLoaded", () => {
    const elements = document.querySelectorAll(".fade-in, .slide-up, .result-box, .container");
    elements.forEach((el, i) => {
        el.style.opacity = 0;
        setTimeout(() => {
            el.style.transition = "opacity 0.6s ease, transform 0.6s ease";
            el.style.opacity = 1;
            el.style.transform = "translateY(0)";
        }, i * 120);
    });

    // Efek klik halus pada tombol
    document.querySelectorAll("button").forEach(btn => {
        btn.addEventListener("mousedown", () => btn.style.transform = "scale(0.95)");
        btn.addEventListener("mouseup", () => btn.style.transform = "scale(1)");
    });
});
