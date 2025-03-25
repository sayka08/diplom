<template>
  <div>
    <h2>Profile</h2>
    <p v-if="errorMessage">{{ errorMessage }}</p>
    <p v-else>Username: {{ username }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const username = ref('')
const errorMessage = ref('')

onMounted(async () => {
  try {
    const token = localStorage.getItem('access_token')
    if (!token) {
      throw new Error('No token found')
    }
    const response = await axios.get('http://localhost:8000/api/v1/me', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    username.value = response.data.username
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || 'Error: ' + error.message
  }
})
</script>
