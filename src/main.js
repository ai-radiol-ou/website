document.addEventListener('DOMContentLoaded', function() {
  const burger = document.getElementById('hamburger');
  burger.addEventListener('click', function() {
    const target = burger.dataset.target;
    const $target = document.getElementById(target);
    burger.classList.toggle('is-active');
    $target.classList.toggle('is-active');
  });
});

require('./styles.scss');
