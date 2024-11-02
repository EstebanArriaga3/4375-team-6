<template>
    <div class="quote-page">
      <h1>Customer Quotes</h1>
  
      <!-- Display Quotes -->
      <div class="quotes-list">
        <div v-for="(quote, index) in quotes" :key="index" class="quote-item">
          <p><strong>Service:</strong> {{ quote.service }}</p>
          <p><strong>Project Description:</strong> {{ quote.description }}</p>
          <p><strong>Email:</strong> {{ quote.email }}</p>
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  
  const quotes = ref([]);
  
  // Fetch quotes on page load
  async function fetchQuotes() {
    try {
      const response = await axios.get('http://localhost:3000/api/quotes');
      quotes.value = response.data;
    } catch (error) {
      console.error('Error fetching quotes:', error);
    }
  }
  
  onMounted(fetchQuotes);
  </script>
  
  <style scoped>
  .quote-page {
    max-width: 600px;
    margin: 0 auto;
    padding: 2rem;
    background-color: #f9f9f9;
    border-radius: 8px;
  }
  
  h1 {
    color: #333;
    text-align: center;
  }
  
  .quotes-list {
    margin-top: 2rem;
  }
  
  .quote-item {
    margin-bottom: 1.5rem;
    padding: 1rem;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: #fff;
  }
  
  .quote-item p {
    margin: 0.5rem 0;
  }
  </style>
  