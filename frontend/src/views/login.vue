<template>
  <div>
    <!--Header-->
    <h1 class="font-bold text-4xl text-red-700 tracking-widest text-center mt-10">Welcome</h1>
      <!--Form-->
      <form @submit.prevent="store.login(username, password)" novalidate="true">
        <div class="flex justify-center mt-10">
          <label>
            <span class="text-gray-700">Username</span>
            <span style="color: #ff0000">*</span>
            <input type="text"
              class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              placeholder v-model="username" />
          </label>
        </div>
        <div class="flex justify-center mt-10">
          <label>
            <span class="text-gray-700">Password</span>
            <span style="color: #ff0000">*</span>
            <input type="password"
              class="w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
              placeholder v-model="password" />
          </label>
        </div>
        <!--Login button-->
        <div class="flex justify-center mt-10">
          <button class="bg-red-700 text-white rounded" type="submit" @click="login(username, password)">Login</button>
        </div>
      </form>
    </div>
</template>

<!-- Composite API-->
<script setup>
import { ref } from "vue";
import { useLoggedInUserStore } from "../stores/loggedInUser.js";

const username = ref("");
const password = ref("");
const role = ref(""); // Initialize role with an empty string
const store = useLoggedInUserStore();
const errorMessage = ref(""); // Add a reactive variable to store error messages

// Function to handle login
const login = () => {
  // Check if the user is trying to log in as an 'editor'
  if (username.value === "admin" && password.value === "admin") {
    // Set role to 'editor'
    role.value = "editor";
    // Update the user's information in the store
    store.login(username.value, password.value, role.value);
    // Reset error message
    errorMessage.value = "";
  } else {
    // Set error message for incorrect credentials
    errorMessage.value = "Incorrect username or password. Please try again.";
    // Clear username and password fields
    username.value = "";
    password.value = "";
  }
};
</script>



