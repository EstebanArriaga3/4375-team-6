// This pinia store contains state with respect to whether a user is logged in 
import { defineStore } from 'pinia'
import router from '../router/index.ts';

// Defining a store
export const useLoggedInUserStore = defineStore({
  id: 'loggedInUser',
  state: () => {
    return {
      name: "",
      role: "", // New field for user role
      isLoggedIn: false
    }
  },
  actions: {
    login(username, password, role) {
      // Check if the user is trying to log in as an 'editor'
      if (username === "admin" && password === "admin") {
        // Set role to 'editor'
        role = "editor",
        this.isLoggedIn = true,
        router.push("/");
      }
      // Update the user's information in the store
      this.$patch({
        role: role, // Set the user's role
        name: "User Name" // You may update the name based on the user's actual name
      });
      
    },
    logout() {
      // Log the user out by resetting the store's state
      this.$patch({
        name: "",
        role: "",
        isLoggedIn: false
      });
      
      // Navigate the user to the home page
      router.push("/");
      
    }
  }
});
