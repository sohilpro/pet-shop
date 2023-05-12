<template>
  <SlideProductSliderCatProduct
    :breakpoints="breakpoints"
    :favored="favorite"
    @add-to-cart="addToCart"
    @favor="handleFavorite"
  />
  <SlideProductSliderBirdProduct
    :breakpoints="breakpoints"
    :favored="favorite"
    @add-to-cart="addToCart"
    @favor="handleFavorite"
  />
  <SlideProductSliderDogProduct
    :breakpoints="breakpoints"
    :favored="favorite"
    @add-to-cart="addToCart"
    @favor="handleFavorite"
  />
  <SlideProductSliderFishProduct
    :breakpoints="breakpoints"
    :favored="favorite"
    @add-to-cart="addToCart"
    @favor="handleFavorite"
  />
</template>

<script setup>
import { useCart } from "@/store/cart.js";
const breakpoints = ref({
  640: {
    slidesPerView: 1,
  },
  768: {
    slidesPerView: 2,
  },
  1024: {
    slidesPerView: 4,
    spaceBetween: 40,
  },
});

const cart = useCart();

const addToCart = (product) => {
  cart.addToCart(product);
};

const favorite = useLocalStorage("favorite", {});
const handleFavorite = (id) => {
  if (id in favorite.value) {
    delete favorite.value[id];
  } else {
    favorite.value = {
      ...favorite.value,
      [id]: true,
    };
  }
};
</script>