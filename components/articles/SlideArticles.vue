<template>
  <NuxtLayout name="slideproduct">
    <Swiper
      :modules="[SwiperScrollbar, SwiperAutoplay]"
      :scrollbar="true"
      :centered-slides="true"
      :breakpoints="breakpoints"
      :grab-cursor="true"
      :loop="true"
      :autoplay="{
        delay: 3000,
        disableOnInteraction: true,
      }"
    >
      <div class="rtl flex justify-center items-center space-x-2 absolute top-0 w-full">
        <svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 36 36"><g transform="translate(36 0) scale(-1 1)"><path fill="#C1694F" d="M32 34a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V7a2 2 0 0 1 2-2h24a2 2 0 0 1 2 2v27z"/><path fill="#FFF" d="M29 32a1 1 0 0 1-1 1H8a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1h20a1 1 0 0 1 1 1v23z"/><path fill="#CCD6DD" d="M25 3h-4a3 3 0 1 0-6 0h-4a2 2 0 0 0-2 2v5h18V5a2 2 0 0 0-2-2z"/><circle cx="18" cy="3" r="2" fill="#292F33"/><path fill="#99AAB5" d="M20 14a1 1 0 0 1-1 1h-9a1 1 0 0 1 0-2h9a1 1 0 0 1 1 1zm7 4a1 1 0 0 1-1 1H10a1 1 0 0 1 0-2h16a1 1 0 0 1 1 1zm0 4a1 1 0 0 1-1 1H10a1 1 0 1 1 0-2h16a1 1 0 0 1 1 1zm0 4a1 1 0 0 1-1 1H10a1 1 0 1 1 0-2h16a1 1 0 0 1 1 1zm0 4a1 1 0 0 1-1 1h-9a1 1 0 1 1 0-2h9a1 1 0 0 1 1 1z"/></g></svg>
        <h1 class="pr-2 dark:text-white">آنچه باید بدانید</h1>
        <SlideProductNextPrevBtn />
      </div>
      <SwiperSlide v-for="picture in pictures" :key="picture.id">
        <NuxtLink to="/">
          <figure
            class="relative hoverArticle rounded-lg overflow-hidden flex flex-col justify-center items-center max-w-sm transition-all duration-300 cursor-pointer filter"
          >
            <img
              class="transition-transform w-full h-full"
              :src="picture.src"
              :alt="picture.alt"
            />
            <figcaption
              class="transition-all rtl hover:transition-all opacity-70 bg-slate-200 w-3/5 h-full absolute top-1/2 right-0 -translate-y-1/2 flex justify-end px-4 text-lg text-white"
            >
              <div class="flex flex-col justify-between text-black">
                <div class="space-y-4">
                  <h1 class="text-base mt-3">
                    {{ picture.title }}
                  </h1>
                  <p class="text-base">
                    {{ picture.desc }}
                  </p>
                </div>
                <div class="flex items-center mb-4">
                  <h2 class="text-sm">مشاهده بیشتر</h2>
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="18"
                    height="18"
                    viewBox="0 0 24 24"
                  >
                    <path
                      fill="currentColor"
                      d="M13 19L2 12l11-7l-3.425 6H22v2H9.575L13 19Z"
                    />
                  </svg>
                </div>
              </div>
            </figcaption>
          </figure>
        </NuxtLink>
      </SwiperSlide>
    </Swiper>
  </NuxtLayout>
</template>

<script setup>
const breakpoints = ref({
  640: {
    slidesPerView: 1,
  },
  768: {
    slidesPerView: 2,
  },
  1024: {
    slidesPerView: 3,
    spaceBetween: 40,
  },
});
const pictures = ref([
  {
    id: 0,
    title: "گربه ها چه غذا های انسانی را می وانند بخورند؟",
    desc: "بعضی از گربه ها خیلی دوست دارند به بشقاب غذا انسان ها دست درازی کنند...",
    src: "https://baranpet.com/blog/sites/default/files/styles/rss_newset_image/public/1401-12/human-foods-cats-can-eat-What%20Human%20Foods%20Can%20Cats%20EatTEASER.jpg?itok=MisGTEqJ",
    alt: "Picture 1",
  },
  {
    id: 1,
    title: "آیا سگ من می تواند سیر بخورد؟",
    desc: "ما با شما می گوییم که چگونه به سگ خود سیر بدهید...",
    src: "https://baranpet.com/blog/sites/default/files/styles/rss_newset_image/public/1401-11/garlic-for-dog-Can-Dogs-Eat-Garlic.jpg?itok=wVvvbn8C",
    alt: "Picture 2",
  },
  {
    id: 2,
    title: "مزیت های سیرابی برای سگ ها",
    desc: " تعداد زیادی از صاحبان سگ هستند که به سگ‌های خود سیرابی می‌دهند...",
    src: "https://baranpet.com/blog/sites/default/files/styles/rss_newset_image/public/1401-12/tripe-for-dogs.jpg?itok=4mxUTTec",
    alt: "Picture 3",
  },
  {
    id: 3,
    title: "معرفی برند سلبن (Celebone)",
    desc: "برند سلبن محصولات خود را با بالاترین استانداردهای جهانی تولید می کند...",
    src: "https://baranpet.com/blog/sites/default/files/styles/rss_newset_image/public/1401-12/celebone-Banner-1.jpg?itok=hgMpEYC_",
    alt: "Picture 4",
  },
  {
    id: 4,
    title: "چرا گربه من پلاستیک می خورد؟",
    desc: "تمام کسانی که گربه‌دوست هستند، می‌دانند برخی از گربه ها رفتار بسیار عجیب و غریب دارند...",
    src: "https://baranpet.com/blog/sites/default/files/styles/rss_newset_image/public/1401-10/why-cats-eat-plastic-2.jpg?itok=Twuspp4N",
    alt: "Picture 5",
  },
]);
</script>

<style lang="scss" scoped>
.hoverArticle {
  img {
    transition: all 0.3s ease;
  }
  &:hover {
    img {
      transition: all 0.3s ease;
      --tw-blur: blur(8px);
      filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast)
        var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert)
        var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow);
    }
  }
}
</style>
