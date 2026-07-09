/* Scroll-reveal via IntersectionObserver, honoring prefers-reduced-motion.
   Without JS (or with reduced motion) everything renders fully visible. */
(function () {
  document.documentElement.classList.add("js");

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

  var heroVideo = document.querySelector(".landing-hero video");
  if (heroVideo && reduceMotion.matches) {
    heroVideo.removeAttribute("autoplay");
    heroVideo.pause();
  }

  var targets = document.querySelectorAll(".reveal");
  if (!targets.length || reduceMotion.matches || !("IntersectionObserver" in window)) {
    targets.forEach(function (el) { el.classList.add("is-visible"); });
    return;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: "0px 0px -5% 0px" }
  );

  targets.forEach(function (el) { observer.observe(el); });
})();
