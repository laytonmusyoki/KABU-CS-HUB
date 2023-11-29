$(document).ready(function () {
    $(window).scroll(function () {
        if (this.scrollY > 20) {
            $('.navbar').addClass("sticky");
        } else {
            $('.navbar').removeClass("sticky");
        }
        if (this.scroll > 500) {
            $('.scroll-up-btn').addClass("show")
        } else {
            $('.scroll-up-btn').removeClass('show')
        }
    });
    $('.scroll-up-btn').click(function () {
        $('html').animate({scrollTop:0})
    })

    //toggle menu/navbar script 
    $(document).ready(function() {
        $('#icon').click(function(){
          $('ul').toggleClass('show')
        });
    });
    //typing animation script
    var typed = new Typed(".typing", {
        strings: ["Web Designer", "Web Developer", "Freelancer", "Mentor"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });
    var typed = new Typed(".typing-2", {
        strings: ["Web Designer", "Web Developer", "Freelancer", "Mentor"],
        typeSpeed: 100,
        backSpeed: 60,
        loop: true
    });

// Initialize Swiper
    var swiper = new Swiper('.swiper-container', {
        loop: true,
        autoplay: {
        delay: 2000,
        },
    });
    const videoLinks = document.querySelectorAll('.video-link');
    const videoModal = document.getElementById('videoModal');
    const videoIframe = document.getElementById('videoIframe');
    const closeBtn = document.getElementById('closeBtn');

    videoLinks.forEach(link => {
    link.addEventListener('click', (event) => {
        event.preventDefault();
        const videoId = link.getAttribute('data-video-id');
        const videoUrl = `https://www.youtube.com/embed/${videoId}`;
        videoIframe.src = videoUrl;
        videoModal.style.display = 'flex';
    });
    });
    


  

    $('.carousel').owlCarousel({
        margin: 20,
        loop: true,
        autoplayTimeOut: 2000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1,
                nav: false
            },
            600: {
                items: 2,
                nav: false
            },
            1000: {
                items: 3,
                nav: false
            }
        }

    });
    // Wait for the page to load

});

const hamburger = document.querySelector(".hamburger");
const navmenu = document.querySelector("ul");

hamburger.addEventListener("click", () =>{
    hamburger.classList.toggle("active");
    navmenu.classList.toggle("active");
})
document.querySelectorAll(".nav-link").forEach(n=>n.addEventListener("click", () =>{
    hamburger.classList.remove("active");
    navmenu.classList.remove("active");
}))