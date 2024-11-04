<template>
  <div class="login-field">
    <!--Header-->
    <h1 class="font-bold text-4xl text-red-700 tracking-widest text-center mt-10">Welcome</h1>
      <!--Form-->
      <form @submit.prevent="store.login(username, password)" novalidate="true">
        <div class="flex justify-center mt-10">
          <label>
            <span class="text-gray-700">Username</span>
            <span style="color: #ff0000">*</span>
            <input type="text"
              class=""
              placeholder v-model="username" />
          </label>
        </div>
        <div class="flex justify-center mt-10">
          <label>
            <span class="text-gray-700">Password</span>
            <span style="color: #ff0000">*</span>
            <input type="password"
              class=""
              placeholder v-model="password" />
          </label>
        </div>
        <!--Login button-->
        <div class="flex justify-center mt-10">
          <button class="" type="submit" @click="login(username, password)">Login</button>
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

<style scoped>
.login-field input,
.login-field textarea,
.login-field select {
    width: 100%;
    padding: 12px;
    margin-bottom: 15px;
    border: 1px solid #555;
    border-radius: 5px;
    font-size: 1rem;
    background-color: #444;
    color: #fff;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.3);
}

.login-field input::placeholder,
.login-field textarea::placeholder {
    color: #888;
}

.login-field button {
    display: block;
    width: 100%;
    padding: 15px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1.1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.login-field button:hover {
    background-color: #218838;
}
</style>

