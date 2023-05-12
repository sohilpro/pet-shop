<template>
  <nav class="rtl z-[999]">
    <div
      class="fixed z-[999] shadow items-center justify-center w-full flex md:justify-around top-0 -mt-1 h-16 dark:bg-gray-900 bg-white"
    >
      <div class="md:flex hidden items-center gap-2">
        <button
          @click="logout"
          v-if="userAuth"
          class="bg-blue-600 text-white transition-all hover:bg-blue-800 px-4 py-2 rounded"
        >
          خروج از حساب
        </button>
        <button
          v-else
          class="bg-blue-600 text-white transition-all hover:bg-blue-800 px-4 py-2 rounded-md"
        >
          <NuxtLink to="/auth/register">
            ثبت نام / ورود
          </NuxtLink>
        </button>

          <NuxtLink v-if="userAuth" to="/cart" class="relative">
            <img src="/svg/cart.svg" alt="..." />
            <div
              class="absolute inline-flex items-center justify-center w-4 h-4 text-[0.5rem] font-bold text-white bg-blue-600 rounded-full -top-1 left-2 dark:border-gray-900"
            >
              {{ itemOnCart }}
            </div>
          </NuxtLink>

        <img
          v-show="$colorMode.value === 'light'"
          @click="
            setColorTheme($colorMode.preference === 'dark' ? 'light' : 'dark')
          "
          class="cursor-pointer"
          src="/svg/light.svg"
          alt="..."
        />

        <img
          v-show="$colorMode.value === 'dark'"
          @click="
            setColorTheme($colorMode.preference === 'dark' ? 'light' : 'dark')
          "
          class="cursor-pointer"
          src="/svg/dark.svg"
          alt=""
        />
      </div>
      <div>
        <ul class="md:flex hidden gap-5 cursor-pointer dark:text-white">
          <li>
            <NuxtLink to="/"
            class="hover:text-blue-600"
            :class="{'text-blue-600 dark:font-semibold': $route.path === '/'}">
              خانه
            </NuxtLink>
          </li>
          <li>
            <NuxtLink
              to="/about-us"
              :class="{
                'text-blue-600 dark:font-semibold': $route.path === '/about-us',
              }"
              class="hover:text-blue-600"
              >درباره ما</NuxtLink
            >
          </li>
          <li class="flex group h-full flex-col">
            <div class="flex items-center">
              محصولات
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
              >
                <path
                  fill="currentColor"
                  d="m11.3 14.3l-2.6-2.6q-.475-.475-.212-1.087T9.425 10h5.15q.675 0 .938.613T15.3 11.7l-2.6 2.6q-.15.15-.325.225T12 14.6q-.2 0-.375-.075T11.3 14.3Z"
                />
              </svg>
            </div>
            <div
              class="absolute transition-all group-hover:visible group-hover:opacity-100 invisible opacity-0 w-40 top-16 bg-gray-100 dark:bg-gray-900 dark:text-white rounded-b-xl"
            >
              <ul class="w-full h-full ml-auto dark:opacity-70">
                <li class="border-b hover:text-blue-600 p-2 gap-1 flex items-center"
                :class="{'text-blue-600': $route.path === '/product/dogs'}"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 512 512" > <path fill="currentColor" d="m393.3 161.33l-58.768-84.892a48.09 48.09 0 0 0-38.775-20.673l-111.527-1.6H184c-57.579 0-101.757 9.631-130.21 56.634C27.3 154.551 16 229.08 16 360v16h36.557L29.024 496h32.61l23.533-120H96a99.521 99.521 0 0 0 70.088-27.992c16.979-16.246 29.226-38.472 35.419-64.274l.056-.232L229.006 152h-32.69l-25.979 124.488C162.425 309.168 138.766 344 96 344H48.06c.869-113.266 11.182-180.419 33.105-216.634c18.4-30.4 45.295-41.191 102.724-41.206l111.408 1.6a16.026 16.026 0 0 1 12.925 6.891L374.7 190.67l89.3 14.884v16.959l-14.892 79.421c-4.395 23.441-11.908 35.249-42.718 38.95l-126.306 21.609L279.249 496h32l.667-106.493l98.7-16.9c22.36-2.749 38.857-9.955 50.426-22.023c9.89-10.318 15.909-23.5 19.519-42.752L496 225.487v-47.041Z" /></svg>
                  <NuxtLink to="/product/dogs">
                      سگ
                  </NuxtLink>
                </li>
                <li class="border-b gap-1 hover:text-blue-600 p-2 flex items-center"
                :class="{ 'text-blue-600': $route.path === '/product/cats' }"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 28 28" > <path fill="currentColor" d="M8.523 26h11.852a2.574 2.574 0 0 0 2.573-2.574V12.01c2.413-.096 3.86-2.775 2.57-4.857l-.754-1.216a3.18 3.18 0 0 0-2.703-1.506h-2.152V3.48A1.48 1.48 0 0 0 18.43 2a3.668 3.668 0 0 0-3.667 3.669v5.185c-1.917.187-3.364 1.095-4.427 2.371c-1.174 1.41-1.865 3.248-2.277 5.013c-.413 1.775-.56 3.538-.603 4.85a28.575 28.575 0 0 0-.013 1.412h-.988a2.957 2.957 0 0 1-2.16-4.975l1.38-1.48a5.383 5.383 0 0 0-.13-7.477L4.192 9.213a.75.75 0 1 0-1.06 1.06l1.355 1.356a3.88 3.88 0 0 1 .093 5.392l-1.38 1.48A4.459 4.459 0 0 0 6.454 26h2.068ZM18.41 3.5v1.682c0 .415.335.75.75.75h2.9c.583 0 1.123.301 1.43.796l.753 1.217c.695 1.12-.11 2.569-1.429 2.569h-.616a.75.75 0 0 0-.75.75v12.162c0 .593-.48 1.074-1.073 1.074h-1.074v-1.074a4.397 4.397 0 0 0-4.396-4.399h-1.52a.75.75 0 0 0 0 1.5h1.52c1.6 0 2.897 1.298 2.897 2.899V24.5h-8.86a27.01 27.01 0 0 1 .012-1.363c.042-1.254.181-2.912.565-4.558c.386-1.655 1.006-3.238 1.969-4.393c.94-1.129 2.217-1.868 4.025-1.868a.75.75 0 0 0 .75-.75v-5.9c0-1.19.959-2.157 2.147-2.168Z" /></svg>
                  <NuxtLink
                    to="/product/cats"
                  >
                    گربه
                  </NuxtLink>
                </li>
                <li class="border-b hover:text-blue-600 p-2 gap-1 flex items-center"
                :class="{ 'text-blue-600': $route.path === '/product/Birds' }"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 256 256" ><path fill="currentColor" d="M174 68a10 10 0 1 1-10-10a10 10 0 0 1 10 10Zm-50.16 63.39a6 6 0 0 0-8.45.77l-40 48a6 6 0 1 0 9.22 7.68l40-48a6 6 0 0 0-.77-8.45ZM238 80a6 6 0 0 1-2.67 5L214 99.21V120a102.12 102.12 0 0 1-102 102H8a6 6 0 0 1-4.69-9.75L98 93.9V76a58 58 0 0 1 113.51-16.87L235.33 75a6 6 0 0 1 2.67 5Zm-16.82 0L203 67.88a6 6 0 0 1-2.47-3.48A46 46 0 0 0 110 76v20a6 6 0 0 1-1.31 3.75L20.48 210H112a90.1 90.1 0 0 0 90-90V96a6 6 0 0 1 2.67-5Z" /></svg>
                  <NuxtLink
                    to="/product/Birds"
                  >
                    پرنده
                  </NuxtLink>
                </li>
                <li class="border-b hover:text-blue-600 p-2 gap-1 flex items-center" 
                  :class="{ 'text-blue-600': $route.path === '/product/Fishs' }"
                  >
                  <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" ><path fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M10.5 9s0-2-1-4c4 0 6.5 2.5 6.5 2.5s3.5-.5 6 4.5c-1 5.5-6 6-6 6l-4 2.5v-3c-2.5-1-5-3.5-5-5S10.5 9 10.5 9Zm0 0s1-.5 2-.5M2 9.5l1 3l-1 3s5 0 5-3s-5-3-5-3Zm15 2.51l.01-.011" /></svg>
                  <NuxtLink
                    to="/product/Fishs"
                  >
                    ماهی
                  </NuxtLink>
                </li>
              </ul>
            </div>
          </li>
          <li class="hover:text-blue-600">پشتیبانی</li>
        </ul>
      </div>
      <NuxtLink to="/">
        <img
          v-img="
            $colorMode.preference === 'light'
              ? '/img/logo-black.png'
              : '/img/logo-white.png'
          "
          :src="
            $colorMode.preference === 'light'
              ? '/img/logo-black-pre.png'
              : '/img/logo-white-pre.png'
          "
          class="w-44 md:w-32 h-auto"
          alt="logoPetShop"
        />
      </NuxtLink>
    </div>

    <menu class="menu z-[999] md:invisible rounded-t-3xl">
      <button
      :class="{'active': $route.path === '/'}"
      class="menu__item" style="--bgColorItem: #ff8c00">
      <NuxtLink to="/">
        <svg class="w-[41.6px] h-[41.6px]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><path fill="#E8EAF6" d="M42 39H6V23L24 6l18 17z"/><path fill="#C5CAE9" d="m39 21l-5-5V9h5zM6 39h36v5H6z"/><path fill="#B71C1C" d="M24 4.3L4 22.9l2 2.2L24 8.4l18 16.7l2-2.2z"/><path fill="#D84315" d="M18 28h12v16H18z"/><path fill="#01579B" d="M21 17h6v6h-6z"/><path fill="#FF8A65" d="M27.5 35.5c-.3 0-.5.2-.5.5v2c0 .3.2.5.5.5s.5-.2.5-.5v-2c0-.3-.2-.5-.5-.5z"/></svg>
      </NuxtLink>
      </button>

      <button
      :class="{'active': $route.path === '/about-us'}"
      class="menu__item" style="--bgColorItem: #f54888">
      <NuxtLink to="/about-us">
        <svg xmlns="http://www.w3.org/2000/svg" class="icon" viewBox="0 0 24 24"><path d="M13.5 4A1.5 1.5 0 0 0 12 5.5A1.5 1.5 0 0 0 13.5 7A1.5 1.5 0 0 0 15 5.5A1.5 1.5 0 0 0 13.5 4m-.36 4.77c-1.19.1-4.44 2.69-4.44 2.69c-.2.15-.14.14.02.42c.16.27.14.29.33.16c.2-.13.53-.34 1.08-.68c2.12-1.36.34 1.78-.57 7.07c-.36 2.62 2 1.27 2.61.87c.6-.39 2.21-1.5 2.37-1.61c.22-.15.06-.27-.11-.52c-.12-.17-.24-.05-.24-.05c-.65.43-1.84 1.33-2 .76c-.19-.57 1.03-4.48 1.7-7.17c.11-.64.41-2.04-.75-1.94Z"/></svg>
      </NuxtLink>
      </button>

      <button 
      :class="{'active': $route.path === '/cart'}"
      class="menu__item" style="--bgColorItem: #4343f5">
        <NuxtLink to="/cart">
                  <svg class="w-[31.6px] h-[31.6px]" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><g transform="translate(64 0) scale(-1 1)"><path fill="#b2c1c0" d="M53.1 38.6h-7.5v3.8h7.5c1 0 1.9.8 1.9 1.9s-.8 1.9-1.9 1.9H6.3c-1 0-1.9.8-1.9 1.9c0 1 .8 1.9 1.9 1.9h46.9c3.1 0 5.6-2.5 5.6-5.6c0-3.3-2.6-5.8-5.7-5.8m1.4-12.9l-3.7-.3c0-.1 2.3-13.8 2.8-16.6c.3-1.6.9-6.1 6.6-6.1v3.8c-2.3 0-2.6.9-2.8 2.6c-.6 2.8-2.9 16.4-2.9 16.6"/><path fill="#2C73D2" d="M54.7 12.3H4c-1.9 0-2.2 1.8-1.9 2.8l5.7 25.4c.3 1 1.3 1.8 2.4 1.8H50c1 0 2-.8 2.2-1.9l4.2-26.3c.1-.9-.7-1.8-1.7-1.8M6.9 20.8l-1-3.8c-.1-.5.2-.9.7-.9h7.1c.5 0 1 .4 1 .9l.4 3.8c.1.5-.3.9-.8.9H8c-.5 0-1-.4-1.1-.9m3.2 9.3c-.5 0-1-.4-1.2-.9l-.7-2.9c-.1-.5.2-.9.7-.9h5.7c.5 0 1 .4 1 .9l.3 2.8c.1.5-.3.9-.8.9c.1.1-5 .1-5 .1m6 8.5h-3.9c-.5 0-1-.4-1.2-.9l-.7-2.9c-.1-.5.2-.9.7-.9h4.5c.5 0 1 .4 1 .9l.3 2.8c.2.5-.2 1-.7 1m11.5-1c0 .5-.4.9-.9.9h-4.9c-.5 0-1-.4-1-.9l-.3-2.8c-.1-.5.3-.9.8-.9h5.4c.5 0 .9.4.9.9v2.8m0-8.4c0 .5-.4.9-.9.9h-5.8c-.5 0-1-.4-1-.9l-.3-2.8c-.1-.5.3-.9.8-.9h6.3c.5 0 .9.4.9.9v2.8m0-8.4c0 .5-.4.9-.9.9H20c-.5 0-1-.4-1-.9l-.5-3.8c-.1-.5.3-.9.8-.9h7.3c.5 0 .9.4.9.9c.1 0 .1 3.8.1 3.8m10.2 16.8c-.1.5-.5.9-1 .9h-4.4c-.5 0-.9-.4-.9-.9v-2.8c0-.5.4-.9.9-.9h4.9c.5 0 .9.4.8.9l-.3 2.8m.9-8.4c-.1.5-.5.9-1 .9h-5.3c-.5 0-.9-.4-.9-.9v-2.8c0-.5.4-.9.9-.9h5.8c.5 0 .9.4.8.9l-.3 2.8m.9-8.4c-.1.5-.5.9-1 .9h-6.2c-.5 0-.9-.4-.9-.9V17c0-.5.4-.9.9-.9h6.8c.5 0 .9.4.8.9l-.4 3.8m8.7 16.8c-.1.5-.6.9-1.1.9h-4.8c-.5 0-.9-.4-.8-.9l.3-2.8c.1-.5.5-.9 1-.9H48c.5 0 .9.4.8.9l-.5 2.8m1.3-8.4c-.1.5-.6.9-1.1.9h-5.3c-.5 0-.9-.4-.8-.9l.3-2.8c.1-.5.5-.9 1-.9h5.5c.5 0 .9.4.8.9l-.4 2.8m1.3-8.4c-.1.5-.6.9-1.1.9h-5.7c-.5 0-.9-.4-.8-.9l.4-3.8c.1-.5.5-.9 1-.9h5.9c.5 0 .9.4.8.9l-.5 3.8"/><circle cx="12.3" cy="56.4" r="5.6" fill="#62727a"/><circle cx="12.3" cy="56.4" r="2.8" fill="#fff"/><circle cx="46.1" cy="56.4" r="5.6" fill="#62727a"/><path fill="#fff" d="M48.9 56.4c0 1.6-1.3 2.8-2.8 2.8c-1.6 0-2.8-1.3-2.8-2.8c0-1.6 1.3-2.8 2.8-2.8c1.5 0 2.8 1.2 2.8 2.8"/><path fill="#62727a" d="M61.1 2h-2.8v5.6h2.8c.5 0 .9-.4.9-.9V2.9c0-.5-.4-.9-.9-.9"/><path fill="#2C73D2" d="M12.3 48.9c-4.1 0-7.5 3.4-7.5 7.5h15c0-4.2-3.3-7.5-7.5-7.5m33.8 0c-4.1 0-7.5 3.4-7.5 7.5h15c0-4.2-3.4-7.5-7.5-7.5"/></g></svg>
        </NuxtLink>
      </button>

      <button class="menu__item">
        <img
          v-show="$colorMode.value === 'light'"
          @click="
            setColorTheme($colorMode.preference === 'dark' ? 'light' : 'dark')
          "
          class="cursor-pointer icon"
          src="/svg/light.svg"
          alt="..."
        />

        <img
          v-show="$colorMode.value === 'dark'"
          @click="
            setColorTheme($colorMode.preference === 'dark' ? 'light' : 'dark')
          "
          class="cursor-pointer icon"
          src="/svg/dark.svg"
          alt=""
        />
      </button>

      <button @click="logout" v-if="userAuth" :disabled="loading" class="menu__item" style="--bgColorItem: #65ddb7">
        <svg xmlns="http://www.w3.org/2000/svg" v-if="loading" class="icon" viewBox="0 0 24 24"><circle cx="18" cy="12" r="0" fill="currentColor"><animate attributeName="r" begin=".67" calcMode="spline" dur="1.5s" keySplines="0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8" repeatCount="indefinite" values="0;2;0;0"/></circle><circle cx="12" cy="12" r="0" fill="currentColor"><animate attributeName="r" begin=".33" calcMode="spline" dur="1.5s" keySplines="0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8" repeatCount="indefinite" values="0;2;0;0"/></circle><circle cx="6" cy="12" r="0" fill="currentColor"><animate attributeName="r" begin="0" calcMode="spline" dur="1.5s" keySplines="0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8;0.2 0.2 0.4 0.8" repeatCount="indefinite" values="0;2;0;0"/></circle></svg>

        <svg
          v-else
          class="icon"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
        >
          <path
            d="M16 17v-3H9v-4h7V7l5 5l-5 5M14 2a2 2 0 0 1 2 2v2h-2V4H5v16h9v-2h2v2a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9Z"
          />
        </svg>
      </button>

      <button v-else
      :class="{'active': $route.path === '/auth/register' || $route.path === '/auth/login'}"
      class="menu__item" style="--bgColorItem: #65ddb7">
        <NuxtLink
        to="/auth/register">
          <svg xmlns="http://www.w3.org/2000/svg" class="icon" viewBox="0 0 24 24"><path d="M4 15h2v5h12V4H6v5H4V3a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v18a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-6Zm6-4V8l5 4l-5 4v-3H2v-2h8Z"/></svg>
        </NuxtLink>
      </button>
    </menu>

    <div class="svg-container md:invisible">
      <svg viewBox="0 0 202.9 45.5">
        <clipPath
          id="menu"
          clipPathUnits="objectBoundingBox"
          transform="scale(0.0049285362247413 0.021978021978022)"
        >
          <path
            d="M6.7,45.5c5.7,0.1,14.1-0.4,23.3-4c5.7-2.3,9.9-5,18.1-10.5c10.7-7.1,11.8-9.2,20.6-14.3c5-2.9,9.2-5.2,15.2-7
                c7.1-2.1,13.3-2.3,17.6-2.1c4.2-0.2,10.5,0.1,17.6,2.1c6.1,1.8,10.2,4.1,15.2,7c8.8,5,9.9,7.1,20.6,14.3c8.3,5.5,12.4,8.2,18.1,10.5
                c9.2,3.6,17.6,4.2,23.3,4H6.7z"
          />
        </clipPath>
      </svg>
    </div>
  </nav>
</template>

<script setup>
import { useCart } from "@/store/cart";
import { useToast } from "vue-toastification";

const { userAuth } = useAuth();
const setColorTheme = (newTheme) => {
  useColorMode().preference = newTheme;
};
const toast = useToast();
const cart = useCart();
const loading = ref(false);
const itemOnCart = computed(() => cart.count);
const logout = async () => {
  try {
    loading.value = true;
    await $fetch("/api/auth/logout", {
      method: "POST",
    });
    userAuth.value = null;
    navigateTo('/');
    window.location.reload();
    toast.warning("خروج از حساب با موفقیت بود.");
  } catch (error) {
    toast.error("متاسفانه مشکلی رخ داده");
  } finally {
    loading.value = false;
  }
};
</script>