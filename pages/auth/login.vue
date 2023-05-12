<template>
  <Body class="bg-custom overflow-hidden w-screen h-screen">
    <div class="center m-auto">
      <AuthHead />
      <form @submit.prevent="login" class="login">
        <label>
          <div class="fa fa-phone"></div>
          <input
            class="username"
            type="text"
            autocomplete="on"
            placeholder="Username"
            v-model="formData.username"
          />
        </label>
        <label>
          <div class="fa fa-commenting"></div>
          <input
            class="password"
            type="password"
            autocomplete="off"
            placeholder="Password"
            v-model="formData.password"
          />
          <button type="button" class="password-button">نمایش</button>
        </label>
        <button
          :disabled="loading"
          v-if="loading"
          type="submit"
          class="login-button"
        >
          <div role="status">
            <svg
              aria-hidden="true"
              class="inline w-5 h-5 mr-2 text-gray-200 animate-spin dark:text-gray-600 fill-gray-600 dark:fill-gray-300"
              viewBox="0 0 100 101"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
                fill="currentColor"
              />
              <path
                d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
                fill="currentFill"
              />
            </svg>
            <span class="sr-only">Loading...</span>
          </div>
        </button>
        <button v-else class="login-button" type="submit">ورود</button>
      </form>
      <AuthScoial />
      <div class="footer text-white">
        .حساب ندارید؟
        <NuxtLink
          to="/auth/register"
          class="hover:opacity-80 hover:transition-all transition-all"
        >
          کلیک کنید
        </NuxtLink>
      </div>
    </div>
  </Body>
</template>

<script setup>
import { useToast } from "vue-toastification";

definePageMeta({
  middleware: "guest",
});

useHead({
  title: toTitleCase("login page"),
});

onMounted(() => {
  let usernameInput = document.querySelector(".username");
  let passwordInput = document.querySelector(".password");
  let showPasswordButton = document.querySelector(".password-button");
  let face = document.querySelector(".face");

  passwordInput.addEventListener("focus", (event) => {
    document.querySelectorAll(".hand").forEach((hand) => {
      hand.classList.add("hide");
    });
    document.querySelector(".tongue").classList.remove("breath");
  });

  passwordInput.addEventListener("blur", (event) => {
    document.querySelectorAll(".hand").forEach((hand) => {
      hand.classList.remove("hide");
      hand.classList.remove("peek");
    });
    document.querySelector(".tongue").classList.add("breath");
  });

  usernameInput.addEventListener("focus", (event) => {
    let length = Math.min(usernameInput.value.length - 16, 19);
    document.querySelectorAll(".hand").forEach((hand) => {
      hand.classList.remove("hide");
      hand.classList.remove("peek");
    });

    face.style.setProperty("--rotate-head", `${-length}deg`);
  });

  usernameInput.addEventListener("blur", (event) => {
    face.style.setProperty("--rotate-head", "0deg");
  });

  usernameInput.addEventListener(
    "input",
    _.throttle((event) => {
      let length = Math.min(event.target.value.length - 16, 19);

      face.style.setProperty("--rotate-head", `${-length}deg`);
    }, 100)
  );

  showPasswordButton.addEventListener("click", (event) => {
    if (passwordInput.type === "text") {
      passwordInput.type = "password";
      document.querySelectorAll(".hand").forEach((hand) => {
        hand.classList.remove("peek");
        hand.classList.add("hide");
      });
    } else {
      passwordInput.type = "text";
      document.querySelectorAll(".hand").forEach((hand) => {
        hand.classList.remove("hide");
        hand.classList.add("peek");
      });
    }
  });
});

const formData = reactive({
  username: "",
  password: "",
});

const { userAuth } = useAuth();
const toast = useToast();
const loading = ref(false);
const login = async () => {
  if (
    formData.password === "" ||
    formData.username === ""
  ) {
    toast.warning("پر کردن فیلد ها الزامی است.");
    return;
  }
  const userNamePattern = /^\w([\.-]?\w){5,8}$/;
  if (!userNamePattern.test(formData.username)) {
    toast.error("نام کاربری باید بین 6 تا 10 رقم باشد.");
    toast.warning("فقط استفاده از کارکتر های (- . _) مجاز است.");
    return;
  }
  const passwordPattern = /^(?=.*\d)(?=.*[a-z]?)(?=.*[A-Z]?)(?=.*[a-zA-Z]?).{6,}$/;
  if (!passwordPattern.test(formData.password)) {
    toast.error("پسورد را بدرستی وارد کنید (6 رقمی باشد).");
    return;
  }
  try {
    loading.value = true;
    const user = await $fetch("/api/auth/login", {
      method: "POST",
      body: formData,
    });
    userAuth.value = user;
    navigateTo("/");
    window.location.reload();
    toast.success("ورود شما با موفقیت بود.");
  } catch (error) {
    toast.error("اطلاعات وارد شده صحیح نمی باشد!");
  } finally {
    loading.value = false;
  }
};
</script>

<style scoped>
.center {
  width: 400px;
  height: 500px;
}
</style>
