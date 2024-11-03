<template>
  <div class="edit-review-modal" v-if="show">
      <div class="modal-content">
          <h2>Edit Review</h2>
          <input v-model="review.CustomerName" placeholder="Reviewer Name" />
          <input v-model="review.Rating" type="number" min="1" max="5" placeholder="Rating (1-5)" />
          <textarea v-model="review.Comment" placeholder="Your Review"></textarea>
          <button @click="updateReview">Update Review</button>
          <button @click="close">Cancel</button>
      </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    review: Object,
    show: Boolean,
  },
  methods: {
    async updateReview() {
      try {
        await axios.put(`http://localhost:5000/api/Reviews/update`, this.review);
        this.$emit('close'); // Close the modal
        alert('Review updated successfully!');
      } catch (error) {
        console.error('Error updating review:', error);
        alert('Failed to update the review. Please try again.');
      }
    },
    close() {
      this.$emit('close');
    }
  },
};
</script>

<style scoped>
.edit-review-modal {
  /* Basic modal styles */
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 5px;
  width: 400px;
}
</style>
