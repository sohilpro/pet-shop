<template>
  <NuxtLayout name="slideproduct">
    <ClientOnly>
      <Swiper
        class="slideProducts pt-9"
        :modules="[SwiperScrollbar, SwiperAutoplay]"
        :scrollbar="{ draggable: true }"
        :breakpoints="props.breakpoints"
        :centered-slides="true"
        :grab-cursor="true"
        :loop="true"
        :autoplay="{
          delay: 2000,
          disableOnInteraction: true,
        }"
      >
        <div
          class="rtl flex justify-between items-center absolute top-0 w-full"
        >
        <img src="/svg/dogSlider.svg" alt="">
          <h1 class="pr-2 dark:text-white">محصولات سگ</h1>
          <SlideProductNextPrevBtn />
        </div>
        <SwiperSlide v-for="dogProduct in dogCategor" :key="dogProduct.id">
          <figure
          class="relative rounded-lg overflow-hidden figSlideProduct flex flex-col justify-center items-center max-w-sm transition-all duration-300 cursor-pointer filter"
          >
          <NuxtLink target="_blank" :to="`/products/${dogProduct.slug}`">
              <img
                class="transition-transform w-full h-full"
                v-img="`${apiBase}${dogProduct.src}`"
                src="/img/preloader.jpg"
                :alt="dogProduct.alt"
              />
              <figcaption
                class="transition-all hover:transition-all figCapSlideProduct opacity-0 bg-slate-200 w-full h-full absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 justify-center flex items-center text-lg text-black"
              >
                <p class="text-center font-semibold text-black">
                  {{ dogProduct.name }}
                </p>
              </figcaption>
            </NuxtLink>
              <div
                class="absolute rounded-bl-lg addProduct opacity-0 transition-all text-white top-0 right-0 space-y-3 py-3 px-3 bg-gray-700"
              >
                <svg
                  @click="emit('addToCart', dogProduct)"
                  class="hover:opacity-90 transition-all hover:transition-all"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                >
                  <path
                    fill="currentColor"
                    d="M15.55 13c.75 0 1.41-.41 1.75-1.03l3.58-6.49A.996.996 0 0 0 20.01 4H5.21l-.94-2H1v2h2l3.6 7.59l-1.35 2.44C4.52 15.37 5.48 17 7 17h12v-2H7l1.1-2h7.45zM6.16 6h12.15l-2.76 5H8.53L6.16 6zM7 18c-1.1 0-1.99.9-1.99 2S5.9 22 7 22s2-.9 2-2s-.9-2-2-2zm10 0c-1.1 0-1.99.9-1.99 2s.89 2 1.99 2s2-.9 2-2s-.9-2-2-2z"
                  />
                </svg>
                <div class="border-b"></div>
                <svg
                  v-if="dogProduct.favorite_id in props.favored"
                  @click="emit('favor', dogProduct.favorite_id)"
                  class="text-red-700"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                >
                  <path
                    fill="currentColor"
                    d="m12 21.35l-1.45-1.32C5.4 15.36 2 12.27 2 8.5C2 5.41 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.08C13.09 3.81 14.76 3 16.5 3C19.58 3 22 5.41 22 8.5c0 3.77-3.4 6.86-8.55 11.53L12 21.35Z"
                  />
                </svg>

                <svg
                  v-else
                  @click="emit('favor', dogProduct.favorite_id)"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                >
                  <path
                    fill="currentColor"
                    d="m12.1 18.55l-.1.1l-.11-.1C7.14 14.24 4 11.39 4 8.5C4 6.5 5.5 5 7.5 5c1.54 0 3.04 1 3.57 2.36h1.86C13.46 6 14.96 5 16.5 5c2 0 3.5 1.5 3.5 3.5c0 2.89-3.14 5.74-7.9 10.05M16.5 3c-1.74 0-3.41.81-4.5 2.08C10.91 3.81 9.24 3 7.5 3C4.42 3 2 5.41 2 8.5c0 3.77 3.4 6.86 8.55 11.53L12 21.35l1.45-1.32C18.6 15.36 22 12.27 22 8.5C22 5.41 19.58 3 16.5 3Z"
                  />
                </svg>
              </div>
            </figure>
        </SwiperSlide>
      </Swiper>
    </ClientOnly>
  </NuxtLayout>
</template>

<script setup>
const {
  public: { apiBase },
} = useRuntimeConfig();
const { data } = await useFetch(`${apiBase}/products/`);

const dogCategor = data.value.filter(c => c.category === "dogProduct")

const props = defineProps(["breakpoints", "favored"]);

const emit = defineEmits(["addToCart", "favor"]);
</script>

<style lang="scss">
.swiper {
  padding-top: 35px;
}
.slideProducts .figSlideProduct {
  &:hover {
    img {
      transform: scale(1.2);
      transition: transform 0.3s ease;
      --tw-blur: blur(3px);
      filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast)
        var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert)
        var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
    }
    .figCapSlideProduct {
      opacity: 0.6;
    }
    .addProduct {
      opacity: 0.8;
    }
  }
}
</style>