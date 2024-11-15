<template>
  <div class="login-field">
    <!--Header-->
    <h1>Welcome</h1>
    <!--Form-->
    <form @submit.prevent="login" autocomplete="off">
      <div class="flex justify-center mt-10">
        <label>
          <span class="text-gray-700">Username</span>
          <span style="color: #ff0000">*</span>
          <input type="text" v-model="username" autocomplete="off"/>
        </label>
      </div>
      <div class="flex justify-center mt-10">
        <label>
          <span class="text-gray-700">Password</span>
          <span style="color: #ff0000">*</span>
          <input type="password" v-model="password" autocomplete="off"/>
        </label>
      </div>
      <!--Login button-->
      <div class="flex justify-center mt-10">
        <button type="submit" :disabled="isSubmitting">Login</button>
      </div>
      <!-- Display error message -->
      <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useLoggedInUserStore } from '../stores/loggedInUser';
import axios from 'axios';

const username = ref('');
const password = ref('');
const errorMessage = ref('');

const store = useLoggedInUserStore();
const isSubmitting = ref(false);

const login = async () => {
  if (isSubmitting.value) return;  // Prevent multiple submissions
  isSubmitting.value = true;  // Disable the submit button
  const payload = {
    username: username.value,
    password: password.value,
  };
  console.log(axios);

  console.log("Payload before sending:", payload);
  console.log("Username input:", username.value);  // This should print the value bound to the username field
  console.log("Password input:", password.value);  // This should print the value bound to the password field
//   axios.interceptors.request.use(request => {
//   console.log("Request data:", request.data);  // Log the request data here
//   return request;
// }, error => {
//   return Promise.reject(error);
// });
console.log('Login method called');
  try {
    // console.log("Payload before sending:", payload);
    // const response = await axios.post('http://localhost:5000/api/login', 
    // // {
    // //   username: username.value,
    // //   password: password.value,
    // // },
    // payload,
    // { withCredentials: true, headers: { 'Content-Type': 'application/json' } }
    // );
    await store.login(username.value, password.value);
    // if (response.data.success) {
    //   store.login(username.value, response.data.role);
    errorMessage.value = '';  // Clear any error messages
    // } else {
    //   errorMessage.value = response.data.message || 'Login failed.';
    // }
  } catch (error) {
    errorMessage.value = 'An error occurred during login.';
    console.error(error);
  }
  finally {
    isSubmitting.value = false;
  }
};
</script>

<style scoped>
.login-field input,
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

.login-field input::placeholder {
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
