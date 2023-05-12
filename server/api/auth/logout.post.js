export default defineEventHandler(async (e) => {
  const {
    public: { apiBase },
  } = useRuntimeConfig();
  const token = getCookie(e, 'refreshToken');
  try {
    const data = await $fetch(`${apiBase}/user/logout/`, {
      method: "POST",
      body: {"refresh" : token},
      headers: {
        Accept: "application/json",
      },
    });
    setCookie(e, "refreshToken", "", {
      httpOnly: true,
      secure: true,
      maxAge: new Date(0),
      path: "/",
    });
    setCookie(e, "accessToken", "", {
      httpOnly: true,
      secure: true,
      maxAge: new Date(0),
      path: "/",
    });
    return data;
  } catch (error) {
    console.log(error);
    return error;
  }
});
