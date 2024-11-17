<template>
    <div class="reviews-page">
      <h1>Customer Reviews</h1>
  
      <div class="description">
        <p>
          Welcome to our landscaping company! We take pride in transforming
          outdoor spaces into beautiful, functional environments. Check out what
          our customers are saying about our services.
        </p>
      </div>
  
      <!-- Customer Reviews Section -->
      <div class="reviews-container">
        <div class="review" v-for="review in reviews" :key="review.ReviewID">
          <div class="review-header">
            <h2>{{ review.CustomerName || 'Anonymous' }}</h2>
            <p class="rating">★ {{ review.Rating }} / 5</p>
          </div>
          <p class="review-text">{{ review.Comment }}</p>
  
        </div>
      </div>
  
      <!-- Edit Review Modal (Admin Only) -->
      <div v-if="showEditModal" class="modal">
        <div class="modal-content">
          <h2>Edit Review</h2>
          <input type="text" v-model="reviewToEdit.CustomerName" placeholder="Your Name" />
          <textarea v-model="reviewToEdit.Comment" placeholder="Your Review" rows="5"></textarea>
          <select v-model="reviewToEdit.Rating">
            <option disabled value="">Rating</option>
            <option value="5">5 - Excellent</option>
            <option value="4">4 - Good</option>
            <option value="3">3 - Average</option>
            <option value="2">2 - Below Average</option>
            <option value="1">1 - Poor</option>
          </select>
          <button @click="updateReview">Update Review</button>
          <button @click="closeEditModal">Cancel</button>
        </div>
      </div>
  
      <!-- Leave a Review Section (For All Users) -->
      <div class="leave-review">
        <h2>Leave Your Review</h2>
        <input type="text" v-model="newReview.name" placeholder="Your Name" />
        <textarea v-model="newReview.Comment" placeholder="Your Review" rows="5"></textarea>
        <select v-model="newReview.Rating">
          <option disabled value="">Rating</option>
          <option value="5">5 - Excellent</option>
          <option value="4">4 - Good</option>
          <option value="3">3 - Average</option>
          <option value="2">2 - Below Average</option>
          <option value="1">1 - Poor</option>
        </select>
        <button @click="submitReview">Submit Review</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import { useLoggedInUserStore } from '../stores/loggedInUser';
  
  export default {
    data() {
      return {
        reviews: [],
        showEditModal: false,
        reviewToEdit: null,
        newReview: {
          name: '',
          Comment: '',
          Rating: '',
          ReviewDate: new Date().toISOString().slice(0, 10),
          ServiceID: 1,
        },
      };
    },
    computed: {
      user() {
        const userStore = useLoggedInUserStore();
        console.log("User data in computed:", userStore);
        return userStore;
      },
      isAdmin() {
        return this.user.role === 'admin';
      },
    },
    methods: {
      async fetchReviews() {
        try {
          const response = await axios.get('http://localhost:5000/api/Reviews');
          this.reviews = response.data.map(review => ({
            ...review,
            CustomerName: review.CustomerName || 'Anonymous',
          }));
        } catch (error) {
          console.error('Error fetching reviews:', error);
        }
      },
      async submitReview() {
        if (this.newReview.name && this.newReview.Comment && this.newReview.Rating) {
          try {
            await axios.post('http://localhost:5000/api/Reviews/add', this.newReview);
            alert('Review submitted successfully!');
            this.newReview = { name: '', Comment: '', Rating: '', ReviewDate: '', ServiceID: 1 };
            this.fetchReviews();
          } catch (error) {
            console.error('Error submitting review:', error);
            alert('Failed to submit the review. Please try again.');
          }
        } else {
          alert('Please fill in all fields before submitting.');
        }
      },

      closeEditModal() {
        this.showEditModal = false;
        this.reviewToEdit = null;
      },
    },
    mounted() {
      this.fetchReviews();
    },
  };
  </script>
  
  <style scoped>
.reviews-page {
  padding: 40px 20px;
  font-family: 'Poppins', sans-serif;
  background-color: #f4f0eb;
  color: #040303;
  text-align: center;
  animation: fadeIn 1s ease-in-out;
}
/* Animation for fade-in effect */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}
h1 {
  font-size: 3rem;
  margin-bottom: 20px;
  color: #0e0d0d;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-weight: 700;
  border-bottom: 3px solid #444;
  padding-bottom: 10px;
}

.description {
  font-size: 1.2rem;
  color: #030202;
  margin-bottom: 50px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.8;
}

/* Stats Bar */
.stats-bar {
  display: flex;
  justify-content: center;
  gap: 3rem;
  margin-bottom: 3rem;
  padding: 2rem;
  background: white;
  border-radius: 15px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  max-width: 600px;
  margin: 0 auto 3rem;
}

.stat-item {
  text-align: center;
}

.stat-item h3 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 0.5rem;
}

/* Stars */
.stars {
  display: flex;
  gap: 4px;
  justify-content: center;
  margin-bottom: 0.5rem;
}
.rating {
  font-size: 1.2rem;
  color: #7c623e;
  font-weight: bold;
}
.star {
  color: #ddd;
  font-size: 1.4rem;
  cursor: default;
  transition: color 0.3s ease;
}

.star.filled {
  color: #ffd700;
}

/* Reviews Container */
.reviews-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem;
}

.review {
  background-color: #c2b3a3;
  padding: 25px;
  border-radius: 15px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  overflow: hidden;
  text-align: left;
}

.review:hover {
  transform: translateY(-10px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.9);
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

h2 {
  font-size: 1.6rem;
  color: #010101;
  font-weight: 700;
}

.rating {
  font-size: 1.2rem;
  color: #7c623e;
  font-weight: bold;
}

/* Review Text */
.review-text {
  color: #232222;
  font-size: 1rem;
  line-height: 1.6;
  font-style: italic;
}

/* Leave a Review Section */
.leave-review {
    margin-top: 60px;
    padding: 30px;
    background-color: #c2b3a3;
    border-radius: 15px;
    box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
  }
  
  .leave-review h2 {
    font-size: 1.8rem;
    margin-bottom: 20px;
    color: #fff;
  }
  
  .leave-review input,
  .leave-review textarea,
  .leave-review select {
    width: 100%;
    padding: 12px;
    margin-bottom: 15px;
    border: 1px solid #555;
    border-radius: 5px;
    font-size: 1rem;
    background-color: #F5F5F5;
    color: #070707;
    box-shadow: 0 3px 6px rgba(0, 0, 0, 0.3);
  }
  
  .leave-review input::placeholder,
  .leave-review textarea::placeholder {
    color: #888;
  }
  
  .leave-review button {
    display: block;
    width: 100%;
    padding: 15px;
    background-color: #333333;
    color: white;
    border: none;
    border-radius: 5px;
    font-size: 1.1rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }
  
  .leave-review button:hover {
    background-color: #218838;
  }

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  width: 90%;
  max-width: 500px;
}

.modal h2 {
  text-align: center;
  margin-bottom: 2rem;
}

.modal-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.modal-actions {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
}

/* Buttons */
.submit-btn,
.save-btn {
  width: 100%;
  padding: 1rem;
  background: #28a745;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background 0.3s ease;
}

.cancel-btn {
  width: 100%;
  padding: 1rem;
  background: #6c757d;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background 0.3s ease;
}

.admin-controls {
  display: flex;
  gap: 1rem;
  margin-top: 1.5rem;
  border-top: 1px solid #eee;
  padding-top: 1rem;
}

.edit-btn,
.delete-btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.3s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.edit-btn {
  background: #007bff;
  color: white;
}

.delete-btn {
  background: #dc3545;
  color: white;
}

@media (max-width: 768px) {
  .reviews-container {
    grid-template-columns: 1fr;
  }

  .stats-bar {
    flex-direction: column;
    gap: 1.5rem;
  }

  .modal {
    width: 95%;
    padding: 1.5rem;
  }
}
</style>