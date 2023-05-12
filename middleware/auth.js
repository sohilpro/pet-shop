export default defineNuxtRouteMiddleware(() => {
  const { userAuth } = useAuth();
  if (!userAuth.value) {
    return navigateTo("/auth/login");
  }
});
