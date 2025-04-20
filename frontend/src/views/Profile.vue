<!-- frontend/src/views/Profile.vue -->
<template>
  <div>
    <h2>Profile</h2>
    <div v-if="errorMessage" class="alert alert-danger">{{ errorMessage }}</div>
    <div v-else-if="user" class="card p-3">
      <h4>{{ user.username }}</h4>
      <p>Email: {{ user.email || 'Not set' }}</p>
      <h5 class="mt-3">Edit Profile</h5>
      <form @submit.prevent="updateProfile">
        <div class="mb-3">
          <input v-model="form.username" class="form-control" placeholder="Username" />
        </div>
        <div class="mb-3">
          <input v-model="form.email" class="form-control" placeholder="Email" />
        </div>
        <button type="submit" class="btn btn-primary">Save</button>
      </form>
    </div>
    <div v-else>Loading...</div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const user = ref(null);
const errorMessage = ref('');
const router = useRouter();
const form = ref({
  username: '',
  email: '',
});

onMounted(async () => {
  try {
    const response = await axios.get('/me');
    user.value = response.data;
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || 'Failed to load profile';
    router.push('/login');
  }
});

async function updateProfile() {
  try {
    const updateData = {};
    if (form.value.username) updateData.username = form.value.username;
    if (form.value.email) updateData.email = form.value.email;
    await axios.put(`/${user.value.id}`, updateData);
    form.value.username = '';
    form.value.email = '';
    alert('Profile updated!');
    onMounted();
  } catch (error) {
    errorMessage.value = error.response?.data?.detail || 'Failed to update profile';
  }
}
</script>