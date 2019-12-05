// JavaScript Document

$(document).ready(function () {
  "use strict";

  $(window).on('resize', function () {

    if ($(this).width() < 992) {
      $("nav").addClass("scrolled-md");
    } else {
      $("nav").removeClass("scrolled-md");
    }
  });//cambiar de color nav al achicar pantalla

  $(window).scroll(function () {
    $("nav").toggleClass("scrolled", $(this).scrollTop() > 550);
  });//cambiar de color nav

  $('.navbar-nav>li>a').on('click', function () {
    $('.navbar-collapse').collapse('hide');
  });

  $(".img-hover").mouseover(function () {
    $(".img-hover img").css("filter", "blur(10px)");
    $(this).find("img").css("filter", "blur(0px)");
  });
  $(".img-hover").mouseout(function () {
    $(".img-hover img").css("filter", "blur(0px)");
  });//enfocar/desenfocar imagenes carta.

});

