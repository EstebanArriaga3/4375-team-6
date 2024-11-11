// src/stores/loggedInUser.ts
import { defineStore } from 'pinia';
import axios from 'axios';
import router from '../router';

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
        });

        if (response.data.success) {
          this.$patch({
            name: username,
            role: response.data.role,
            isLoggedIn: true,
          });
          router.push("/"); // Redirect to home page or another protected route
        } else {
          throw new Error(response.data.message || "Invalid credentials");
        }
      } catch (error) {
        console.error("Login error:", error instanceof Error ? error.message : error);
        alert(error instanceof Error ? error.message : "Login failed");
      }
    },
    logout() {
      this.$patch({
        name: "",
        role: "",
        isLoggedIn: false,
      });
      router.push("/"); // Redirect to the home page or login page
    },
  },
});
