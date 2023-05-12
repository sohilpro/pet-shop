export const useAuth = () => {
  const userAuth = useState("user_auth", () => null);
  return { userAuth };
};