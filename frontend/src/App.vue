<script>
import { defineComponent } from 'vue'
import MultiplicationCalculator from './components/MultiplicationCalculator.vue'

export default defineComponent({
  name: 'App',
  components: {
    MultiplicationCalculator
  }
})
</script>

<template>
  <div class="app">
    <MultiplicationCalculator />
  </div>
</template>