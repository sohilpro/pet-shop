<template>
  <Swiper
    class="max-w-max Header mt-6 md:mt-4"
    :height="600"
    :modules="[
      SwiperAutoplay,
      SwiperEffectFade,
      SwiperPagination,
      SwiperNavigation,
    ]"
    :slides-per-view="1"
    :loop="true"
    :effect="'fade'"
    :pagination="{
      clickable: true,
      dot: true,
    }"
    :navigation="true"
    :autoplay="{
      delay: 8000,
      disableOnInteraction: true,
    }"
  >
    <SwiperSlide v-for="(Header, id) in Headers" :key="id">
      <img class="w-full h-full" :src="Header.src" :alt="Header.alt" />
    </SwiperSlide>
  </Swiper>
</template>

<script setup>
const Headers = ref([
  {
    id: 0,
    src: '/img/slide-1.webp',
    alt: 'slide-1.webp',
  },
  {
    id: 1,
    src: '/img/slide-2.webp',
    alt: 'slide-2.webp',
  },
  {
    id: 2,
    src: '/img/slide-3.webp',
    alt: 'slide-3.webp',
  }
])
</script>

<style>
.Header .swiper-button-prev {
  opacity: 0.39;
  transition: all 0.3s ease;
}
.Header .swiper-button-prev:hover {
  opacity: 1;
  transition: all 0.2s ease;
}
.Header .swiper-button-next {
  opacity: 0.39;
  transition: all 0.3s ease;
}
.Header .swiper-button-next:hover {
  opacity: 1;
  transition: all 0.2s ease;
}
.Header .swiper-pagination-bullet-active {
  background-color: rgba(68, 47, 159, 0.695);
  transform: scale(1.5);
  transition: 0.3s;
}
</style>
