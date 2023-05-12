export default defineNuxtPlugin(async (nuxtApp) => {
  const { userAuth } = useAuth();
  try {
    const user = await $fetch("/api/auth/me", {
      headers: useRequestHeaders(["cookie"]),
    });
    userAuth.value = user;
  } catch (error) {
    userAuth.value = null;
  }
});