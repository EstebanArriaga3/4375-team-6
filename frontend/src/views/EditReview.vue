<template>
  <div class="reviews-page">
      <h1>Customer Reviews</h1>

      <!-- Description Section -->
      <div class="description">
          <p>
              Welcome to our landscaping company! We take pride in transforming outdoor spaces into beautiful, 
              functional environments. Check out what our customers are saying about our services.
          </p>
      </div>

      <!-- Customer Reviews Section -->
      <div class="reviews-container">
          <div class="review" v-for="review in reviews" :key="review.ReviewID">
              <div class="review-header">
                  <h2>{{ review.CustomerName }}</h2>
                  <p class="rating">★ {{ review.Rating }} / 5</p>
              </div>
              <p class="review-text">{{ review.Comment }}</p>
          </div>
      </div>

      <!-- Delete Review Section -->
      <div class="delete-review">
          <h2>Delete a Review</h2>
          <input type="text" v-model="reviewToDelete.name" placeholder="Reviewer Name" />
          <button @click="deleteReview">Delete Review</button>
      </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      reviews: [],
      reviewToDelete: {
        name: '', // This will hold the name of the reviewer to delete
      }
    };
  },
  methods: {
    async fetchReviews() {
      try {
        const response = await axios.get('http://localhost:5000/api/Reviews');
        this.reviews = response.data.map(review => ({
          ...review,
          CustomerName: review.name || 'Anonymous'
        }));
      } catch (error) {
        console.error('Error fetching reviews:', error);
      }
    },
    async deleteReview() {
      if (this.reviewToDelete.name) {
        try {
          // Send DELETE request to delete the review by reviewer name
          await axios.delete(`http://localhost:5000/api/Reviews/delete`, {
            data: { name: this.reviewToDelete.name }
          });
          alert('Review deleted successfully!');
          this.reviewToDelete.name = '';
          this.fetchReviews(); // Refresh the reviews after deletion
        } catch (error) {
          console.error('Error deleting review:', error);
          alert('Failed to delete the review. Please try again.');
        }
      } else {
        alert('Please enter a reviewer name before submitting.');
      }
    }
  },
  mounted() {
    this.fetchReviews();
  }
};
</script>

<style scoped>
/* Main Container */
.reviews-page {
  padding: 40px 20px;
  font-family: 'Poppins', sans-serif;
  background-color: #181818;
  color: #f0f0f0;
  text-align: center;
  animation: fadeIn 1s ease-in-out;
}

/* Animation for fade-in effect */
@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Title */
h1 {
  font-size: 3rem;
  margin-bottom: 20px;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-weight: 700;
  border-bottom: 3px solid #444;
  padding-bottom: 10px;
}

/* Description */
.description {
  font-size: 1.2rem;
  color: #bbb;
  margin-bottom: 50px;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.8;
}

/* Reviews Section */
.reviews-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 30px;
}

.review {
  background-color: #222;
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
  color: #fff;
  font-weight: 700;
}

.rating {
  font-size: 1.2rem;
  color: #f39c12;
  font-weight: bold;
}

/* Review Text */
.review-text {
  color: #ccc;
  font-size: 1rem;
  line-height: 1.6;
  font-style: italic;
}

/* Delete Review Section */
.delete-review {
  margin-top: 60px;
  padding: 30px;
  background-color: #333;
  border-radius: 15px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.delete-review h2 {
  font-size: 1.8rem;
  margin-bottom: 20px;
  color: #fff;
}

.delete-review input {
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

.delete-review input::placeholder {
  color: #888;
}

.delete-review button {
  display: block;
  width: 100%;
  padding: 15px;
  background-color: #dc3545;
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1.1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.delete-review button:hover {
  background-color: #c82333;
}

/* Responsive */
@media (max-width: 768px) {
  .delete-review,
  .description {
      padding: 20px;
  }

  .reviews-container {
      grid-template-columns: 1fr;
  }

  h1 {
      font-size: 2.5rem;
  }
}
</style>
