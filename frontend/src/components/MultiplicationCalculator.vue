<template>
  <div class="calculator-container">
    <h2 class="title">Number Multiplication</h2>
    
    <div class="input-group">
      <div class="form-control">
        <label for="number1">First Number:</label>
        <input
          id="number1"
          v-model.number="number1"
          type="number"
          placeholder="Enter first number"
          :class="{ 'error': validationErrors.number1 }"
        />
        <span class="error-message" v-if="validationErrors.number1">
          {{ validationErrors.number1 }}
        </span>
      </div>

      <div class="form-control">
        <label for="number2">Second Number:</label>
        <input
          id="number2"
          v-model.number="number2"
          type="number"
          placeholder="Enter second number"
          :class="{ 'error': validationErrors.number2 }"
        />
        <span class="error-message" v-if="validationErrors.number2">
          {{ validationErrors.number2 }}
        </span>
      </div>
    </div>

    <button 
      @click="calculateMultiplication"
      :disabled="isLoading"
      class="multiply-button"
    >
      {{ isLoading ? 'Calculating...' : 'Multiply' }}
    </button>

    <div v-if="result !== null" class="result">
      <h3>Result:</h3>
      <p class="result-value">{{ result }}</p>
    </div>

    <div v-if="error" class="error-container">
      {{ error }}
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import apiClient from '@/plugins/axios';

export default defineComponent({
  name: 'MultiplicationCalculator',
  
  data() {
    return {
      number1: null,
      number2: null,
      result: null,
      error: null,
      isLoading: false,
      validationErrors: {
        number1: '',
        number2: ''
      }
    };
  },

  methods: {
    validateInputs() {
      this.validationErrors = {
        number1: '',
        number2: ''
      };
      
      if (this.number1 === null || isNaN(this.number1)) {
        this.validationErrors.number1 = 'Please enter a valid number';
      }
      if (this.number2 === null || isNaN(this.number2)) {
        this.validationErrors.number2 = 'Please enter a valid number';
      }

      return !this.validationErrors.number1 && !this.validationErrors.number2;
    },

    async calculateMultiplication() {
      if (!this.validateInputs()) {
        return;
      }

      this.isLoading = true;
      this.error = null;
      this.result = null;

      try {
        const response = await apiClient.post('/api/multiply/', {
          number1: this.number1,
          number2: this.number2
        });

        this.result = response.data.result;
      } catch (err) {
        this.error = err.response?.data?.message || 'An error occurred while calculating';
      } finally {
        this.isLoading = false;
      }
    }
  }
})
</script>

<style scoped>
.calculator-container {
  max-width: 500px;
  margin: 2rem auto;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  background-color: #ffffff;
}

.title {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 2rem;
}

.input-group {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.form-control {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

label {
  font-weight: 600;
  color: #2c3e50;
}

input {
  padding: 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 1rem;
}

input.error {
  border-color: #dc3545;
}

.error-message {
  color: #dc3545;
  font-size: 0.875rem;
}

.multiply-button {
  width: 100%;
  padding: 0.75rem;
  background-color: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s;
}

.multiply-button:hover {
  background-color: #3aa876;
}

.multiply-button:disabled {
  background-color: #a8e0c9;
  cursor: not-allowed;
}

.result {
  margin-top: 2rem;
  text-align: center;
}

.result h3 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.result-value {
  font-size: 2rem;
  font-weight: bold;
  color: #42b983;
}

.error-container {
  margin-top: 1rem;
  padding: 0.75rem;
  background-color: #ffebee;
  color: #dc3545;
  border-radius: 4px;
  text-align: center;
}
</style>