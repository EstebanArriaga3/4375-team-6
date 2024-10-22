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
            <div class="review" v-for="review in reviews" :key="review.id">
                <div class="review-header">
                    <h2>{{ review.name }}</h2>
                    <p class="rating">★ {{ review.rating }} / 5</p>
                </div>
                <p class="review-text">{{ review.text }}</p>
            </div>
        </div>

        <!-- Leave a Review Section -->
        <div class="leave-review">
            <h2>Leave Your Review</h2>
            <input type="text" v-model="newReview.name" placeholder="Your Name" />
            <textarea v-model="newReview.text" placeholder="Your Review" rows = '5'></textarea>
            <select v-model="newReview.rating">
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

/* Leave a Review Section */
.leave-review {
    margin-top: 60px;
    padding: 30px;
    background-color: #333;
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
    background-color: #444;
    color: #fff;
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
    background-color: #28a745;
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

/* Responsive */
@media (max-width: 768px) {
    .leave-review,
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
