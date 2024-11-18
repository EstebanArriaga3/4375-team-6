// src/stores/loggedInUser.ts
import { defineStore } from 'pinia';
import axios from 'axios';
import router from '../router';

axios.defaults.withCredentials = true;

function debounce<T extends (...args: any[]) => void>(func: T, wait: number): (...args: Parameters<T>) => void {
  let timeout: ReturnType<typeof setTimeout> | null = null;
  return function (this: ThisParameterType<T>, ...args: Parameters<T>) {
    if (timeout) clearTimeout(timeout);
    timeout = setTimeout(() => func.apply(this, args), wait);
  };
}

export const useLoggedInUserStore = defineStore({
  id: 'loggedInUser',
  state: () => ({
    name: "" as string,
    role: "" as string,
    isLoggedIn: false as boolean,
    lastActivity: 0 as number,
  }),
  actions: {
    async login(username: string, password: string) {
      try {
        const response = await axios.post(
          "http://localhost:5000/api/login",
          { username, password },
          { withCredentials: true }
        );

        if (response.data.success) {
          const now = Date.now();
          this.$patch({
            name: username,
            role: response.data.role,
            isLoggedIn: true,
            lastActivity: now,
          });
          // Store user data in localStorage for persistence
          localStorage.setItem(
            'user',
            JSON.stringify({
              name: username,
              role: response.data.role,
              isLoggedIn: true,
              lastActivity: now,
            })
          );
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
          lastActivity: 0,
        });

        localStorage.removeItem('user');
        router.push("/"); // Redirect to the home page or login page
      } catch (error) {
        console.error("Logout error:", error);
      }
    },

    loadUserSession() {
      const userData = localStorage.getItem('user');
      const logoutTime = localStorage.getItem('logoutTime');
      const now = Date.now();

      if (logoutTime && now - parseInt(logoutTime) > 2 * 60 * 60 * 1000) {
        // If it's been more than 2 hours since logout, do not restore session
        localStorage.removeItem('user');
        return;
      }

      if (userData) {
        const parsedData = JSON.parse(userData);
        const { lastActivity } = parsedData;

        if (now - lastActivity > 1 * 60 * 60 * 1000) {
          // If it's been more than 1 hour since last activity, log out automatically
          this.logout();
        } else {
          this.$patch({
            name: parsedData.name,
            role: parsedData.role,
            isLoggedIn: parsedData.isLoggedIn,
            lastActivity: parsedData.lastActivity,
          });
        }
      }
    },

    updateActivity: debounce(function (this: { lastActivity: number }) {
      const now = Date.now();
      this.lastActivity = now;

      const userData = localStorage.getItem('user');
      if (userData) {
        const parsedData = JSON.parse(userData);
        parsedData.lastActivity = now;
        localStorage.setItem('user', JSON.stringify(parsedData));
      }
    }, 1000), // 1-second delay between updates to reduce traffic
  },
});
