// Brandons version of edit review
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
      <div class="filter-container">
        <label for="filter-reviews">Sort Reviews:</label>
        <select id="filter-reviews" v-model="sortOrder" @change="sortReviews">
          <option value="most-positive">Most Positive</option>
          <option value="most-negative">Most Negative</option>
          <option value="newest">Newest</option>
          <option value="oldest">Oldest</option>
        </select>
      </div>
      <!-- Customer Reviews Section -->
      <div class="reviews-container">
          <div class="review" v-for="review in reviews" :key="review.ReviewID">
              <div class="review-header">
                  <h2>{{ review.CustomerName }}</h2>
                  <p class="rating">★ {{ review.Rating }} / 5</p>
              </div>
              <p class="review-text">{{ review.Comment }}</p>
              <button @click="confirmDeleteReview(review.ReviewID)" class="delete-button">Delete Review</button>
          </div>
      </div>


  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      reviews: [],
      sortOrder: '',
    };
  },
  methods: {
    async fetchReviews() {
      try {
        const response = await axios.get('http://localhost:5000/api/Reviews');
        this.reviews = response.data.map(review => ({
          ...review,
          CustomerName: review.CustomerName || 'Anonymous',
          ReviewDate: new Date(review.ReviewDate),
        }));
      } catch (error) {
        console.error('Error fetching reviews:', error);
      }
    },
    sortReviews() {
      if (this.sortOrder === 'most-positive') {
        this.reviews.sort((a, b) => b.Rating - a.Rating); // Sort by descending Rating
      } else if (this.sortOrder === 'most-negative') {
        this.reviews.sort((a, b) => a.Rating - b.Rating); // Sort by ascending Rating
      } else if (this.sortOrder === 'newest') {
        this.reviews.sort((a, b) => new Date(b.ReviewDate) - new Date(a.ReviewDate)); // Sort by descending date
      } else if (this.sortOrder === 'oldest') {
        this.reviews.sort((a, b) => new Date(a.ReviewDate) - new Date(b.ReviewDate));
      }
    },
    confirmDeleteReview(reviewId) {
        if (confirm("Are you sure you want to delete this review?")) {
          this.deleteReview(reviewId);
        }
      },
      async deleteReview(reviewId) {
        try {
          await axios.delete(`http://localhost:5000/api/Reviews/delete`, {
            data: { review_id: reviewId }, // Send the review ID to delete
          });
          alert('Review deleted successfully!');
          this.fetchReviews(); // Refresh the reviews after deletion
        } catch (error) {
          console.error('Error deleting review:', error);
          alert('Failed to delete the review. Please try again.');
        }
      },

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

/* Title */
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

/* Description */
.description {
  font-size: 1.2rem;
  color: #030202;
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


/* Delete Review Button */
.review button {
    margin-top: 10px;
    padding: 10px;
    background-color: #dc3545; /* Bootstrap Danger Color */
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.review button:hover {
    background-color: #c82333; /* Darker shade on hover */
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

.filter-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.filter-container label {
  margin-right: 10px;
  font-size: 1rem;
  color: #444;
}

.filter-container select {
  padding: 8px;
  font-size: 1rem;
  border-radius: 5px;
  border: 1px solid #ccc;
  background-color: #f5f5f5;
  color: #444;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

</style>