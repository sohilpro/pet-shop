export default defineEventHandler(async (e) => {
  const {
    public: { apiBase },
  } = useRuntimeConfig();
  const token = getCookie(e, "accessToken");

  try {
    const data = await $fetch(`${apiBase}/user/information/`, {
      headers: {
        Accept: "application/json",
        Authorization: `Bearer ${token}`,
      },
    });

    return data;
  } catch (error) {
    if (error.statusCode === 401) {
      setCookie(e, "accessToken", "", {
        httpOnly: true,
        secure: true,
        maxAge: new Date(0), //1 WEEK
        path: "/",
      });
      setCookie(e, "refreshToken", "", {
        httpOnly: true,
        secure: true,
        maxAge: new Date(0), //1 WEEK
        path: "/",
      });
    }
  }
});
