// src/stores/loggedInUser.ts
import { defineStore } from 'pinia';
import axios from 'axios';
import router from '../router';

axios.defaults.withCredentials = true;

// axios.interceptors.request.use(request => {
//   console.log("Interceptor request data:", request.data);  // Check the data here
//   return request;
// });

export const useLoggedInUserStore = defineStore({
  id: 'loggedInUser',
  state: () => ({
    name: "" as string,
    role: "" as string,
    isLoggedIn: false as boolean,
  }),
  actions: {
    async login(username: string, password: string) {
      try {
        const response = await axios.post("http://localhost:5000/api/login", {
          username,
          password,
        },
        {
          withCredentials: true
        }
      );

        if (response.data.success) {
          this.$patch({
            name: username,
            role: response.data.role,
            isLoggedIn: true,
          });
          // Store user data in localStorage for persistence
          localStorage.setItem('user', JSON.stringify({
            name: username,
            role: response.data.role,
            isLoggedIn: true,
          }));
          router.push("/"); // Redirect to home page or another protected route
        } else {
          throw new Error(response.data.message || "Invalid credentials");
        }
      } catch (error) {
        console.error("Login error:", error instanceof Error ? error.message : error);
        throw new Error(error instanceof Error ? error.message : "Login failed");
      }
    },

    async logout() {
      try {
        await axios.post("http://localhost:5000/api/logout");

        this.$patch({
          name: "",
          role: "",
          isLoggedIn: false,
        });
        
        localStorage.removeItem('user');
        
        router.push("/"); // Redirect to the home page or login page
      } catch (error) {
        console.error("Logout error:", error);
      }
    },

    loadUserSession() {
      const userData = localStorage.getItem('user');
      if (userData) {
        const parsedData = JSON.parse(userData);
        this.$patch({
          name: parsedData.name,
          role: parsedData.role,
          isLoggedIn: parsedData.isLoggedIn,
        });
      }
    }
  },
});
