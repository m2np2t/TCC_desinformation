new SimpleAnime();

new SimpleSlide({
    slide: 'principal', 
    nav: true, 
    auto: true, 
    time: 2000, 
    pauseOnHover: true, 
});

function initAccordion() {
    const accordionList = document.querySelectorAll('.js-accordion dt');
    const activeClass = 'ativo';

    if (accordionList.length) {
        
        function activeAccordion() {
            this.classList.toggle(activeClass);
            this.nextElementSibling.classList.toggle(activeClass);
        }

        accordionList.forEach((item) => {
            item.addEventListener('click', activeAccordion);
        });
    }
}
initAccordion();
