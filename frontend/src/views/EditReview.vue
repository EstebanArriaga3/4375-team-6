<template>
    <div class="reviews">
      <h2>Customer Reviews</h2>
      <ul>
        <li v-for="review in reviews" :key="review.id" class="review-item">
          <p><strong>{{ review.name }}</strong>: {{ review.text }}</p>
          <p v-if="review.response"><strong>Response:</strong> {{ review.response }}</p>
  
          <div v-if="!review.response" class="response-section">
            <textarea v-model="response" placeholder="Write a response..."></textarea>
            <button @click="submitResponse(review.id)">Respond</button>
          </div>
  
          <button class="delete-btn" @click="deleteReview(review.id)">Delete Review</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        reviews: [],
        response: "",
      };
    },
    created() {
      this.fetchReviews();
    },
    methods: {
      async fetchReviews() {
        try {
          const response = await axios.get("http://localhost:3000/api/reviews");
          this.reviews = response.data;
        } catch (error) {
          console.error("Error fetching reviews:", error);
        }
      },
      async submitResponse(reviewId) {
        try {
          await axios.post(`http://localhost:3000/api/reviews/${reviewId}/respond`, {
            response: this.response,
          });
          this.response = "";
          this.fetchReviews();
        } catch (error) {
          console.error("Error adding response:", error);
        }
      },
      async deleteReview(reviewId) {
        try {
          await axios.delete(`http://localhost:3000/api/reviews/${reviewId}`);
          this.fetchReviews();
        } catch (error) {
          console.error("Error deleting review:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .reviews {
    max-width: 600px;
    margin: 0 auto;
  }
  .review-item {
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ddd;
  }
  .response-section textarea {
    width: 100%;
    margin-top: 10px;
  }
  button {
    margin-top: 5px;
  }
  .delete-btn {
    color: red;
  }
  </style>
  