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
        <div class="review" v-for="review in reviews" :key="review.id">
            <h2>{{ review.name }}</h2>
            <p>{{ review.text }}</p>
            <p class="rating">Rating: {{ review.rating }} / 5</p>
        </div>

        <!-- Leave a Review Section -->
        <div class="leave-review">
            <h2>Leave a Review</h2>
            <input type="text" v-model="newReview.name" placeholder="Your Name">
            <textarea v-model="newReview.text" placeholder="Your Review"></textarea>
            <select v-model="newReview.rating">
                <option disabled value="">Rating</option>
                <option value="5">5 - Excellent</option>
                <option value="4">4 - Good</option>
                <option value="3">3 - Average</option>
                <option value="2">2 - Below Average</option>
                <option value="1">1 - Poor</option>
            </select>
            <button @click="submitReview">Submit</button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            reviews: [
                { id: 1, name: 'John Doe', text: 'Great landscaping service! Highly recommended.', rating: 5 },
                { id: 2, name: 'Jane Smith', text: 'Very professional and reliable.', rating: 4 },
                { id: 3, name: 'Mark Johnson', text: 'They transformed my garden beautifully!', rating: 5 }
            ],
            newReview: {
                name: '',
                text: '',
                rating: ''
            }
        };
    },
    methods: {
        submitReview() {
            if (this.newReview.name && this.newReview.text && this.newReview.rating) {
                const newId = this.reviews.length + 1;
                this.reviews.push({ ...this.newReview, id: newId });
                this.newReview = { name: '', text: '', rating: '' };
            } else {
                alert('Please fill in all fields before submitting.');
            }
        }
    }
};
</script>

<style scoped>
.reviews-page {
    padding: 20px;
}

.description {
    margin-bottom: 40px;
    font-size: 18px;
    color: #555;
}

.review {
    margin-bottom: 20px;
    border-bottom: 1px solid #ccc;
    padding-bottom: 10px;
}

.rating {
    font-weight: bold;
    color: green;
}

.leave-review {
    margin-top: 40px;
}

.leave-review input, 
.leave-review textarea, 
.leave-review select {
    display: block;
    margin-bottom: 10px;
    padding: 8px;
    width: 100%;
    max-width: 400px;
}

button {
    padding: 10px 20px;
    background-color: green;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: darkgreen;
}
</style>
