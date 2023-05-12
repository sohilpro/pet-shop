<script setup>
const swiper = useSwiper();
</script>

<template>
  <div
    class="w-28 md:w-[34rem] opacity-20 lg:w-[62rem] h-[1px] bg-blue-500 dark:opacity-80"
  ></div>
  <div class="flex space-x-2 z-[999] items-center">
    <button @click="swiper.slideNext()" class="border text-gray-400 transition-all hover:text-gray-500 hover:border-gray-500 hover:transition-all">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
      >
        <path
          fill="currentColor"
          d="M9.31 6.71a.996.996 0 0 0 0 1.41L13.19 12l-3.88 3.88a.996.996 0 1 0 1.41 1.41l4.59-4.59a.996.996 0 0 0 0-1.41L10.72 6.7c-.38-.38-1.02-.38-1.41.01z"
        />
      </svg>
    </button>

    <button @click="swiper.slidePrev()" class="border text-gray-400 transition-all hover:text-gray-500 hover:border-gray-500 hover:transition-all">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="24"
        height="24"
        viewBox="0 0 24 24"
      >
        <path
          fill="none"
          stroke="currentColor"
          stroke-width="2"
          d="m15 6l-6 6l6 6"
        />
      </svg>
    </button>
  </div>
</template>