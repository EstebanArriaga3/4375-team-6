<template>
  <div class="login-field">
    <!-- Header -->
    <h1>Welcome</h1>

    <!-- Form -->
    <form @submit.prevent="login">
      <div class="flex justify-center mt-10">
        <label>
          <span class="text-gray-700">Username</span>
          <span style="color: #ff0000">*</span>
          <input type="text" v-model="username" />
        </label>
      </div>
      <div class="flex justify-center mt-10">
        <label>
          <span class="text-gray-700">Password</span>
          <span style="color: #ff0000">*</span>
          <input type="password" v-model="password" />
        </label>
      </div>
      
      <!-- Error Message -->
      <div v-if="errorMessage" class="text-red-500 text-center mt-4">{{ errorMessage }}</div>

      <!-- Login Button -->
      <div class="flex justify-center mt-10">
        <button type="submit" class="login-button">Login</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useLoggedInUserStore } from "../stores/loggedInUser";

const username = ref("");
const password = ref("");
const store = useLoggedInUserStore();
const errorMessage = ref("");

// Function to handle login using the store's action
const login = async () => {
  try {
    await store.login(username.value, password.value);
    errorMessage.value = ""; // Clear error if successful
  } catch (error) {
    // Store the error message from the store's action
    errorMessage.value = error.message || "An error occurred during login.";
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

.login-button {
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

.login-button:hover {
  background-color: #218838;
}
</style>
