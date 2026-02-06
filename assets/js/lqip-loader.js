/**
 * LQIP Loader - Handles lazy loading of images with blur-to-sharp transitions.
 *
 * Images with class "lqip" start with a low-quality placeholder in src
 * and the full image URL in data-full. When the image enters the viewport,
 * the full image is loaded and swapped in with a smooth transition.
 */
(function () {
  "use strict";

  var BLUR_CLASS = "lqip";
  var LOADED_CLASS = "lqip-loaded";
  var ROOT_MARGIN = "200px"; // Start loading 200px before visible

  // IntersectionObserver for lazy loading full images
  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var img = entry.target;
          var fullSrc = img.dataset.full;

          if (!fullSrc) return;

          if (fullSrc.indexOf("://") === -1) {
            // data-full is relative — resolve against src's parent directory
            // src is {cdn}/{folder}/lqip/X.webp, data-full is webp/X.webp
            // both are relative to {cdn}/{folder}/, so go up one dir from src
            fullSrc = new URL(fullSrc, new URL("..", img.src)).href;
          }

          // Preload full image
          var fullImg = new Image();
          fullImg.onload = function () {
            img.src = fullSrc;
            img.classList.add(LOADED_CLASS);
          };
          fullImg.onerror = function () {
            // On error, still try to load the full image directly
            // This handles cases where the LQIP might not exist yet
            img.src = fullSrc;
            img.classList.add(LOADED_CLASS);
          };
          fullImg.src = fullSrc;

          observer.unobserve(img);
        }
      });
    },
    {
      rootMargin: ROOT_MARGIN,
    }
  );

  // Initialize on DOM ready
  function init() {
    var images = document.querySelectorAll("img." + BLUR_CLASS);
    images.forEach(function (img) {
      observer.observe(img);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
